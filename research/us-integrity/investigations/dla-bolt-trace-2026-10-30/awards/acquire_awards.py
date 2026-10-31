#!/usr/bin/env python3
"""Finite official public award trace. No payment or price inference.
New output directory required. Seven contract keys come from the committed DLA
history table. Detail snapshots omit location/contact fields; wire hashes and
selected-snapshot hashes have distinct scopes.
"""
import argparse,hashlib,json,urllib.request,urllib.error
from pathlib import Path
from datetime import datetime,timezone
KEYS=['SPE4A626V138W','SPE4A626P5931','SPE4A625V346U','SPE4A625V252D','SPE4A625V208Q','SPE4A625PK654','SPE4A625V4508']
BASE='https://api.usaspending.gov/api/v2/'

def sha(b):return hashlib.sha256(b).hexdigest()
def serialized(d):return (json.dumps(d,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
def acquire(out):
 out.mkdir(exist_ok=False,parents=True); manifest=[]
 def get(name,url,payload=None,selector=None):
  reqbytes=serialized(payload) if payload is not None else None
  if payload is not None:(out/(name+'.request.json')).write_bytes(reqbytes)
  m={'id':name,'url':url,'method':'POST' if payload is not None else 'GET','retrieved_at_utc':datetime.now(timezone.utc).isoformat(),'request_sha256':sha(reqbytes) if reqbytes else None,'request_file':name+'.request.json' if reqbytes else None}
  try:
   req=urllib.request.Request(url,data=reqbytes,headers={'Content-Type':'application/json','User-Agent':'PublicResearch/1.0'})
   with urllib.request.urlopen(req,timeout=20) as r:body=r.read(4_194_305);m.update(http_status=r.status,content_type=r.headers.get('Content-Type'))
   if len(body)>4_194_304:raise ValueError('response exceeds4MiB')
   d=json.loads(body);m.update(wire_bytes=len(body),wire_sha256=sha(body),wire_bytes_archived=selector is None)
   retained=serialized(selector(d)) if selector else body
   path=name+'.json';(out/path).write_bytes(retained);m.update(snapshot=path,snapshot_sha256=sha(retained),snapshot_bytes=len(retained),snapshot_scope='selected_fields_reformatted' if selector else 'original_response_bytes')
   manifest.append(m);(out/'manifest.json').write_bytes(serialized(manifest));return d
  except Exception as e:
   m['error']=type(e).__name__+': '+str(e);manifest.append(m);(out/'manifest.json').write_bytes(serialized(manifest));return None
 fields=['Award ID','generated_internal_id','Recipient Name','Recipient UEI','recipient_id','Awarding Agency','Awarding Agency Code','Awarding Sub Agency','Awarding Sub Agency Code','Start Date','End Date','Award Amount','Description','Place of Performance State Code','PSC']
 p={'filters':{'award_type_codes':['A','B','C','D'],'award_ids':KEYS},'fields':fields,'limit':100,'page':1,'sort':'Award ID','order':'asc','subawards':False}
 results=get('exact-award-search',BASE+'search/spending_by_award/',p)
 p2=dict(p,page=2);terminal=get('exact-award-terminal',BASE+'search/spending_by_award/',p2)
 if results is None:return
 rows=results['results']
 if len(rows)>7 or len({x['Award ID'] for x in rows})!=len(rows) or any(x['Award ID'] not in KEYS for x in rows):raise ValueError('Unexpected award-match population; review required')
 if not terminal or terminal['results']:raise ValueError('Search terminal page not proven')
 def select_detail(d):
  keys=['id','generated_unique_award_id','piid','category','type','type_description','description','date_signed','total_obligation','base_and_all_options_value','base_exercised_options_val','total_outlay','total_outlays','total_subaward_amount','subaward_count','transaction_count','period_of_performance','awarding_agency','funding_agency','latest_transaction_contract_data','parent_award','fpds_id','last_modified_date','certified_date','create_date','update_date']
  x={k:d[k] for k in keys if k in d}
  r=d.get('recipient') or {};x['recipient']={k:r[k] for k in ['recipient_name','recipient_unique_id','recipient_uei','parent_recipient_unique_id','parent_recipient_name','parent_recipient_uei','recipient_id','recipient_hash'] if k in r}
  # Detailed contract data includes company public address; select business/award keys.
  c=d.get('latest_transaction_contract_data') or {}
  wanted=['piid','parent_award_id','modification_number','transaction_number','action_date','federal_action_obligation','total_dollars_obligated','base_and_all_options_value','base_exercised_options_val','current_total_value_of_award','potential_total_value_of_award','period_of_performance_start_date','period_of_performance_current_end_date','period_of_performance_potential_end_date','recipient_name','recipient_uei','recipient_unique_id','cage_code','legal_entity_id','recipient_id','award_description','product_or_service_code','product_or_service_code_description','naics_code','naics_description','number_of_offers_received','extent_competed','extent_competed_description','type_of_contract_pricing','type_of_contract_pricing_description','solicitation_identifier','solicitation_procedures','solicitation_procedures_description','type_set_aside','type_set_aside_description','contracting_officers_determination_of_business_size','contracting_officers_determination_of_business_size_description','cost_or_pricing_data','cost_or_pricing_data_description','other_than_full_and_open_competition','other_than_full_and_open_competition_description','commercial_item_acquisition_procedures','commercial_item_acquisition_procedures_description','multi_year_contract','multi_year_contract_description']
  x['latest_transaction_contract_data']={k:c[k] for k in wanted if k in c}
  return x
 for row in rows:
  get('award-'+row['Award ID'],BASE+'awards/'+str(row['generated_internal_id'])+'/',selector=select_detail)
 (out/'coverage.json').write_bytes(serialized({'requested_keys':KEYS,'returned_keys':[r['Award ID'] for r in rows],'missing_keys':sorted(set(KEYS)-{r['Award ID'] for r in rows}),'terminal_page_empty':True,'scope':'Seven exact PIID search keys; not nationwide/recipient history; award summary and latest contract transaction are not invoices or contract line items.'}))
 print(json.dumps({'output':str(out),'search_matches':len(rows),'requests':len(manifest),'failures':sum('error'in m for m in manifest)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);acquire(p.parse_args().output)
