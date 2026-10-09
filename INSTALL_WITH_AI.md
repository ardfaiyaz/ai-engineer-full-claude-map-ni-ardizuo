# <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Install with any capable AI assistant

**Copy the prompt below into Claude Code, Codex or an AI with computer/terminal access.** If your AI cannot access your PC, it must provide manual steps rather than claiming it installed anything.

<br />

## <img src="docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> Before you paste the prompt

1. Install [Claude Code](./docs/installation/claude-code.md), [Git](./docs/installation/git.md), [Python](./docs/installation/python.md) and [Node/npm](./docs/installation/nodejs-npm.md).
2. Clone this GitHub repository and open the **local clone** in your AI assistant.
3. Review [security](./SECURITY.md) and [the Full installer guide](./docs/installation/full-setup.md).

<br />

## <img src="docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> Copy this prompt

> Help me install **AI Engineer Full Claude Map ni Ardizuo** globally on my Windows machine from this cloned repository.
>
> 1. Read README.md, SECURITY.md, setup/full-stack.json, setup/development-assets.json, the Full installer script, and the relevant component docs. Do not make up dependencies or package names.
> 2. Detect my actual home folder and optional `CLAUDE_CONFIG_DIR`. Never hardcode an author's username or read/private-copy credentials.
> 3. Run `scripts/doctor.ps1` and `python scripts/verify-all.py`. Explain prerequisites needed before proceeding.
> 4. Run `scripts/install-all.ps1 -All` **without -Apply** and explain its dry-run plan.
> 5. Ask for explicit approval before using `-Apply`, external downloads, OAuth/login, vault creation, dashboard patches, changes to settings.json, Git actions or expensive operations.
> 6. With approval, run the installer with the requested components. Never treat failed CLI steps as installed, or configured MCPs as connected.
> 7. Follow official provider links for plugin marketplaces and credential-dependent Tavily, Morph and GitHub MCP setups. Guide the user to enter keys locally; never ask them to paste keys into the chat.
> 8. For an isolated test, use `-ConfigDir` WITHOUT external installation flags. Verify collisions, hash checks and hook registration before touching a live configuration.
> 9. Verify Claude's `/skills`, `/mcp`, `/hooks` and the local dashboard. Do not assert any agent delegation, vault write, testing or deployment unless it actually happened.
> 10. Never commit/push/deploy, edit projects, or write Obsidian notes without separate approval. No social-media integrations.
> 11. Summarize installed, configured, connected, blocked and manual steps. Provide safe rollback guidance.

<br />

## <img src="docs/assets/lucide/command.svg" width="18" height="18" alt="" /> If the AI cannot run commands

It should walk you through the exact [PowerShell steps](./docs/installation/full-setup.md) and wait for pasted command results. It must never claim remote access to your computer.

[Back to README](./README.md) · [API keys guide](./docs/security/api-keys-and-powershell.md)


## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Audit reference completeness before release

Ask the assistant to execute `python scripts/coverage-doctor.py --json` and compare the **literal names and statuses** for all 21 agents, 62 global skills, 32 commands, 12 plugins and nine MCP servers. Treat `cached-unconfirmed` and `missing` as uninstalled. Do not guess that SuperClaude, plugins or native commands include a specific file without verifying it.

When a file exists only on your personal machine, follow [private source review](./docs/installation/private-source-migration.md) first. Never use `settings.json`, `.claude.json`, provider caches, session transcripts or Obsidian notes as migration input. The external provider must prompt for its own account credentials.


## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Inspect a real install without touching it

Use the [read-only installed-layer verification](./docs/installation/installed-layer-audit.md) to check which expected files, hook registrations, and vault templates actually landed in your chosen Claude configuration. It does not claim that provider authentication or skill execution succeeded.
