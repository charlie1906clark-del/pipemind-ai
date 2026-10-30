#!/usr/bin/env python3
"""Replay retained public pilot evidence into the durable queue. No remote calls.

Independent review receipts are supplied separately; this script never invents
or accepts its own review. The database is operational state, not a Git artifact.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parents[1]
spec = importlib.util.spec_from_file_location('run_price_runtime', ROOT/'price-agents/runtime/agent_runtime.py')
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)
PILOT = ROOT/'investigations/federal-price-pilot-2026-10-30'
OWNER = 'codex-evidence-coordinator'


def load(path):
    return json.loads(path.read_text())


def write_once(path, obj):
    body = json.dumps(obj, indent=2, ensure_ascii=False) + '\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_text() != body:
            raise ValueError('Refusing to replace different retained run artifact: '+str(path))
    else:
        path.write_text(body)


def evidence(db, task, token, ordinal, path, url, observed, locator, scope, event=None):
    ident = task+'-E'+str(ordinal)
    capture = {'artifact_path':str(path.relative_to(REPO)),
               'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
               'observed_at':observed,'hash_scope':'selected_extract',
               'provenance_note':'Local replay of previously acquired selected public evidence; original retrieval remains in the pilot manifest. No new download.'}
    request = {'attempt_id':ident+'-REUSE','task_id':task,'url':url,
               'method':'LOCAL_CAPTURE_REUSE','purpose':'Verify retained bytes and reuse them under this task',
               'new_network_requests':0,'original_capture':capture}
    runtime.start_attempt(db,task,OWNER,token,request,repository=REPO)
    runtime.finish_attempt(db,task,OWNER,token,{'attempt_id':request['attempt_id'],
        'outcome':'success','detail':'Retained selected bytes revalidated locally; no network request',
        'new_network_requests':0})
    record = {'id':ident,'task_id':task,'attempt_id':request['attempt_id'],
              'source_url':url,'source_kind':'selected_public_record','locator':locator,
              'claim_scope':scope,'visibility':'public','synthetic':False,'event_date':event,
              **{k:v for k,v in capture.items() if k!='provenance_note'}}
    runtime.append_evidence(db,task,OWNER,token,record,REPO)
    return ident


def result(task, plan, evidence_ids, statements, unknowns, next_record):
    return {'schema_version':'1.0','result_id':task+'-RESULT-01','task_id':task,
            'producer':OWNER,'input_commit':plan['base_commit'],'data_origin':'public',
            'outcome':'observations','evidence_ids':evidence_ids,
            'facts':[{'id':task+'-FACT-'+str(i+1),'statement':s,'evidence_ids':evidence_ids}
                     for i,s in enumerate(statements)],
            'candidate_signals':[],
            'pricing_eligibility':{'status':'unqualified','reason':'No independently qualified equivalent benchmark or complete paid-value evidence','evidence_ids':evidence_ids},
            'benefit_evidence':{'status':'unresolved','reason':'These source selections do not establish buyer influence or a personal benefit','evidence_ids':[]},
            'unknowns':unknowns,
            'ordinary_alternatives':['Award summaries and source availability do not indicate misconduct; supply terms and separately priced services can explain differences.'],
            'conclusion':'Narrow public observations only. A completed and accepted packet does not establish price fairness, buyer independence, loss or fraud.',
            'next_record':next_record,
            'supplemental_input_scope':'New source selections acquired after the plan base commit, identified by evidence hashes; not represented as existing at that baseline.'}


def prepare_cohorts(db,plan,out):
    manifest = load(PILOT/'capture/manifest.json')
    mapping = {'dla-bolts':'DLA','va-medical':'VA','hhs-medical':'HHS'}
    for item in manifest:
        task='PA-W1-COHORT-'+mapping[item['id']]
        current=runtime.task_row(db,task)
        if current['status'] in {'accepted','awaiting_review'}:
            continue
        claim=runtime.claim(db,task,OWNER)
        path=PILOT/'capture'/item['snapshot_path']
        data=load(path)
        if len(data['results'])!=10 or data['page_metadata']['hasNext'] is not True:
            raise ValueError('Pilot scope changed; independently review before replay')
        ev=evidence(db,task,claim['lease_token'],1,path,item['url'],item['observed_at'],
            'results and page_metadata','Ten selected award summaries; first page has further results')
        packet=result(task,plan,[ev],[
            'The declared July3–31,2026 new-awards query retained ten unique award summaries for this stratum.',
            'The response reports hasNext:true; this is an incomplete first-page sample sorted by cumulative award amount, not a random or nationwide cohort.',
            'Cumulative obligations are not unit prices, period spending or paid cash.'
        ],['Original priced lines are not established by these summary rows.','Full population coverage and payment are not established.'],
        'Original priced line and applicable procurement terms for the selected exact award.')
        runtime.submit_result(db,task,OWNER,claim['lease_token'],packet,REPO)
        write_once(out/(task+'.json'),packet)


def prepare_line(db,plan,out):
    task='PA-W1-LINE-DLA'
    if runtime.task_row(db,task)['status'] in {'accepted','awaiting_review'}:
        return
    claim=runtime.claim(db,task,OWNER)
    manifest=load(PILOT/'selected_manifest.json');attempt=load(PILOT/'dla-document-attempt.json')
    ids=[]
    for i,file in enumerate(['dla-award-page2.txt','dla-award-page4.txt','dla-award-page5-selected.txt'],1):
        ids.append(evidence(db,task,claim['lease_token'],i,PILOT/'selected'/file,
            manifest['source_url'],attempt['retrieved_at_utc'],file,
            'Selected text from original award SPE4A626PW775; original PDF is not publicly archived', '2026-07-09'))
    packet=result(task,plan,ids,[
        'Order SPE4A626PW775 prices NSN5306004457358, part39-8820-501, at USD272.99 per EA for2243EA: USD612316.57.',
        'A separate government first-article-test line is USD3500.00. The two lines sum to USD615816.57; they are different priced deliverables.',
        'The contract names dealer Don Industrial Group LLC, CAGE745V4, and intended approved manufacturer SPS Technologies LLC, CAGE27624. This is not verification of actual delivery, invoices or payment.'
    ],['No independent equivalent market price has been qualified.','Actual receipt, payment, bid prices and buyer-benefit evidence remain unverified.'],
    'Dated exact-part compliant offer and actual bid/price-reasonableness records for SPE4A626Q0688.')
    runtime.submit_result(db,task,OWNER,claim['lease_token'],packet,REPO)
    write_once(out/(task+'.json'),packet)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--db',type=Path,required=True)
    p.add_argument('--phase',choices=['cohorts','line','review','block-known-gaps','export'],required=True)
    p.add_argument('--out',type=Path,default=HERE/'current-run')
    p.add_argument('--review-receipts',type=Path)
    args=p.parse_args()
    args.db.parent.mkdir(parents=True,exist_ok=True)
    db=runtime.connect(args.db)
    plan=load(ROOT/'price-agents/plans/current-wave.json')
    runtime.import_plan(db,plan)
    try:
        if args.phase=='cohorts':prepare_cohorts(db,plan,args.out/'results')
        elif args.phase=='line':prepare_line(db,plan,args.out/'results')
        elif args.phase=='review':
            if not args.review_receipts:p.error('--review-receipts is required')
            receipts=load(args.review_receipts)
            for receipt in receipts['receipts']:runtime.review(db,receipt,REPO)
        elif args.phase=='block-known-gaps':
            gaps={
                'PA-W1-SPEC-BOLT':'Authoritative unrestricted NIIN016864912 Characteristics and Reference exports, with source release and qualifiers.',
                'PA-W1-BIDS-BOLT':'Actual bid abstracts and price-reasonableness determinations for the identified bolt solicitations.',
                'PA-W1-LINE-VA':'Original order36C79126F0030 priced device/accessory lines with model, quantity and accepted terms.',
                'PA-W1-LINE-HHS':'Original order75N98026F00268 defibrillator model, quantity and ordered line prices.',
                'PA-W1-SPEC-DLA-PILOT':'Unrestricted exact-part technical/revision and compliance match sufficient to qualify an independent price benchmark.'}
            for task,missing in gaps.items():
                if runtime.task_row(db,task)['status']=='blocked':continue
                claim=runtime.claim(db,task,OWNER)
                runtime.block(db,task,OWNER,claim['lease_token'],missing,
                    'Prior bounded research package documents this exact remaining gate; no network request made in this replay.')
        export=runtime.export(db,REPO)
        label = args.phase
        if args.phase == 'review':
            label += '-' + args.review_receipts.stem
        write_once(args.out/(label+'-state.json'),export)
        print(json.dumps({'phase':args.phase,'state_counts':{
            s:sum(t['status']==s for t in export['status']['tasks']) for s in ['queued','claimed','awaiting_review','accepted','blocked']},
            'new_network_requests':0,'out':str(args.out)}))
    finally:db.close()


if __name__=='__main__':main()
