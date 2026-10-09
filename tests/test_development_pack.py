"""Phase 1 source manifest, portability, and package integrity checks."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACK = ROOT / 'ardizuo-plugin'

class DevelopmentPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / 'setup' / 'development-assets.json').read_text(encoding='utf-8'))
        cls.files = cls.manifest['filePaths']

    def test_exact_packaged_files(self):
        self.assertEqual(len(self.files), 28)
        self.assertEqual(len(set(self.files)), 28)
        expected = {p.relative_to(PACK).as_posix() for p in PACK.rglob('*') if p.is_file() and p.name != 'README.md' and '.claude-plugin' not in p.parts}
        self.assertEqual(expected, set(self.files))

    def test_paths_are_bounded(self):
        for path in self.files:
            parts = pathlib.PurePosixPath(path).parts
            self.assertNotIn('..',parts)
            self.assertIn(parts[0],{'agents','skills','hooks','rules','commands','workflows'})

    def test_no_author_specific_path(self):
        for rel in self.files:
            content = (PACK / rel).read_text(encoding='utf-8-sig')
            self.assertNotIn('C:\\Users\\Melthon',content,rel)
            self.assertNotIn('Melthon',content,rel)

    def test_required_hook_shared_helper_exists(self):
        self.assertIn('hooks/lib/common.mjs',self.files)
        for rel in self.files:
            if rel.startswith('hooks/') and rel != 'hooks/lib/common.mjs':
                content = (PACK / rel).read_text(encoding='utf-8')
                if './lib/common.mjs' in content:
                    self.assertTrue((PACK / 'hooks/lib/common.mjs').is_file())

    def test_approval_intent_retained(self):
        txt = (PACK / 'commands/log-to-vault.md').read_text(encoding='utf-8')
        self.assertIn('explicit',txt.lower())
        self.assertIn('Revise first',txt)
        self.assertIn("Don't save",txt)

if __name__ == '__main__':
    unittest.main()
