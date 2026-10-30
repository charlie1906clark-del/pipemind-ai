"""Four exact CAGE lookups through the site's ordinary public form.
Never retains session cookies, hidden form tokens or source addresses.
"""
from urllib.request import Request,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode,urljoin
from http.cookiejar import CookieJar
from html.parser import HTMLParser
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parent
if (ROOT/'cage_batch_lookup_log.json').exists():raise SystemExit('Refusing to overwrite dated capture; use a new dated directory')
class Parser(HTMLParser):
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
op=build_opener(HTTPCookieProcessor(CookieJar()));log=[]
def req(url,body=None):
 with op.open(Request(url,data=urlencode(body).encode() if body is not None else None,headers={'User-Agent':'PipeMind-Public-Identity-Research/1.0'}),timeout=20) as r:
  b=r.read(1000000);log.append({'url':url,'method':'POST' if body is not None else 'GET','status':r.status,'wire_sha256':hashlib.sha256(b).hexdigest(),'raw_archived':False});p=Parser();p.feed(b.decode());return r.url,p
try:
 u,p=req('https://cage.dla.mil/Home/UsageAgree');f=next(f for f in p.forms if f['action']=='/Home/UsageAgree');u,p=req(urljoin(u,f['action']),{x['name']:x.get('value','') for x in f['inputs'] if x.get('name')})
 if not any(f['action']=='/Search' for f in p.forms):u,p=req('https://cage.dla.mil/Search')
 for cage in ['0NFB8','7W108','8A1E8','51Y73']:
  f=next(f for f in p.forms if f['action']=='/Search');data={x['name']:x.get('value','') for x in f['inputs'] if x.get('name')};data['SearchString']=cage;u,p=req(urljoin(u,f['action']),data)
  links=[l for l in p.links if '/Search/Details?' in l['href']]
  needles=[cage,'BUTT','FAREED','GWEEKJ2PNL45','DIALOGIC','JEJSN59MQVK3','SUBURBAN','JE5NG1MWNU77','CARLISLE','KJGWN783BNB5','CASCADE','US4BABY42KV8','PRECISION','Status','Updated','CAGE','UEI','Legal']
  selected=[x for x in p.data if any(n in x for n in needles) and len(x)<250]
  result={'source_url':u,'query':cage,'selected_text':selected,'result_links':links,'selection':'Only identifier/name/status labels and result links; no addresses or contacts; raw content not archived.'}
  (ROOT/('snapshots/cage-'+cage+'-selected.json')).write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps(result,indent=2),flush=True)
except Exception as e:log.append({'error':type(e).__name__+': '+str(e)});print(str(e))
finally:(ROOT/'cage_batch_lookup_log.json').write_text(json.dumps({'as_of':'2026-10-30','requests':log},indent=2)+'\n')
