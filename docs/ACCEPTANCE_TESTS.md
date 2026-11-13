# Acceptance test catalog

A feature can be called "working" only when reproducible on permitted input. Log exact tool versions, system, commands and SHA-256. The repo CI intentionally begins offline.

## Mandatory testing matrix
| Case | Input | Expected |
| --- | --- | --- |
| T01 | Minimal valid glTF with no animations | Inspect as 0 GLTF animations (not "missing" unless expected > 0) |
| T02 | GLB with 2 clips | List exactly 2 named clips and validate nonempty channels |
| T03 | Wrong/corrupt GLB magic | Nonzero exit and actionable error |
| T04 | Inconsistent GLB length or missing JSON chunk | Reject |
| T05 | glTF with external missing resource | Identify incomplete dependency at packaging/import step |
| T06 | ZIP entry `../escape.glb` | Reject archive as unsafe |
| T07 | ZIP with duplicate names/huge unzip ratio | Reject or flagged unsafe |
| T08 | FBX model only, clips supplied separately | Never declare "all animations" until source-to-output reconciled |
| T09 | Base FBX with zero imported actions | `animation_count=unknown` when only fast inspector used; Blender audit required |
| T10 | 13 expected clips, 12 packed | Fail completeness with missing clip name/ID |
| T11 | Viewer HTML returned in place of binary | `WRONG_MIME`/validation error, not success |
| T12 | Provider returns 401/403 | `AUTH_REQUIRED/FORBIDDEN`, no abusive retries |
| T13 | DNS or proxy 403 | Distinct connectivity error and safe diagnostic |
| T14 | Provider asset ID differs from requested ID | `WRONG_MODEL_ID` and refuse bundle |
| T15 | Splat SPZ file | Correctly identify splat, not pretend topology-editable FBX |
| T16 | Browser viewer with sample 2-clip GLB | Both animations selectable/playable |
| T17 | Car with separate wheels and doors | Independent tested movements in GLB |
| T18 | Cloud render job | Low-res preview, correct artifact manifest, bounded resource usage |

## Evidence required
A test result must include input license, source checksum, command, exit code, sample output manifest, static or video preview when visual, count comparison, known defects and expected cost. If source download is not authorized/possible, record **blocked**, not passing.

## CI coverage versus future manual tests
Initial CI should cover glTF/GLB/ZIP parser safety and negative cases. Real provider API integration, Blender FBX import, browser render/animation, and GPU jobs require separately configured and reviewed test infrastructure.
