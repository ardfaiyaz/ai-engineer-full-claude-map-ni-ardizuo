"""Rehearsal must isolate subprocesses and preserve the actual package files."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ardizuo_rehearsal',ROOT/'scripts/install-dashboard.py')
dash=importlib.util.module_from_spec(spec)
spec.loader.exec_module(dash)


def fixture(root):
    (root/'public').mkdir(exist_ok=True)
    app='''const TAB_GROUPS_GLOBAL = [\n];
const TAB_GROUPS_PROJECT = [\n];
const TAB_META = {\n};
const renderers = {\n    mcp:      renderMCP,\n};
function renderMCP() { return ''; }
'''
    server="const app = {get(){}};\napp.get('/api/scan', async (req, res) => { });\n"
    (root/'server.js').write_text(server)
    (root/'public/app.js').write_text(app)
    (root/'package.json').write_text('{"version":"1.2.3"}')
    return app,server


class RehearsalTests(unittest.TestCase):
    def test_live_source_is_never_targeted_and_temp_home_is_used(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); app,server=fixture(root)
            calls=[]
            def fake_run(argv,**kwargs):
                calls.append((argv,kwargs))
                if 'env' in kwargs:
                    self.assertNotEqual(kwargs['env']['USERPROFILE'],str(Path.home()))
                    self.assertNotEqual(kwargs['env']['HOME'],str(Path.home()))
                    self.assertNotEqual(kwargs['env']['CLAUDE_CONFIG_DIR'],str(Path.home()/'.claude'))
                    self.assertNotIn(str(root/'public/app.js'),str(argv))
                    self.assertTrue(Path(kwargs['env']['USERPROFILE']).is_dir())
                return SimpleNamespace(returncode=0,stdout='ok',stderr='')
            with patch.object(dash.subprocess,'run',side_effect=fake_run):
                self.assertEqual(dash.rehearse_overlay(root,'node'),0)
            self.assertEqual(len(calls),7)
            self.assertEqual((root/'public/app.js').read_text(),app)
            self.assertEqual((root/'server.js').read_text(),server)

    def test_mutually_exclusive_live_apply_and_rehearse(self):
        with self.assertRaises(SystemExit) as exc:
            dash.main(['--apply','--rehearse'])
        self.assertEqual(exc.exception.code,2)

    def test_real_rehearsal_refuses_incompatible_anchors_without_live_changes(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); app,server=fixture(root)
            try:
                dash.main(['--map-root',str(root),'--rehearse'])
            except RuntimeError as exc:
                self.assertIn('REHEARSAL BLOCKED',str(exc))
            self.assertEqual((root/'public/app.js').read_text(),app)
            self.assertEqual((root/'server.js').read_text(),server)

if __name__=='__main__': unittest.main()
