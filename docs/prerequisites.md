# 🛠️ Prerequisites — command index


**Use Windows PowerShell 5.1 or newer for the supported installer.** Install only the tools your machine is missing. Links are optional help; you can copy commands here without opening another page.


<br />
<br />


## 🚀 Required — Windows PowerShell


```powershell
winget install --id Git.Git --exact --source winget
winget install --id OpenJS.NodeJS.LTS --exact --source winget
winget install --id Python.Python.3.13 --exact --source winget
winget install --id Anthropic.ClaudeCode --exact --source winget
```

Reopen PowerShell:

```powershell
git --version
node --version
npm.cmd --version
python --version
claude --version
```


<br />
<br />


## 🧩 Optional tools — install only when needed


```powershell
# For Serena (uvx), Snyk Agent Scan and Spec Kit:
winget install --id astral-sh.uv --exact --source winget

# GitHub CLI / browser-based login:
winget install --id GitHub.cli --exact --source winget

# Docker-backed GitHub MCP:
winget install --id Docker.DockerDesktop --exact --source winget

# View the local Obsidian vault:
winget install --id Obsidian.Obsidian --exact --source winget

# Optional newer PowerShell:
winget install --id Microsoft.PowerShell --exact --source winget
```

For WSL (only if you need Linux tools), `wsl --install` may require an administrator terminal and reboot.


<br />
<br />


## 🧩 Extra tools used by the extended stack


`-All` installs the extended stack, which relies on these. A missing one is reported as `missing-dependency` and the rest of the installation continues; install it and re-run.

| Prerequisite | Used by | Install command |
| --- | --- | --- |
| Node.js / npm / npx | Codex CLI, Beads CLI, MCP Inspector, ccusage, n8n MCP, Playwright MCP, Agentation | Covered by Node.js LTS above |
| uv | Snyk Agent Scan, Spec Kit, Semgrep for Trail of Bits `static-analysis` | `winget install --id astral-sh.uv --exact --source winget` |
| Bun + a Bash shell (Git Bash) | gstack setup | `winget install --id Oven-sh.Bun --exact --source winget` (Git Bash comes with Git) |
| winget | ToolHive (`thv`) | Built into Windows 10/11 |
| Docker Desktop or Podman | Running servers with ToolHive | `winget install --id Docker.DockerDesktop --exact --source winget` |
| Python 3.11+ | Spec Kit | Covered by Python 3.13 above |

Accounts, not tools: Codex needs `codex login`; Firecrawl, Exa, 21st Magic and Browserbase need their own sign-in or key. See [API key safety](./security/api-keys-and-powershell.md).


<br />
<br />


## 🖥️ Optional upstream Claude Map


```powershell
npm.cmd install --global claude-map@1.2.3
claude-map -p 8888
```

The Ardizuo overlay is a separate compatibility-sensitive step; use [Claude Map instructions](./installation/claude-map.md).


<br />
<br />


## ⌨️ Bash examples (macOS or Linux)


```bash
# If you're on macOS and already have Homebrew:
brew install git node python uv gh

# After git and npm are installed:
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo
npm install --global claude-map@1.2.3
```

The Ardizuo global installer is Windows PowerShell-first; the Bash examples only install their named upstream tools.


<br />
<br />


## ✅ Find help for one tool


[Git](./installation/git.md) · [Node/npm](./installation/nodejs-npm.md) · [Python](./installation/python.md) · [Claude Code](./installation/claude-code.md) · [uv](./installation/uv.md) · [GitHub CLI](./installation/github-cli.md) · [Docker](./installation/docker.md) · [WSL](./installation/wsl.md) · [Obsidian](./installation/obsidian.md)

[Start the installer](../START-HERE.md)
