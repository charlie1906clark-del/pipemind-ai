#!/usr/bin/env python3
"""Finite ordinary public registry reads; retains selected business identifiers only."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode,urljoin
from http.cookiejar import CookieJar
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parent
class FormParser(HTMLParser):
 def __init__(self):super().__init__();self.forms=[];self.f=None;self.links=[];self.a=None;self.data=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ['script','style']:self.skip+=1
  if tag=='form':self.f={'action':d.get('action'),'inputs':[]};self.forms.append(self.f)
  if tag=='input' and self.f is not None:self.f['inputs'].append(d)
  if tag=='a':self.a={'href':d.get('href',''),'text':''};self.links.append(self.a)
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip=max(0,self.skip-1)
  if tag=='form':self.f=None
  if tag=='a':self.a=None
 def handle_data(self,data):
  if self.skip:return
  if data.strip():self.data.append(data.strip())
  if self.a is not None:self.a['text']+=data

def save(name,value):
 p=ROOT/name;p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n');return {'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def main():
 manifest=ROOT/'acquisition_log.json'
 if manifest.exists():raise SystemExit('Refusing to overwrite acquisition')
 op=build_opener(HTTPCookieProcessor(CookieJar()));log=[];captures=[]
 def req(url,data=None,json_body=False):
  if len(log)>=10:raise ValueError('request budget exhausted')
  body=(json.dumps(data).encode() if json_body else urlencode(data).encode()) if data is not None else None
  rec={'url':url,'method':'POST' if body else 'GET','accessed_at':datetime.now(timezone.utc).isoformat(),'raw_archived':False}
  log.append(rec)
  try:
   headers={'User-Agent':'PipeMind-Public-Identity-Research/1.0'}
   if json_body:headers['Content-Type']='application/json'
   with op.open(Request(url,data=body,headers=headers),timeout=20) as z:
    b=z.read(2000001);rec.update(status=z.status,wire_sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
   if len(b)>2000000:raise ValueError('response cap exceeded')
   return b
  except Exception as e:rec['error']=type(e).__name__+': '+str(e);raise
 def page(url,data=None):
  p=FormParser();p.feed(req(url,data).decode());return p
 try:
  url='https://cage.dla.mil/Home/UsageAgree';p=page(url);f=next(x for x in p.forms if x['action']=='/Home/UsageAgree')
  p=page(urljoin(url,f['action']),{x['name']:x.get('value','') for x in f['inputs'] if x.get('name')})
  if not any(x['action']=='/Search' for x in p.forms):p=page('https://cage.dla.mil/Search')
  for cage,name,uei in [('745V4','DON INDUSTRIAL GROUP LLC','XN9HKU6LUM59'),('27624','SPS TECHNOLOGIES LLC','E6KFWWNKEQ49')]:
   f=next(x for x in p.forms if x['action']=='/Search');data={x['name']:x.get('value','') for x in f['inputs'] if x.get('name')};data['SearchString']=cage
   p=page('https://cage.dla.mil/Search',data)
   selected=[x for x in p.data if x in {cage,name,uei}]
   links=[x for x in p.links if '/Search/Details?' in x['href']]
   selected_links=[{'href':x['href'],'text':x['text'].strip()} for x in links]
   captures.append(save('cage-'+cage+'-selected.json',{'source_url':'https://cage.dla.mil/Search','query':cage,'observed_on':'2026-10-30','selected_text':selected,'result_links':selected_links,'scope':'Exact expected business identifier/name fields and result link only; no address, contacts, classifications or form/session values','expected_values_found':all(x in selected for x in [cage,name,uei]),'registration_status_verified':False}))
  profile_ids={'745V4':'516cae19-6195-34c1-0e8f-71a1fd4f3702-C'}
  q=json.loads(req('https://api.usaspending.gov/api/v2/recipient/',{'keyword':'E6KFWWNKEQ49','award_type':'contracts','sort':'name','order':'asc','limit':100,'page':1},True))
  selected={'results':[{k:r.get(k) for k in ['id','name','uei']} for r in q['results']],'page_metadata':q.get('page_metadata')};captures.append(save('sps-recipient-query.json',selected))
  children=[r for r in q['results'] if r.get('uei')=='E6KFWWNKEQ49' and r['id'].endswith('-C')]
  if len(children)==1:profile_ids['27624']=children[0]['id']
  for cage,pid in profile_ids.items():
   d=json.loads(req('https://api.usaspending.gov/api/v2/recipient/'+pid+'/'))
   selected={k:d.get(k) for k in ['name','alternate_names','uei','recipient_id','recipient_level','parent_id','parent_name','parent_uei']}
   selected['location']={k:(d.get('location') or {}).get(k) for k in ['state_code','country_code']}
   captures.append(save('profile-'+cage+'-selected.json',selected))
 except Exception as e:log.append({'terminal_error':type(e).__name__+': '+str(e)})
 finally:save('acquisition_log.json',{'as_of':'2026-10-30','max_requests':10,'requests':log,'captures':captures,'automatic_retries':0,'session_values_archived':False})
 print(json.dumps({'requests':len(log),'captures':captures,'last':log[-1]},indent=2))
if __name__=='__main__':main()
