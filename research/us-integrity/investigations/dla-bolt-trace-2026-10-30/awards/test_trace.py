import copy,hashlib,json,shutil,tempfile,unittest
from pathlib import Path
from analyze import verify,ROOT,HISTORY
class TraceTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.p=Path(self.tmp.name)/'capture';shutil.copytree(ROOT/'capture-success',self.p)
 def modify(self,name,change,rehash=True):
  p=self.p/name;d=json.loads(p.read_text());change(d);p.write_text(json.dumps(d,indent=2)+'\n')
  if rehash:
   mp=self.p/'manifest.json';m=json.loads(mp.read_text())
   for x in m:
    if x.get('snapshot')==name:x['snapshot_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();x['snapshot_bytes']=p.stat().st_size
   mp.write_text(json.dumps(m,indent=2)+'\n')
 def test_baseline_remains_summary_not_payment(self):
  d=verify(self.p);self.assertEqual(d['summary']['arithmetic_matches'],7);self.assertEqual(d['summary']['sum_current_award_obligations_usd'],'4962.02')
  self.assertTrue(all(not x['invoice_or_payment_verified'] and not x['historical_clin_verified'] and not x['fraud_finding'] for x in d['observations']))
 def test_tampered_response_rejected(self):
  self.modify('award-SPE4A626V138W.json',lambda d:d.update(total_obligation=999),False)
  with self.assertRaisesRegex(ValueError,'digest'):verify(self.p)
 def test_changed_identifier_rejected_even_with_new_digest(self):
  self.modify('award-SPE4A626V138W.json',lambda d:d.update(piid='OTHER'))
  with self.assertRaisesRegex(ValueError,'identifier'):verify(self.p)
 def test_changed_recipient_rejected_even_with_new_digest(self):
  self.modify('award-SPE4A626V138W.json',lambda d:d['recipient'].update(recipient_uei='OTHER'))
  with self.assertRaisesRegex(ValueError,'Recipient'):verify(self.p)
 def test_missing_terminal_page_rejected(self):
  self.modify('exact-award-terminal.json',lambda d:d.update(results=[{'Award ID':'OTHER'}]))
  with self.assertRaisesRegex(ValueError,'Terminal'):verify(self.p)
 def test_changed_history_rejected(self):
  p=Path(self.tmp.name)/'history.json';p.write_bytes(HISTORY.read_bytes()+b' ')
  with self.assertRaisesRegex(ValueError,'seed digest'):verify(self.p,p)
 def test_private_profile_field_rejected(self):
  self.modify('award-SPE4A626V138W.json',lambda d:d['recipient'].update(location={'address_line1':'not retained'}))
  with self.assertRaisesRegex(ValueError,'profile'):verify(self.p)
if __name__=='__main__':unittest.main()
