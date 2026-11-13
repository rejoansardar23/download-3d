# New contributor onboarding

**This file replaces the need to read old chats.**

## What to read in the first 10 minutes
1. [README](../README.md) and [PRODUCT_REQUIREMENTS](PRODUCT_REQUIREMENTS.md) for vision and must-haves.
2. [PROJECT_HISTORY](PROJECT_HISTORY.md) to understand the animation-missing problem and historical examples.
3. [ROADMAP](ROADMAP.md) and [ACCEPTANCE_TESTS](ACCEPTANCE_TESTS.md) to select testable work.
4. [SECURITY](../SECURITY.md), [PROVIDERS](PROVIDERS.md), [AGENT_INSTRUCTIONS](AGENT_INSTRUCTIONS.md) for rules.

## Working locally (optional for contributors; *not* creator requirement)
Use Python 3.11+ to run the standard-library inspector:
```sh
python -m unittest discover -s tests -v
PYTHONPATH=src python -m download3d inspect path/to/authorized/model.glb --out report.json
```
On Windows PowerShell, set environment as `$env:PYTHONPATH="src"` first. When packaging is configured, `pip install -e .` can replace PYTHONPATH.

## Cloud-first workflow
A Codex Cloud contributor can work entirely in a cloud repository checkout, running tests, editing docs/scripts, and making PRs. It should not assume local user installation or remote access to a graphical Blender process.

## First contribution
Pick a P0 issue, reproduce a failure with a **synthetic/permissive** fixture, add a regression test, implement a small fix, run CI and document observed results. Avoid large architectural rewrites before P0 inspector and manifest are reliable.

## Contribution template
```
Goal:
Relevant requirement / roadmap task:
Input fixture and rights:
Commands:
Expected:
Observed:
Files changed:
Tests:
Known limitations:
Next tasks:
```

## What not to do
- Do not announce "download complete" on HTTP 200 without file signature + checksum.
- Do not assume an FBX includes motions or a Gaussian splat is an editable mesh.
- Do not collect provider cookies, private API tokens or user passwords.
- Do not invent "13 animations" for a model without measured inventory.
- Do not upload private or restricted assets to this public GitHub repository.
