# Providers and legal integration boundaries

**Disclaimer:** Listed capabilities are aspirations or historically discussed vendor features, not audited current API entitlements. Re-check official current docs and terms before implementation. The provider may charge, gate downloads, vary by plan, or change APIs.

| Service | Intended role | First integration strategy | Limitation / fallback |
| --- | --- | --- | --- |
| Tripo3D | model generation, rigs/motions | Official export/API for owned/authorized models or user-supplied FBX/GLB | Model FBX and motion FBXs may be separate; enumerate and audit |
| Meshy | characters/props/buildings/GLB | Official exports or user upload | Rigging/animation may need Blender/Voidless/Mixamo |
| World Labs Marble | large coherent world prompts / 3D scenes | Supported world exports with permitted rights | SPZ splats not automatically edit-ready polygon meshes |
| Mixamo | animation library, human rigging | User-supplied licensed motion files | Humanoid rig and license/retargeting requirements |
| Voidless | browser-based property/character animation experimentation | User supplies GLB, exports authorized animation | Results and format compatibility require practical validation |
| KIRI Engine | photogrammetry/source geometry | User provides authorized scan export | Scan cleanup/decimation/retopo may be required |
| Blender | scene processing/animation/render | Headless scripts in cloud worker | GUI not hosted inside Codex by default |
| Three.js | browser scene and animation preview | GLTFLoader and AnimationMixer | Cannot edit arbitrary .blend or directly render SPZ by itself |
| Kaggle | optional GPU for batch rendering | User-initiated notebook / supported data handoff | Quotas, notebook policies, session expiration; not an always-on render farm |

## Adapter policy
Every provider adapter must first check whether this exact operation is supported and the user is entitled. An accessible viewer can expose **preview content** while downloads remain gated.

Output contract:
```json
{
  "source_provider": "tripo3d",
  "requested_asset_id": "example",
  "status": "AUTH_REQUIRED",
  "rights_asserted_by_user": false,
  "files": [],
  "warnings": ["Provide an authorized download or supported API grant."],
  "errors": [{"stage": "authorize", "code": "AUTH_REQUIRED"}]
}
```
Codes: `OK`, `AUTH_REQUIRED`, `RIGHTS_UNCLEAR`, `EXPORT_NOT_SUPPORTED`, `NETWORK_FAILURE`, `WRONG_ASSET`, `INCOMPLETE`, `ERROR`.

## Signed URLs and page metadata
Previous discussions mentioned locating `model_url` inside Tripo page data such as `__NUXT_DATA__`. This is a *diagnostic clue* only. Reading public page metadata does not expand user entitlement, and expiring signed URLs must be treated as secrets. **Do not** use page internals to evade export limits, log/store signed links publicly, defeat authentication or redistribute restricted data. Prefer provider APIs, explicit authorized exports and direct user uploads. Never assume cached URL tokens remain valid.

## Download verification
- Verify *requested ID* against provider asset ID before transfer.
- Require HTTP success, allowed MIME/content signature, reasonable size, SHA-256 and no HTML masquerading as FBX/GLB.
- Run checks on each referenced animation clip, not only base model.
- Download retry only for transient network/5xx, with bounded exponential backoff; no 401/403 retry loops.
- If a download requires user sign-in, return `AUTH_REQUIRED`. Do not ask for users' passwords or session cookies in GitHub issues.
