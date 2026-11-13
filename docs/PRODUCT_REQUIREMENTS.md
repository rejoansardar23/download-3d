# Product requirements — Download 3D

**Status:** proposed scope; not yet an operational app. **Audience:** product owner, Codex agent, engineering contributors.

## Problem / promise
Today, 3D creation uses disconnected services: Tripo3D/Meshy for models, Marble for environments, Mixamo/Voidless for motion, Blender for editing, and renderers for final video. Downloads may be confusing, animated FBX files may be separate from base model files, and cloud agents may produce a ZIP missing motion, textures, or project files. The creator wants the whole pipeline on the **web**, not local installations, and wants agents to operate repeatably with useful error reports.

## Personas
- **Creator:** submits a model/world URL or uploads files; expects complete editable or previewable output, consistent characters/environments, and no local software installs.
- **Codex Cloud agent:** writes deterministic commands/workflows, records provenance, uploads GitHub source, runs tests, hands off long renders to separately configured compute.
- **Developer:** opens repository, reads requirements and integration contracts, runs the tests, tackles an issue without seeing any private chat.

## Functional requirements
| ID | Requirement | Acceptance evidence |
|---|---|---|
| F01 | Import user-supplied GLB/GLTF/FBX, ZIP and other supported asset formats | File validation + manifest + tests |
| F02 | Source-specific adapters for authorized downloads/exports | Permission gate + adapter tests + diagnostics |
| F03 | Verify asset ID matches requested ID; never silently return a different model | ID assertion test |
| F04 | Preserve original raw files and all available associated animation clips | Source-to-output clip reconciliation |
| F05 | Verify bones, hierarchy, animations, skins, materials, textures | Inspector report + Blender audit if required |
| F06 | Produce ZIP of assets plus manifest, diagnostic report, checksums and license metadata | Unpack/test replay |
| F07 | Browser viewer for meshes/textures and animation selection | Demonstration on authorized sample GLB |
| F08 | Support large Marble worlds, with explicit differentiation: splats, meshes, colliders | Correct viewer/format fallback |
| F09 | Automate mechanical props: doors, car wheels/steering/trunk, drawers, fan rotation | Deterministic object animation tests |
| F10 | Create/retarget human animation and eventually facial acting/lip-sync | Skeletal mapping reports + visually reviewed shots |
| F11 | Headless Blender scene assembly/conversion/rendering in a cloud environment | Captured commands, logs, output checksums |
| F12 | Optional Kaggle-based GPU batch render with authorized credentials and quota | Job package + smoke test, not assumed live integration |
| F13 | Generate preview PNG, GLB, .blend and MP4 when supported | Render/report verification |
| F14 | Reusable named scenes, sets, characters across long video series | Scene manifest and repeatable build |
| F15 | GitHub Actions CI: lint/tests, integrity checks and diagnostics on failure | Green CI with negative cases |
| F16 | Explicit meaningful error for unsupported/authenticated/failed asset retrieval | Error code matrix |

## Non-functional requirements
- Browser-only from creator perspective; *cloud* installation allowed (e.g. container Blender).
- Source files immutable; transformations non-destructive and reproducible.
- No security bypasses, scraping protected exports, published API key harvesting, or unauthorized redistribution.
- No unauthenticated third-party file downloads in CI; no untrusted script execution from assets.
- Start free or near-zero-cost, disclose cloud/GPU/storage usage and limits; do not promise unlimited free compute.
- Usable on Windows browsers, including a portable viewer link; local Blender install never required for a creator.
- Quality over quantity: scene scale, clean topology, pleasant lighting, face/eye quality and lip-sync must be assessed visually, not only by script exit code.

## Proposed first user story
1. User supplies an authorized source link or GLB/FBX.
2. System identifies source and entitlement. If not verifiable, asks user to supply the official export / grant access.
3. Source downloaded via supported workflow or uploaded; source file hashed.
4. Model and optional independent motion clips matched by IDs, skeleton compatibility and metadata.
5. Inspector reports meshes, animation names/count, materials, textures, warnings.
6. Blender-based automated verification converts to browser-ready GLB where appropriate.
7. Web viewer and report show every available animation; optional ZIP includes raw and derived assets.
8. Failures include stage, error code, provider response category, suggested fix and safe log excerpts.

## Key unknowns
Provider export rights/APIs and available file formats vary by plan and asset. No private asset binaries were handed to this repository. Existing model URL reference is not a grant of export rights. See [PROVIDERS](PROVIDERS.md) and [PROJECT_HISTORY](PROJECT_HISTORY.md).
