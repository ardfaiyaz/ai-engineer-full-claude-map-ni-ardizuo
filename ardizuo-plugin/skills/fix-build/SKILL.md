---
name: fix-build
description: Diagnose and fix application build failures with minimal changes.
disable-model-invocation: true
---

# Fix Build

This is an original local development-focused adapter, not an official third-party skill.

Run the repository build command when permitted. Save the exact error. Identify the first root cause rather than fixing secondary errors blindly. Inspect package scripts and toolchain versions. Make a scoped change, then rerun the failed build and relevant checks. Report the actual exit status.
