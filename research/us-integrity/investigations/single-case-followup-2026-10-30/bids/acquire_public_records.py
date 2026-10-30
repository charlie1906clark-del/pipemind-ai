#!/usr/bin/env python3
"""Finite exact-record public reads; full bodies stay outside public Git.

Only the ordinary DIBBS notice is acknowledged. No account, quote, bid, contact,
or agency request is submitted. Redirect counts are not claimed as HTTP totals.
"""
import argparse, hashlib, http.cookiejar, json
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode, urljoin, urlsplit
from urllib.request import build_opener, HTTPCookieProcessor, Request

TARGETS = [
    ('current-rfq', 'https://www.dibbs.bsm.dla.mil/rfq/rfqrec.aspx?sn=spe4a626u3619', 'Exact observed RFQ-record link in indexed source; ordinary notice route'),
    ('SPE4A625V4508', 'https://dibbs2.bsm.dla.mil/Downloads/Awards/04DEC24/SPE4A625V4508.PDF', 'Date-derived candidate using verified award date and previously observed DIBBS archive format; not an attached link'),
    ('SPE4A626V138W', 'https://dibbs2.bsm.dla.mil/Downloads/Awards/26MAY26/SPE4A626V138W.PDF', 'Date-derived candidate using verified award date and previously observed DIBBS archive format; not an attached link'),
]

class Notice(HTMLParser):
    def __init__(self):
        super().__init__(); self.action=None; self.fields={}; self.agree=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='form' and a.get('method','').lower()=='post':self.action=a.get('action')
        if tag=='input' and a.get('name'):
            self.fields[a['name']]=a.get('value','')
            if a['name']=='butAgree' and a.get('value')=='OK':self.agree=True

def acquire(out, receipt, targets=TARGETS):
    out.mkdir(parents=True,exist_ok=False); records=[]
    for ident,url,lineage in targets:
        rec={'id':ident,'source_url':url,'url_lineage':lineage,'observed_at':datetime.now(timezone.utc).isoformat(),'operations':[], 'max_operations':2,'hidden_form_values_retained':False,'original_body_archived_publicly':False}
        opener=build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))
        def read(req,method):
            op={'method':method};rec['operations'].append(op)
            try:
                with opener.open(req,timeout=25) as response:
                    body=response.read(5_000_001)
                    op.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
                if len(body)>5_000_000:raise ValueError('Body exceeds finite cap')
                return body
            except Exception as exc:
                op.update(outcome='failed',error=type(exc).__name__+': '+str(exc));raise
        try:
            body=read(url,'GET')
            if not body.startswith(b'%PDF-'):
                notice=Notice();notice.feed(body.decode('utf-8',errors='replace'))
                if notice.action and notice.agree:
                    # A relative form action belongs to the final response URL,
                    # which may be the ordinary consent redirect, not the RFQ.
                    action=urljoin(rec['operations'][-1]['final_url'],notice.action);parsed=urlsplit(action)
                    if parsed.scheme!='https' or parsed.netloc!=urlsplit(url).netloc or parsed.path.lower()!='/dodwarning.aspx':raise ValueError('Unexpected consent route')
                    notice.fields['butAgree']='OK'
                    body=read(Request(action,data=urlencode(notice.fields).encode()),'POST ordinary public notice consent')
            ext='.pdf' if body.startswith(b'%PDF-') else '.html'
            (out/(ident+ext)).write_bytes(body)
            rec.update(outcome='pdf_acquired' if ext=='.pdf' else 'html_acquired',original_sha256=hashlib.sha256(body).hexdigest(),original_bytes=len(body),scratch_filename=ident+ext)
        except Exception as exc:
            rec.update(outcome='failed_no_retry',error=type(exc).__name__+': '+str(exc))
        records.append(rec)
    receipt.write_text(json.dumps({'records':records,'operation_count':sum(len(r['operations']) for r in records),'counter_scope':'urllib opener operations; redirects may issue additional HTTP requests; no hidden form values retained'},indent=2)+'\n')
    return records

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);p.add_argument('--award-record',action='store_true');a=p.parse_args()
    targets=[('current-award-record','https://www.dibbs.bsm.dla.mil/Awards/AwdRec.aspx?contract=SPE4A626D61WS&dlv=','Observed exact link on acquired original RFQ record')] if a.award_record else TARGETS
    result=acquire(a.output,a.receipt,targets)
    print(json.dumps([{'id':r['id'],'outcome':r['outcome'],'operations':len(r['operations'])} for r in result]))
