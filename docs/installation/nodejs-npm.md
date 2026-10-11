# 🟩 Node.js and npm


Node.js is needed for the hook scripts, JavaScript MCP servers (Sequential Thinking, Chrome DevTools) and Claude Map. npm and `npx` are included with Node.js.

The [extended stack](./extensions.md) installed by `-All` also uses npm and `npx`: n8n MCP, Playwright MCP, MCP Inspector, ccusage, mcp-use, Agentation, Probity, the Codex CLI (`@openai/codex`) and the Beads CLI (`@beads/bd`). Use the LTS release; the installer never upgrades Node for you.


<br />
<br />


## 📥 Windows PowerShell — install the LTS release


```powershell
winget install --id OpenJS.NodeJS.LTS --exact --source winget
```

Reopen PowerShell, then verify:

```powershell
node --version
npm.cmd --version
npx.cmd --version
```


<br />
<br />


## ⌨️ Bash alternative


On macOS **with Homebrew already installed**:

```bash
brew install node
node --version
npm --version
```

On Linux, install a supported Node.js LTS version using your distribution's official package instructions or an existing Node version manager. A Windows `.ps1` installer cannot be run from Bash.


<br />
<br />


## 🛠️ If npm does not start


If Windows PowerShell blocks `npm.ps1`, call `npm.cmd` / `npx.cmd` rather than changing the system-wide execution policy. If `node` cannot be found, reopen the shell. See [Node.js releases](https://nodejs.org/en/download).

[Installation index](./README.md) · [Claude Map](./claude-map.md)
