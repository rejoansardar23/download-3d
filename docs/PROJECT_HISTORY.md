# Project history and recovered context

This is a **human-readable summary of earlier project discussions**, not a complete verbatim chat export. Dates are November 2026 where known. Many asset/download outcomes were *reported in prior chats* and are not independently reproduced in this repository. Keep a bright line between historical report and verified engineering evidence.

## Core conversations
- **November 10:** User requested downloading World Labs Marble scene via viewer links without the manual Export control; wanted a full environment reusable across hours of episodes rather than one small set per prompt. Requested detailed prompts and asset segmentation guidance.
- **November 10:** User requested the actual Tripo asset, not a webpage/screenshot/empty ZIP. A prior text transcript described a method of reading a page data payload (including `__NUXT_DATA__`), matching the **exact model ID**, and using a returned model URL. Treat as unverified historical method, **not an authorization shortcut**, API guarantee, or prescription to bypass export controls.
- **November 10–11:** The user identified that downloading only a character FBX was insufficient: the rig and motion clips may reside in **separate files**. They requested that all supported animations be bundled; the intended motion list from a prior report is below.
- **November 11:** User requested a complete guide plus improved GitHub Actions so other agents can diagnose model download errors, correct ID mismatches, ZIP omissions and failed imports.
- **November 12–13:** Broader vision encompasses Meshy/Tripo, Marble, mechanical props, cloud Blender + web preview, Kaggle GPU rendering, Codex Cloud, GitHub, and eventual high-quality animated films / long series.

## Tripo cases
### Reference A
https://studio.tripo3d.ai/3d-model/0dd9240e-82d2-4885-b44b-657bba4c9b3a

This is the user's November 11 example. Download access, file payloads, license, bones/animation inventory and export status are **not verified here**.

### Reference B
https://studio.tripo3d.ai/3d-model/e3bca070-3984-4aa3-8d54-1192acc9da1e

Earlier work reportedly:
- found a model FBX with textures and 65-bone skeleton;
- found **13 additional animation FBX files**, separate from the original model;
- claimed four packed textures and clip types: walking, running, running upstairs, turning, waiting, sitting, agreeing, hugging, fear, crying, anger, digging, falling;
- described a validation/bundling flow after the initial rigged FBX lacked animations.

**Evidence status:** reported by a previous assistant, not verified by repository contents, live provider access, imported FBX tests or artifact hashes. Do not assert that these clips are guaranteed to exist for all Tripo models, and do not set 13 as a universal clip count.

### Recorded failure classes
- Network/proxy failures such as `CONNECT tunnel failed, response 403` and `Could not resolve host`;
- model ID mismatch or stale page data;
- expiring/unauthorized asset URLs;
- base FBX downloaded but animation FBXs missing;
- textures absent from extracted archive;
- unsupported FBX import/no Blender;
- ZIP produced with wrong directory structure;
- network accessible viewer but authenticated download endpoint;
- viewer returned HTML rather than real 3D binary.

See [TROUBLESHOOTING](TROUBLESHOOTING.md).

## Marble case
- World: https://marble.worldlabs.ai/world/608d6222-8bb9-4575-8845-b1efd2f980ab
- VR view: https://marble.worldlabs.ai/worldvr/608d6222-8bb9-4575-8845-b1efd2f980ab
- Prior chat reportedly identified `Futuristic_Tropical_Ocean_Cliff_Resort.spz` (approx. 30 MB and 1.92 million Gaussian splats).
- Prior report also described authenticated download gating (`Sign In To Download Assets` / an HTTP 401 API response).

**Evidence status:** not accompanied by authorized file, hashes or a reproducible asset manifest in this repo. SPZ Gaussian splats are not equivalent to a textured topology-editable GLB/FBX mesh. A viewer page that opens does not give license to redistribute the world.

## Relevant wider creative requirements
- Character appearance must be clean, human-like, expressive and consistent across front/side/back camera views, not low-quality or dirty tiny assets.
- Sets can include market buildings, roads, interiors, sea/boats, railway station, passengers, vehicles, props; prioritize reusable modular scenes.
- Mechanical animation: independently controlled doors, wheels, steering, fans, drawers and trunks; rigs have pivots, constraints and proper naming.
- Video output should eventually include dialogue, expressive sound, lip-sync, subtitles, emojis where appropriate, intros/outros and director-level pacing.
- User uses Codex Cloud, wants cloud Blender visualization, might use Kaggle GPU for heavy rendering, and wants no local installation.

## Evidence ladder
1. **Discussion** — user goal, error report, historical assistant claim.
2. **Recipe** — proposed approach documented, but untested.
3. **Reproduced** — command, version, authorized fixture, logs and output files.
4. **Verified** — automated inspector checks + manual visual review where needed, with checksums.
5. **Production-ready** — stable across varied assets, failure modes, platforms and documented rights.

No live provider integration should advance beyond **recipe** purely on chat history.
