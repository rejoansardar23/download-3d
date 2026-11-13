# Animation completeness & rigging strategy

## Crucial distinction
A model can have **geometry + 65-bone skeleton + textures** and still have **zero embedded motion clips**. A separate set of animation FBXs may exist. Report (a) base rig quality, (b) number of discovered source motion files, (c) clips actually imported, and (d) clips successfully exported into GLB. Do not call a job complete when only (a) succeeded.

## Clip inventory & verification
1. Discover authorized inventory from provider API/official export or user upload (do not infer from preview count).
2. For each motion: record source ID, filename, SHA-256, expected target skeleton, imported action names.
3. Import into Blender *without mutating original sources*; compare armature/bone names, rest poses, scaling, hierarchy and animation durations.
4. Convert/retarget where appropriate; record losses or errors per clip.
5. Export one or multiple GLB animations with stable names. Blender's export behavior must be tested; check resulting `animations[]` rather than trusting an export-success message.
6. Web viewer should expose animation selection, looping, controls and clear names.
7. ZIP must include *both* raw source motions and converted motions (subject to license).

## Historical Tripo reference (not a fixture)
An earlier assistant **reported** 13 motion categories for one example: walking, running, upstairs, turning, waiting, sitting, agreeing, hugging, afraid/fear, crying, angry/anger, digging, falling. This is neither a current provider guarantee nor a mandatory expected count for other models.

## Mechanical rigs
Create separate named parts with correct pivots:
- Sedan: `car_body`, `wheel_FL/FR/RL/RR`, `door_FL/FR/RL/RR`, `steering_wheel`, `trunk`, `steering_link`; wheel rotation, front-wheel steer, hinge door swing, trunk lift, body translation.
- Train/carriage: wheel bogies, sliding/hinged doors, seats, handrails; keep moving units modular.
- Props: fan rotor on hinge; drawer along one local axis; cabinet door with hinge pivot.
Keep transforms reversible, geometry collisions plausible, use animations and constraints that can be exported reliably.

## Human rig priorities
Retarget stable humanoid body poses, foot contacts, walking/root motion, eye gaze and face controls. Facial expressions, dialogue timing, speech/audio sync and consistent appearance are a later *visually validated* phase. T-pose/A-pose, scale and bone mapping must be explicit.

## Animation acceptance
- When expected clip inventory is known: `source_count == acquired_count == validated_count == output_count`, or produce a named loss table and fail completeness gate.
- No silently missing or duplicate clip IDs.
- At least one nonzero-duration keyed channel for each claimed action.
- Browser demonstration of at least two distinct motions on a synthetic rig (and per-project expected motions).
- For car test: independent door and wheel transforms at distinct times, not entire vehicle mesh spinning.
