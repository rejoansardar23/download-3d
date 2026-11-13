# Instructions for Codex Cloud and any contributing AI agent

## Objective
Advance the **Download 3D** project at https://github.com/rejoansardar23/download-3d from documented requirements to tested browser/cloud asset intake, animation preservation and filmmaking workflows. Treat README and docs as canonical; never need the original ChatGPT chat history.

## Non-negotiable constraints
- Creator uses browser only; do not require them to install Blender, Python or a desktop app.
- Never bypass authentication, subscriptions, license/export restrictions or technical access controls.
- Never publish user model binaries, private footage, provider tokens, signed URLs, passwords, cookies or access keys.
- Use provider-supported API/export or user-supplied authorized files.
- "Successful download" requires identity + nonzero file size + format detection + checksum + actual payload presence.
- "All animations" requires reconciling **each** authorized source animation with imported and exported clips. If inventory is unknown, report unknown and block completeness claim.
- Validate features with automated tests on clean synthetic/permissive fixtures before live integrations.
- Avoid expensive full renders until low-cost preflight succeeds.
- Push code, docs and test fixtures, not restricted large assets.

## Recommended task sequence
1. Inventory repo and tests; select first unfinished P0 task.
2. Write a 5-line plan referencing requirement IDs.
3. Implement smallest working change with structured errors and safe logs.
4. Run offline unit tests; capture commands + outputs. Mark external tests blocked if authorization unavailable.
5. Open PR or commit with clear title, tests, limitations and next step.
6. When asked to automate vendor retrieval, first verify authorization and supported official integration. If not possible, return `AUTH_REQUIRED`/`EXPORT_NOT_SUPPORTED` with legal user steps rather than substituting a screenshot, HTML page or empty ZIP.

## Debugging downloads
Log stage, requested vs actual model ID, HTTP status category, host (not full signed URL), content-length, magic bytes/format, size, hash and animation count. Distinguish network DNS/proxy failures from provider 401/403/404, stale signed URLs and malformed files. Use retries only for temporary failures.

## Completion report
```
Implemented:
Evidence:
Test commands and result:
Output artifact hashes:
Rights/source assumptions:
Known gaps:
Next backlog item:
```
No fabricated results, downloads, GIFs, screenshots or GPU job success.
