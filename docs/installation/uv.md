# 📦 uv and uvx


`uvx` is needed for the existing Serena MCP registration. The [extended stack](./extensions.md) installed by `-All` also uses it to install Snyk Agent Scan (`uv tool install snyk-agent-scan`) and GitHub Spec Kit (`uv tool install specify-cli`), and it can install Semgrep for Trail of Bits `static-analysis` (`uv tool install semgrep`). Without uv, those tools are reported as missing and the rest of the installation continues.


<br />
<br />


## 📥 Windows PowerShell


```powershell
winget install --id astral-sh.uv --exact --source winget
uv --version
uvx --version
```

Reopen PowerShell if the command is not recognized.


<br />
<br />


## ⌨️ Bash alternative


macOS with Homebrew:

```bash
brew install uv
uv --version
uvx --version
```

On Linux, use the [official uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for your distribution. Never run an unknown `uvx` package without checking its publisher.

[Installation index](./README.md) · [MCP catalog](../../integrations/mcp/README.md)
