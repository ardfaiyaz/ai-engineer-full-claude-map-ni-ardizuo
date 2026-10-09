# Local Claude Map dashboard

**Optional dashboard extension — packaging pending.** This public repository does not yet contain the tested custom source from the author's machine.

<br />

## Intended appearance

- Five-stage Workflow Surface and Completion Mandate.
- Agent, Skill, Hook, Config, Memory, MCP and Plugin layers.
- Minimal black/white UI; restrained green for confirmed, red for absent, neutral for unknown/built-in.
- Read-only inventory; no automatic commits, deployments or note writes.

<br />

## Setup and requirements

Read [upstream Claude Map](https://github.com/shamim0902/claude-map), [Node/npm](../../docs/installation/nodejs-npm.md) and [local dashboard guide](../../docs/installation/claude-map.md).

Before this project offers a supported installation, the overlay must be pinned to a compatible upstream version, include full notices and tests, and expose **sanitized status only** to localhost.

<br />

## Security and troubleshooting

Never expose tokens, MCP auth headers, process environments, vault content or `.claude.json` through the dashboard server. A missing display entry can be a discovery limitation; verify in Claude Code itself (`/skills`, `/mcp`, `claude plugin list`).

<br />

[Security](../../SECURITY.md) · [Architecture](../../docs/architecture.md) · [README](../../README.md)
