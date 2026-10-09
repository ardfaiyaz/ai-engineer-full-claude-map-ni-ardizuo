# <img src="assets/lucide/download.svg" width="18" height="18" alt="" /> Prerequisites — Windows-first

**You do not need to install everything.** Check what you already have, then follow only the relevant guides. WSL and Docker are optional.

<br />

## <img src="assets/lucide/file-text.svg" width="18" height="18" alt="" /> Check your computer first

From the repository root, open **PowerShell**:

```powershell
.\scripts\doctor.ps1
```

If a command is not recognized, follow its installation guide and reopen PowerShell before retrying.

<br />

## <img src="assets/lucide/terminal.svg" width="18" height="18" alt="" /> Essential and optional tools

| Tool | When it's needed | Open the guide |
| :--- | :--- | :--- |
| **Windows 10/11 + PowerShell** | Supported v1 installer platform | [Windows setup](./installation/windows-powershell.md) |
| **Claude Code** | Required for the Claude development environment | [Claude Code CLI](./installation/claude-code.md) |
| **Git** | Clone this repository and manage changes | [Git](./installation/git.md) |
| **Node.js + npm** | Dashboard and many JavaScript MCP tools | [Node and npm](./installation/nodejs-npm.md) |
| Python | Selected scripts, plugins and Python projects | [Python](./installation/python.md) |
| uv / uvx | Selected Python MCPs such as Serena | [uv and uvx](./installation/uv.md) |
| GitHub CLI (`gh`) | GitHub authentication and repository actions | [GitHub CLI](./installation/github-cli.md) |
| Docker Desktop | Docker-backed MCP and optional gateway | [Docker](./installation/docker.md) |
| Obsidian | Browse optional knowledge vault | [Obsidian](./installation/obsidian.md) |
| WSL | Specific Linux-based development tools | [WSL](./installation/wsl.md) |
| Local Claude Map | Optional runtime inventory/dashboard | [Claude Map](./installation/claude-map.md) |

<br />

## <img src="assets/lucide/download.svg" width="18" height="18" alt="" /> Global setup location

The scripts should use `$env:CLAUDE_CONFIG_DIR` if set; otherwise, the current user's `$HOME\.claude` folder. They must not hardcode the creator's username.

```powershell
$claudeDir = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME '.claude' }
Write-Host "Claude configuration directory: $claudeDir"
```

**Authentication is separate from installation.** A configured MCP server can still require sign-in. See [API keys and PowerShell](./security/api-keys-and-powershell.md) and the [MCP catalog](../integrations/mcp/README.md).

<br />

[Next: installation guide index](./installation/README.md) · [Back to documentation](./README.md)

<br />

## <img src="assets/lucide/download.svg" width="18" height="18" alt="" /> One-package installer

[Read the complete setup guide](./installation/full-setup.md) to prepare your Windows prerequisites before installation. It explains when a plugin or MCP is optional, what requires authentication, and how to preview changes.
