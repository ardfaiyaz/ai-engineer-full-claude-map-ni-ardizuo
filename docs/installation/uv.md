# uv and uvx

**Why you might need it:** Launches isolated Python tooling and some Python-based MCP servers, including Serena.

<br />

## 1. Get it from the official source

[uv and uvx — official installation page](https://docs.astral.sh/uv/getting-started/installation/)

Use the official Astral installer or choose a supported package manager. Official Windows installer command (inspect the source first):

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Do not run unknown `uvx` packages. Check the publisher and version of any MCP launcher before registering it.

<br />

## 2. Verify

```powershell
uv --version
uvx --version
```

<br />

## 3. If something goes wrong

If the tools are not on PATH, reopen PowerShell and inspect the installation location in [Astral's installer documentation](https://docs.astral.sh/uv/reference/installer/).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
