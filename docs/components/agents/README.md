# 🤖 Agent layer


The reference installation lists **21 global agent names**: 20 provided by the upstream [SuperClaude Framework](../../installation/superclaude.md) and one original `diagram-architect` agent.


[All agent names and origins](../coverage.md) · [Diagram architect](./diagram-architect.md)

Global agent definitions belong in `<ClaudeConfig>/agents/`. An installed agent is not necessarily spawned during a task. Verify an actual delegation in the Claude transcript before claiming one ran.

Four researched **agent collections** (wshobson Agents, Everything Claude Code, gstack and Compound Engineering) are listed in the [master extension catalog](../extension-catalog.md). `-All` installs them: ECC, wshobson Agents and Compound Engineering as plugins, gstack as a Git skill suite. Their agents live inside those plugins, so the 21 global agent definitions listed above stay unchanged.
