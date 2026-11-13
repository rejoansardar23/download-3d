# First quality benchmark: railway-station sequence

**Status:** scene plan / product test case, not supplied assets or finished render.

## Goal
A cinematic, coherent, reusable railway station set rather than a tiny or inconsistent scene. A creator can walk an animated character through an exterior approach, entrance/ticket hall, covered platform and railway carriage. Use a limited set of high-quality reusable modular assets and consistent visual scale.

## Asset inventory
- **Environment:** entrance/exterior, ticket hall, signs, timetables, stairs/overpass, covered platform, rails/ballast and carriage interior.
- **Vehicles:** train locomotive/passenger carriages with independently animated doors and bogies where needed.
- **Characters:** main character(s), passengers and staff with rigged walking/standing/sitting actions; clean full-body silhouettes and believable facial features.
- **Props:** ticket counters, benches, lights, suitcases, clocks and signs; movable doors and small mechanical elements.
- **Lighting/cameras:** wide establishing shot, tracking camera, mid-shots and closeups.

## Build strategy
1. Block out geometry using real-world scale and rough cameras.
2. Add stable material/textures and place modular props.
3. Import only licensed/synthetic characters and clip inventory.
4. Verify walking, waiting, entering carriage, opening doors and sitting in source and GLB.
5. Render small preview images/short clips. Review composition before heavy rendering.
6. Keep all shots and asset references in versioned scene JSON; keep binary assets outside source repository.

## Quality scorecard
Geometry scale and spacing, lighting, texture continuity, face/eye quality, animation foot contact, correct pivots, stable camera, dialogue clarity, lip-sync and sound. Passing structural/automated tests is necessary but **not sufficient** for cinematic quality.

## Provenance
This benchmark synthesizes prior creator concerns about poor-looking characters/environments and the wish to create long reusable series. No external video or asset is included or licensed by this plan.
