# Troubleshooting and actionable errors

Do not ask another agent to "somehow download it" without a stage-specific diagnosis. Reproduce with permissioned inputs, capture safe error codes and fix the actual cause.

| Symptom | Likely category | Test | Correct response |
| --- | --- | --- | --- |
| Page loads but file fetch returns 401 | Authentication | Check documented export/API entitlement | Request supported authorization; don't bypass |
| File fetch returns 403 | Forbidden/expired/proxy | Compare provider error vs `CONNECT tunnel failed 403` | Report exact stage; no auth bypass |
| `Could not resolve host` | DNS/network | Check from authorized runner | Fix DNS/egress or change permitted network |
| Link expires after some minutes | Signed URL expired | Check timestamp without exposing query | Re-request from supported flow |
| ZIP contains HTML only | Wrong MIME/payload | Inspect file magic/header | Reject ZIP; don't call download successful |
| Model ID differs | Wrong asset/page data | Compare requested and detected ID | Stop; never package a different model |
| FBX loads without motion | Motions separate or importer issue | Inspect base actions and additional FBXs | Gather authorized motion files; reconcile clips |
| 13 motion files but output has 1 action | Import/export mismatch | Enumerate Blender actions & GLB animations | Fail completeness gate; debug exporter |
| Texture missing | Relative dependencies / unpack failure | Resolve source texture URLs/paths | Include source and report unresolved references |
| Marble SPZ loads as point cloud | Format mismatch | Detect splat encoding | Use splat viewer or supported mesh export |
| Blender CPU render slow | Hardware/scene complexity | Low-res preview first | Optimize + optional permitted GPU batch job |
| Unexpected animation orientation | Rest-pose/scale mismatch | Compare armature mappings | Retarget; store remapping metadata |

## Minimum safe diagnostic record
```json
{
  "stage": "download",
  "code": "NETWORK_FAILURE",
  "provider": "tripo3d",
  "requested_id": "example-id",
  "host": "example.invalid",
  "http_status": null,
  "bytes_received": 0,
  "retryable": true,
  "message": "DNS lookup failed",
  "next_action": "Check allowed runner egress and DNS"
}
```

Never include signed query strings, session cookie headers or bearer tokens in issues, logs or diagnostics.

## Triage sequence for developers
1. Authorization and provider support? 2. Correct ID? 3. Network/HTTP status? 4. Bytes and signature? 5. Unpacked paths/checksums? 6. Model/rig import? 7. All motion files? 8. All exported actions? 9. Web playback? 10. Visual QA?

## When to report blocked
Return a precise `AUTH_REQUIRED` or `EXPORT_NOT_SUPPORTED` rather than recommending unsafe techniques. If provider provides an official file, the user can upload that file to the tool and the rest of the pipeline continues without any special workaround.
