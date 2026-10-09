# Install with an AI assistant

**One prompt, any capable assistant.** Works with Claude Code, Codex, and other assistants that can read local files and run commands. If the assistant cannot access your computer, it can guide you through the commands instead.

> **Important:** This repository is a **bootstrap preview**, not the full stack. The only executable profile currently installs one namespaced global rule. Never claim otherwise.

<br />

## Before you start

1. [Install Claude Code](./docs/installation/claude-code.md) and [Git](./docs/installation/git.md).
2. Read the [prerequisites](./docs/prerequisites.md) and [security guidance](./SECURITY.md).
3. Clone the [public repository](https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo) and open the local folder in your AI coding assistant.

<br />

## Copy this prompt

> Help me install **AI Engineer Full Claude Map ni Ardizuo** from the local repository folder I'm in. **Do not guess, auto-run arbitrary scripts, or silently install external components.**
>
> 1. Read `README.md`, `SECURITY.md`, `setup/manifest.json`, the requested `setup/profiles/*.json`, and the installation scripts. Respect documented limitations: **only the Core bootstrap is executable today**.
> 2. Determine my actual OS, `$HOME` and `$env:CLAUDE_CONFIG_DIR` if set. Do not hardcode a username or modify other people's directories. Run `scripts/doctor.ps1` and summarize tools already present.
> 3. Ask which profile I'd like. For Full, Frontend, Backend, Mobile or Custom, describe pending implementation honestly. **Do not construct a replacement installer from cached plugin files.**
> 4. Run a **dry run** using `scripts/install.ps1 -Profile core`. Explain exactly what file would be created or changed. Stop on collisions.
> 5. **Ask me for explicit approval** before `-Apply`, downloads, credential prompts, provider sign-ins, model-consuming tests, or changes to Git repositories.
> 6. For any desired external plugin or MCP, follow the relevant [official-linked component guide](./docs/README.md) and user-approved supported commands. Prefer OAuth; do not ask me to paste secrets in chat or put tokens in shell history.
> 7. Do not inspect or publish credentials, `.claude.json`, private Obsidian notes, local session logs, or other personal files. Do not add social-media tooling.
> 8. Verify results separately as installed, configured, connected, or executed. Run the documented smoke tests only after approval.
> 9. Do not commit, push, deploy, send requests on my behalf, or write vault notes without explicit instruction.
> 10. Finish with a brief status table and specific commands for verification and rollback.

<br />

## If the AI cannot access your computer

Ask it for a **reviewed, copy-and-paste Windows PowerShell walkthrough**, then run those commands yourself. Do not accept claims that it installed a plugin or authenticated an MCP without actual command output.

<br />

## Quick verification commands

```powershell
.\scripts\doctor.ps1
.\scripts\install.ps1 -Profile core  # dry run only
claude plugin list
claude mcp list
```

**Do not run `-Apply` until you understand the file destination.** See the [Windows permissions guide](./docs/security/windows-permissions.md) and [API key guide](./docs/security/api-keys-and-powershell.md).

[Back to README](./README.md) · [All guides](./docs/README.md)
