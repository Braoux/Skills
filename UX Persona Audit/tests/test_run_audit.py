import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "run_audit.py"
spec = importlib.util.spec_from_file_location("run_audit", MODULE)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.config = {"expected_purpose": "Un site qui vend du café", "key_elements": ["tarifs", "bouton commander"],
                       "motivations": ["commander", "comparer"], "target_audiences": ["amateur", "novice"]}

    def test_profiles_100_unique_and_device_distribution(self):
        ps = audit.profiles(100, self.config, seed=42)
        self.assertEqual(100, len(ps))
        self.assertEqual(len(ps), len({(p['age'], p['job'], p['motivation'], p['audience'], p['device'], p['digital_comfort']) for p in ps}))
        counts = {d: sum(p['device'] == d for p in ps) for d in audit.DEVICES}
        self.assertEqual(counts, {"mobile": 50, "desktop": 35, "tablet": 15})
        self.assertEqual(ps, audit.profiles(100, self.config, seed=42))

    def test_small_pilot_has_devices(self):
        ps = audit.profiles(5, self.config, seed=23)
        self.assertTrue(any(p['device'] == 'mobile' for p in ps))
        self.assertTrue(any(p['device'] == 'desktop' for p in ps))
        self.assertTrue(any(p['device'] == 'tablet' for p in ps))

    def test_report_counts_exact_with_no_invented_top_10(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            persons = audit.profiles(3, self.config, seed=42)
            for i, p in enumerate(persons):
                pid = p['id']
                audit.write_json(root / 'visits' / f'{pid}.json', {"id": pid, "status": "captured", "load_ms": 280})
                audit.write_json(root / 'assessments' / f'{pid}.json', {"id": pid, "status": "ok", "persona": p,
                    "feedback": {"purpose_guess": "café", "felt_clear": i != 2, "lost": "CTA introuvable",
                                 "likes": [], "confusions": ["cta_ambiguous"] if i != 2 else [],
                                 "positives": ["good_visual"] if i == 0 else []}})
            audit.write_json(root / 'judgments' / 'P001-P003.json', {"status": "ok", "judgments": {
                persons[0]['id']: {"purpose_correct": True, "noticed": ["tarifs"]},
                persons[1]['id']: {"purpose_correct": False, "noticed": []},
                persons[2]['id']: {"purpose_correct": False, "noticed": []}}})
            audit.make_report(root, persons, self.config, 'https://example.com', 15, 'mock-model')
            report = (root / 'report.md').read_text()
            summary = audit.read_json(root / 'summary.json')
            self.assertIn('2/3 (67 %)', report)
            self.assertIn('1/3 (33 %)', report)
            self.assertIn('Seulement', report)
            self.assertEqual(summary['captured'], 3)
            self.assertEqual(summary['assessed'], 3)
            self.assertEqual(summary['understood_correctly'], 1)
            self.assertEqual(summary['confusions']['cta_ambiguous'], 2)
            self.assertEqual(sum(x['count'] == 2 for x in summary['priorities']) > 0, True)
            self.assertTrue((root / 'personas.csv').exists())


if __name__ == '__main__':
    unittest.main()
