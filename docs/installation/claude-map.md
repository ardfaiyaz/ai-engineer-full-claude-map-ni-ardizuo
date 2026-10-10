# 🖥️ Claude Map (optional)


Claude Map is an **upstream npm application** for browsing local Claude Code configuration. Ardizuo's five-stage Development Hub is a **separate, version-sensitive overlay**.


## 📥 Install upstream Claude Map — Windows PowerShell


First install [Node.js](./nodejs-npm.md). The existing overlay was rehearsed against upstream `claude-map@1.2.3`:

```powershell
npm.cmd install --global claude-map@1.2.3
claude-map --version
claude-map -p 8888
```

Then open <http://localhost:8888>. Use `Ctrl+C` to stop the server.


## ⌨️ Bash (macOS/Linux with Node.js and npm)


```bash
npm install --global claude-map@1.2.3
claude-map -p 8888
```

Bash can launch **upstream** Claude Map, but Ardizuo's current package patch/testing workflow is **Windows-first**. Do not assume the dashboard overlay has been verified on Linux or macOS.


## 🧪 Add the existing five-stage Development Hub


In a separate PowerShell window, from the cloned Ardizuo repository:

```powershell
# Confirm the local Claude Map files and check the first scaffold.
python .\scripts\install-dashboard.py

# Rehearse all five overlays against disposable copies first.
python .\scripts\install-dashboard.py --rehearse
```

If rehearsal passes, stop Claude Map, back up your **complete** globally installed `claude-map` directory, and only then consider:

```powershell
# Review and approve the live modification separately.
python .\scripts\install-dashboard.py --apply
claude-map -p 8888
```

Open <http://localhost:8888/?tab=devhub>. **`-Apply -All` does not patch the live dashboard automatically.** A successful rehearsal checks patch compatibility and JavaScript syntax, not runtime browser rendering.


## 🛠️ Common issues


- If `node-pty` cannot build or the terminal is broken, check [upstream installation guidance](https://github.com/shamim0902/claude-map) for your installed Node.js version.
- If an overlay conflicts with upstream files, **stop**; do not repeatedly apply the patch. Use the full [dashboard backup and rehearsal procedure](../../dashboard/claude-map/README.md).
- Keep the dashboard bound to localhost and never expose MCP secrets or vault notes.

[Quick start](../../START-HERE.md) · [Full dashboard setup](../../dashboard/claude-map/README.md)
