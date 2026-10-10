# 🟩 Node.js and npm


Node.js is needed for JavaScript MCP servers and Claude Map. npm is included with Node.js.


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
