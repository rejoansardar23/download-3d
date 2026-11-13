# Cloud-only workflow: Codex, Blender, browser viewer, GitHub, Kaggle

## Creator constraint
The creator does **not** want to install Blender locally. Codex Cloud can write scripts and run CLI tools in its execution environment, but the creator cannot assume direct access to Codex's private GUI/workspace. A separate deployed browser preview is required.

## Minimum working path
1. Developer/Codex commits source, fixtures and CI to GitHub.
2. An authorized user-supplied 3D asset is stored in controlled artifact storage, not in a public repository.
3. Blender in a cloud container executes e.g. `blender -b --python scripts/scene_build.py -- --config job.json`.
4. Worker emits `.blend`, `.glb`, preview PNG and structured logs; later video renders `.mp4`.
5. Files upload to an artifact bucket (or GitHub Actions artifacts for small test outputs) with signed **short-lived** access.
6. Static frontend on GitHub Pages/Netlify/Vercel loads the GLB and plays animations; edits remain in scripted Blender jobs.
7. Optional separate Kaggle notebook consumes a **pre-signed, permissioned job package** and writes results back to controlled storage. User may need to run a notebook manually, and Kaggle limits apply.

## Limitations to communicate
- **Codex Cloud is not a guaranteed GPU workstation.**
- **Kaggle GPUs are not a persistent general-purpose server,** and programmatic orchestration depends on currently supported APIs, authentication and quotas.
- **GitHub Pages is not a 3D rendering backend**, but can host a viewer.
- **GLB web viewer is not full Blender in the browser.** It can display meshes and play animation clips; authoring needs scripts/services.
- **Spending zero money** is an optimization target; storage, data transfer, credits and GPU hours may impose caps.
- No API keys in the repo or GitHub workflow input fields that might be public; use scoped secrets only in private trusted environments when needed.

## Suggested job package
```
job/
  job.json              # source artifact identifiers, script entry, settings
  scene_assets.json     # refs to permitted immutable source objects
  checksums.sha256
  scripts/              # pinned, reviewed code
```
Outputs:
```
results/
  job-report.json
  scene.blend
  preview.png
  preview.glb
  render.mp4            # optional, rendered only if requested
  checksums.sha256
```

## Cost-conscious render ordering
Validate schema -> smoke-test import -> low-res graybox preview -> brief test animation -> full-quality render. Reject oversized jobs early; cache assets and intermediate transformations; support cancellation and retries with checkpoints.

## CI approach
GitHub Actions runs **offline Python tests and optional tiny synthetic model checks only** by default. It must never secretly fetch private Tripo/Marble assets or use undisclosed third-party accounts. Add provider end-to-end tests only with explicit authorized test assets and suitable secret handling, never public signed links.
