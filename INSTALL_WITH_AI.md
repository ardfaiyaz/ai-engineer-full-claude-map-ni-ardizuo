# Install with any capable AI assistant

**Copy the prompt below into Claude Code, Codex or an AI with computer/terminal access.** If your AI cannot access your PC, it must provide manual steps rather than claiming it installed anything.

<br />

## Before you paste the prompt

1. Install [Claude Code](./docs/installation/claude-code.md), [Git](./docs/installation/git.md), [Python](./docs/installation/python.md) and [Node/npm](./docs/installation/nodejs-npm.md).
2. Clone this GitHub repository and open the **local clone** in your AI assistant.
3. Review [security](./SECURITY.md) and [the Full installer guide](./docs/installation/full-setup.md).

<br />

## Copy this prompt

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

## If the AI cannot run commands

It should walk you through the exact [PowerShell steps](./docs/installation/full-setup.md) and wait for pasted command results. It must never claim remote access to your computer.

[Back to README](./README.md) · [API keys guide](./docs/security/api-keys-and-powershell.md)
