# 🛠️ Prerequisites — command index


**Use Windows PowerShell 5.1 or newer for the supported installer.** Install only the tools your machine is missing. Links are optional help; you can copy commands here without opening another page.


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


## 🧩 Optional tools — install only when needed


```powershell
# For Serena (uvx):
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


## 🖥️ Optional upstream Claude Map


```powershell
npm.cmd install --global claude-map@1.2.3
claude-map -p 8888
```

The Ardizuo overlay is a separate compatibility-sensitive step; use [Claude Map instructions](./installation/claude-map.md).


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


## ✅ Find help for one tool


[Git](./installation/git.md) · [Node/npm](./installation/nodejs-npm.md) · [Python](./installation/python.md) · [Claude Code](./installation/claude-code.md) · [uv](./installation/uv.md) · [GitHub CLI](./installation/github-cli.md) · [Docker](./installation/docker.md) · [WSL](./installation/wsl.md) · [Obsidian](./installation/obsidian.md)

[Start the installer](../START-HERE.md)
