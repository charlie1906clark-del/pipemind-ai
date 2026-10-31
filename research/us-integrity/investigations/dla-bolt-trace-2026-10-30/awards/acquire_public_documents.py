#!/usr/bin/env python3
"""Try only the seven dated public DLA award URLs derived from known history keys.
A missing derived URL is not proof that no public document exists elsewhere.
The ordinary DoD notice is submitted once; no account or bypass is attempted.
"""
import argparse,hashlib,json,urllib.request,urllib.parse,urllib.error,http.cookiejar
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
class Notice(HTMLParser):
 def __init__(self):super().__init__();self.action=None;self.fields={};self.agree=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='form' and a.get('method','').lower()=='post':self.action=a.get('action')
  if tag=='input' and a.get('name'):
   self.fields[a['name']]=a.get('value','')
   if a['name']=='butAgree' and a.get('value')=='OK':self.agree=True

def one(row,out):
 k=row['contract_number'];day=datetime.fromisoformat(row['award_date']).strftime('%d%b%y').upper()
 url=f'https://dibbs2.bsm.dla.mil/Downloads/Awards/{day}/{k}.PDF'
 m={'contract':k,'source_url':url,'url_derivation':'Known award date formatted DDMMMYY and exact PIID, using observed public DIBBS award-document route; unconfirmed posting-date component','retrieved_at_utc':datetime.now(timezone.utc).isoformat(),'requests':[],'hidden_form_values_retained':False}
 op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
 try:
  with op.open(url,timeout=20) as r:b=r.read(5_000_001);m['requests'].append({'method':'GET','status':r.status,'content_type':r.headers.get('Content-Type'),'final_url':r.url})
  if not b.startswith(b'%PDF-'):
   p=Notice();p.feed(b.decode('utf-8'))
   if not p.action or not p.agree:raise ValueError('Expected public notice absent; stop')
   action=urllib.parse.urljoin(url,p.action);u=urllib.parse.urlsplit(action)
   if u.scheme!='https' or u.netloc!='dibbs2.bsm.dla.mil' or u.path.lower()!='/dodwarning.aspx':raise ValueError('Unexpected consent action; stop')
   p.fields['butAgree']='OK'
   with op.open(urllib.request.Request(action,data=urllib.parse.urlencode(p.fields).encode()),timeout=20) as r:b=r.read(5_000_001);m['requests'].append({'method':'POST public notice consent','status':r.status,'content_type':r.headers.get('Content-Type'),'final_url':r.url})
  if len(b)>5_000_000:raise ValueError('Response size cap exceeded')
  if not b.startswith(b'%PDF-'):raise ValueError('Document response was not PDF; no further attempt')
  f=k+'.pdf';(out/f).write_bytes(b);m.update(snapshot=f,snapshot_sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),result='pdf_acquired')
 except urllib.error.HTTPError as e:m.update(result='unavailable_at_derived_url',http_status=e.code,error=str(e))
 except Exception as e:m.update(result='retrieval_failed',error=type(e).__name__+': '+str(e))
 return m

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=False)
 source=Path(__file__).resolve().parents[2]/'discovery-policy-2026-10-30/pricing/snapshots/selected_evidence.json'
 rows=json.loads(source.read_text())['observations']
 with ThreadPoolExecutor(max_workers=3) as pool:ms=list(pool.map(lambda r:one(r,a.output),rows))
 (a.output/'manifest.json').write_text(json.dumps(ms,indent=2)+'\n')
 print(json.dumps([{'contract':m['contract'],'result':m['result'],'status':m.get('http_status'),'steps':len(m['requests'])} for m in ms]))
if __name__=='__main__':main()
