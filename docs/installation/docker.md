# 📄 Docker Desktop

**Why you might need it:** Needed only for container-based MCP servers or optional gateway integrations.

<br />

## 📁 1. Get it from the official source

[Docker Desktop — official installation page](https://docs.docker.com/desktop/setup/install/windows-install/)

Download Docker Desktop from Docker's official site. Check CPU virtualization, Windows requirements and supported backend first. Choose per-user installation where appropriate.

Docker may use WSL 2. Install WSL only if the selected backend requires it. Be aware of [Docker Desktop licensing](https://www.docker.com/pricing/) for some business environments.

<br />

## ☑️ 2. Verify

```powershell
docker --version
docker info
```

<br />

## 📄 3. If something goes wrong

`docker --version` shows only that the CLI is installed. `docker info` also checks that the daemon is available. If it fails, start Docker Desktop, confirm WSL 2, and check virtualization.


Do not mount the entire home directory or secrets into a container unless the MCP actually requires them.

<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
