# 💻 Claude Code CLI

**Why you might need it:** The actual coding assistant that loads global rules, skills, agents, plugins and MCP registrations.

<br />

## 📁 1. Get it from the official source

[Claude Code CLI — official installation page](https://code.claude.com/docs/en/setup)

**Recommended:** use Anthropic's native Windows installer after reading its official instructions. As a package-manager alternative, the Claude Code docs support:

```powershell
winget install Anthropic.ClaudeCode
```

Native install script (review before execution): `https://claude.ai/install.ps1`. The official command is `irm https://claude.ai/install.ps1 | iex`; only use it after reviewing and trusting the source.

Launch Claude, sign in with your own supported account, and confirm that global settings are in your user profile:

```powershell
claude
```

Inside Claude Code, use `/login`, `/skills`, and `/mcp` as applicable.

<br />

## ☑️ 2. Verify

```powershell
claude --version
claude doctor
```

<br />

## 📄 3. If something goes wrong

If it says `claude: command not found`, reopen PowerShell, then follow the [official troubleshooting guide](https://code.claude.com/docs/en/troubleshooting). Avoid storing API keys unless you intentionally use API billing.


**More reading:** [official plugin instructions](https://code.claude.com/docs/en/discover-plugins) · [MCP docs](https://code.claude.com/docs/en/mcp) · [skills](https://code.claude.com/docs/en/skills).

<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
