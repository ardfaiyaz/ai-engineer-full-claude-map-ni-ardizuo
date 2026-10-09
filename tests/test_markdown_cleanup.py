"""Tests for non-destructive cleanup of presentation-only Markdown assets."""
from pathlib import Path
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/cleanup-markdown.py'
spec = importlib.util.spec_from_file_location('markdown_cleanup', SCRIPT)
cleanup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cleanup)

class MarkdownCleanupTests(unittest.TestCase):
    def test_converts_known_icons_but_keeps_a_real_banner(self):
        data = ('# <img src="assets/lucide/workflow.svg" width="18" /> Start\n'
                '<img src="./banner.png" width="100%" />\n'
                '## <img src="docs/assets/icons/shield.svg" /> Security\n')
        converted = cleanup.transform(data)
        self.assertIn('# 🔄 Start', converted)
        self.assertIn('## 🛡️ Security', converted)
        self.assertIn('<img src="./banner.png" width="100%" />', converted)
    def test_preserves_yaml_frontmatter_and_fenced_code(self):
        data = ('---\nname: example\n---\n'
                '## <img src="assets/lucide/download.svg" /> Install\n'
                '```md\n# <img src="assets/lucide/monitor.svg" /> literal example\n```\n')
        x = cleanup.transform(data)
        self.assertIn('name: example', x)
        self.assertIn('## 📥 Install', x)
        self.assertIn('# <img src="assets/lucide/monitor.svg" /> literal example', x)
    def test_idempotent(self):
        data = '# <img src="assets/lucide/book-open.svg" /> Guide\n'
        self.assertEqual(cleanup.transform(cleanup.transform(data)), cleanup.transform(data))
    def test_plan_only_deletes_known_handoff_notes_and_presentation_icons(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root/'README.md').write_text('# <img src="docs/assets/lucide/rocket.svg" /> Welcome\n## 🛡️ Security and licensing\n',encoding='utf8')
            (root/'SPRINT-2-READ-ME.md').write_text('# old sprint\n',encoding='utf8')
            (root/'keep.md').write_text('# keep\n',encoding='utf8')
            (root/'docs/assets/lucide').mkdir(parents=True)
            (root/'docs/assets/lucide/rocket.svg').write_text('<svg />')
            (root/'docs/assets/lucide/diagram.png').write_bytes(b'123')
            changes,retired,icons=cleanup.plan(root)
            self.assertEqual([x.name for x in changes], ['README.md'])
            self.assertEqual([x.name for x in retired], ['SPRINT-2-READ-ME.md'])
            self.assertEqual([x.name for x in icons], ['rocket.svg'])
            self.assertTrue((root/'docs/assets/lucide/diagram.png').exists())
    def test_unrecognized_icon_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'Unknown presentation icon'):
            cleanup.transform('# <img src="assets/lucide/unknown-brand-new-icon.svg" /> Untested\n')
    def test_repository_passes_read_only_check(self):
        r=subprocess.run([sys.executable,str(SCRIPT),'--check'],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)

if __name__=='__main__':unittest.main()
