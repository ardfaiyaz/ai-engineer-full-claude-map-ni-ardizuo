# Maintainer next steps

Your repository scaffold is not the same as your installed machine. Import reviewed original assets deliberately.

1. Run `scripts/doctor.ps1` and `scripts/export-inventory.ps1` on your own Windows system. This gives filenames without copying private source or API credentials.
2. **Review** the names-only inventory report before sharing it. Confirm authorship and licenses; remove unwanted components.
3. Review each global original agent, skill and hook *source* privately before adding it to `ardizuo-plugin`. Replace absolute user paths, local vault names and project names with documented, opt-in variables.
4. Reference third-party plugins/MCPs in the manifest and create tested installation instructions. Never publish their caches or live OAuth/API keys.
5. Extend `install.ps1` with manifest-driven, pinned, opt-in components; add tests for idempotence, changes, undo and user-scoped registration.
6. Package local Claude Map as a version-pinned, attributed patch. Test route security and response redaction.
7. Choose an OSI-approved license for original code, complete `THIRD_PARTY_NOTICES.md`, and run a secret audit before your first public push.

**Proof expectations:** tool detected ≠ invoked; MCP configured ≠ authenticated; note folder exists ≠ memory persisted; hook source exists ≠ active hook. Document test evidence separately.
