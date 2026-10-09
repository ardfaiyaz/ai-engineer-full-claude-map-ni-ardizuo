# <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> Installation guides

These are short, **Windows-first** guides. Every tool gets its own page, official download, recommended method, verification command, and common fixes.

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Required for most users

| Guide | Verification |
| :--- | :--- |
| [Windows and PowerShell](./windows-powershell.md) | `$PSVersionTable.PSVersion` |
| [Git](./git.md) | `git --version` |
| [Claude Code CLI](./claude-code.md) | `claude --version` |
| [Node.js + npm](./nodejs-npm.md) | `node -v; npm -v` |

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Select only what you need

| Guide | Use case |
| :--- | :--- |
| [Python](./python.md) | Python scripts and development |
| [uv / uvx](./uv.md) | Python MCP launchers |
| [GitHub CLI](./github-cli.md) | GitHub authentication |
| [Docker Desktop](./docker.md) | Container-based MCPs |
| [WSL](./wsl.md) | Linux tools on Windows |
| [Obsidian](./obsidian.md) | Optional local knowledge vault |
| [Claude Map](./claude-map.md) | Optional localhost dashboard |

<br />

**Before connecting providers:** read [API keys and PowerShell](../security/api-keys-and-powershell.md). Installing the executable is not the same as connecting a service.

[Back to prerequisites](../prerequisites.md) · [Documentation hub](../README.md)

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Original Ardizuo development pack

[Install 28 reviewed global Claude Code assets](./ardizuo-development-pack.md). This is optional and separate from external plugin/MCP installation.

<br />

## <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> Complete guided setup

[Full installation — one orchestrator and optional integrations](./full-setup.md).

<br />

## <img src="../assets/lucide/bot.svg" width="18" height="18" alt="" /> Agent framework

[SuperClaude (20 agents and sc commands)](./superclaude.md).

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Verify everything

[30-step install and end-to-end checklist](./verification-checklist.md).


## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> What the public installer really reproduces

The reference machine has **21 agent files, 62 direct skill definitions, 31 executable command files plus one `README.md`, 12 enabled plugins and nine target user MCP servers**. The public installer does **not yet** exactly reproduce all of those on a fresh account. See the [release coverage matrix](reproducibility-matrix.md) for default, optional, provider-authenticated, and blocked items. Never publish personal provider configuration or private vault content.


## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Inspect a real install without touching it

Use the [read-only installed-layer verification](./installed-layer-audit.md) to check which expected files, hook registrations, and vault templates actually landed in your chosen Claude configuration. It does not claim that provider authentication or skill execution succeeded.
