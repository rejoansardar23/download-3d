# Contributing to Download 3D

Thanks for helping. We want practical, reproducible contributions that move the project toward a usable cloud-only 3D workflow.

## Before a PR
Read [README](README.md), [roadmap](docs/ROADMAP.md), [acceptance tests](docs/ACCEPTANCE_TESTS.md) and [security policy](SECURITY.md). Pick one unblocked issue or open a scoped design discussion for large changes.

## Pull request requirements
- Problem, approach, behavior before/after, linked requirement/task.
- Fixture and **redistribution permissions** where applicable; prefer synthetic data.
- Tests and exact commands to rerun; status of CI.
- What is *not* implemented or unverified, provider-specific entitlement limitations.
- No third-party secrets, copied protected source code, vendor paywall bypass, unauthorized models/textures, or large media commits.
- Keep changes small, with JSON logs and actionable error handling.

## Style
Python 3.11+ for the initial inspector; standard library first; type hints/docstrings where useful. No unnecessary paid dependencies. Add regression test for every parser bug and negative case. Avoid unbounded memory use, subprocess command injection and opaque exceptions.

## Licensing
This repository has **not yet chosen** a project-wide software license. Contributions are accepted for project review, but do not imply the right to redistribute somebody else's models, textures, sounds or copyrighted source code. Maintainers should choose a license before treating this as general open-source code.

## Branching
Branch from `main`; open PR with conventional commits such as `feat:`, `fix:`, `docs:`, `test:`. Direct main pushes by the maintainer may be used for initial foundation.
