# 🐳 Docker Desktop (optional)


Only required if you choose the existing Docker-backed GitHub MCP flow. It is **not** needed for most Ardizuo files.


<br />
<br />


## 📥 Windows PowerShell


```powershell
winget install --id Docker.DockerDesktop --exact --source winget
```

Launch Docker Desktop and complete its first-run setup. WSL 2 may be required for your selected backend.

```powershell
docker --version
docker info
```

`docker info` checks that the Docker engine is running; `docker --version` does not.


<br />
<br />


## ⌨️ Bash alternative


On macOS with Homebrew:

```bash
brew install --cask docker
```

Launch Docker Desktop manually and verify with `docker info`. On Linux, follow the distro-specific [Docker Engine guide](https://docs.docker.com/engine/install/); macOS Docker Desktop and Linux Docker Engine are different products.


<br />
<br />


## 🛡️ Security


Docker has its own licensing and system requirements. Don't publish private home-directory mounts or tokens in MCP configuration examples.

[Installation index](./README.md) · [MCP catalog](../../integrations/mcp/README.md)
