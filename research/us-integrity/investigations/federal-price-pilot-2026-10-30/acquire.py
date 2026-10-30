#!/usr/bin/env python3
"""Explicit bounded public samples, not a nationwide census or fraud ranking."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from decimal import Decimal
import argparse,hashlib,json,re
BASE='https://api.usaspending.gov/api/v2/'
START='2026-07-03';END='2026-07-31';LIMIT=10
STRATA={
 'dla-bolts':{'psc':'5306','agency':{'type':'awarding','tier':'subtier','name':'Defense Logistics Agency','toptier_name':'Department of Defense'}},
 'va-medical':{'psc':'6515','agency':{'type':'awarding','tier':'toptier','name':'Department of Veterans Affairs'}},
 'hhs-medical':{'psc':'6515','agency':{'type':'awarding','tier':'toptier','name':'Department of Health and Human Services'}}}
FIELDS=['Award ID','generated_internal_id','Recipient Name','Recipient UEI','recipient_id','Awarding Agency','Awarding Agency Code','Awarding Sub Agency','Awarding Sub Agency Code','Funding Agency','Funding Sub Agency','Start Date','Base Obligation Date','End Date','Award Amount','Total Outlays','Description','Place of Performance State Code','PSC','NAICS','Contract Award Type','Last Modified Date']
def encoded(x):return (json.dumps(x,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def build_request(name):
 s=STRATA[name]
 return {'filters':{'award_type_codes':['A','B','C','D'],'time_period':[{'start_date':START,'end_date':END,'date_type':'new_awards_only'}],'psc_codes':[s['psc']],'agencies':[s['agency']]},'fields':FIELDS,'limit':LIMIT,'page':1,'sort':'Award Amount','order':'desc','subawards':False}
def select_search(d):
 return {'results':[{k:v for k,v in r.items() if k in FIELDS or k in ['internal_id','awarding_agency_id','agency_slug','funding_agency_id']} for r in d['results']],'page_metadata':d['page_metadata'],'messages':d.get('messages',[]),'limit':d.get('limit')}
def validate_search(d,name):
 if not isinstance(d,dict) or not isinstance(d.get('results'),list) or len(d['results'])>LIMIT:raise ValueError('Invalid bounded results')
 m=d.get('page_metadata',{})
 if m.get('page')!=1 or type(m.get('hasNext'))is not bool:raise ValueError('Missing pagination')
 seen=set()
 for r in d['results']:
  k=r.get('generated_internal_id')
  if not isinstance(k,str) or not k or k in seen:raise ValueError('Missing/duplicate exact award ID')
  seen.add(k);psc=r.get('PSC');psc=psc.get('code') if isinstance(psc,dict) else str(psc or '').split(':')[0].strip()
  if psc!=STRATA[name]['psc']:raise ValueError('PSC mismatch')
  field='Awarding Agency' if STRATA[name]['agency']['tier']=='toptier' else 'Awarding Sub Agency'
  if r.get(field)!=STRATA[name]['agency']['name']:raise ValueError('Agency mismatch')
  amount=Decimal(str(r['Award Amount']))
  if not amount.is_finite():raise ValueError('Nonfinite award amount')
  base=r.get('Base Obligation Date')
  if not isinstance(base,str) or not START<=base<=END:raise ValueError('Base obligation date outside declared window')
  datetime.fromisoformat(base)
 return d
class Capture:
 def __init__(self,out,max_requests=12):self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.manifest=[];self.max=max_requests
 def get(self,name,url,payload=None,selector=lambda x:x):
  if len(self.manifest)>=self.max:raise ValueError('Request budget exhausted')
  if any(r['id']==name for r in self.manifest):raise ValueError('Duplicate capture ID')
  rb=encoded(payload) if payload is not None else None
  m={'id':name,'url':url,'method':'POST' if rb else 'GET','observed_at':datetime.now(timezone.utc).isoformat(),'timeout_seconds':20,'max_response_bytes':4194304,'success':False,'wire_bytes_archived':False}
  if rb:(self.out/(name+'.request.json')).write_bytes(rb);m.update(request_path=name+'.request.json',request_sha256=sha(rb))
  d=None
  try:
   req=Request(url,data=rb,headers={'Content-Type':'application/json','Accept':'application/json','User-Agent':'PipeMind-PublicPriceResearch/1.0'})
   with urlopen(req,timeout=20) as response:
    body=response.read(4194305);m.update(http_status=response.status,final_url=response.url,response_date_header=response.headers.get('Date'))
   if len(body)>4194304:raise ValueError('Response size cap exceeded; no full response saved')
   m.update(wire_sha256=sha(body),wire_bytes=len(body));d=json.loads(body);selected=encoded(selector(d));(self.out/(name+'.json')).write_bytes(selected);m.update(snapshot_path=name+'.json',snapshot_sha256=sha(selected),snapshot_bytes=len(selected),snapshot_scope='selected public business-award fields, reformatted; not original response bytes',success=True)
  except HTTPError as e:m.update(http_status=e.code,error_type='HTTPError',error=str(e))
  except Exception as e:m.update(error_type=type(e).__name__,error=str(e)[:300])
  self.manifest.append(m);(self.out/'manifest.json').write_bytes(encoded(self.manifest));return d
DETAIL_TOP=['id','generated_unique_award_id','piid','category','type','type_description','description','date_signed','total_obligation','base_and_all_options_value','base_exercised_options_val','total_outlay','total_outlays','transaction_count','period_of_performance','awarding_agency','funding_agency','parent_award','last_modified_date','certified_date','create_date','update_date']
DETAIL_RECIPIENT=['recipient_name','recipient_unique_id','recipient_uei','parent_recipient_unique_id','parent_recipient_name','parent_recipient_uei','recipient_id','recipient_hash']
DETAIL_TRANSACTION=['piid','parent_award_id','modification_number','transaction_number','action_date','federal_action_obligation','total_dollars_obligated','base_and_all_options_value','base_exercised_options_val','current_total_value_of_award','potential_total_value_of_award','period_of_performance_start_date','period_of_performance_current_end_date','period_of_performance_potential_end_date','recipient_name','recipient_uei','cage_code','award_description','product_or_service_code','product_or_service_code_description','naics_code','naics_description','number_of_offers_received','extent_competed','extent_competed_description','type_of_contract_pricing','type_of_contract_pricing_description','solicitation_identifier','solicitation_procedures','solicitation_procedures_description','type_set_aside','type_set_aside_description','cost_or_pricing_data','cost_or_pricing_data_description','awarding_office_code','awarding_office_name','funding_office_code','funding_office_name']
def select_detail(d):
 x={k:d[k] for k in DETAIL_TOP if k in d};x['recipient']={k:v for k,v in(d.get('recipient')or{}).items() if k in DETAIL_RECIPIENT};x['latest_transaction_contract_data']={k:v for k,v in(d.get('latest_transaction_contract_data')or{}).items() if k in DETAIL_TRANSACTION};return x
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--details',type=Path);args=p.parse_args();c=Capture(args.output)
 if args.details:
  for item in json.loads(args.details.read_text()):c.get('detail-'+item['piid'],BASE+'awards/'+item['generated_award_id']+'/',selector=select_detail)
 else:
  for name in STRATA:
   d=c.get(name,BASE+'search/spending_by_award/',build_request(name),select_search)
   if d is not None:validate_search(d,name)
 print(json.dumps({'output':args.output,'requests':len(c.manifest),'successes':sum(x['success']for x in c.manifest)}))
