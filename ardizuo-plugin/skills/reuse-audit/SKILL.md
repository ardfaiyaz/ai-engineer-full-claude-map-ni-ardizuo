---
name: reuse-audit
description: Audit modified software code for duplicated logic, unnecessary abstractions, and opportunities to reuse existing components, hooks, utilities, and services.
disable-model-invocation: true
---


# ☑️ Reuse Audit


Inspect the relevant repository before recommending changes.

1. Identify duplicated components, functions and business logic.
2. Search for existing utilities and abstractions that could be reused.
3. Identify unnecessary wrappers and redundant implementations.
4. Report findings with file paths and supporting evidence.
5. Distinguish genuine duplication from deliberate separation.
6. Prioritize simple, maintainable improvements.
7. Do not modify code unless separately authorized.

Output:
- Finding
- File location
- Existing reusable alternative
- Suggested improvement
- Risk or trade-off
