# 🚀 Install Ardizuo's Claude Code setup

**For Windows 10/11, PowerShell, and your own Claude account.** This is a public, assisted setup—not a copy of the maintainer's private credentials, vault, or every customized skill file.

## ✅ 1. Prerequisites

You need **Git, Python 3, Node.js/npm, and Claude Code** installed and available in a new PowerShell window. Check them:

```powershell
git --version
python --version
node --version
npm --version
claude --version
```

Missing something? Use the [prerequisites guide](./docs/prerequisites.md). Optional MCP servers may also need `uvx`, Docker, GitHub CLI, or a provider account.

## 📥 2. Clone, preview, install

```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

# Inspect exactly what will change. No writes.
.\scripts\install-all.ps1 -All

# Apply only after approving the preview.
.\scripts\install-all.ps1 -Apply -All
```

**`-Apply -All` is consequential.** It can install plugins, register MCP servers and hooks, and create a separate optional Obsidian vault. It does not import login sessions or credentials. The customized Claude Map overlay is **not** applied automatically; follow the [dashboard guide](./dashboard/claude-map/README.md) if you want it.

If you **already have** a personal Claude configuration, preview first. The installer refuses to overwrite different files. Do **not** delete your existing `.claude` folder to force an install. Resolve conflicts by comparing the files you actually want to retain. For an isolated preview, use `-ConfigDir "$HOME\Documents\Ardizuo-Preview" -PinnedSuperClaude -PinnedSkills` **without** `-All`.

## 🔑 3. Connect the services you use

```powershell
claude plugin list
claude mcp list
```

Open Claude Code and inspect `/skills`, `/hooks`, and `/mcp`. Authenticate only services you intend to use. Atlassian authentication may remain optional. Other users need their **own** API keys and OAuth grants; never share an exported `.claude.json` or `settings.json`.

## ☑️ 4. One quick local verification

```powershell
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
```

This checks package files and hook registration—not whether a skill executed or an MCP is authenticated. For an exact reference-versus-public-package view, run `python .\scripts\release-audit.py`.

## 📦 What you actually get

| Layer | Public installation path |
| --- | --- |
| Agents | **21/21** definitions by default |
| Skills | **36/62** direct definitions by default, up to **41/62** using different upstream variants |
| Executable commands | **20/31** by default, up to **31/31** using different upstream variants |
| Plugins | 12 guided CLI installations; individual logins may be necessary |
| MCP servers | 9 targeted integrations; registration and authentication are separate |
| Hooks | Five handlers, registered in `-All` with explicit `-Apply` |
| Workflow / rules | Five-stage instructions, `CLAUDE.md`, rule files and gates |
| Memory / dashboard | Empty vault templates are optional; the dashboard overlay needs a separate compatibility rehearsal |

**The missing skills are not silently invented.** Seventeen other direct-skill origins, four unknown-source skill definitions, and certain publisher sidecar files are not yet reproduced by this public installer. A plugin's own skills and built-in Claude commands are not additional bundled global `SKILL.md` files. The [by-name reproducibility matrix](./docs/installation/reproducibility-matrix.md) gives the exact distinctions.

Need details? Read the [full setup](./docs/installation/full-setup.md), [troubleshooting](./docs/troubleshooting.md), [security policy](./SECURITY.md), or [release checklist](./docs/release-checklist.md).
