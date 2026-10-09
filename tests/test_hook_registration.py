"""Regression tests for repeated hook registration, including Windows paths."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "scripts/register-hooks.mjs"
HOOK_NAMES = (
    "skill-gate-check.mjs",
    "vault-session-init.mjs",
    "log-to-vault.mjs",
    "dead-code-check.mjs",
    "stop-vault-log.mjs",
)

@unittest.skipUnless(shutil.which("node"), "Node.js is required for registration tests")
class HookRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cfg = Path(self.tmp.name) / "Claude Test Config"
        (self.cfg / "hooks").mkdir(parents=True)
        for name in HOOK_NAMES:
            (self.cfg / "hooks" / name).write_text("// test fixture\n", encoding="utf-8")

    def run_register(self, *args):
        result = subprocess.run(
            ["node", str(REGISTER), "--config-dir", str(self.cfg), *args],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return result.stdout

    def test_first_apply_then_preview_and_repeat_apply_are_idempotent(self):
        self.assertIn("New hook registrations: 5", self.run_register())
        self.assertFalse((self.cfg / "settings.json").exists())
        self.assertIn("Added 5", self.run_register("--apply"))
        target = self.cfg / "settings.json"
        initial = target.read_bytes()
        self.assertIn("New hook registrations: 0", self.run_register())
        self.assertIn("New hook registrations: 0", self.run_register("--apply"))
        self.assertEqual(initial, target.read_bytes(), "repeat apply must not modify settings")
        data = json.loads(initial)
        self.assertEqual(set(data["hooks"]), {"UserPromptSubmit","SessionStart","PostToolUse","Stop"})
        self.assertEqual(sum(len(v) for v in data["hooks"].values()), 5)

    def test_existing_windows_style_hook_paths_are_detected(self):
        # The old registrar failed here, because Windows backslashes were
        # interpreted incorrectly inside its dynamic regular expression.
        entries = {
            "UserPromptSubmit": [("skill-gate-check.mjs", None)],
            "SessionStart": [("vault-session-init.mjs", "startup|resume")],
            "PostToolUse": [("log-to-vault.mjs", "Write|Edit|MultiEdit|NotebookEdit"),
                            ("dead-code-check.mjs", "Write|Edit|MultiEdit")],
            "Stop": [("stop-vault-log.mjs", None)]
        }
        hooks = {}
        for event, specs in entries.items():
            hooks[event] = []
            for name, matcher in specs:
                entry = {"hooks": [{"type": "command", "command": f'node "C:\\Users\\Test User\\.claude\\hooks\\{name}"'}]}
                if matcher: entry["matcher"] = matcher
                hooks[event].append(entry)
        settings = {"permissions": {"allow": ["Read"]}, "hooks": hooks}
        target = self.cfg / "settings.json"
        target.write_text(json.dumps(settings, indent=2), encoding="utf-8")
        before = target.read_bytes()
        self.assertIn("New hook registrations: 0", self.run_register())
        self.assertIn("New hook registrations: 0", self.run_register("--apply"))
        self.assertEqual(before, target.read_bytes())

    def test_preserves_unrelated_existing_hooks_and_settings(self):
        settings = {
            "permissions": {"deny": ["Bash(rm -rf *)"]},
            "hooks": {"Stop": [{"hooks": [{"type": "command", "command": "node special-unrelated-hook.js"}]}]},
        }
        target = self.cfg / "settings.json"
        target.write_text(json.dumps(settings), encoding="utf-8")
        self.assertIn("Added 5", self.run_register("--apply"))
        result = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(result["permissions"], settings["permissions"])
        self.assertEqual(result["hooks"]["Stop"][0], settings["hooks"]["Stop"][0])
        self.assertEqual(len(result["hooks"]["Stop"]), 2)
        self.assertIn("New hook registrations: 0", self.run_register())

if __name__ == "__main__":
    unittest.main()
