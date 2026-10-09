"""Safety tests for the unreviewed skills source-comparison step."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('remaining_skill_sources',ROOT/'scripts/verify-remaining-skill-sources.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class RemainingSkillsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=json.loads((ROOT/'setup/skill-source-candidates.json').read_text('utf-8'))['entries']

    def test_manifest_unapproved_and_bounded(self):
        mod.validate_candidates(self.rows)
        self.assertEqual(len(self.rows),19)
        self.assertEqual(sum(bool(x.get('candidateRepository')) for x in self.rows),15)
        self.assertTrue(all(x['approvedForInstall'] is False for x in self.rows))
        self.assertEqual(sum(x['status']=='matched-pinned-in-source-lock' for x in self.rows),12)
        self.assertEqual(sum(x['status']=='content-differs-upstream-opt-in-variant' for x in self.rows),3)
        self.assertEqual(sum(x['status']=='source-unknown' for x in self.rows),4)

    def test_preview_reads_no_private_bytes_and_does_not_write_report(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'report.csv'
            r=subprocess.run([sys.executable,str(ROOT/'scripts/verify-remaining-skill-sources.py'),'--private-root',str(Path(d)/'missing'),'--output',str(f)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('DRY RUN',r.stdout)
            self.assertFalse(f.exists())

    def test_local_comparison_without_network(self):
        target=next(x for x in self.rows if x.get('candidateRepository'))
        body=b'---\nname: example\n---\n';row=dict(target)
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/row['target'];src.parent.mkdir(parents=True)
            src.write_bytes(body.replace(b'\n',b'\r\n'))
            result=mod.compare_rows([row],Path(d),fetch=lambda _:body)
            self.assertEqual(result[0]['comparison'],'TEXT_MATCH_LINE_ENDINGS_ONLY')
            src.write_bytes(b'other')
            result=mod.compare_rows([row],Path(d),fetch=lambda _:body)
            self.assertEqual(result[0]['comparison'],'DIFFERENT_CONTENT')

    def test_fail_closed_on_unreviewed_source(self):
        row=dict(next(x for x in self.rows if x.get('candidateRepository')))
        row['candidateRepository']='untrusted/random'
        with self.assertRaises(ValueError):mod.validate_candidates([row]*19)

if __name__=='__main__':unittest.main()
