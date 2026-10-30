#!/usr/bin/env python3
"""Two explicit read-only official API rechecks; no generalized crawler."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from datetime import datetime, timezone
from decimal import Decimal
import hashlib,json,argparse
HERE=Path(__file__).resolve().parent
PILOT=HERE.parents[1]/'investigations/federal-price-pilot-2026-10-30'
KEYS=('CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-','CONT_AWD_75N98026F00268_7529_36F79720D0041_3600')
def normalized(d):
 return {'generated_unique_award_id':d.get('generated_unique_award_id'),'piid':d.get('piid'),'date_signed':d.get('date_signed'),'total_obligation_usd':str(d.get('total_obligation')),'recipient_uei':(d.get('recipient')or{}).get('recipient_uei'),'awarding_toptier_code':d.get('awarding_agency',{}).get('toptier_agency',{}).get('code'),'awarding_subtier_code':d.get('awarding_agency',{}).get('subtier_agency',{}).get('code'),'psc':(d.get('latest_transaction_contract_data')or{}).get('product_or_service_code'),'solicitation_identifier':(d.get('latest_transaction_contract_data')or{}).get('solicitation_identifier'),'parent_piid':(d.get('parent_award')or{}).get('piid')}
def write(path,value):path.write_text(json.dumps(value,indent=2)+'\n')
def run(out):
 out.mkdir(parents=True,exist_ok=False);manifest=[]
 for key in KEYS:
  url='https://api.usaspending.gov/api/v2/awards/'+key+'/'
  row={'url':url,'method':'GET','observed_at':datetime.now(timezone.utc).isoformat(),'success':False,'original_response_archived':False,'request_scope':'Independent exact-key public award check; no search or population-completeness claim'}
  try:
   with urlopen(Request(url,headers={'Accept':'application/json','User-Agent':'PipeMind-IndependentReview/1.0'}),timeout=20) as response:
    raw=response.read(1048577);row.update(http_status=response.status,final_url=response.url)
   if len(raw)>1048576:raise ValueError('Response cap exceeded')
   data=json.loads(raw,parse_float=Decimal);selected=normalized(data)
   assert selected['generated_unique_award_id']==key
   piid=selected['piid'];expected=normalized(json.loads((PILOT/'detail-capture'/('detail-'+piid+'.json')).read_text(),parse_float=Decimal))
   assert Decimal(selected['total_obligation_usd']).is_finite()
   matches={field:selected[field]==expected[field] for field in selected}
   filename='spotcheck-'+piid+'.json';write(out/filename,selected)
   row.update(success=True,wire_sha256=hashlib.sha256(raw).hexdigest(),wire_bytes=len(raw),selected_file=filename,selected_sha256=hashlib.sha256((out/filename).read_bytes()).hexdigest(),hash_scope='selected normalized independent JSON; raw bytes hashed but not retained',field_matches=matches,all_selected_fields_match=all(matches.values()),amount_basis='Cumulative reported obligation, not unit price, monthly spend, invoice or paid cash')
  except HTTPError as e:row.update(http_status=e.code,error=str(e))
  except Exception as e:row.update(error=type(e).__name__+': '+str(e))
  manifest.append(row);write(out/'manifest.json',manifest)
 print(json.dumps({'requests':len(manifest),'successful_rechecks':sum(x['success'] for x in manifest),'all_successful_matches':all(x.get('all_selected_fields_match') for x in manifest)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--acquire',action='store_true');p.add_argument('--output',type=Path,default=HERE/'official-rechecks');a=p.parse_args()
 if not a.acquire:p.error('Use --acquire for exactly two ordinary public GET requests')
 run(a.output)
