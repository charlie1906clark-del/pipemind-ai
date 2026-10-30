#!/usr/bin/env python3
"""Execute an isolated, deterministic synthetic durable-work demonstration."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import agent_runtime as rt

PREFIX='research/us-integrity/price-agents/runtime/fixtures/'


def plan():
    task={'id':'DEMO-SPEC','title':'Resolve mock specification','agent_role':'Technical equivalence auditor','question':'Can the exact missing mock record be obtained?','scope':{'data':'synthetic workflow only; no government transaction'},'depends_on':[],'allowed_source_hosts':['example.invalid'],'max_attempts':3,'max_evidence':3,'max_reopens':1}
    return {'schema_version':'1.0','plan_id':'DEMO-PRICE-WORKFLOW-V1','base_commit':'a'*40,'evidence_mode':'synthetic','tasks':[task,{**task,'id':'DEMO-PRICE','title':'Check mock comparison gates','depends_on':['DEMO-SPEC']}]}


def evidence(ident):
    path=PREFIX+'later.txt'
    return {'id':ident,'task_id':'DEMO-SPEC','attempt_id':'DEMO-ATTEMPT-2','source_url':'https://example.invalid/mock-specification','source_kind':'synthetic','observed_at':'2026-10-30','event_date':None,'artifact_path':path,'sha256':hashlib.sha256((rt.REPOSITORY/path).read_bytes()).hexdigest(),'hash_scope':'synthetic_fixture','locator':'entire invented fixture','claim_scope':'Workflow demonstration only; contains no actual product characteristics','visibility':'public','synthetic':True}


def run():
    with tempfile.TemporaryDirectory(prefix='price-agent-demo-') as folder:
        path=Path(folder)/'demo.sqlite';db=rt.connect(path);rt.import_plan(db,plan(),now=1000)
        first=rt.claim(db,'DEMO-SPEC','demo-producer',now=1001)
        request={'attempt_id':'DEMO-ATTEMPT-1','task_id':'DEMO-SPEC','url':'https://example.invalid/mock-specification','method':'PUBLIC_TOOL_READ','purpose':'Simulated failed acquisition; no network call'}
        rt.start_attempt(db,'DEMO-SPEC','demo-producer',first['lease_token'],request,now=1002)
        rt.finish_attempt(db,'DEMO-SPEC','demo-producer',first['lease_token'],{'attempt_id':'DEMO-ATTEMPT-1','outcome':'unavailable','detail':'Simulated missing record; no website contacted'},now=1003)
        rt.block(db,'DEMO-SPEC','demo-producer',first['lease_token'],'Exact mock specification export','Simulated unavailable source',now=1004)
        db.close()
        # A second connection represents a later worker session using the same ledger.
        db=rt.connect(path)
        rt.reopen(db,'DEMO-SPEC','demo-coordinator',{'reopen_id':'DEMO-REOPEN-1','reason':'A distinct mock record is supplied','addresses_required_record':'Exact mock specification export','evidence':evidence('DEMO-TRIGGER-1')},now=1010)
        second=rt.claim(db,'DEMO-SPEC','demo-producer',now=1011)
        stale_rejected=False
        try:rt.start_attempt(db,'DEMO-SPEC','demo-producer',first['lease_token'],{**request,'attempt_id':'DEMO-STALE'},now=1012)
        except rt.RuntimeError:stale_rejected=True
        rt.start_attempt(db,'DEMO-SPEC','demo-producer',second['lease_token'],{**request,'attempt_id':'DEMO-ATTEMPT-2','purpose':'Read local synthetic fixture; no network call'},now=1012)
        rt.finish_attempt(db,'DEMO-SPEC','demo-producer',second['lease_token'],{'attempt_id':'DEMO-ATTEMPT-2','outcome':'success','detail':'Local invented fixture read; no external source authenticated'},now=1013)
        rt.append_evidence(db,'DEMO-SPEC','demo-producer',second['lease_token'],evidence('DEMO-EVIDENCE-1'),now=1014)
        result={'schema_version':'1.0','result_id':'DEMO-RESULT-1','task_id':'DEMO-SPEC','producer':'demo-producer','input_commit':'a'*40,'data_origin':'synthetic','outcome':'unresolved','evidence_ids':['DEMO-EVIDENCE-1'],'facts':[{'id':'DEMO-FACT-1','statement':'An explicitly invented local fixture was read','evidence_ids':['DEMO-EVIDENCE-1']}],'candidate_signals':[],'pricing_eligibility':{'status':'blocked','reason':'Synthetic fixture does not establish any real product equivalence','evidence_ids':[]},'benefit_evidence':{'status':'unresolved','reason':'No real procurement or benefit evidence exists in this demonstration','evidence_ids':[]},'unknowns':['Actual specifications, market prices and buyer decisions'],'ordinary_alternatives':['Any apparent price difference could reflect ordinary supply terms; no actual difference was computed'],'conclusion':'Workflow demonstrated; no procurement conclusion','next_record':'An actual independently reviewed primary item record'}
        submitted=rt.submit_result(db,'DEMO-SPEC','demo-producer',second['lease_token'],result,now=1015)
        dependency_blocked=False
        try:rt.claim(db,'DEMO-PRICE','demo-analyst',now=1016)
        except rt.RuntimeError:dependency_blocked=True
        db.close()
        # A third connection demonstrates separately attributed review after restart.
        db=rt.connect(path)
        receipt={'review_id':'DEMO-REVIEW-1','result_id':'DEMO-RESULT-1','reviewer':'demo-reviewer','result_sha256':submitted['sha256'],'decision':'accepted','checks':{'provenance':'Mock artifact bytes match; source is explicitly synthetic','comparability':'No actual benchmark eligible; blocked state preserved','alternative_explanations':'Ordinary terms remain an alternative; no real price residual','amount_basis':'No government monetary measure is present','privacy':'Invented names and .invalid source; no personal data'},'reason':'Accept the correctly limited demonstration packet, not any product or financial claim'}
        rt.review(db,receipt,now=1020)
        output=rt.export(db,now=1021);db.close()
        output['demonstration']={'synthetic':True,'network_requests':0,'model_calls':0,'ledger_connections':3,'simulated_clock':True,'blocked_before_new_artifact':True,'new_lease_fenced_old_worker':stale_rejected,'dependency_blocked_before_review':dependency_blocked,'accepted_packet_pricing_eligibility':'blocked','continuing_task':'DEMO-PRICE','persistent_service_deployed':False}
        assert stale_rejected and dependency_blocked
        assert next(t for t in output['status']['tasks'] if t['task_id']=='DEMO-PRICE')['available']
        return output


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output');a=p.parse_args();data=run();encoded=json.dumps(data,indent=2,sort_keys=True)+'\n'
    if a.output:
        with open(a.output,'x') as f:f.write(encoded)
        print(json.dumps({'output':a.output,'sha256':hashlib.sha256(encoded.encode()).hexdigest(),'demonstration':data['demonstration']},indent=2))
    else:print(encoded,end='')


if __name__=='__main__':main()
