import concurrent.futures
import copy
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

import agent_runtime as rt
import price_check


def plan():
    task=dict(id='TASK-A',title='Investigate exact item',agent_role='Specification auditor',question='Can an exact comparable record be obtained?',scope={'fixture':'synthetic calibration only'},depends_on=[],allowed_source_hosts=['example.invalid'],max_attempts=4,max_evidence=3,max_reopens=2)
    dependent={**task,'id':'TASK-B','depends_on':['TASK-A']}
    return dict(schema_version='1.0',plan_id='PLAN-SYNTHETIC-1',base_commit='a'*40,evidence_mode='synthetic',tasks=[task,dependent])


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.path=self.root/'ledger.sqlite';self.db=rt.connect(self.path);self.addCleanup(self.db.close)
        self.plan=plan();rt.import_plan(self.db,self.plan,now=100)
        (self.root/'first.txt').write_text('Synthetic original observation\n');(self.root/'later.txt').write_text('Synthetic newly available specification\n')
        self.claim=rt.claim(self.db,'TASK-A','Producer-A',now=100);self.token=self.claim['lease_token']
    def request(self,i='ATTEMPT-1'):
        return dict(attempt_id=i,task_id='TASK-A',url='https://example.invalid/source',method='GET',purpose='Synthetic acquisition calibration')
    def evidence(self,i='EVIDENCE-1',file='first.txt',attempt='ATTEMPT-1'):
        return dict(id=i,task_id='TASK-A',attempt_id=attempt,source_url='https://example.invalid/source',source_kind='synthetic',observed_at='2026-10-30',event_date=None,artifact_path=file,sha256=hashlib.sha256((self.root/file).read_bytes()).hexdigest(),hash_scope='synthetic_fixture',locator='whole invented fixture',claim_scope='Synthetic workflow test, not actual procurement',visibility='public',synthetic=True)
    def acquire(self,i='ATTEMPT-1',eid='EVIDENCE-1',file='first.txt'):
        rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request(i),now=101)
        rt.finish_attempt(self.db,'TASK-A','Producer-A',self.token,dict(attempt_id=i,outcome='success',detail='Synthetic fixture read'),now=102)
        return rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,self.evidence(eid,file,i),self.root,now=103)
    def result(self,rid='RESULT-1',refs=None):
        refs=['EVIDENCE-1'] if refs is None else refs
        return dict(schema_version='1.0',result_id=rid,task_id='TASK-A',producer='Producer-A',input_commit='a'*40,data_origin='synthetic',outcome='unresolved',evidence_ids=refs,facts=[dict(id='FACT-1',statement='An invented fixture was acquired',evidence_ids=refs)] if refs else [],candidate_signals=[],pricing_eligibility=dict(status='blocked',reason='No actual price comparator',evidence_ids=[]),benefit_evidence=dict(status='unresolved',reason='No actual buyer benefit evidence',evidence_ids=[]),unknowns=['Real price and specifications'],ordinary_alternatives=['An ordinary compliant supply cost may explain a difference'],conclusion='Synthetic unresolved packet; no adverse finding',next_record='Exact specification export')
    def submit(self):
        self.acquire();result=self.result();return rt.submit_result(self.db,'TASK-A','Producer-A',self.token,result,self.root,now=104)
    def receipt(self,decision='accepted',reviewer='Reviewer-B'):
        return dict(review_id='REVIEW-1',result_id='RESULT-1',reviewer=reviewer,result_sha256=rt.digest(self.result()),decision=decision,checks={k:'Independently checked synthetic '+k+' scope' for k in rt.REVIEW_CHECKS},reason='Unresolved research packet correctly reports its limits',required_record='Exact specification export' if decision!='accepted' else None)
    def trigger(self):
        return dict(reopen_id='REOPEN-1',reason='New exact requested fixture became available',addresses_required_record='Exact specification export',evidence=self.evidence('TRIGGER-1','later.txt'))
    def test_plan_immutable_atomic_and_cycle(self):
        self.assertTrue(rt.import_plan(self.db,self.plan,now=101)['idempotent'])
        changed=copy.deepcopy(self.plan);changed['tasks'][0]['max_attempts']=99
        with self.assertRaises(rt.RuntimeError):rt.import_plan(self.db,changed)
        self.assertEqual(rt.definition(rt.task_row(self.db,'TASK-A'))['max_attempts'],4)
        changed=plan();changed['tasks'][0]['depends_on']=['TASK-B']
        with self.assertRaises(rt.RuntimeError):rt.validate_plan(changed)
    def test_live_claim_idempotence_dependency_and_fencing(self):
        self.assertEqual(rt.claim(self.db,'TASK-A','producer-a',now=101)['lease_token'],self.token)
        with self.assertRaises(rt.RuntimeError):rt.claim(self.db,'TASK-A','other',now=101)
        with self.assertRaises(rt.RuntimeError):rt.claim(self.db,'TASK-B','other',now=101)
        new=rt.claim(self.db,'TASK-A','producer-a',now=1901)
        self.assertNotEqual(new['lease_token'],self.token)
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request(),now=1902)
    def test_expired_worker_cannot_write(self):
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request(),now=1900)
    def test_pending_and_failed_attempts_consume_budget(self):
        for i in range(4):
            r=self.request('ATTEMPT-'+str(i));rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,r,now=101)
            if i%2:rt.finish_attempt(self.db,'TASK-A','Producer-A',self.token,dict(attempt_id=r['attempt_id'],outcome='failure',detail='Synthetic timeout'),now=102)
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request('ATTEMPT-5'),now=103)
        s=rt.status(self.db,now=1901)['tasks'][0];self.assertTrue(s['available']);self.assertEqual(s['effective_status'],'closeout_ready')
        closeout=rt.claim(self.db,'TASK-A','Producer-A',now=1901);self.assertEqual(closeout['work_mode'],'closeout_only')
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',closeout['lease_token'],self.request('ATTEMPT-5'),now=1902)
        result=self.result(refs=[]);result['unknowns']=['Four attempts exhausted, including interrupted requests; no successful record available']
        rt.submit_result(self.db,'TASK-A','Producer-A',closeout['lease_token'],result,self.root,now=1902)
    def test_attempt_and_evidence_replay_are_immutable(self):
        self.acquire();self.assertTrue(rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,self.evidence(),self.root,now=104)['idempotent'])
        bad=self.request();bad['purpose']='Changed claim'
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,bad,now=104)
        bad=self.evidence();bad['claim_scope']='changed extraction'
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,bad,self.root,now=104)
    def test_evidence_requires_success_actual_hash_and_safe_path(self):
        r=self.request();rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,r,now=101)
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,self.evidence(),self.root,now=102)
        rt.finish_attempt(self.db,'TASK-A','Producer-A',self.token,dict(attempt_id=r['attempt_id'],outcome='success',detail='Read fixture'),now=102)
        e=self.evidence();e['sha256']='0'*64
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=103)
        e=self.evidence();e['artifact_path']='../first.txt'
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=103)
        (self.root/'link.txt').symlink_to(self.root/'first.txt');e=self.evidence();e['artifact_path']='link.txt'
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=103)
    def test_public_synthetic_and_private_fields_rejected(self):
        self.acquire();e=self.evidence('EVIDENCE-2');e['synthetic']=False
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=104)
        e=self.evidence('EVIDENCE-2');e['nested']={'home_address':'private value'}
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=104)
        e=self.evidence();e.update(synthetic=False,source_kind='official_record',hash_scope='raw_response')
        with self.assertRaises(rt.RuntimeError):rt.artifact(e,self.root,['example.invalid'],'public')
    def test_result_requires_known_evidence_and_exact_commit(self):
        self.acquire();r=self.result();r['input_commit']='b'*40
        with self.assertRaises(rt.RuntimeError):rt.submit_result(self.db,'TASK-A','Producer-A',self.token,r,self.root,now=104)
        r=self.result();r['facts'][0]['evidence_ids']=['MISSING']
        with self.assertRaises(rt.RuntimeError):rt.submit_result(self.db,'TASK-A','Producer-A',self.token,r,self.root,now=104)
    def test_independent_review_and_dependency_acceptance(self):
        self.submit()
        with self.assertRaises(rt.RuntimeError):rt.claim(self.db,'TASK-B','worker-b',now=105)
        with self.assertRaises(rt.RuntimeError):rt.review(self.db,self.receipt(reviewer='PRODUCER-A'),self.root,now=105)
        bad=self.receipt();bad['result_sha256']='0'*64
        with self.assertRaises(rt.RuntimeError):rt.review(self.db,bad,self.root,now=105)
        rt.review(self.db,self.receipt(),self.root,now=105)
        self.assertTrue(rt.review(self.db,self.receipt(),self.root,now=106)['idempotent'])
        self.assertEqual(rt.claim(self.db,'TASK-B','worker-b',now=107)['owner'],'worker-b')
        # Acceptance of an unresolved packet did not change eligibility.
        stored=json.loads(self.db.execute("SELECT payload FROM results WHERE id='RESULT-1'").fetchone()[0]);self.assertEqual(stored['pricing_eligibility']['status'],'blocked')
    def test_result_idempotent_after_review_and_changed_replay_rejected(self):
        self.submit();rt.review(self.db,self.receipt(),self.root,now=105)
        self.assertTrue(rt.submit_result(self.db,'TASK-A','producer-a',self.token,self.result(),self.root,now=106)['idempotent'])
        changed=self.result();changed['conclusion']='invented conclusion'
        with self.assertRaises(rt.RuntimeError):rt.submit_result(self.db,'TASK-A','producer-a',self.token,changed,self.root,now=106)
    def test_block_reopen_new_exact_artifact_and_resume(self):
        self.acquire();rt.block(self.db,'TASK-A','Producer-A',self.token,'Exact specification export','Still missing',now=104)
        trigger=self.trigger();bad=copy.deepcopy(trigger);bad['addresses_required_record']='Any document'
        with self.assertRaises(rt.RuntimeError):rt.reopen(self.db,'TASK-A','coordinator',bad,self.root,now=105)
        bad=copy.deepcopy(trigger);bad['evidence']=self.evidence('OLD-COPY')
        with self.assertRaises(rt.RuntimeError):rt.reopen(self.db,'TASK-A','coordinator',bad,self.root,now=105)
        result=rt.reopen(self.db,'TASK-A','coordinator',trigger,self.root,now=105);self.assertEqual(result['remaining_attempts'],3)
        self.assertTrue(rt.reopen(self.db,'TASK-A','coordinator',trigger,self.root,now=106)['idempotent'])
        claim=rt.claim(self.db,'TASK-A','Producer-A',now=107);self.assertNotEqual(claim['lease_token'],self.token)
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request('OLD'),now=108)
    def test_exhaustion_cannot_be_reset_by_reopen(self):
        for i in range(4):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,self.request('ATTEMPT-'+str(i)),now=101)
        rt.block(self.db,'TASK-A','Producer-A',self.token,'Exact specification export','Budget exhausted',now=103)
        with self.assertRaises(rt.RuntimeError):rt.reopen(self.db,'TASK-A','coordinator',self.trigger(),self.root,now=104)
        self.assertEqual(rt.counts(self.db,'TASK-A')['attempts'],4)
    def test_rejected_result_can_reopen_but_accepted_cannot(self):
        self.submit();rt.review(self.db,self.receipt('needs_more_evidence'),self.root,now=105)
        self.assertEqual(rt.task_row(self.db,'TASK-A')['status'],'blocked')
        rt.reopen(self.db,'TASK-A','coordinator',self.trigger(),self.root,now=106)
        other=rt.claim(self.db,'TASK-A','new-producer',now=107);self.assertEqual(other['owner'],'new-producer')
    def test_file_tampering_detected_at_review_and_export(self):
        self.submit();(self.root/'first.txt').write_text('Tampered')
        with self.assertRaises(rt.RuntimeError):rt.review(self.db,self.receipt(),self.root,now=105)
        with self.assertRaises(rt.RuntimeError):rt.export(self.db,self.root,now=105)
    def test_reopen_trigger_tampering_detected_on_export(self):
        rt.block(self.db,'TASK-A','Producer-A',self.token,'Exact specification export','Still missing',now=104)
        rt.reopen(self.db,'TASK-A','coordinator',self.trigger(),self.root,now=105)
        (self.root/'later.txt').write_text('Tampered trigger')
        with self.assertRaises(rt.RuntimeError):rt.export(self.db,self.root,now=106)
    def test_accepted_packet_requires_new_version_for_followup(self):
        self.submit();rt.review(self.db,self.receipt(),self.root,now=105)
        with self.assertRaises(rt.RuntimeError):rt.reopen(self.db,'TASK-A','coordinator',self.trigger(),self.root,now=106)
    def test_sql_append_only_and_export_excludes_fencing_token(self):
        self.acquire()
        with self.assertRaises(sqlite3.IntegrityError):self.db.execute("UPDATE evidence SET payload='{}'")
        with self.assertRaises(sqlite3.IntegrityError):self.db.execute('DELETE FROM attempts')
        exported=json.dumps(rt.export(self.db,self.root,now=104));self.assertNotIn(self.token,exported)
    def test_existing_price_engine_adapter_preserves_real_and_synthetic_gates(self):
        cases=price_check.CALCULATOR.parent/'scenarios'
        real=price_check.run(cases/'dla-current-no-qualified-benchmark.json')
        self.assertEqual(real['result']['eligible_lines'],0)
        self.assertEqual(real['result']['aggregates'],[])
        self.assertFalse(real['automatic_task_completion'])
        synthetic=price_check.run(cases/'uniform-12-percent.json')
        self.assertEqual(synthetic['result']['aggregates'][0]['weighted_premium_against_reference_percent'],'12.000000')
        self.assertEqual(synthetic['result']['data_origin'],'illustrative')
    def test_local_capture_reuse_preserves_original_provenance_and_zero_network(self):
        e=self.evidence();req=self.request();req.update(method='LOCAL_CAPTURE_REUSE',new_network_requests=0,original_capture={k:e[k] for k in ('artifact_path','sha256','observed_at','hash_scope')});req['original_capture']['provenance_note']='Earlier selected artifact, replayed locally'
        bad=copy.deepcopy(req);bad['new_network_requests']=1
        with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,bad,now=101,repository=self.root)
        rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,req,now=101,repository=self.root)
        finish=dict(attempt_id='ATTEMPT-1',outcome='success',detail='Retained bytes revalidated',new_network_requests=0)
        bad=copy.deepcopy(finish);bad['new_network_requests']=1
        with self.assertRaises(rt.RuntimeError):rt.finish_attempt(self.db,'TASK-A','Producer-A',self.token,bad,now=102)
        rt.finish_attempt(self.db,'TASK-A','Producer-A',self.token,finish,now=102)
        bad=copy.deepcopy(e);bad['observed_at']='2026-10-29'
        with self.assertRaises(rt.RuntimeError):rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,bad,self.root,now=103)
        rt.append_evidence(self.db,'TASK-A','Producer-A',self.token,e,self.root,now=103)
        summary=rt.status(self.db,now=104)['tasks'][0]
        self.assertEqual(summary['local_capture_reuse_attempts'],1)
        self.assertEqual(summary['remote_attempt_reservations'],0)
    def test_read_url_boundary(self):
        for url in ['http://example.invalid/x','https://evil.invalid/x','https://example.invalid:444/x','https://user:pass@example.invalid/x','https://example.invalid/x?token=secret','https://@example.invalid/x','https://example.invalid/x?X-Amz-Credential=secret','https://example.invalid/x?session_id=secret','https://example.invalid/x#access_token=secret','https://example.invalid/space here']:
            req=self.request();req['url']=url
            with self.assertRaises(rt.RuntimeError):rt.start_attempt(self.db,'TASK-A','Producer-A',self.token,req,now=101)
    def test_concurrent_reclaim_has_one_owner(self):
        def work(owner):
            db=rt.connect(self.path)
            try:
                try:return rt.claim(db,'TASK-A',owner,now=1901)['owner']
                except rt.RuntimeError:return None
            finally:db.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:answers=list(pool.map(work,['worker-x','worker-y']))
        self.assertEqual(sum(a is not None for a in answers),1)

if __name__=='__main__':unittest.main()
