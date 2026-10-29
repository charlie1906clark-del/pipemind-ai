"""Semantic regressions: provenance and statuses matter more than note counts."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]

class AssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph=json.loads((ROOT/'data/graph.json').read_text())
        cls.nodes={n['id']:n for n in cls.graph['nodes']}

    def test_negated_conviction_is_charges(self):
        self.assertEqual(self.nodes['HC-C02']['properties']['legal_status'],'charged')

    def test_unchecked_sentencing_does_not_upgrade_plea(self):
        for cid in ['PROC-C006','XS-C05','XS-C07']:
            self.assertEqual(self.nodes[cid]['properties']['legal_status'],'guilty_plea')

    def test_people_are_not_organizations(self):
        for cid in ['HC-C07-entity-2','HC-C08-entity-2']:
            self.assertEqual(self.nodes[cid]['type'],'person')

    def test_samples_never_rank_fraud_or_claim_population(self):
        cohorts=[n for n in self.nodes.values() if n['type']=='cohort']
        self.assertEqual(sum(n['properties']['rows'] for n in cohorts),65)
        for n in cohorts:
            self.assertFalse(n['properties']['sample_complete'])
            self.assertFalse(n['properties']['is_fraud_rank'])

    def test_no_legal_matter_is_linked_to_neutral_award(self):
        award='PROC-AWARD-W31P4Q24C0003'
        case_ids={n['id'] for n in self.nodes.values() if n['type']=='case'}
        for e in self.graph['edges']:
            self.assertFalse((e['source']==award and e['target'] in case_ids) or
                             (e['target']==award and e['source'] in case_ids))

    def test_all_amounts_explicit_and_nonadditive(self):
        money=[n for n in self.nodes.values() if n['type']=='money_measure']
        for n in money:
            p=n['properties'];self.assertFalse(p['aggregation_permitted'])
            self.assertIn('qualifier',p['money']);self.assertIn('period',p['money'])

    def test_source_collection_claim_not_independent_verification(self):
        measures=[n for n in self.nodes.values() if n['id'].startswith('HC-C06-amount')]
        for n in measures:
            p=n['properties']
            self.assertEqual(p['source_reports_collection_verified'],p['source_amount_details'].get('collection_verified',False))
            self.assertFalse(p['independently_verified_collection'])

    def test_raw_bytes_match_source_hashes(self):
        for n in self.nodes.values():
            p=n['properties']
            if n['type']=='source' and p.get('source_bytes_archived'):
                self.assertEqual(hashlib.sha256((ROOT/p['snapshot_path']).read_bytes()).hexdigest(),p['content_sha256'])

    def test_repeat_build_reproduces_canonical_graph(self):
        before=(ROOT/'data/graph.json').read_bytes()
        subprocess.run([sys.executable,str(ROOT/'tools/assemble.py')],check=True,capture_output=True)
        self.assertEqual(before,(ROOT/'data/graph.json').read_bytes())

if __name__=='__main__':unittest.main()
