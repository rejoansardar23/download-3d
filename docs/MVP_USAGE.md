# Baseline inspector: developer quickstart

**Implemented scope:** offline structural checks for provided GLB, glTF, FBX, ZIP, SPZ; JSON reports and negative-case tests. **Not implemented:** provider downloads, true FBX animation import, SPZ decode, Blender conversion, server app, viewer or renders.

## Try it (cloud runner or any developer computer)
```bash
export PYTHONPATH=src
python -m unittest discover -s tests -v
python -m download3d inspect tests/fixtures/two_animations.gltf \
  --expected-count 2 --expected-clip Walk --expected-clip Wave \
  --out reports/synthetic-inspection.json
```
PowerShell: `$env:PYTHONPATH="src"`.

## Inspect an authorized real model
```bash
PYTHONPATH=src python -m download3d inspect /path/to/authorized/model.glb --out report.json
```

Exit code `0` means the quick **structural** inspection succeeded, not that a full Blender import or provider entitlement succeeded. Exit code `1` means check failed and JSON includes structured error code.

For FBX or SPZ, counts are explicitly unknown unless a proper format-aware inspector is added. A ZIP is checked for *unsafe entries and metadata only*, not unpacked, CRC-validated or declared a complete model. All source animations must be reconciled before claiming a complete bundle.

## CI
[GitHub Actions](../.github/workflows/ci.yml) runs tests and validates a synthetic two-clip glTF fixture. No vendor credentials or paid services are required; CI attaches a small diagnostic report. Future provider integrations will need separately reviewed permissioned tests.
