"""Reject source tampering and contradictory identifier joins."""
import contextlib,io,json,shutil,tempfile,unittest
from pathlib import Path
import build_records as b
class IdentityContractTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.r=Path(self.tmp.name);self.old=(b.ROOT,b.INV,b.BASE)
  inv=self.r/'investigations/dla-bolt-trace-2026-10-30';root=inv/'identity';base=self.r/'investigations/discovery-policy-2026-10-30'
  shutil.copytree(b.ROOT,root,ignore=shutil.ignore_patterns('__pycache__'))
  shutil.copytree(b.INV/'awards/capture-success',inv/'awards/capture-success')
  (base/'pricing/snapshots').mkdir(parents=True)
  shutil.copy2(b.BASE/'pricing/snapshots/selected_evidence.json',base/'pricing/snapshots/selected_evidence.json')
  b.ROOT,b.INV,b.BASE=root,inv,base
 def tearDown(self):b.ROOT,b.INV,b.BASE=self.old;self.tmp.cleanup()
 def run_build(self):
  with contextlib.redirect_stdout(io.StringIO()):b.main()
 def test_unrepinned_profile_tampering_rejected(self):
  p=b.ROOT/'snapshots/6ZF42-profile.json';d=b.read(p);d['uei']='WRONG1234567';b.write(p,d)
  with self.assertRaisesRegex(ValueError,'hash mismatch'):self.run_build()
 def test_repinned_cage_contradiction_rejected(self):
  p=b.ROOT/'snapshots/cage-6ZF42-selected.json';d=b.read(p);d['selected_text']=[x.replace('GWEEKJ2PNL45','WRONG1234567') for x in d['selected_text']];b.write(p,d)
  m=b.read(b.ROOT/'capture_manifest.json')
  for x in m['cage_captures']:
   if x['id']=='CAGE-6ZF42':x['snapshot_sha256']=b.digest(p)
  b.write(b.ROOT/'capture_manifest.json',m)
  with self.assertRaisesRegex(ValueError,'CAGE registry selection'):self.run_build()
 def test_repinned_award_uei_contradiction_rejected(self):
  p=b.INV/'awards/capture-success/award-SPE4A626V138W.json';d=b.read(p);d['recipient']['recipient_uei']='WRONG1234567';b.write(p,d)
  m=b.read(p.parent/'manifest.json')
  for x in m:
   if x['snapshot']==p.name:x['snapshot_sha256']=b.digest(p)
  b.write(p.parent/'manifest.json',m)
  with self.assertRaisesRegex(ValueError,'Historical award/identity mismatch'):self.run_build()
 def test_current_hierarchy_does_not_assert_ownership_or_historical_eligibility(self):
  self.run_build();d=b.read(b.ROOT/'entity_records.json')
  for e in d['entities']:
   self.assertIsNone(e['beneficial_owners']);self.assertIsNone(e['historical_registration_status']);self.assertIsNone(e['alias_effective_dates']);self.assertFalse(e['sam_active_registration_verified']);self.assertFalse(e['fraud_assessment'])
  for r in b.read(b.ROOT/'relationships.json')['relationships']:
   if r['relationship']=='source_reports_parent':self.assertFalse(r['beneficial_ownership_inferred'])
if __name__=='__main__':unittest.main()
