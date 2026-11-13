# Architecture decisions and open questions

## Recorded decisions
- **D001 Browser-only for creator.** Agents may use cloud workers; creator installs nothing locally.
- **D002 GitHub is for code and metadata.** Large / restricted 3D source assets and render outputs live in controlled artifact storage.
- **D003 All animations are a hard acceptance gate** when source inventory/expected clips is known; never silently omit motion files.
- **D004 Preserve original source.** Derived GLB/BLEND/MP4 must have provenance and hash links to input.
- **D005 Use existing tools.** Three.js viewer, Blender automation, ffmpeg, authorized vendor APIs rather than rebuilding everything.
- **D006 Provider export rights first.** No bypassing paid/export controls or login barriers; page URLs alone do not imply ownership.
- **D007 Marble SPZ is treated as splat data.** Do not represent it as mesh without actual meshing process/proof.
- **D008 Kaggle is optional batch compute.** Not a guaranteed permanent GPU server or direct Codex bridge.
- **D009 Start with offline, synthetic tests.** Providers must not be required to run basic CI.
- **D010 No default repository-wide license chosen.** Maintainers decide an appropriate license and third-party attribution policy before external code reuse is encouraged.

## Open questions (do not block foundational work)
- Official Tripo/Meshy/Marble API access, subscription entitlements and permitted public redistribution.
- Which server-side stack and object storage vendor to use when first actual job is deployed.
- Preferred Blender version for FBX importer and GLB exporter.
- Browser splat renderer selection and performance limits for large worlds.
- Standard humanoid skeleton naming, animation fps and scale conventions.
- Job cancellation, storage retention, privacy policy and cost budgets.
- Whether release assets, private bucket or CI artifacts host downloadable sample outputs.
- How to validate motion quality automatically beyond count and clip structure.

## Change process
Record major changes here as `D011+` with problem, alternatives, chosen approach, tradeoff and date. Keep historical decisions; mark superseded instead of silently deleting them.
