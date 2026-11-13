# Roadmap & contribution backlog

**Priority rule:** first solve reproducible asset verification. A beautiful frontend cannot repair missing motion clips or a fake download ZIP.

## P0: foundation and trustworthy intake
- [ ] **P0.1** Establish complete docs + contributor rules + safe CI (this repo foundation).
- [ ] **P0.2** Build offline GLB/glTF header and metadata inspector with JSON reports and malicious-input tests.
- [ ] **P0.3** Implement ZIP inspection/packaging with path traversal and size checks; file checksums.
- [ ] **P0.4** Introduce rights provenance, source ID validation and manifest schema validation.
- [ ] **P0.5** Provide synthetic sample rig with 2+ animations and baseline metrics.

## P1: authorized provider acquisition
- [ ] **P1.1** Formal provider-adapter interface plus mock adapter and failure code mapping.
- [ ] **P1.2** Tripo: confirm documented official export API/rights; map base model + separately available motion clips.
- [ ] **P1.3** Meshy: supported export API/user upload and texture handling.
- [ ] **P1.4** Marble: authorized world export; SPZ vs GLB vs collider differentiation.
- [ ] **P1.5** Retries, response integrity, exact ID matching, no token logging, diagnostics.
- [ ] **P1.6** Cloud storage for raw/derived assets and retention/deletion.

## P2: web proof
- [ ] **P2.1** Three.js GLB viewer with camera orbit, scale, lighting, animation list and scrub/play.
- [ ] **P2.2** Error/metadata panel listing every discovered, downloaded and exported clip.
- [ ] **P2.3** Separate splat viewer if SPZ source is present and license permits preview.

## P3: Blender automation
- [ ] **P3.1** Headless Blender importer/exporter and automation tool version pinning.
- [ ] **P3.2** Validate FBX skeleton, textures, action counts, export mapping to GLB.
- [ ] **P3.3** Mechanical rigging: sedan doors/wheels/steering/trunk, fan and drawer.
- [ ] **P3.4** Human retargeting and motion QA.
- [ ] **P3.5** Modular scene assembly with cameras and lighting presets.

## P4: cloud rendering
- [ ] **P4.1** Reproducible CPU small preview builds and test assets.
- [ ] **P4.2** Web artifact storage/download with hashes and access controls.
- [ ] **P4.3** Optional Kaggle notebook/job-packaging integration, verify quotas and policies.
- [ ] **P4.4** Video output pipeline, deterministic encoding, render QA.

## P5: creator-quality films
- [ ] **P5.1** Cinematic sets: train station, markets, interiors, coast/boats; reusable scene library.
- [ ] **P5.2** Visual quality rubric for face/eyes/expressions, environments, textures and pacing.
- [ ] **P5.3** Dialogue, multilingual speech, lip-sync, sound and subtitles.
- [ ] **P5.4** Multi-episode production planning and asset catalog with provenance.

## Definition of done for every item
- Clear owner, reproduction command, *authorized* test input, expected result, actual evidence and cost.
- Offline unit tests or deterministic fixture tests and passing CI where applicable.
- No unredacted secrets, signed query parameters or restricted media files committed.
- Docs updated, next limitations recorded.
- No declaration of full animation preservation without verifying all expected clips.

## Starter issue suggestions
1. **[P0] glTF/GLB metadata inspector + JSON manifest** — no vendor access needed.
2. **[P0] ZIP safety and check-sum packaging** — adversarial regression tests.
3. **[P0] synthetic animation fixture** — two distinct clips; check animation names/durations.
4. **[P1] provider adapter spec** — fake/mock provider first, include 401/403/DNS cases.
5. **[P2] GLB viewer** — static deployed demo using synthetic rig.
6. **[P3] Blender FBX action reconciler** — license-clean test assets.
