# Deployment blueprint (proposed, not provisioned)

## Browser viewer
Build a static Three.js site that loads a **permissively licensed test GLB** (or local upload) and enumerates `gltf.animations`; deploy to GitHub Pages/Netlify/Vercel. Provide an upload control that does not send user assets to any server unless explicitly required. Larger private files should be served from authorized object storage.

## API + worker
A managed job API accepts authenticated job requests with immutable asset pointers, validates rights/provenance, schedules bounded Blender workers and publishes results to private artifact storage. Default CPU builds do cheap previews; GPU is optional and billed/limited.

## GitHub
Use code/issues/PRs for development. Use Actions as CI and small artifacts, not a permanent large media CDN. For release media ensure distribution rights and storage policy.

## Kaggle
If authorized, prepare separate Kaggle notebook template that pulls only permitted job packages and saves renders. Confirm current Kaggle API/GPU restrictions and quotas before integrating; avoid any design depending on indefinite sessions.

## Minimum live MVP acceptance
A creator can open the web UI, upload a GLB with two animations, see both listed and played in browser, receive an inspection JSON report, and export a ZIP with source and report. **No provider account is required** for this baseline.
