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


<br />
<br />


## 🧩 Plugin and marketplace commands used by this project


The installer calls these for you, but they are useful for checking or fixing a single plugin by hand:

```powershell
claude plugin marketplace list                       # registered marketplaces
claude plugin marketplace add openai/codex-plugin-cc # add one marketplace (owner/repo)
claude plugin install codex@openai-codex             # install plugin@marketplace
claude plugin list                                   # installed and enabled plugins
claude plugin disable codex@openai-codex             # turn off without removing
claude plugin uninstall codex@openai-codex           # remove
```

Inside Claude Code, `/plugin` opens the plugin manager, and `/reload-plugins` (on versions that have it) picks up newly installed plugins without a restart. The 12 baseline plugins are in the [plugin catalog](../../integrations/plugins/README.md); the extended stack that `-All` installs is in the [extended stack guide](./extensions.md).

[Full Ardizuo installation](./full-setup.md)
