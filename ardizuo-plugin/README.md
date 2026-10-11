# 📦 Ardizuo development assets (Phase 1)


This folder contains **reviewed, portable, development-only local assets**:

- 17 manually authored helper skills, including `reuse-audit`, `dead-code-scan`, `vault-learning` and `version-log` (keeps a `VERSIONLOG.md` in every repository you change).
- `diagram-architect` subagent, a session-note command, five hook scripts plus `hooks/lib/common.mjs`.
- Workflow configuration files and a global orchestration rule.

These originated in the author's own setup and have been adapted to avoid the author's hard-coded Windows paths. A preliminary secret scan and syntax checks are included; verify provenance and perform a manual review before a public release. No third-party plugin cache is redistributed.

The full installer (`scripts/install-all.ps1 -Apply -All`) installs these files together with everything else. To install only this pack, use **`scripts/install-development.ps1`** from the repository root. The installer is a separate global asset installer; `plugin.json` is not a substitute for the workflow and hook installation.

By default it only previews changes. `-Apply` copies files only when targets are absent or identical; it will not overwrite user-modified files. Hook activation is optional and handled by `scripts/register-hooks.mjs` with an independent approval step.

See [Phase 1 setup guide](../docs/installation/ardizuo-development-pack.md).
