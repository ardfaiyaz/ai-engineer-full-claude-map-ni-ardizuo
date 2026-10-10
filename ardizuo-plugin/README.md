# 📦 Ardizuo development assets (Phase 1)


This folder contains **reviewed, portable, development-only local assets**:

- 16 manually authored helper skills, including `reuse-audit`, `dead-code-scan` and `vault-learning`.
- `diagram-architect` subagent, a session-note command, five hook scripts plus `hooks/lib/common.mjs`.
- Workflow configuration files and a global orchestration rule.

These originated in the author's own setup and have been adapted to avoid the author's hard-coded Windows paths. A preliminary secret scan and syntax checks are included; verify provenance and perform a manual review before a public release. No third-party plugin cache is redistributed.

Use **`scripts/install-development.ps1`** from the repository root. The installer is a separate global asset installer; `plugin.json` is not a substitute for the workflow and hook installation.

By default it only previews changes. `-Apply` copies files only when targets are absent or identical; it will not overwrite user-modified files. Hook activation is optional and handled by `scripts/register-hooks.mjs` with an independent approval step.

See [Phase 1 setup guide](../docs/installation/ardizuo-development-pack.md).
