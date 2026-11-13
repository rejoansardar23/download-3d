# Authorized model download and animation-preservation runbook

This runbook is intended for humans, Codex Cloud agents and contributors. It is **not proof of live vendor access** and does not authorize bypassing export restrictions.

## Key historical case
The creator wanted the 3D model referenced at [Tripo model e3bca070...](https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e) and a later example at [0dd9240e...](https://studio.tripo3d.ai/3d-model/0dd9240e-82d2-4885-b44b-657bba4c9b3a). Prior work **reported** a separately downloadable base rig FBX and 13 animation FBXs for one example, with 65 bones and four textures. These are chat reports, not reproduced files, hashes or universal provider behavior.

The required outcome is the model **and all motion that the specific user is entitled to export**; a base FBX without clips does not satisfy the user's request.

## Procedure (supported exports/files only)

### 1. Identify and authorize
Record exact provider, exact model ID, user entitlement, approved export method, timestamp and expected formats. Verify an official API/export is available for the specific account or ask user to supply the permitted exported files. A shareable preview is **not** a download authorization.

### 2. Enumerate files
Get the supported provider inventory or a user-uploaded file list. Classify base model, texture files, motion files, rig, previews, colliders, splats; list exact per-file names/IDs, sizes if known, and which animations each contains. **Do not assume 13** for all models.

### 3. Acquire each entitled file separately
Use official API/export/direct user-provided file location. Verify requested asset identity **before** download, obey rate limits, and never dump a signed URL (query tokens, cookies) to logs. Retry transient network failures only. Differentiate:
- `AUTH_REQUIRED`: valid login/grant required;
- `FORBIDDEN`: provider denied this export, including paid-plan or rights restrictions;
- `EXPIRED_URL`: time-limited authorized link expired; request another through official means;
- `DNS_FAILURE`, `PROXY_DENIED`: runner network problem (`Could not resolve host`, `CONNECT tunnel failed, response 403`);
- `WRONG_MODEL_ID`: discovered file doesn't match requested model ID;
- `WRONG_MIME`: HTML/JSON preview instead of actual FBX/GLB/etc;
- `INCOMPLETE_TRANSFER`: partial size or checksum failure.

### 4. Validate files
On available file:
```bash
PYTHONPATH=src python -m download3d inspect /path/to/authorized/model.glb --out report.json
```
For FBX this quick checker can only identify probable format, **not count bones/actions**. Use a cloud Blender worker to import and audit motions/textures. For .SPZ use a dedicated splat verifier. A ZIP header check is not a complete unpack/test.

### 5. Reconcile all motions
Create matrix:
| Source motion ID | Source file hash | Imported Blender action | Exported GLB animation | Result |
| --- | --- | --- | --- | --- |
| e.g. walk | measured | measured | measured | pass/fail |
| e.g. run | measured | measured | measured | pass/fail |

If the provider reports N entitled motions, require all N rows to pass. Never interpret missing source inventory as N=0. Document skipped/unsupported motions as failures or waivers, not silent omissions.

### 6. Package and prove
Expected structure: `raw/model.*`, `animations/*.fbx`, `textures/*`, `converted/*.glb`, `manifest.json`, `diagnostics.json`, `CHECKSUMS.sha256`, optional previews. Re-open the ZIP in a clean job; revalidate hashes, imports and motion list. Store resulting archives in authorized artifact storage, not public source GitHub.

### 7. Browser preview and video
Show meshes/textures, rig/skeleton evidence, animation selectors and motion counts. Browser viewer is not an actual Blender editor. Cloud Blender should render a short preview before any long GPU render.

## If the provider cannot be accessed
Return a blocking status and precise instructions for obtaining authorized files; do not fabricate the archive, claim success from a screenshot, bypass authentication or keep retrying 403 indefinitely. The project must still work with **user-provided exported files** while provider adapters are developed.

## What to send in a GitHub issue
Safe diagnostic: provider name, *non-secret* model ID, stage, error code, HTTP category (not signed URL), file type/size/checksum, expected vs actual motion count, Blender version if relevant, redacted stack trace, reproduction steps using a synthetic fixture. Never publish credentials, private asset URLs, downloads or personal data.
