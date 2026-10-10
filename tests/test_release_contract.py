"""Release status is a statically verified contract, not a claimed full replica."""
from pathlib import Path
import json
import re
import subprocess
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]

class ReleaseContractTests(unittest.TestCase):
    def test_static_release_exit_codes(self):
        r=subprocess.run([sys.executable,str(ROOT/'scripts/release-audit.py'),'--json'],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        j=json.loads(r.stdout)
        self.assertEqual(j['agentNames']['default'],21)
        self.assertEqual(j['directSkillNames']['default'],36)
        self.assertEqual(j['directSkillNames']['withUpstreamVariants'],41)
        self.assertEqual(j['directSkillNames']['target'],62)
        self.assertEqual(j['executableCommandNames']['default'],20)
        self.assertEqual(j['executableCommandNames']['withUpstreamVariants'],31)
        self.assertEqual(j['plugins']['documented'],12)
        self.assertEqual(j['targetMCPs']['documented'],9)
        self.assertFalse(j['freshWindowsAllLayersVerified'])
        strict=subprocess.run([sys.executable,str(ROOT/'scripts/release-audit.py'),'--strict'],capture_output=True,text=True)
        self.assertEqual(strict.returncode,2)
    def test_all_markdown_titles_use_emoji_without_svg_icon_dependencies(self):
        import importlib.util
        spec=importlib.util.spec_from_file_location('cleanup_markdown',ROOT/'scripts/cleanup-markdown.py')
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        valid={emoji+' ' for emoji in module.EMOJI.values()}
        total=0
        for file in ROOT.rglob('*.md'):
            if '__pycache__' in file.parts:continue
            total+=1; lines=file.read_text(encoding='utf-8-sig').splitlines()
            fence=False;fm=bool(lines and lines[0].strip()=='---')
            for i,line in enumerate(lines):
                if fm:
                    if i and line.strip()=='---':fm=False
                    continue
                if re.match(r'^\s*(```|~~~)',line):fence=not fence;continue
                if fence:continue
                m=re.match(r'^#{1,4}\s+(.*)$',line)
                if m:
                    self.assertTrue(any(m.group(1).startswith(emoji) for emoji in valid),f'{file.relative_to(ROOT)}: {line}')
                    self.assertNotIn('<img src=',m.group(1))
        self.assertGreaterEqual(total,65)
        changes,retired,images=module.plan(ROOT)
        self.assertEqual((len(changes),len(retired),len(images)),(0,0,0))
    def test_docs_disclose_personas_and_missing_origins(self):
        text=(ROOT/'docs/components/development-hub-surface.md').read_text(encoding='utf-8-sig')
        for fragment in ('personas','17 externally sourced','four unknown-source','178 discovered','five-stage'):
            self.assertIn(fragment,text)
        guide=(ROOT/'docs/installation/installed-layer-audit.md').read_text(encoding='utf-8-sig')
        self.assertIn('verify-installed-layers.py',guide)
    def test_dashboard_never_auto_reinstalls_live_npm(self):
        script=(ROOT/'scripts/install-all.py').read_text(encoding='utf-8-sig')
        dashboard=script[script.index('    if args.dashboard:'):script.index("    print('\\nFINAL STATUS')")]
        self.assertNotIn('npm install -g',dashboard)
        self.assertNotIn("'--apply'",dashboard)
        self.assertIn('manual-rehearsal-required',dashboard)

if __name__=='__main__':unittest.main()
