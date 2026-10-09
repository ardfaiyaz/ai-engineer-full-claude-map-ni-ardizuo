# <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> uv and uvx

**Why you might need it:** Launches isolated Python tooling and some Python-based MCP servers, including Serena.

<br />

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> 1. Get it from the official source

[uv and uvx — official installation page](https://docs.astral.sh/uv/getting-started/installation/)

Use the official Astral installer or choose a supported package manager. Official Windows installer command (inspect the source first):

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Do not run unknown `uvx` packages. Check the publisher and version of any MCP launcher before registering it.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 2. Verify

```powershell
uv --version
uvx --version
```

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. If something goes wrong

If the tools are not on PATH, reopen PowerShell and inspect the installation location in [Astral's installer documentation](https://docs.astral.sh/uv/reference/installer/).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
