#!/usr/bin/env python3
"""Offline source-link, identifier-join and unsupported-role regression checks."""
import copy,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
ROOT=R.parents[2]
def load(p):return json.loads((R/p).read_text())
def digest(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def validate(graph):
 src=load('sources.json')['sources'];ids={s['id'] for s in src}
 nodes={n['id']:n for n in graph['nodes']}
 assert len(nodes)==len(graph['nodes']),'duplicate node'
 for s in src:assert digest(s['snapshot_path'])==s['snapshot_sha256'],'source snapshot drift'
 for x in graph['nodes']+graph['edges']:
  assert set(x['source_ids'])<=ids,'unknown evidence source'
  assert x['status'] not in {'allegation','conviction','audit_finding'},'unsupported adverse status'
 for e in graph['edges']:assert e['source'] in nodes and e['target'] in nodes,'dangling edge'
 for cage,tag in [('745V4','DON'),('27624','SPS')]:
  c=load('cage-'+cage+'-selected.json');p=load('profile-'+cage+'-selected.json');n=nodes['TP-ORG-'+tag]
  assert c['query']==cage and len(c['result_links'])==1,'ambiguous registry result'
  assert {cage,p['name'],p['uei']}<=set(c['selected_text']),'registry/profile join mismatch'
  assert n['properties']['cage']==cage and n['properties']['uei']==p['uei'],'graph identity mismatch'
  assert n['properties']['beneficial_owner'] is None,'unsupported owner'
 a=load('../detail-capture/detail-SPE4A626PW775.json')
 assert a['recipient']['recipient_uei']==nodes['TP-ORG-DON']['properties']['uei'],'wrong award recipient'
 page=(R/'../selected/dla-award-page2.txt').read_text()
 for token in ['SPE4A6-26-P-W775','745V4','27624','39-8820-501']:assert token in page,'order mismatch'
 assert nodes['TP-AWARD-W775']['properties']['actual_payee'] is None,'unproved payee'
 people=[n for n in graph['nodes'] if n['type']=='person']
 assert len(people)==1 and people[0]['id']=='TP-PERSON-OFFICER-W775','unverified candidate person promoted into award graph'
 person=people[0]
 assert person['source_ids']==['TP-S-ORDER-ROLE'] and person['properties']['public_record'] is True,'officer provenance missing'
 role=(R/'../selected/dla-award-page1-role-selected.txt').read_text()
 for token in ['Joseph Felhauer','CONTRACTING/ORDERING OFFICER','2026 JUL 09','SPE4A6-26-P-W775']:assert token in role,'officer role mismatch'
 for key in ['signature_execution_authenticated','price_selection_authority_verified','payment_authority_verified']:assert person['properties'][key] is False,'printed role promoted to decision authority'
 assert person['properties']['personal_benefit'] is None,'unsupported personal benefit'
 for e in graph['edges']:
  assert e['type'] not in {'paid','paid_to','kickback','beneficial_owner','selected_price'},'unsupported money/person edge'
  if e['type'].startswith('federally_reported'):
   assert e['properties']['beneficial_ownership_verified'] is False,'parent promoted to owner'
   assert e['properties']['ownership_percentage'] is None,'unsupported percentage'
 unknown=load('unresolved.json')
 for k in ['actual_payee','actual_supplier_invoice_party','invoice_unit_cost','gross_margin','kickback_or_personal_benefit','buyer_employee','contract_signatory','price_evaluator']:
  assert unknown[k] is None,'gap silently filled'
 budget=load('research-budget.json')
 assert budget['web_query_count']<=8 and budget['public_read_attempt_count']<=15,'research budget exceeded'
 assert budget['direct_requests']==len(load('acquisition_log.json')['requests']),'request count mismatch'
 return True

def main():
 graph=load('graph.json');validate(graph)
 checks=['8 selected source hashes and graph references','two single-result exact CAGE/UEI joins','award recipient and intended-manufacturer contract tokens','unknown payee/price/benefit and person-role boundaries','public request budget']
 mutations=[]
 for label,mutate in [
  ('printed officer asserted as price selector',lambda g:next(n for n in g['nodes'] if n['id']=='TP-PERSON-OFFICER-W775')['properties'].update(price_selection_authority_verified=True)),
  ('wrong manufacturer UEI',lambda g:next(n for n in g['nodes'] if n['id']=='TP-ORG-SPS')['properties'].update(uei='WRONGUEI0000')),
  ('recipient asserted as payee',lambda g:next(n for n in g['nodes'] if n['id']=='TP-AWARD-W775')['properties'].update(actual_payee='TP-ORG-DON')),
  ('reported parent asserted beneficial owner',lambda g:next(e for e in g['edges'] if e['id']=='TP-E-PARENT-SPS')['properties'].update(beneficial_ownership_verified=True))]:
  bad=copy.deepcopy(graph);mutate(bad)
  try:validate(bad)
  except AssertionError:mutations.append({'mutation':label,'rejected':True})
  else:raise AssertionError('negative control accepted: '+label)
 import runpy
 engine=runpy.run_path(str(ROOT/'engine/integrity.py'))
 engine['validate_graph'](graph,public=True)
 checks.append('repository engine public graph validation')
 for f in load('manifest.json')['files']:assert digest(f['path'])==f['sha256'],'manifest drift: '+f['path']
 checks.append('all local artifact manifest hashes')
 result={'status':'pass','checked_on':'2026-10-30','checks':checks,'negative_controls':mutations,'truth_limit':'Offline checks establish internal source lineage and semantic boundaries, not that official source assertions are complete or that misconduct is present.'}
 (R/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
