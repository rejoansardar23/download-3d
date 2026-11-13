# Data contracts (draft v0.1)

## Manifest
```json
{
  "schema_version": "0.1.0",
  "job_id": "example-safe-fixture",
  "status": "inspected",
  "source": {
    "provider": "upload",
    "requested_asset_id": "synthetic-rig",
    "detected_asset_id": "synthetic-rig",
    "rights_asserted": true,
    "license": "CC0-1.0",
    "url_redacted": null
  },
  "files": [
    {
      "path": "raw/synthetic.glb",
      "role": "model",
      "format": "glb",
      "size_bytes": 512,
      "sha256": "record_real_sha256_here"
    }
  ],
  "inventory": {
    "mesh_count": 1,
    "skin_count": 1,
    "animations": [
      {"name": "Walk", "source_file": "raw/synthetic.glb"},
      {"name": "Wave", "source_file": "raw/synthetic.glb"}
    ],
    "texture_count": 0
  },
  "errors": [],
  "warnings": []
}
```

The values above are **illustrative** and not an observed artifact. Do not claim `size_bytes=512` or 2 animations for real files without inspection.

## Diagnostic record
```json
{
  "stage": "inspect",
  "code": "GLB_INVALID_LENGTH",
  "severity": "error",
  "message": "Declared length differs from actual bytes.",
  "retryable": false,
  "suggested_action": "Re-export the authorized GLB or retry a permitted download."
}
```

## Future provider adapter interface
```python
class ProviderAdapter:
    def validate_reference(self, reference): ...
    def check_entitlement(self, request_context): ...
    def list_official_exports(self, asset_id): ...
    def fetch_authorized_artifact(self, artifact_id): ...
    def report(self): ...
```
No developer should write a generic "download any link with credentials" implementation. Use an explicit allowlisted supported provider integration and private authorization system.

## Versioning
Contract change rules: patch for more diagnostics, minor for additive fields, major for incompatible rename/removal. The first implementation can emit a reduced quick-inspection report; explicitly label it an **inspection report**, not a complete provider manifest.
