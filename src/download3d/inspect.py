"""Conservative, dependency-free inspection of authorized 3D files.

This is a structural inspector, NOT a Blender import, renderer, conversion
engine, or certification that every externally available animation was acquired.
It never follows URLs, executes embedded instructions, or extracts archives.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import stat
import struct
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

MAX_JSON_BYTES = 32 * 1024 * 1024
MAX_ZIP_FILES = 5000
MAX_ZIP_UNCOMPRESSED = 3 * 1024 * 1024 * 1024
MAX_ZIP_ENTRY = 1024 * 1024 * 1024
MAX_ZIP_RATIO = 1000


class InspectionError(Exception):
    """An actionable validation failure with a machine-readable code."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_bytes(raw: bytes) -> dict:
    try:
        obj = json.loads(raw.decode("utf-8-sig"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise InspectionError("INVALID_JSON", "glTF JSON is malformed or not UTF-8") from exc
    if not isinstance(obj, dict):
        raise InspectionError("INVALID_GLTF", "glTF top-level JSON must be an object")
    return obj


def _check_uri(uri: str, base_dir: Path, warnings: list[str]) -> None:
    if not isinstance(uri, str):
        raise InspectionError("UNSAFE_URI", "glTF dependency URI is not a string")
    if uri.startswith("data:"):
        return
    parsed = urlsplit(uri)
    if parsed.scheme in ("http", "https"):
        warnings.append("Remote dependency referenced; not fetched or checked")
        return
    if parsed.scheme or parsed.netloc:
        raise InspectionError("UNSAFE_URI", "Unsupported external dependency URI scheme")
    p = unquote(parsed.path)
    if not p or p.startswith("/") or "\\" in p or ":" in p:
        raise InspectionError("UNSAFE_URI", "glTF resource path is absolute or invalid")
    normal = posixpath.normpath(p)
    if normal == ".." or normal.startswith("../"):
        raise InspectionError("UNSAFE_URI", "glTF resource path escapes asset directory")
    if not (base_dir / normal).is_file():
        warnings.append("Missing referenced local dependency: " + normal)


def _inspect_gltf_object(obj: dict, base_dir: Path, warnings: list[str]) -> dict:
    asset = obj.get("asset", {})
    if not isinstance(asset, dict) or not str(asset.get("version", "")).startswith("2."):
        raise InspectionError("INVALID_GLTF", "Expected glTF 2.x asset.version")
    names = []
    animations = obj.get("animations", [])
    if not isinstance(animations, list):
        raise InspectionError("INVALID_GLTF", "animations field must be an array")
    for idx, anim in enumerate(animations):
        if not isinstance(anim, dict):
            raise InspectionError("INVALID_GLTF", "Animation entry must be an object")
        names.append(str(anim.get("name") or ("animation_" + str(idx))))
        if not anim.get("channels"):
            warnings.append("Animation has no channels: " + names[-1])
    for collection in ("buffers", "images"):
        items = obj.get(collection, [])
        if not isinstance(items, list):
            raise InspectionError("INVALID_GLTF", collection + " field must be an array")
        for item in items:
            if not isinstance(item, dict):
                raise InspectionError("INVALID_GLTF", collection + " entry must be an object")
            if "uri" in item:
                _check_uri(item["uri"], base_dir, warnings)
    inventory = {
        "animations": len(names),
        "animation_names": names,
        "meshes": len(obj.get("meshes", [])),
        "skins": len(obj.get("skins", [])),
        "materials": len(obj.get("materials", [])),
        "textures": len(obj.get("textures", [])),
        "images": len(obj.get("images", [])),
        "nodes": len(obj.get("nodes", [])),
    }
    warnings.append("Structural metadata only; use Blender/browser for animation playback and external reference validation")
    return inventory


def _inspect_glb(path: Path, warnings: list[str]) -> dict:
    size = path.stat().st_size
    if size < 20:
        raise InspectionError("INVALID_GLB", "GLB shorter than mandatory header and JSON chunk")
    with path.open("rb") as inp:
        magic, version, declared = struct.unpack("<4sII", inp.read(12))
        if magic != b"glTF":
            raise InspectionError("INVALID_GLB", "Missing glTF binary signature; maybe HTML or truncated response")
        if version != 2:
            raise InspectionError("INVALID_GLB", "Only glTF binary version 2 is supported")
        if declared != size:
            raise InspectionError("GLB_INVALID_LENGTH", "Declared GLB length does not equal actual size")
        offset = 12
        found_json = False
        inventory = {}
        while offset < size:
            if size - offset < 8:
                raise InspectionError("INVALID_GLB", "Truncated GLB chunk header")
            chunk_len, chunk_type = struct.unpack("<I4s", inp.read(8))
            offset += 8
            if chunk_len % 4 or chunk_len > size - offset:
                raise InspectionError("INVALID_GLB", "GLB chunk has invalid alignment or length")
            if chunk_type == b"JSON":
                if found_json or offset != 20:
                    raise InspectionError("INVALID_GLB", "JSON chunk must occur once and first")
                if chunk_len > MAX_JSON_BYTES:
                    raise InspectionError("JSON_TOO_LARGE", "GLB JSON chunk exceeds 32 MiB safety cap")
                obj = _json_bytes(inp.read(chunk_len).rstrip(b"\\x00 \t\r\n"))
                inventory = _inspect_gltf_object(obj, path.parent, warnings)
                found_json = True
            else:
                inp.seek(chunk_len, 1)
            offset += chunk_len
        if not found_json:
            raise InspectionError("INVALID_GLB", "GLB has no JSON chunk")
        return inventory


def _inspect_gltf(path: Path, warnings: list[str]) -> dict:
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InspectionError("JSON_TOO_LARGE", "glTF JSON exceeds 32 MiB safety cap")
    return _inspect_gltf_object(_json_bytes(path.read_bytes()), path.parent, warnings)


def _inspect_zip(path: Path, warnings: list[str]) -> dict:
    try:
        with zipfile.ZipFile(path) as zf:
            info = zf.infolist()
            if len(info) > MAX_ZIP_FILES:
                raise InspectionError("ZIP_TOO_MANY_FILES", "Archive has too many entries")
            total = 0
            seen: set[str] = set()
            entries = []
            for item in info:
                name = item.filename.replace("\\", "/")
                normalized = posixpath.normpath(name)
                if (name.startswith("/") or normalized in ("..", ".") or
                        normalized.startswith("../") or ":" in name or
                        name != item.filename or not name or "\\x00" in name):
                    raise InspectionError("UNSAFE_ZIP_PATH", "Archive has an unsafe entry path")
                if normalized in seen:
                    raise InspectionError("DUPLICATE_ZIP_PATH", "Archive contains duplicate paths")
                seen.add(normalized)
                mode = (item.external_attr >> 16) & 0xFFFF
                if stat.S_IFMT(mode) == stat.S_IFLNK:
                    raise InspectionError("ZIP_SYMLINK", "Archive contains symbolic links")
                if item.file_size > MAX_ZIP_ENTRY:
                    raise InspectionError("ZIP_ENTRY_TOO_LARGE", "Archive entry exceeds 1 GiB")
                total += item.file_size
                if total > MAX_ZIP_UNCOMPRESSED:
                    raise InspectionError("ZIP_TOO_LARGE", "Archive expanded size exceeds 3 GiB")
                if item.file_size > 0 and item.file_size / max(item.compress_size, 1) > MAX_ZIP_RATIO:
                    raise InspectionError("ZIP_BOMB", "Suspicious compression ratio")
                entries.append(name)
    except (zipfile.BadZipFile, OSError) as exc:
        raise InspectionError("INVALID_ZIP", "Archive headers cannot be read") from exc
    warnings.append("ZIP headers inspected only; entries not extracted or CRC-validated")
    return {"entries": len(entries), "entry_names": entries[:100], "animations": None, "animation_names": []}


def _inspect_fbx(path: Path, warnings: list[str]) -> dict:
    with path.open("rb") as fh:
        header = fh.read(256)
    if header.startswith(b"Kaydara FBX Binary  "):
        fmt = "binary"
    elif b"FBXHeaderExtension" in header or header.startswith(b"; FBX"):
        fmt = "ascii"
    else:
        raise InspectionError("INVALID_FBX", "FBX signature not recognized; possible wrong download")
    warnings.append("FBX " + fmt + " detected; animation counts, bones and textures require Blender import")
    return {"fbx_encoding": fmt, "animations": None, "animation_names": []}


def inspect_file(path: str | Path, expected_count: int | None = None,
                 expected_clips: list[str] | None = None) -> dict:
    """Return a JSON-serializable conservative report; never raise user errors."""
    src = Path(path)
    report = {
        "schema_version": "0.1.0",
        "status": "error",
        "file": {"name": src.name},
        "format": src.suffix.lower().lstrip("."),
        "inventory": {},
        "warnings": [],
        "errors": [],
    }
    try:
        if not src.is_file():
            raise InspectionError("FILE_NOT_FOUND", "Input file not found or inaccessible")
        size = src.stat().st_size
        if size == 0:
            raise InspectionError("EMPTY_FILE", "Input is empty")
        report["file"]["size_bytes"] = size
        report["file"]["sha256"] = sha256_file(src)
        kind = report["format"]
        if kind == "glb":
            inventory = _inspect_glb(src, report["warnings"])
        elif kind == "gltf":
            inventory = _inspect_gltf(src, report["warnings"])
        elif kind == "zip":
            inventory = _inspect_zip(src, report["warnings"])
        elif kind == "fbx":
            inventory = _inspect_fbx(src, report["warnings"])
        elif kind == "spz":
            inventory = {"animations": None, "animation_names": []}
            report["warnings"].append("SPZ identified by extension only; splat format, rights and integrity require a compatible viewer")
        else:
            raise InspectionError("UNSUPPORTED_FORMAT", "Supported quick-inspection formats: GLB, glTF, FBX, ZIP, SPZ")
        report["inventory"] = inventory
        if expected_count is not None:
            if inventory.get("animations") is None:
                raise InspectionError("ANIMATION_COUNT_UNKNOWN", "Cannot verify expected animations without format-aware import")
            if inventory["animations"] != expected_count:
                raise InspectionError("ANIMATION_COUNT_MISMATCH", "Animation count does not match expected value")
        if expected_clips:
            if inventory.get("animations") is None:
                raise InspectionError("ANIMATION_COUNT_UNKNOWN", "Cannot verify clip names without format-aware import")
            missing = sorted(set(expected_clips) - set(inventory.get("animation_names", [])))
            if missing:
                raise InspectionError("MISSING_ANIMATIONS", "Missing expected clip names: " + ", ".join(missing))
        report["status"] = "ok"
    except InspectionError as exc:
        report["errors"].append({"code": exc.code, "message": str(exc)})
    except (OSError, ValueError, struct.error) as exc:
        report["errors"].append({"code": "READ_FAILURE", "message": type(exc).__name__ + ": " + str(exc)})
    return report
