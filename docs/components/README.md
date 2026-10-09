# Component catalog

**The following is the reference-machine inventory, not a list of assets installed by the public Core script.** Choose the appropriate guide for a component before installing it.

<br />

| Component | What exists in the author's setup | Open the guide |
| :--- | :--- | :--- |
| Workflow | Triage → Contract → Dispatch → Review → Ship | [Architecture](../architecture.md) |
| Completion | simplify, code-review, reuse-audit, dead-code-scan, vault-learning | [Architecture](../architecture.md) |
| Agent definitions | 21 global Markdown files | [Agent packaging notes](../../ardizuo-plugin/README.md) |
| Skills | 62 global `SKILL.md` files; plugin caches may contain duplicates | [Plugins](../../integrations/plugins/README.md) |
| Hooks | Five Node `.mjs` scripts | [Agent/plugin packaging](../../ardizuo-plugin/README.md) |
| Commands | 32 global command names | [Architecture](../architecture.md) |
| Plugins | 12 enabled plugin names | [12 provider guides](../../integrations/plugins/README.md) |
| MCPs | Nine configured user servers | [9 server guides](../../integrations/mcp/README.md) |
| Memory | Optional Obsidian templates | [Obsidian](../installation/obsidian.md) |
| Dashboard | Local Claude Map customization | [Dashboard distribution](../../dashboard/claude-map/README.md) |

<br />

## What each guide answers

**What is it?** · **Do I need it?** · **Official source** · **Prerequisites** · **How to install** · **How to verify** · **How to troubleshoot or remove**

Some plugins supply differently named skills from those shown in the reference dashboard. **Via MCP or Via plugin does not equal an exact original skill.**

<br />

[Installation guides](../installation/README.md) · [API keys](../security/api-keys-and-powershell.md) · [Docs hub](../README.md)

<br />

## Full reference matrix

[All 21 agents and 62 global skill names, with provenance](./coverage.md) · [16 original skill guides](./skills/README.md)

<br />

## Deep dives by layer

[Agent layer](./agents/README.md) · [16 original skills](./skills/README.md) · [Five hooks](./hooks/README.md) · [Original commands](./commands/README.md)
