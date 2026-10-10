# 🤖 Claude Code


Claude Code is the assistant that actually loads your agents, commands, plugins, MCP registrations and skills. Every user signs in with **their own** account.


<br />
<br />


## 📥 Windows PowerShell


```powershell
winget install --id Anthropic.ClaudeCode --exact --source winget
claude --version
claude
```

If Winget cannot find the package, use Anthropic's [official native setup guide](https://code.claude.com/docs/en/setup) to select the current supported Windows installer.


<br />
<br />


## ⌨️ Bash alternative (macOS/Linux only)


Anthropic provides a native installation script. **Review the linked official source before executing a remote script**:

```bash
curl -fsSL https://claude.ai/install.sh -o claude-install.sh
less claude-install.sh
bash claude-install.sh
claude --version
```

This is for systems supported by the official installer, **not** a Bash substitute for Ardizuo's Windows `.ps1` scripts.


<br />
<br />


## ✅ Sign in and verify


```powershell
claude
claude doctor
claude plugin list
claude mcp list
```

Inside Claude Code, use `/skills`, `/hooks` and `/mcp`. If a command is missing, reopen your terminal and check the [official troubleshooting guide](https://code.claude.com/docs/en/troubleshooting).

[Full Ardizuo installation](./full-setup.md)
