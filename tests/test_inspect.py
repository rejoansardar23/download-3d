"""Unit tests do not contact providers, external websites or paid APIs."""
from __future__ import annotations

import json
import struct
import tempfile
import unittest
import zipfile
from pathlib import Path

from download3d.inspect import inspect_file


class InspectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def put(self, name: str, content: bytes | str) -> Path:
        path = self.root / name
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)
        return path

    def assert_error(self, path: Path, code: str, **kwargs) -> None:
        result = inspect_file(path, **kwargs)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["errors"][0]["code"], code)

    def sample_gltf(self) -> dict:
        return json.loads((Path(__file__).parent / "fixtures" / "two_animations.gltf").read_text())

    def test_sample_fixture_names_and_counts(self):
        path = self.put("sample.gltf", json.dumps(self.sample_gltf()))
        report = inspect_file(path, expected_count=2, expected_clips=["Walk", "Wave"])
        self.assertEqual(report["status"], "ok")
        self.assertEqual(report["inventory"]["animation_names"], ["Walk", "Wave"])
        self.assertEqual(len(report["file"]["sha256"]), 64)

    def test_gltf_mismatch(self):
        path = self.put("sample.gltf", json.dumps(self.sample_gltf()))
        self.assert_error(path, "ANIMATION_COUNT_MISMATCH", expected_count=13)
        self.assert_error(path, "MISSING_ANIMATIONS", expected_clips=["Hug"])

    def test_gltf_malformed(self):
        self.assert_error(self.put("bad.gltf", "{broken"), "INVALID_JSON")

    def test_wrong_metadata_type(self):
        obj = self.sample_gltf()
        obj["meshes"] = None
        self.assert_error(self.put("invalid.gltf", json.dumps(obj)), "INVALID_GLTF")

    def test_glb_with_nul_json_padding(self):
        obj = json.dumps(self.sample_gltf()).encode("utf-8")
        padded = obj + bytes((4 - len(obj) % 4) % 4)
        payload = struct.pack("<4sII", b"glTF", 2, 20 + len(padded)) + struct.pack("<I4s", len(padded), b"JSON") + padded
        self.assertEqual(inspect_file(self.put("nul.glb", payload))["status"], "ok")

    def test_empty(self):
        self.assert_error(self.put("empty.gltf", ""), "EMPTY_FILE")

    def test_missing(self):
        self.assert_error(self.root / "missing.glb", "FILE_NOT_FOUND")

    def test_safe_uri_rejection(self):
        obj = self.sample_gltf()
        obj["images"] = [{"uri": "../secrets.txt"}]
        self.assert_error(self.put("bad.gltf", json.dumps(obj)), "UNSAFE_URI")

    def test_percent_encoded_traversal(self):
        obj = self.sample_gltf()
        obj["buffers"] = [{"uri": "%2e%2e/secret.bin", "byteLength": 10}]
        self.assert_error(self.put("bad.gltf", json.dumps(obj)), "UNSAFE_URI")

    def test_missing_dependency_warns(self):
        obj = self.sample_gltf()
        obj["images"] = [{"uri": "texture.png"}]
        result = inspect_file(self.put("missing_texture.gltf", json.dumps(obj)))
        self.assertEqual(result["status"], "ok")
        self.assertTrue(any("Missing referenced" in x for x in result["warnings"]))

    def test_valid_glb(self):
        obj = json.dumps(self.sample_gltf()).encode("utf-8")
        padded = obj + b" " * ((4 - len(obj) % 4) % 4)
        payload = struct.pack("<4sII", b"glTF", 2, 20 + len(padded)) + struct.pack("<I4s", len(padded), b"JSON") + padded
        result = inspect_file(self.put("sample.glb", payload), expected_count=2)
        self.assertEqual(result["status"], "ok")

    def test_wrong_glb_length(self):
        data = b"glTF" + struct.pack("<II", 2, 200) + b"\\x00" * 8
        self.assert_error(self.put("bad.glb", data), "GLB_INVALID_LENGTH")

    def test_html_disguised_as_glb(self):
        self.assert_error(self.put("oops.glb", "<html>not an asset</html>"), "INVALID_GLB")

    def test_zip_slip(self):
        path = self.root / "slip.zip"
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("../secret.txt", "bad")
        self.assert_error(path, "UNSAFE_ZIP_PATH")

    def test_zip_normalized_parent_path_rejected(self):
        path = self.root / "nested.zip"
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("sub/../model.glb", "bad")
        self.assert_error(path, "UNSAFE_ZIP_PATH")

    def test_zip_duplicate(self):
        path = self.root / "dup.zip"
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(path, "w") as zf:
                zf.writestr("same.txt", "one")
                zf.writestr("same.txt", "two")
        self.assert_error(path, "DUPLICATE_ZIP_PATH")

    def test_zip_metadata_only(self):
        path = self.root / "good.zip"
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("raw/model.txt", "not a 3d model")
        report = inspect_file(path)
        self.assertEqual(report["status"], "ok")
        self.assertEqual(report["inventory"]["entries"], 1)
        self.assertTrue(any("headers" in x for x in report["warnings"]))

    def test_fbx_count_unknown(self):
        path = self.put("rig.fbx", b"Kaydara FBX Binary  " + b"\\x00" * 50)
        report = inspect_file(path)
        self.assertEqual(report["status"], "ok")
        self.assertIsNone(report["inventory"]["animations"])
        self.assert_error(path, "ANIMATION_COUNT_UNKNOWN", expected_count=13)

    def test_spz_not_claimed_mesh(self):
        report = inspect_file(self.put("splat.spz", b"not necessarily a valid splat"))
        self.assertEqual(report["status"], "ok")
        self.assertTrue(any("extension only" in x for x in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
