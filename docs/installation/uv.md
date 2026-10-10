# 📦 uv and uvx


`uvx` is needed for the existing Serena MCP registration. Skip this installation if you are not using Serena.


## 📥 Windows PowerShell


```powershell
winget install --id astral-sh.uv --exact --source winget
uv --version
uvx --version
```

Reopen PowerShell if the command is not recognized.


## ⌨️ Bash alternative


macOS with Homebrew:

```bash
brew install uv
uv --version
uvx --version
```

On Linux, use the [official uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for your distribution. Never run an unknown `uvx` package without checking its publisher.

[Installation index](./README.md) · [MCP catalog](../../integrations/mcp/README.md)
