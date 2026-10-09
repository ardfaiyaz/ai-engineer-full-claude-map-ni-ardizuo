"""Sprint 4: strict private-to-upstream matching policies, never copied private content."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('sprint4_skills',ROOT/'scripts/install-pinned-skills.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class SkillPromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock=json.loads((ROOT/'setup/source-provenance-lock.json').read_text('utf-8'))
        cls.rows={r['target']:r for r in cls.lock['entries'] if r['target'].startswith('skills/')}
        cls.leads=json.loads((ROOT/'setup/skill-source-candidates.json').read_text('utf-8'))['entries']

    def test_exactly_four_unmapped_remain(self):
        expected={'accessibility-diff','accessibility-inspect','accessibility-scan','owasp-security'}
        got={r['target'].split('/')[1] for r in self.rows.values() if r['installPolicy']=='manual-source-review'}
        self.assertEqual(got,expected)

    def test_three_new_opt_in_variants_not_in_default(self):
        new={'accessibility-audit','accessibility-fix','playwright-best-practices'}
        self.assertEqual({r['target'].split('/')[1] for r in self.rows.values() if r['installPolicy']=='opt-in-upstream-variant'},new|{'impeccable','supabase'})
        defaults={r['target'].split('/')[1] for r,_ in mod.selected_rows(self.lock)}
        variants={r['target'].split('/')[1] for r,_ in mod.selected_rows(self.lock,True)}
        self.assertTrue(new.isdisjoint(defaults))
        self.assertTrue(new.issubset(variants))

    def test_twelve_new_verified_matches(self):
        verified=[r for r in self.leads if r.get('lastComparedStatus') in ('EXACT_BYTE_MATCH','TEXT_MATCH_LINE_ENDINGS_ONLY')]
        self.assertEqual(len(verified),12)
        self.assertTrue(all(self.rows[r['target']]['installPolicy']=='automatic-reviewed-upstream' for r in verified))
        self.assertTrue(all(len(self.rows[r['target']]['gitBlobSHA1'])==40 for r in verified))

    def test_unknowns_have_no_downloadable_metadata(self):
        for row in self.rows.values():
            if row['installPolicy']=='manual-source-review':
                self.assertNotIn('gitBlobSHA1',row)
                self.assertNotIn('upstreamRepository',row)

    def test_public_lock_contains_no_private_hashes(self):
        txt=(ROOT/'setup/source-provenance-lock.json').read_text('utf-8')
        self.assertNotIn('localSHA256',txt)
        self.assertNotIn('privateDirectory',txt)

if __name__=='__main__':unittest.main()
