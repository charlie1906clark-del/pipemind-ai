"""Inspect public CAGE forms through their normal notice/consent flow.
Does not solve CAPTCHA, log in, query private endpoints or retain session tokens.
"""
from urllib.request import Request,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode,urljoin
from http.cookiejar import CookieJar
from html.parser import HTMLParser
import json,hashlib
from pathlib import Path
if Path(__file__).with_name('cage_access_log.json').exists():raise SystemExit('Refusing to overwrite dated capture; use a new dated directory')
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.forms=[];self.current=None
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='form':self.current={'action':d.get('action'),'method':d.get('method'),'inputs':[]};self.forms.append(self.current)
  if tag=='input' and self.current is not None:self.current['inputs'].append(d)
 def handle_endtag(self,tag):
  if tag=='form':self.current=None
op=build_opener(HTTPCookieProcessor(CookieJar()));log=[]
def get(url,body=None):
 with op.open(Request(url,data=urlencode(body).encode() if body is not None else None,headers={'User-Agent':'PipeMind-Public-Identity-Research/1.0'}),timeout=20) as r:
  data=r.read(1000000);log.append({'url':url,'method':'POST' if body is not None else 'GET','status':r.status,'final_url':r.url,'wire_sha256':hashlib.sha256(data).hexdigest(),'raw_archived':False,'note':'Session-only response; no cookies, form tokens, or personal contact fields retained.'});return r.url,data.decode()
try:
 u,t=get('https://cage.dla.mil/Home/UsageAgree');p=Parser();p.feed(t);f=next(f for f in p.forms if f['action']=='/Home/UsageAgree')
 d={x['name']:x.get('value','') for x in f['inputs'] if x.get('name')};u,t=get(urljoin(u,f['action']),d)
 if '/Search' not in u:u,t=get('https://cage.dla.mil/Search')
 p=Parser();p.feed(t)
 clean=[{'action':f['action'],'method':f['method'],'inputs':[{'name':x.get('name'),'type':x.get('type'),'value':None if x.get('type')=='hidden' else x.get('value')} for x in f['inputs']]} for f in p.forms]
 print(json.dumps({'url':u,'forms':clean,'captcha_present':'captcha' in t.lower(),'title_start':t[:100]},indent=2))
except Exception as e:log.append({'error':type(e).__name__+': '+str(e)});print(str(e))
finally:
 Path(__file__).with_name('cage_access_log.json').write_text(json.dumps({'as_of':'2026-10-30','earlier_attempts':[{'url':'https://cage.dla.mil','method':'web_open','result':'public usage agreement','source_ref':'turn201view0'},{'url':'https://cage.dla.mil/Home/UsageAgree','method':'GET','result':'HTTP200 public consent form; session not retained'}],'requests':log},indent=2)+'\n')
