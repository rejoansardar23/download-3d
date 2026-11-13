# Codex and AI agent instructions

This file is the entry point for repository-aware coding agents. The user should **not** need to copy previous ChatGPT chats.

## Before writing code
Read in order: [README](README.md), [PRODUCT_REQUIREMENTS](docs/PRODUCT_REQUIREMENTS.md), [PROJECT_HISTORY](docs/PROJECT_HISTORY.md), [ROADMAP](docs/ROADMAP.md), [ACCEPTANCE_TESTS](docs/ACCEPTANCE_TESTS.md), [SECURITY](SECURITY.md), then [AGENT_INSTRUCTIONS](docs/AGENT_INSTRUCTIONS.md). Check GitHub Issues for the smallest unfinished task.

## North star
A creator who uses **only a web browser** should be able to import assets they have the right to obtain (Tripo/Meshy/Marble or user-uploaded), preserve original files and **all available independent motion clips**, preview animations in a browser, process with cloud Blender and optionally batch-render on permitted GPU services. The first blocker is trustworthy asset completeness and failure diagnosis, **not** a flashy interface.

## Strict agent behaviors
- Do not ask the user to install local Blender/Python.
- No unauthorized access-control bypass, export/payment workarounds, cookie extraction or exposing expiring download URLs.
- If a provider download requires login or has no lawful interface, mark **AUTH_REQUIRED** or **EXPORT_NOT_SUPPORTED**. Never substitute preview HTML, screenshots or empty ZIP.
- Never claim an FBX has all animations because it has a skeleton. Audit *each* independent source motion clip against output. Counts not inspected are **unknown**.
- Do not add third-party models/textures/videos without redistribution rights.
- Write small tested changes; run `python -m unittest discover -s tests -v` with `PYTHONPATH=src`.
- Use CI and safe synthetic fixtures first; protect time and free cloud/GPU credits.
- Record source ID, size, SHA-256, format, motion inventory, failures and exact command.
- All tool/provider claims are tentative until live tests with authorization prove them.
- End each task with proof, known gaps and next issue.

## Working code
The offline inspector is `src/download3d`; CI is `.github/workflows/ci.yml`. These are *not* a full downloader or Blender replacement. Start from [MVP usage](docs/MVP_USAGE.md).

## Existing Github issues
https://github.com/rejoansardar23/download-3d/issues
