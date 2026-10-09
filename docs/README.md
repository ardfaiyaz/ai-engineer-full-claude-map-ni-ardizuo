# <img src="assets/lucide/book-open.svg" width="18" height="18" alt="" /> Documentation hub

**Welcome.** This directory is organized so you only read what you need. Start with the tools you don't have; skip ones already installed.

<br />

## <img src="assets/lucide/download.svg" width="18" height="18" alt="" /> Install the basics

[Windows requirements](./prerequisites.md) · [All installation guides](./installation/README.md)

| Start here | Why |
| :--- | :--- |
| [Claude Code CLI](./installation/claude-code.md) | Install the AI coding runtime and sign in |
| [Git](./installation/git.md) | Clone projects and use worktrees |
| [Node.js and npm](./installation/nodejs-npm.md) | Run JavaScript-based tools and MCP servers |
| [Python](./installation/python.md) | Run Python-based tools and validations |
| [uv and uvx](./installation/uv.md) | Launch isolated Python MCP tooling |
| [GitHub CLI](./installation/github-cli.md) | Authenticate and work with GitHub |

<br />

## <img src="assets/lucide/file-text.svg" width="18" height="18" alt="" /> Optional infrastructure

[Docker](./installation/docker.md) · [WSL](./installation/wsl.md) · [Obsidian](./installation/obsidian.md) · [Claude Map](./installation/claude-map.md)

<br />

## <img src="assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Skills, integrations and privacy

| Guide | What it covers |
| :--- | :--- |
| [Claude Code plugins](../integrations/plugins/README.md) | Individual guides for 12 reference plugins |
| [MCP integrations](../integrations/mcp/README.md) | Nine server references; authentication and verification |
| [API keys & PowerShell](./security/api-keys-and-powershell.md) | Protect and rotate credentials; temporary environment values |
| [Windows permissions](./security/windows-permissions.md) | User-scoped installs and least-privilege operation |
| [Troubleshooting](./troubleshooting.md) | Known install and auth problems |

<br />

## <img src="assets/lucide/file-text.svg" width="18" height="18" alt="" /> How the pieces fit

[Architecture](./architecture.md) · [Component catalog](./components/README.md) · [Release plan](./release-checklist.md) · [Maintainer plan](./maintainer-next-steps.md)

> **Assisted Full preview:** The Core rule and 28 reviewed Ardizuo files can be installed locally. The Full orchestrator attempts supported upstream packages, MCPs, hooks, Obsidian and dashboard setup after explicit approval. OAuth, three credential-dependent MCPs, and version-specific overlay testing still require manual follow-up.

[Back to project README](../README.md)

<br />

## <img src="assets/lucide/download.svg" width="18" height="18" alt="" /> One-package assisted setup

[Full installation and limitations](./installation/full-setup.md) · [Component coverage](./components/README.md).


---

## <img src="assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Completeness audit and source migration

- [Exact Development Hub capability coverage](./components/exact-coverage.md) — offline audit of all named reference agents, skills, commands, plugins and MCP registrations, without claiming connections
- [Private review of missing definitions](./installation/private-source-migration.md) — safely collect candidate direct-scope sources *outside* the repository, review licenses and redact private data before redistribution
- [Full installer](./installation/full-setup.md) — marketplace preflight, official GitHub OAuth registration and vault template provisioning


## <img src="assets/lucide/list-checks.svg" width="18" height="18" alt="" /> What the public installer really reproduces

The reference machine has **21 agent files, 62 direct skill definitions, 31 executable command files plus one `README.md`, 12 enabled plugins and nine target user MCP servers**. The public installer does **not yet** exactly reproduce all of those on a fresh account. See the [release coverage matrix](installation/reproducibility-matrix.md) for default, optional, provider-authenticated, and blocked items. Never publish personal provider configuration or private vault content.


## <img src="assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Inspect a real install without touching it

Use the [read-only installed-layer verification](./installation/installed-layer-audit.md) to check which expected files, hook registrations, and vault templates actually landed in your chosen Claude configuration. It does not claim that provider authentication or skill execution succeeded.


[Development Hub surface (the actual displayed workflow, groups, agents and integrations)](./components/development-hub-surface.md) explains which badges correspond to existing local definitions, Claude built-ins, plugins, or MCP equivalents.
