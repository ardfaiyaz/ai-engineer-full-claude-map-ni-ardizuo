---
name: dead-code-scan
description: Investigate potentially unused code, imports, dependencies and unreachable branches using repository-aware analysis tools.
disable-model-invocation: true
---


# 📄 Dead Code Scan


Use the existing dead-code-check hook as an advisory signal.

1. Inspect the repository structure and supported tooling.
2. Use the project's linter, compiler, and type checker when available.
3. Investigate unused imports, variables, functions and exports.
4. Review potentially unreachable code.
5. Check references before declaring public exports unused.
6. Account for dynamic imports, reflection and framework conventions.
7. Categorize findings as confirmed, likely or uncertain.
8. Never automatically delete code.

Prefer project-native analysis over regular expressions.

Report relevant file paths, evidence and recommended actions.
