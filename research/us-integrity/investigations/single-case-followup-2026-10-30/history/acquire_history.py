#!/usr/bin/env python3
"""Read two exact historical DLA instruments; full PDFs stay outside Git.

Routes are derived from the published award identifiers/dates and a previously
observed official DIBBS path pattern. A failed route is not proof of absence.
Only the ordinary public DoD notice can be acknowledged; no account is used.
"""
import argparse
import hashlib
import http.cookiejar
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlencode, urlunsplit
from urllib.request import build_opener, HTTPCookieProcessor, Request

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location('prior_dla_notice', ROOT/'investigations/federal-price-pilot-2026-10-30/acquire_dla_document.py')
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
SEEDS = [('SPE4A626P5931','14NOV25','2025-11-14'),('SPE4A625PK654','24MAR25','2025-03-24')]

def safe_url(url):
    p=urlsplit(url)
    return urlunsplit((p.scheme,p.netloc,p.path,'',''))

def acquire(seed, raw_dir):
    piid, folder, date=seed
    url=f'https://dibbs2.bsm.dla.mil/Downloads/Awards/{folder}/{piid}.PDF'
    rec={'piid':piid,'award_date_from_existing_official_capture':date,'source_url':url,
         'url_lineage':'Derived from exact published PIID/date and prior observed official path pattern; not a clicked award hyperlink',
         'observed_at':datetime.now(timezone.utc).isoformat(),'operations':[],
         'full_pdf_archived_publicly':False,'hidden_notice_values_retained':False}
    opener=build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))
    def fetch(req,method):
        op={'method':method,'started_at':datetime.now(timezone.utc).isoformat()}
        rec['operations'].append(op)
        try:
            with opener.open(req,timeout=20) as response:
                op.update(status=response.status,final_url_without_query=safe_url(response.url),content_type=response.headers.get('Content-Type'))
                body=response.read(5_000_001)
                final=response.url
            if len(body)>5_000_000:raise ValueError('Five-megabyte response limit exceeded')
            op.update(received_bytes=len(body),finished_at=datetime.now(timezone.utc).isoformat())
            return body,final
        except Exception as exc:
            op.update(error_type=type(exc).__name__,finished_at=datetime.now(timezone.utc).isoformat())
            raise
    try:
        body,final=fetch(url,'GET')
        if not body.startswith(b'%PDF-'):
            notice=MOD.Notice();notice.feed(body.decode('utf-8'))
            if not notice.action or not notice.agree:raise ValueError('No ordinary public notice form; stop')
            action=urljoin(final,notice.action);p=urlsplit(action)
            if p.scheme!='https' or p.hostname!='dibbs2.bsm.dla.mil' or p.path.lower()!='/dodwarning.aspx':raise ValueError('Unrecognized notice destination; stop')
            notice.fields['butAgree']='OK'
            body,final=fetch(Request(action,data=urlencode(notice.fields).encode()),'POST ordinary public notice consent')
        if not body.startswith(b'%PDF-'):raise ValueError('No PDF returned')
        with (raw_dir/(piid+'.pdf')).open('xb') as output:
            output.write(body)
        rec.update(result='pdf_acquired',original_sha256=hashlib.sha256(body).hexdigest(),original_bytes=len(body))
    except Exception as exc:
        rec.update(result='failed_no_retry',error_type=type(exc).__name__,error_message=str(exc)[:200])
    return rec

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--raw-dir',type=Path,required=True);p.add_argument('--manifest',type=Path,required=True);args=p.parse_args()
    if args.manifest.exists():raise ValueError('Retain existing run; use a new manifest for another attempt')
    args.raw_dir=args.raw_dir.resolve()
    if args.raw_dir.is_relative_to(ROOT.parents[1]):
        raise ValueError('Complete source PDFs must remain outside this repository')
    if args.raw_dir.exists():
        raise ValueError('Use a fresh raw-source directory; prior source files are immutable')
    args.raw_dir.mkdir(parents=True,exist_ok=False)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as pool:
        records=list(pool.map(lambda seed:acquire(seed,args.raw_dir),SEEDS))
    args.manifest.parent.mkdir(parents=True,exist_ok=True)
    args.manifest.write_text(json.dumps({'schema_version':'1.0','scope':'Two exact historical original award routes','max_opener_operations':4,'redirect_http_hops_not_separately_counted':True,'notice_parser_source_sha256':hashlib.sha256(Path(SPEC.origin).read_bytes()).hexdigest(),'records':records},indent=2)+'\n')
    print(json.dumps([{'piid':r['piid'],'result':r['result'],'operations':len(r['operations']),'bytes':r.get('original_bytes'),'error':r.get('error_type')} for r in records]))

if __name__=='__main__':main()
