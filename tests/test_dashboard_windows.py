"""Windows npm command-resolution and read-only dashboard preflight checks."""
import importlib.util
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / 'scripts/install-dashboard.py'
spec = importlib.util.spec_from_file_location('ardizuo_dashboard_windows', MODULE)
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)


class DashboardWindowsTests(unittest.TestCase):
    def test_windows_uses_npm_cmd_not_bare_npm(self):
        with patch.object(dashboard.shutil, 'which', side_effect=lambda exe: 'C:/node/npm.cmd' if exe == 'npm.cmd' else None) as finder:
            self.assertEqual(dashboard.find_cli('npm', windows=True), 'C:/node/npm.cmd')
            self.assertEqual(finder.call_args_list[0].args, ('npm.cmd',))

    def test_missing_npm_recommends_explicit_map_root(self):
        with patch.object(dashboard.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(RuntimeError, '--map-root'):
                dashboard.find_cli('npm', windows=True)

    def test_windows_npm_root_lookup(self):
        with patch.object(dashboard, 'find_cli', return_value='C:/Program Files/nodejs/npm.cmd'):
            with patch.object(dashboard.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='C:/Users/Test/AppData/Roaming/npm/node_modules\n')) as run:
                root = dashboard.detect_map_root()
                self.assertEqual(root.name, 'claude-map')
                self.assertTrue(root.as_posix().endswith('node_modules/claude-map'))
                self.assertEqual(run.call_args.args[0][1:], ['root', '-g'])

    def test_explicit_folder_preview_is_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'public').mkdir()
            (root / 'package.json').write_text('{"version":"1.2.3"}')
            source = """const TAB_GROUPS_GLOBAL = [
const TAB_GROUPS_PROJECT = [
const TAB_META = {
    mcp:      renderMCP,
function renderMCP() {
"""
            (root / 'public/app.js').write_text(source)
            (root / 'server.js').write_text('const x = 1;\n')
            self.assertEqual(dashboard.main(['--map-root', str(root)]), 0)
            self.assertEqual((root / 'public/app.js').read_text(), source)
            self.assertEqual((root / 'server.js').read_text(), 'const x = 1;\n')

    def test_incompatible_upstream_refuses_before_change(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'public').mkdir()
            (root / 'public/app.js').write_text('const completely_different = 1;')
            (root / 'server.js').write_text('const x = 1;\n')
            with self.assertRaisesRegex(RuntimeError, 'Nothing changed'):
                dashboard.main(['--map-root', str(root)])
            self.assertEqual((root / 'public/app.js').read_text(), 'const completely_different = 1;')


if __name__ == '__main__':
    unittest.main()
