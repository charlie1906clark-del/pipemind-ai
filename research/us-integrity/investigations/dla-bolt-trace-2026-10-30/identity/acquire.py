#!/usr/bin/env python3
"""Explicit finite public-identity capture; no automatic inference or merging."""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parent
MAX_BYTES=4*1024*1024

def encoded(d):return (json.dumps(d,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(encoded(d))
def capture(label,url,payload=None,selector=None):
 manifest_path=ROOT/'capture_manifest.json'
 manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else {'as_of':'2026-10-30','read_budget':25,'automatic_retries':0,'requests':[],'scope':'Five exact CAGE identifiers in the seven historical rows of DLA RFQ SPE4A626U3619; no national census.'}
 if len(manifest['requests'])>=25:raise ValueError('read budget exhausted')
 if any(r['id']==label for r in manifest['requests']):raise ValueError('label already acquired; do not overwrite')
 body=encoded(payload) if payload is not None else None
 rec={'id':label,'url':url,'method':'POST' if body else 'GET','accessed_at':datetime.now(timezone.utc).isoformat(),'timeout_seconds':20,'original_wire_bytes_archived':False}
 if body:
  rp=ROOT/'requests'/(label+'.json');rp.parent.mkdir(exist_ok=True);rp.write_bytes(body)
  rec.update(request_path=str(rp.relative_to(ROOT)),request_sha256=sha(body))
 try:
  with urlopen(Request(url,data=body,headers={'Content-Type':'application/json','User-Agent':'PipeMind-Public-Identity-Research/1.0'}),timeout=20) as resp:
   raw=resp.read(MAX_BYTES+1);rec.update(http_status=resp.status,response_date=resp.headers.get('Date'))
  if len(raw)>MAX_BYTES:raise ValueError('oversized response')
  rec.update(wire_response_sha256=sha(raw),wire_bytes=len(raw))
  data=json.loads(raw) if 'api.usaspending.gov' in url else raw.decode('utf-8')
  selected=selector(data) if selector else data
  dest=ROOT/'snapshots'/(label+'.json');write(dest,selected)
  rec.update(snapshot_path=str(dest.relative_to(ROOT)),snapshot_sha256=sha(dest.read_bytes()),selection='selected/reformatted JSON; wire hash is not snapshot hash')
  return_value=selected
 except Exception as e:
  rec['error']=type(e).__name__+': '+str(e);return_value=None
 manifest['requests'].append(rec);write(manifest_path,manifest)
 return return_value

def select_profile(d):
 keys=['name','alternate_names','duns','uei','recipient_id','recipient_level','parent_id','parent_name','parent_duns','parent_uei']
 r={k:d.get(k) for k in keys}
 r['business_structure_types']=[x for x in d.get('business_types',[]) if x in {'corporate_entity_not_tax_exempt','sole_proprietorship','partnership','subchapter_s_corporation'}]
 r['location']={k:(d.get('location') or {}).get(k) for k in ['state_code','country_code']}
 return r

if __name__=='__main__':
 queries={'6ZF42':'GWEEKJ2PNL45','0NFB8':'JEJSN59MQVK3','7W108':'SUBURBAN BOLT','8A1E8':'KJGWN783BNB5','51Y73':'US4BABY42KV8'}
 for cage,keyword in queries.items():
  for page in [1,2]:
   d=capture(cage+'-recipient-page-'+str(page),'https://api.usaspending.gov/api/v2/recipient/',{'keyword':keyword,'award_type':'contracts','sort':'name','order':'asc','limit':1000,'page':page})
   print(cage,page,json.dumps(d)[:2500])
