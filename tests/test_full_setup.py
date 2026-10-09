"""Fast, offline release checks for the one-entrypoint assisted Full setup."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import re

ROOT=Path(__file__).resolve().parents[1]
class FullSetupTests(unittest.TestCase):
    def test_reference_coverage(self):
        data=json.loads((ROOT/'setup/full-stack.json').read_text())
        self.assertEqual(len(data['plugins']),12)
        self.assertEqual(len(data['mcp']),9)
        self.assertEqual(len(set(x['name'] for x in data['mcp'])),9)
        self.assertEqual(len(set(x['id'] for x in data['plugins'])),12)
        self.assertEqual(len(json.loads((ROOT/'setup/development-assets.json').read_text())['filePaths']),28)
    def test_manifest_never_embeds_auth(self):
        text=(ROOT/'setup/full-stack.json').read_text().lower()
        self.assertNotIn('ghp_',text)
        self.assertNotIn('authorization: bearer ',text)
        self.assertNotIn('c:\\users\\melthon',text)
        self.assertNotIn('vidiq',text)
    def test_dryrun_and_safe_reinstall(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)/'config'
            entry=[sys.executable,str(ROOT/'scripts/install-all.py'),'--config-dir',str(cfg)]
            a=subprocess.run(entry,capture_output=True,text=True)
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertFalse(cfg.exists())
            b=subprocess.run(entry+['--apply'],capture_output=True,text=True)
            self.assertEqual(b.returncode,0,b.stderr)
            self.assertTrue((cfg/'hooks/lib/common.mjs').is_file())
            c=subprocess.run(entry+['--apply'],capture_output=True,text=True)
            self.assertEqual(c.returncode,0,c.stderr)
            self.assertIn('identical',c.stdout)
            self.assertTrue((cfg/'CLAUDE.md').is_file())
            self.assertTrue((cfg/'assets/lucide/workflow.svg').is_file())
            (cfg/'agents/diagram-architect.md').write_text('user customization')
            d=subprocess.run(entry+['--apply'],capture_output=True,text=True)
            self.assertNotEqual(d.returncode,0)
            self.assertIn('CONFLICT',d.stdout)
            self.assertEqual((cfg/'agents/diagram-architect.md').read_text(),'user customization')
            e=subprocess.run(entry+['--apply','--external','--plugins'],capture_output=True,text=True)
            self.assertNotEqual(e.returncode,0)
            self.assertIn('Cannot isolate external',e.stderr)
    def test_all_markdown_local_links(self):
        miss=[]
        for file in ROOT.rglob('*.md'):
            if '__pycache__' in file.parts:continue
            source=file.read_text(encoding='utf-8-sig')
            # only regular Markdown links and <img src>; skip HTTP, dynamic anchors, code examples
            parts=re.findall(r'(?<!!)\[[^]\n]*\]\(([^)]+)\)',source)+re.findall(r'<img\s+[^>]*src="([^"]+)"',source)
            for part in parts:
                target=part.split('#',1)[0].split(' ',1)[0]
                if not target or target.startswith(('http:','https:','#','mailto:','data:')):continue
                if not (file.parent/target).exists():miss.append((str(file.relative_to(ROOT)),target))
        self.assertEqual(miss,[])
if __name__=='__main__':unittest.main()
