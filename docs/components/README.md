# 🗂️ Components and capabilities


This setup has five workflow stages: **Triage → Contract → Dispatch → Review → Ship**. A dashboard label can mean a local definition, native Claude command, plugin skill or MCP-equivalent capability.


<br />
<br />


## 📋 Choose a layer


| Layer | Explanation |
| --- | --- |
| Agents | [21 agent definitions](./agents/README.md) |
| Ardizuo skills | [17 original skills](./skills/README.md), including `version-log` |
| Hooks | [Five lifecycle hooks](./hooks/README.md) |
| Commands | [Original command](./commands/README.md) and pinned SuperClaude commands |
| Plugins | [12-plugin catalog](../../integrations/plugins/README.md) |
| MCP servers | [Nine-MCP catalog](../../integrations/mcp/README.md) |
| Dashboard | [Development Hub display](./development-hub-surface.md) |
| Extended stack | [Master extension catalog](./extension-catalog.md): 74 researched rows, installed by `-All` |


<br />
<br />


## 🔎 What is actually installed?


```powershell
python .\scripts\coverage-doctor.py
python .\scripts\release-audit.py
python .\scripts\install-extensions.py --status
```

Run from the repo root. These check **different things**: the source computer's available names versus what the public package can reproduce. A discovered label is not proof of execution.

[Full reference inventory](./coverage.md) · [Quick start](../../START-HERE.md)
