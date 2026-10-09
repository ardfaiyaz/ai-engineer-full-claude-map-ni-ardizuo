# <img src="../../assets/lucide/bot.svg" width="18" height="18" alt="" /> Diagram architect — original agent

**Purpose:** Generate evidence-based architecture, flow, sequence and data diagrams for development tasks. This agent definition is included under `ardizuo-plugin/agents/diagram-architect.md`.

<br />

## <img src="../../assets/lucide/download.svg" width="18" height="18" alt="" /> Install and verify

```powershell
.\scripts\install-all.ps1
.\scripts\install-all.ps1 -Apply
python .\scripts\verify-all.py
```

In Claude Code, ask the assistant explicitly to delegate a **read-only architecture review** to `diagram-architect`. Confirm the delegation actually happened; neither this README nor Claude Map can prove execution without a trace.

<br />

**Safety:** The agent is intended to inspect repository evidence, avoid fabricated architecture, and refrain from edits without user approval. Review its current tools and scope before using it.

[All agents](./README.md) · [Component coverage](../coverage.md)
