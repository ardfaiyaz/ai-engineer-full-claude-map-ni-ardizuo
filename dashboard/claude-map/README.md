# Claude Map — AI / Software Engineer Claude Setup

**Local-only visualization with the five-stage Workflow Surface and status-colored capability layers.** The customized dashboard extends [upstream Claude Map](https://github.com/shamim0902/claude-map); it is not a hosted website or a replacement for Claude Code.

<br />

## Install the base dashboard

Review [Node.js/npm prerequisites](../../docs/installation/nodejs-npm.md), then:

```powershell
npm install -g claude-map
claude-map -p 8888
```

Stop the running server before modifying the installed package. Open <http://localhost:8888> (never expose port 8888 on an untrusted network).

<br />

## Optional Ardizuo Development Hub overlay

This distribution includes the source patches that created the author's dashboard. They are **version-sensitive**; an updated upstream release may change the code anchors. Always preview and let the installer back up the files before modifying them.

```powershell
python .\scripts\install-dashboard.py          # dry run: no changes
python .\scripts\install-dashboard.py --apply # patch known structure
```

On success, restart Claude Map and open `http://localhost:8888/?tab=devhub`, then press Ctrl+Shift+R.

The overlay attempts to add the actual title **AI / Software Engineer Claude Setup**, monochrome UI with green/red status badges, and the workflow/skill/agent/hook/config/vault/MCP/plugin layers. It does **not** execute checks or log into providers. If the script reports an incompatible upstream version, it restores `server.js` and `app.js`; do not force the patch manually.

<br />

## Compatibility and data safety

- Do not copy personal `.claude.json`, `settings.json` or vault data into the dashboard package.
- Do not expose raw MCP URLs with keys, token headers, environment variables, or session text in HTTP responses.
- Installed files and enabled plugins are configuration evidence only; the live connection-check action is separate.
- Claude Map itself includes file editing and terminal features. Keep it local and trusted.
- Upstream code and license remain attributed to the project author. This repository ships overlays, not the original project's complete source.

[Full setup](../../docs/installation/full-setup.md) · [Architecture](../../docs/architecture.md) · [Security](../../SECURITY.md)
