#!/usr/bin/env python3
"""Offline synthetic demonstration; never a public acquisition or government case."""
import argparse
import json
from pathlib import Path
from trace_links import trace, Response

HERE=Path(__file__).resolve().parent

def build():
    plan={'schema_version':'1.0','case_id':'SYNTHETIC-TRACE-001','allowed_hosts':['example.org'],
          'seeds':[{'url':'https://example.org/awards/SYNTH-ORDER-001.html','kind':'order','identifiers':['SYNTH-ORDER-001','SYNTH-ITEM-001']}],
          'limits':{'max_requests':6,'max_pages':3,'max_depth':2,'max_retries':0}}
    pages={
        'https://example.org/robots.txt':('text/plain',b'User-agent: *\nAllow: /'),
        'https://example.org/awards/SYNTH-ORDER-001.html':('text/html',b'<a href="SYNTH-ORDER-001.pdf">Order attachment</a><a href="SYNTH-ITEM-001.pdf">Item specification</a><a href="SYNTH-ORDER-001.pdf#copy">Duplicate order</a><a href="/home">Home</a><a href="/contact">Contact</a><a href="https://unapproved.example.org/run">Unapproved site</a>'),
        'https://example.org/awards/SYNTH-ORDER-001.pdf':('application/pdf',b'SYNTHETIC PLACEHOLDER. Not a valid PDF or transaction.'),
        'https://example.org/awards/SYNTH-ITEM-001.pdf':('application/pdf',b'SYNTHETIC PLACEHOLDER. No actual item specification.')}
    calls=[]
    def offline(url,ip,timeout,cap):
        calls.append(url);mime,body=pages[url];return Response(200,{'content-type':mime},body,True)
    result=trace(plan,resolver=lambda h,t:['93.184.215.14'],transport=offline)
    result.update(data_origin='synthetic_calibration',synthetic=True,network_used=False,government_transaction=False,
                  synthetic_notice='URLs, transport, resolver answers and body content are fabricated test inputs; no external request made. Fixture MIME does not authenticate a PDF.',coverage_counter_scope='Simulated transport calls only; zero actual DNS/HTTP calls',scope='Offline control for link scheduling, duplicate rejection and URL policy. Not procurement evidence.')
    result['logical_fixture_calls']=calls
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();target=args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('x') as f:json.dump(build(),f,indent=2);f.write('\n')
    print(target)
