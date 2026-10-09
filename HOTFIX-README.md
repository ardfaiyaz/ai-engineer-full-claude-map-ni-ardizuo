# Ardizuo Windows hook-registration hotfix

This patch fixes a bug in `scripts/register-hooks.mjs` where Windows-style backslashes in previously registered commands weren't recognized. As a result, re-running registration kept appending the same five hooks.

## Contents

- `scripts/register-hooks.mjs`: normalize path separators before detecting already registered hooks.
- `tests/test_hook_registration.py`: regression tests for first install, repeated install, and existing Windows paths.

## Apply

Extract this ZIP into your local Ardizuo repository using `Expand-Archive -Force`. It only updates the registration script and adds a test. Run `python -m unittest discover -s tests -v` afterward.

## Existing test-directory duplicates

The patch prevents **new** duplicates; it deliberately does not delete any previous entries from `settings.json`. Use a new isolated test directory to verify fixed behavior. Review/clean old test settings separately, and don't activate duplicates in your live Claude config.
