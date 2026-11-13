# Security & responsible asset handling

## Authorized access only
Do not bypass authentication, paid export features, DRM/technical access controls, rate limits or provider licensing. A shareable 3D preview URL is not proof of permission to download or redistribute original assets. Use supported exports/APIs or user-uploaded files with proper rights.

## Never commit
- API keys, sessions, passwords, cookies, OAuth access tokens, SSH keys;
- signed URLs or private query parameters;
- model binaries, scans, texture packs, video/media lacking redistribution rights;
- personal/private information from chat logs.

## Asset parsing threats
Treat GLB, glTF, FBX and ZIP as untrusted data. Validate declared file lengths/chunks, JSON sizes, archive path safety, symlink flags, file counts, decompressed size and compression ratios. No rendering or executing embedded scripts as part of inspection.

## URL download threats
Avoid arbitrary URL fetching from public GitHub Actions. When provider integrations are added, enforce allowlists, scheme/redirect checks, DNS/IP re-resolution and private-address rejection; cap bytes and time; redact userinfo/query/Authorization headers. Prefer per-provider official APIs.

## CI privilege
Workflow default token `contents: read`. No write permissions to secrets or untrusted PR code. Avoid executing untrusted artifacts or exposing tokens in workflow_dispatch inputs and job logs. Uploaded CI diagnostics must be non-sensitive.

## Reporting
Please open a GitHub issue **without secrets or exploit payloads** for ordinary validation bugs. For sensitive vulnerabilities, contact maintainers privately using GitHub's private vulnerability reporting facility if enabled; do not publicly disclose exploitable authentication details.

## License and redistribution
Follow each third-party provider's terms and the asset's individual license. Never imply that provider-generated assets become open source by being mentioned in a public repository.
