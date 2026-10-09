# Developer orchestration architecture

```text
Triage  →  Contract  →  Dispatch  →  Review  →  Ship
    discovery      ownership         specialists        quality     deliverables

Completion mandate (with actual execution evidence):
simplify · code-review · reuse-audit · dead-code-scan · vault-learning

Layers: Agents → Skills → Hooks → Configuration → Memory → MCP/Plugins
```

**Critical distinction:** a dashboard listing an available skill doesn't prove it ran; a configured MCP doesn't prove live connection; a hook file doesn't prove event activation; an Obsidian folder doesn't prove notes were saved or retrieved.

## Planned global configuration

The author's existing Windows system contains specialist agent definitions, nested/third-party skills, 5 user-authored hook scripts, custom rules/workflows and an Obsidian vault. Those local files are **not** bundled in this bootstrap until each is reviewed for secrets, user-specific paths, dependencies, copyright and side effects.

## Local dashboard

Claude Map remains localhost-only. A future dashboard distribution will use an attributed upstream fork or versioned patch; it will not expose raw configuration or credentials via HTTP endpoints.
