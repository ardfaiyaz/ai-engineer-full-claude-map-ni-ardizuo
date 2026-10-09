# Ardizuo Claude Map — full five-stage sandbox rehearsal

This update adds a **read-only-on-live-files** rehearsal mode. All 5 patch scripts
run against temporary copies of the dashboard source with HOME, USERPROFILE and
CLAUDE_CONFIG_DIR redirected to a temporary workspace. It does NOT execute the
live dashboard or install third-party packages.

1. Extract over the repository with `Expand-Archive -Force`.
2. Run `python -m unittest discover -s tests -v` (expected: 31 tests pass).
3. Run `python .\scripts\install-dashboard.py --rehearse` to test your current
   installed sources (may fail if already patched).
4. For clean-release verification, follow the `npm pack claude-map@1.2.3`
   commands in `dashboard/claude-map/README.md`, then `--map-root ... --rehearse`.
5. Do NOT run `--apply` until the full five-stage rehearsal passes AND the
   browser/runtime behavior is reviewed in a disposable installation.

A rehearsal success is evidence of patch source compatibility and syntax only.
