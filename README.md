# Download 3D — Cloud-first 3D acquisition, animation & filmmaking

> **Stage: project foundation, not a finished product.** This public repository is the durable source of truth for contributors and Codex Cloud agents. The aims below were collected from prior discussions; no external download, Blender job, or GPU integration is claimed functional until verified.

## Vision

Build a **browser-first creator workspace** that helps users obtain **3D assets they are authorized to download**, inspect them, preserve **all existing animation clips**, create or edit new character and mechanical animations, assemble rich reusable environments, preview scenes on the web, and render videos using cloud infrastructure. **No software installation on the user's local Windows computer is required.** Avoid wasting Codex compute reimplementing mature open-source tools.

A key usability goal is to remove repetitive manual *Export* clicks **when an authorized API, provided model file, permitted direct download, or supported integration exists**. Never bypass authentication, payment tiers, rate limits, access controls, or license terms. Publicly viewable preview URLs do not themselves grant export rights.

## What the creator wants

- **Tripo3D / Meshy:** bring in models (GLB/GLTF/FBX with textures where available); verify that the correct asset and **every available animation clip** are preserved, not only mesh, rig, preview or one action.
- **World Labs Marble:** use a small number of prompts to build large reusable environments; understand the difference between **Gaussian splats (SPZ/PLY)**, collider models, and usable high-quality textured **mesh (GLB)** exports.
- **3D animation:** human characters with expressive eyes, believable facial acting/lip-sync, plus independently movable **car wheels/steering/doors, train doors, drawers, fans, props**.
- **Cloud-only creative pipeline:** Codex Cloud orchestrates Blender scripts and tests; browser viewer shows results; optional Kaggle GPU performs batch rendering *only if practical and permitted*. Save source in GitHub, large media in artifact storage.
- **Film production:** reuse characters and sets across long series; generate quality test clips, then dialogue, sound, subtitles, transitions and MP4 deliverables.
- **First case study:** a visually consistent railway-station story using ticket hall, covered platform and passenger-carriage sets, plus separate train/props/characters.

## Development map

| Read this | Purpose |
| --- | --- |
| [docs/PRODUCT_REQUIREMENTS.md](docs/PRODUCT_REQUIREMENTS.md) | Goals, use cases, functional / non-functional requirements |
| [docs/PROJECT_HISTORY.md](docs/PROJECT_HISTORY.md) | Prior discussions, examples, evidence vs unverified claims |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Components, proposed directory layout, data flow |
| [docs/PROVIDERS.md](docs/PROVIDERS.md) | Tripo3D, Meshy, Marble, Mixamo, Voidless, Blender |
| [docs/ASSET_FORMATS.md](docs/ASSET_FORMATS.md) | Mesh, texture, skeleton, animation, SPZ and metadata |
| [docs/ANIMATION.md](docs/ANIMATION.md) | Clip preservation, rigs, vehicles, mechanical animation |
| [docs/CLOUD_PIPELINE.md](docs/CLOUD_PIPELINE.md) | Codex Cloud, browser preview, Blender, Kaggle, GitHub |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Phased delivery and prioritized backlog |
| [docs/ACCEPTANCE_TESTS.md](docs/ACCEPTANCE_TESTS.md) | Proof needed before calling a feature complete |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Decisions, open questions, assumptions |
| [docs/ONBOARDING.md](docs/ONBOARDING.md) | Contributor's first hour and development workflow |
| [docs/AGENT_INSTRUCTIONS.md](docs/AGENT_INSTRUCTIONS.md) | Safe, cost-conscious instructions for Codex |
| [examples/train-station/README.md](examples/train-station/README.md) | First production benchmark and asset plan |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution / PR rules |
| [SECURITY.md](SECURITY.md) | Rights, secrets, URLs, downloads and supply-chain boundaries |

## Project status

| Capability | Status |
| --- | --- |
| Requirements and architecture | Documenting |
| Live Tripo / Marble downloads | **Not verified in this repository** |
| Model or world files stored in repo | **None** |
| Animation clips recovered from example links | **Not verified** |
| Web viewer, cloud Blender, Kaggle rendering | **Not implemented** |
| Reproducible tests / starter scripts | Initializing |

Previous chat transcripts contain some claims of successful model retrieval or SPZ download; they are **historical reports, not independently reproduced proof**. File presence, permitted rights, checksums and inspections are the source of truth.

## How to start contributing

1. Read [ONBOARDING](docs/ONBOARDING.md) and [ROADMAP](docs/ROADMAP.md).
2. Select the earliest **unblocked** issue in [GitHub Issues](../../issues); start with authorized sample-fixture tests and model inspection.
3. Prove behavior with a test and a short before/after report. Update the capability table when evidence changes.
4. Keep downloaded model binaries, credentials and expiring signed URLs **out of git**.
5. Submit a focused pull request with acceptance evidence; no paid API/key should be necessary for baseline tests.

## Tracked historical examples (URLs, **not distributed assets**)

- Tripo model: https://studio.tripo3d.ai/3d-model/0dd9240e-82d2-4885-b44b-657bba4c9b3a
- Other discussed Tripo example: https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e
- Marble world: https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab
- Marble VR viewer (same world): https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab

All links may require authentication/rights, may expire or change, and may expose only a preview. See [PROVIDERS](docs/PROVIDERS.md).

**License:** no repository-wide open-source license has been selected yet. Contributors should not assume permission to redistribute third-party assets or reuse code outside GitHub's default terms until a license is chosen.
