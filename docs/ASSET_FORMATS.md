# Formats, provenance and packaging

## Format matrix
| Format | What it usually stores | Inspector / viewer | Key caveat |
| --- | --- | --- | --- |
| `.glb` | binary glTF mesh/materials/skeleton/animation | Inspect JSON chunk; browser GLTFLoader | Not every external/extension feature supported |
| `.gltf` | JSON glTF referencing buffers/textures | Inspect JSON; browser GLTFLoader | Needs referenced .bin/images and safe paths |
| `.fbx` | mesh/rig/materials/motion depending on export | Blender FBX importer; deeper audit required | Base model may have 0 clips while motion FBXs are separate |
| `.blend` | editable Blender project | Blender CLI/GUI | Version-specific; unsuitable as web viewer input |
| `.obj` | geometry/material reference | Blender import | Does not capture skeletal animation |
| `.spz` | compressed Gaussian splats | Dedicated splat viewer/compatible import | Not topology-editable textured mesh by default |
| `.ply` | polygon/point/splat data depending on producer | Dedicated tools | Determine exact schema before claiming mesh |
| `.zip` | bundle/container | secure inspect before extraction | Unsafe entries/symlinks/bombs must be blocked |
| `.mp4` | encoded final video | browser player | No editable skeleton or 3D scene |

## Mandatory manifest
Keep a JSON manifest accompanying **every** deliverable. See [DATA_CONTRACTS](DATA_CONTRACTS.md). Minimum:
- schema version, job ID, timestamp, provider, requested asset ID, detected asset ID;
- rights/provenance, original URL **without query tokens**, source SHA-256;
- file path, MIME/signature, size, checksum, role (`model`, `motion`, `texture`, `preview`, etc.);
- animation name, count, clip/file mapping, target rig, frames/fps if inspected;
- materials, textures, bones count, mesh count if known;
- conversion tool/version, warnings and errors;
- derived artifact SHA-256, license metadata, storage pointer/retention.

If an inspector does not support FBX motions, it should report `unknown`, never `0` by assumption.

## Safe archive contract
```
download-3d-result/
  manifest.json
  diagnostics.json
  raw/                     # unmodified source files
  animations/              # separately obtained source motions
  converted/               # output GLB/BLEND when available
  previews/                # thumbnails/playblasts
  CHECKSUMS.sha256
```
Raw data stays outside source git. Never overwrite the raw input with a converted mesh. Reject archive paths that leave the extraction root and files that exceed configured limits.

## Integrity gates
Correct asset identity; nonzero size; magic/JSON syntax; known license or user authorization; SHA-256 recorded; animation clips reconciled against available source inventory; textures included or reported; output independently opened by a format-aware tool.
