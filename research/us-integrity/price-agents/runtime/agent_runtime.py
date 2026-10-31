#!/usr/bin/env python3
"""Durable, offline research-work coordination. It is not an LLM or fraud detector."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import secrets
import sqlite3
import sys
import time
from urllib.parse import parse_qsl, urlsplit

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[3]
_spec = importlib.util.spec_from_file_location('integrity_shared', HERE.parents[1] / 'engine/integrity.py')
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)
canonical = _base.canonical
RuntimeError = _base.IntegrityError
SCHEMA = '1.0'
HASH = re.compile(r'^[0-9a-f]{64}$')
COMMIT = re.compile(r'^[0-9a-f]{40}$')
HOST = re.compile(r'^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$')
SOURCE_KINDS = {'official_record','seller_catalog','corporate_filing','court_record','methodology','selected_public_record','synthetic'}
REVIEW_CHECKS = {'provenance','comparability','alternative_explanations','amount_basis','privacy'}
IMMUTABLE = ('plans','attempts','attempt_finishes','evidence','results','reviews','reopens','events')


def text(value, field):
    if not isinstance(value,str) or not value.strip() or len(value)>20000:
        raise RuntimeError(field + ': require nonempty text up to 20000 characters')
    return value


def ident(value, field='id'):
    _base.safe_id(value, field)
    return value


def actor(value):
    ident(value, 'actor')
    return value.casefold()


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def integer(value, field, low, high):
    if type(value) is not int or not low<=value<=high:
        raise RuntimeError(f'{field}: require integer {low}..{high}')
    return value


def public_json(value):
    if not isinstance(value,dict):
        raise RuntimeError('Expected JSON object')
    try:
        json.dumps(value,allow_nan=False)
    except (ValueError,TypeError) as exc:
        raise RuntimeError('Nonfinite or non-JSON input') from exc
    _base._privacy_properties(value,'research packet')
    def visit(x):
        if isinstance(x,dict):
            for key,value in x.items():
                if key.casefold() in {'api_key','access_token','authorization','password','client_secret','lease_token'} and value not in (None,'',[],{}):raise RuntimeError('Credential or fencing token cannot enter a public payload')
            if 'visibility' in x and x['visibility']!='public':
                raise RuntimeError('Only public artifacts may enter this runtime')
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    visit(value)


def hosts(values):
    if not isinstance(values,list) or not values or len(set(values))!=len(values):
        raise RuntimeError('allowed_source_hosts must be a nonempty unique list')
    for h in values:
        if not isinstance(h,str) or not HOST.fullmatch(h) or h.endswith('.local') or h=='localhost':
            raise RuntimeError('Require exact lowercase public DNS host names; no wildcards')
    return values


def public_url(value, allowed):
    text(value,'source_url')
    if any(c.isspace() or ord(c)<33 or ord(c)>126 for c in value) or '\\' in value:raise RuntimeError('Unsafe URL characters')
    try:u=urlsplit(value)
    except ValueError as exc:raise RuntimeError('Invalid URL') from exc
    try:port=u.port
    except ValueError as exc:raise RuntimeError('Invalid URL port') from exc
    if u.scheme!='https' or u.username is not None or u.password is not None or u.fragment or port not in (None,443) or u.hostname not in allowed:
        raise RuntimeError('Source must be HTTPS on an exact approved host without credentials')
    if any(re.search(r'(?:token|credential|signature|secret|password|session|authorization|api.?key|access.?key|^key$|^sig$|^auth$)',k,re.I) for k,v in parse_qsl(u.query)):
        raise RuntimeError('Credential-like URL query cannot enter a public receipt')
    return value


def validate_plan(plan):
    public_json(plan)
    if plan.get('schema_version')!=SCHEMA or plan.get('evidence_mode') not in {'public','synthetic'}:
        raise RuntimeError('Plan needs schema_version1.0 and evidence_mode public/synthetic')
    ident(plan.get('plan_id'),'plan_id')
    if not isinstance(plan.get('base_commit'),str) or not COMMIT.fullmatch(plan['base_commit']):
        raise RuntimeError('base_commit must be an exact 40-character commit digest')
    tasks=plan.get('tasks')
    if not isinstance(tasks,list) or not 1<=len(tasks)<=1000:
        raise RuntimeError('Plan requires 1..1000 tasks')
    ids=[]
    for t in tasks:
        public_json(t);ids.append(ident(t.get('id'),'task.id'))
        for k in ('title','agent_role','question'):text(t.get(k),k)
        if not isinstance(t.get('scope'),dict) or not t['scope']:raise RuntimeError('Task requires explicit nonempty scope')
        if not isinstance(t.get('depends_on'),list) or len(set(t['depends_on']))!=len(t['depends_on']):raise RuntimeError('depends_on must be a unique list')
        for d in t['depends_on']:ident(d,'dependency')
        hosts(t.get('allowed_source_hosts'))
        integer(t.get('max_attempts'),'max_attempts',1,1000)
        integer(t.get('max_evidence'),'max_evidence',1,1000)
        integer(t.get('max_reopens'),'max_reopens',0,10)
        integer(t.get('max_claims',t['max_attempts']+t['max_reopens']+1),'max_claims',1,1100)
    if len(set(ids))!=len(ids):raise RuntimeError('Duplicate task ID')
    by={t['id']:t for t in tasks};done=set();active=set()
    def visit(i):
        if i in done:return
        if i in active:raise RuntimeError('Dependency cycle')
        active.add(i)
        for d in by[i]['depends_on']:
            if d not in by:raise RuntimeError('Dependency must be in the same plan')
            visit(d)
        active.remove(i);done.add(i)
    for i in ids:visit(i)
    return plan


def connect(path):
    db=sqlite3.connect(str(path),timeout=30,isolation_level=None)
    db.row_factory=sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    db.execute('PRAGMA busy_timeout=30000')
    db.executescript('''
CREATE TABLE IF NOT EXISTS runtime_meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS plans(id TEXT PRIMARY KEY,sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY,plan_id TEXT NOT NULL REFERENCES plans(id),sha256 TEXT NOT NULL,payload TEXT NOT NULL,status TEXT NOT NULL,owner TEXT,lease_token TEXT,lease_until REAL,claim_count INTEGER NOT NULL DEFAULT 0,reopen_count INTEGER NOT NULL DEFAULT 0,blocked_record TEXT,current_result_id TEXT);
CREATE TABLE IF NOT EXISTS attempts(id TEXT PRIMARY KEY,task_id TEXT NOT NULL REFERENCES tasks(id),owner TEXT NOT NULL,lease_token TEXT NOT NULL,at REAL NOT NULL,sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS attempt_finishes(attempt_id TEXT PRIMARY KEY REFERENCES attempts(id),at REAL NOT NULL,sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS evidence(id TEXT PRIMARY KEY,task_id TEXT NOT NULL REFERENCES tasks(id),attempt_id TEXT NOT NULL REFERENCES attempts(id),sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS results(id TEXT PRIMARY KEY,task_id TEXT NOT NULL REFERENCES tasks(id),producer TEXT NOT NULL,lease_token TEXT NOT NULL,sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reviews(id TEXT PRIMARY KEY,result_id TEXT NOT NULL UNIQUE REFERENCES results(id),reviewer TEXT NOT NULL,sha256 TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reopens(id TEXT PRIMARY KEY,task_id TEXT NOT NULL REFERENCES tasks(id),actor TEXT NOT NULL,artifact_sha256 TEXT NOT NULL,sha256 TEXT NOT NULL,payload TEXT NOT NULL,UNIQUE(task_id,artifact_sha256));
CREATE TABLE IF NOT EXISTS events(sequence INTEGER PRIMARY KEY AUTOINCREMENT,task_id TEXT,action TEXT NOT NULL,actor TEXT NOT NULL,at REAL NOT NULL,payload TEXT NOT NULL);
''')
    row=db.execute("SELECT value FROM runtime_meta WHERE key='schema_version'").fetchone()
    if row and row['value']!=SCHEMA:raise RuntimeError('Unsupported runtime schema')
    db.execute("INSERT OR IGNORE INTO runtime_meta VALUES('schema_version',?)",(SCHEMA,))
    for table in IMMUTABLE:
        for action in ('UPDATE','DELETE'):
            db.execute(f"CREATE TRIGGER IF NOT EXISTS immutable_{table}_{action.lower()} BEFORE {action} ON {table} BEGIN SELECT RAISE(ABORT,'immutable ledger row'); END")
    return db


@contextmanager
def transaction(db):
    db.execute('BEGIN IMMEDIATE')
    try:
        yield
        db.execute('COMMIT')
    except Exception:
        if db.in_transaction:db.execute('ROLLBACK')
        raise


def now_value(now):return time.time() if now is None else now


def event(db,task,action,owner,payload,now):
    db.execute('INSERT INTO events(task_id,action,actor,at,payload) VALUES(?,?,?,?,?)',(task,action,owner,now,canonical(payload)))


def task_row(db,task):
    ident(task,'task')
    row=db.execute('SELECT * FROM tasks WHERE id=?',(task,)).fetchone()
    if not row:raise RuntimeError('Unknown task')
    return row


def definition(row):return json.loads(row['payload'])


def task_plan(db,row):return json.loads(db.execute('SELECT payload FROM plans WHERE id=?',(row['plan_id'],)).fetchone()[0])


def counts(db,task):
    return {k:db.execute(f'SELECT count(*) FROM {k} WHERE task_id=?',(task,)).fetchone()[0] for k in ('attempts','evidence')}


def import_plan(db,plan,now=None):
    validate_plan(plan);sha=digest(plan);at=now_value(now)
    with transaction(db):
        old=db.execute('SELECT sha256 FROM plans WHERE id=?',(plan['plan_id'],)).fetchone()
        if old:
            if old['sha256']!=sha:raise RuntimeError('Plan ID is immutable; use a new plan/task version')
            return {'plan_id':plan['plan_id'],'idempotent':True,'tasks':len(plan['tasks'])}
        if any(db.execute('SELECT 1 FROM tasks WHERE id=?',(t['id'],)).fetchone() for t in plan['tasks']):raise RuntimeError('Task ID already exists; use a new version')
        db.execute('INSERT INTO plans VALUES(?,?,?)',(plan['plan_id'],sha,canonical(plan)))
        for t in plan['tasks']:
            db.execute('INSERT INTO tasks(id,plan_id,sha256,payload,status) VALUES(?,?,?,?,?)',(t['id'],plan['plan_id'],digest(t),canonical(t),'queued'))
        event(db,None,'plan_imported','coordinator',{'plan_id':plan['plan_id'],'sha256':sha},at)
    return {'plan_id':plan['plan_id'],'idempotent':False,'tasks':len(plan['tasks'])}


def dependency_blockers(db,row):
    return [d for d in definition(row)['depends_on'] if task_row(db,d)['status']!='accepted']


def lease(db,task,owner,token,now):
    row=task_row(db,task)
    if row['status']!='claimed' or row['owner']!=actor(owner):raise RuntimeError('Only current claimed owner may mutate work')
    if not isinstance(token,str) or not row['lease_token'] or not secrets.compare_digest(token,row['lease_token']):raise RuntimeError('Stale or incorrect lease fencing token')
    if row['lease_until']<=now:raise RuntimeError('Lease expired; reacquire before writing')
    return row


def claim(db,task,owner,lease_seconds=1800,now=None):
    owner=actor(owner);integer(lease_seconds,'lease_seconds',30,86400);at=now_value(now)
    with transaction(db):
        row=task_row(db,task);d=definition(row);c=counts(db,task)
        if row['status']=='claimed' and row['lease_until']>at:
            if row['owner']!=owner:raise RuntimeError('Task already has a live owner')
            return {'task_id':task,'owner':owner,'lease_token':row['lease_token'],'lease_until':row['lease_until'],'idempotent':True}
        if row['status'] not in {'queued','claimed'}:raise RuntimeError('Task is '+row['status'])
        if dependency_blockers(db,row):raise RuntimeError('Dependencies need independent accepted packets')
        if row['claim_count']>=d.get('max_claims',d['max_attempts']+d['max_reopens']+1):
            raise RuntimeError('Claim budget exhausted; a new reviewed task scope/version is required')
        token=secrets.token_urlsafe(24);until=at+lease_seconds
        db.execute("UPDATE tasks SET status='claimed',owner=?,lease_token=?,lease_until=?,claim_count=claim_count+1 WHERE id=?",(owner,token,until,task))
        event(db,task,'claimed',owner,{'lease_until':until,'claim_number':row['claim_count']+1},at)
    return {'task_id':task,'owner':owner,'lease_token':token,'lease_until':until,'idempotent':False,'work_mode':'closeout_only' if c['attempts']>=d['max_attempts'] else 'research','attempts_remaining':d['max_attempts']-c['attempts']}


def prior_immutable(db,table,key,value,payload):
    row=db.execute(f'SELECT * FROM {table} WHERE {key}=?',(value,)).fetchone()
    if row and row['sha256']!=digest(payload):raise RuntimeError('Immutable ID replay differs from recorded payload')
    return row


def start_attempt(db,task,owner,token,request,now=None,repository=REPOSITORY):
    public_json(request);ident(request.get('attempt_id'),'attempt_id');text(request.get('purpose'),'purpose');at=now_value(now)
    with transaction(db):
        row=lease(db,task,owner,token,at);d=definition(row)
        if request.get('task_id')!=task:raise RuntimeError('Attempt task mismatch')
        public_url(request.get('url'),d['allowed_source_hosts'])
        if request.get('method') not in {'GET','HEAD','POST_READONLY','PUBLIC_TOOL_READ','LOCAL_CAPTURE_REUSE'}:raise RuntimeError('Unsupported read-only attempt method')
        if request['method']=='LOCAL_CAPTURE_REUSE':
            reuse=request.get('original_capture')
            if not isinstance(reuse,dict):raise RuntimeError('Local reuse requires original_capture metadata')
            _base._date(reuse.get('observed_at'),'original_capture.observed_at')
            if reuse.get('hash_scope') not in {'selected_extract','raw_response','render','metadata','synthetic_fixture'}:raise RuntimeError('Original capture hash scope required')
            text(reuse.get('provenance_note'),'original_capture.provenance_note')
            if request.get('new_network_requests')!=0 or type(request.get('new_network_requests')) is not int:raise RuntimeError('Local capture reuse must declare zero new network requests')
            retained_file(reuse,repository)
        old=prior_immutable(db,'attempts','id',request['attempt_id'],request)
        if old:
            if old['task_id']!=task or old['owner']!=actor(owner) or old['lease_token']!=token:raise RuntimeError('Attempt belongs to another lease')
            return {'attempt_id':request['attempt_id'],'idempotent':True,'budget_consumed':True}
        if counts(db,task)['attempts']>=d['max_attempts']:raise RuntimeError('Attempt budget exhausted')
        db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?)',(request['attempt_id'],task,actor(owner),token,at,digest(request),canonical(request)))
        event(db,task,'attempt_reserved',actor(owner),{'attempt_id':request['attempt_id']},at)
    return {'attempt_id':request['attempt_id'],'idempotent':False,'budget_consumed':True}


def finish_attempt(db,task,owner,token,finish,now=None):
    public_json(finish);ident(finish.get('attempt_id'),'attempt_id');at=now_value(now)
    if finish.get('outcome') not in {'success','failure','unavailable'}:raise RuntimeError('Attempt outcome required')
    text(finish.get('detail'),'detail')
    with transaction(db):
        lease(db,task,owner,token,at)
        attempt=db.execute('SELECT * FROM attempts WHERE id=?',(finish['attempt_id'],)).fetchone()
        if not attempt or attempt['task_id']!=task or attempt['owner']!=actor(owner) or attempt['lease_token']!=token:raise RuntimeError('Attempt not reserved by this task lease')
        if json.loads(attempt['payload'])['method']=='LOCAL_CAPTURE_REUSE' and (finish.get('new_network_requests')!=0 or type(finish.get('new_network_requests')) is not int):raise RuntimeError('Local reuse completion requires zero new network requests')
        old=prior_immutable(db,'attempt_finishes','attempt_id',finish['attempt_id'],finish)
        if old:return {'attempt_id':finish['attempt_id'],'idempotent':True}
        db.execute('INSERT INTO attempt_finishes VALUES(?,?,?,?)',(finish['attempt_id'],at,digest(finish),canonical(finish)))
        event(db,task,'attempt_finished',actor(owner),finish,at)
    return {'attempt_id':finish['attempt_id'],'idempotent':False}


def retained_file(record,repository):
    path=text(record.get('artifact_path'),'artifact_path');relative=Path(path)
    if relative.is_absolute() or any(x in {'..','private','restricted','secrets'} or x.startswith('.') for x in relative.parts):raise RuntimeError('Unsafe or private artifact path')
    root=Path(repository).resolve();target=root/relative
    cursor=root
    for part in relative.parts:
        cursor=cursor/part
        if cursor.is_symlink():raise RuntimeError('Symlink artifact paths are not accepted')
    if not target.resolve().is_relative_to(root) or not target.is_file():raise RuntimeError('Artifact must be an existing repository-relative file')
    if target.stat().st_size>64*1024*1024:raise RuntimeError('Artifact exceeds64MiB; retain a reviewed selected extract')
    sha=record.get('sha256')
    if not isinstance(sha,str) or not HASH.fullmatch(sha):raise RuntimeError('Actual retained-byte SHA256 required')
    if hashlib.sha256(target.read_bytes()).hexdigest()!=sha:raise RuntimeError('Artifact SHA256 does not match current retained bytes')
    return target


def artifact(record,repository,allowed,mode):
    public_json(record);ident(record.get('id'),'evidence.id')
    public_url(record.get('source_url'),allowed)
    if record.get('visibility')!='public' or type(record.get('synthetic')) is not bool:raise RuntimeError('Explicit public visibility and synthetic flag required')
    if record['synthetic']!=(mode=='synthetic'):raise RuntimeError('Public and synthetic evidence must remain in separate plans')
    if mode=='public' and urlsplit(record['source_url']).hostname.endswith('.invalid'):raise RuntimeError('Placeholder domains are not public evidence')
    if record.get('source_kind') not in SOURCE_KINDS:raise RuntimeError('Unknown source_kind')
    if (record['source_kind']=='synthetic')!=record['synthetic']:raise RuntimeError('Synthetic source kind mismatch')
    _base._date(record.get('observed_at'),'observed_at')
    if record.get('event_date') is not None:_base._date(record['event_date'],'event_date')
    for k in ('locator','claim_scope'):text(record.get(k),k)
    if record.get('hash_scope') not in {'selected_extract','raw_response','render','metadata','synthetic_fixture'}:raise RuntimeError('Explicit hash_scope required')
    if (record['hash_scope']=='synthetic_fixture')!=record['synthetic']:raise RuntimeError('Synthetic hash scope mismatch')
    retained_file(record,repository)
    return record


def append_evidence(db,task,owner,token,record,repository=REPOSITORY,now=None):
    at=now_value(now)
    with transaction(db):
        row=lease(db,task,owner,token,at);d=definition(row);plan=task_plan(db,row)
        artifact(record,repository,d['allowed_source_hosts'],plan['evidence_mode'])
        if record.get('task_id')!=task:raise RuntimeError('Evidence task mismatch')
        attempt=db.execute('SELECT a.*,f.payload AS finish FROM attempts a JOIN attempt_finishes f ON a.id=f.attempt_id WHERE a.id=?',(record.get('attempt_id'),)).fetchone()
        if not attempt or attempt['task_id']!=task or json.loads(attempt['finish'])['outcome']!='success':raise RuntimeError('Evidence requires successful completed task attempt')
        if json.loads(attempt['payload'])['url']!=record['source_url']:raise RuntimeError('Evidence source URL differs from recorded attempt; use final URL as explicit separate attempt')
        request=json.loads(attempt['payload'])
        if request['method']=='LOCAL_CAPTURE_REUSE':
            reuse=request['original_capture']
            if any(record.get(k)!=reuse.get(k) for k in ('artifact_path','sha256','observed_at','hash_scope')):raise RuntimeError('Reused evidence must preserve original capture bytes, timestamp and hash scope')
        old=prior_immutable(db,'evidence','id',record['id'],record)
        if old:return {'evidence_id':record['id'],'idempotent':True}
        if counts(db,task)['evidence']>=d['max_evidence']:raise RuntimeError('Evidence budget exhausted')
        db.execute('INSERT INTO evidence VALUES(?,?,?,?,?)',(record['id'],task,record['attempt_id'],digest(record),canonical(record)))
        event(db,task,'evidence_appended',actor(owner),{'evidence_id':record['id'],'artifact_sha256':record['sha256']},at)
    return {'evidence_id':record['id'],'idempotent':False}


def accessible_evidence(db,row):
    tasks={row['id']}
    def visit(r):
        for d in definition(r)['depends_on']:
            dep=task_row(db,d)
            if dep['status']!='accepted':continue
            if d not in tasks:tasks.add(d);visit(dep)
    visit(row)
    return {e['id']:e for t in tasks for e in db.execute('SELECT * FROM evidence WHERE task_id=?',(t,))}


def validate_result(db,row,result,repository):
    public_json(result);ident(result.get('result_id'),'result_id');plan=task_plan(db,row)
    if result.get('schema_version')!=SCHEMA or result.get('task_id')!=row['id']:raise RuntimeError('Result schema/task mismatch')
    if result.get('input_commit')!=plan['base_commit']:raise RuntimeError('Result must identify the immutable plan base commit')
    if result.get('data_origin')!=plan['evidence_mode']:raise RuntimeError('Result data_origin differs from plan evidence mode')
    if result.get('outcome') not in {'observations','ordinary_explanation','unresolved','unsupported_signal'}:raise RuntimeError('Outcome must be an evidence state, never a required fraud finding')
    evidence=accessible_evidence(db,row);refs=result.get('evidence_ids')
    if not isinstance(refs,list) or len(set(refs))!=len(refs) or any(x not in evidence for x in refs):raise RuntimeError('Evidence references must exist in this task or its accepted dependencies')
    for e in refs:
        er=evidence[e];source_task=task_row(db,er['task_id']);artifact(json.loads(er['payload']),repository,definition(source_task)['allowed_source_hosts'],task_plan(db,source_task)['evidence_mode'])
    ids=set()
    for field in ('facts','candidate_signals'):
        if not isinstance(result.get(field),list):raise RuntimeError(field+' must be an array')
        for item in result[field]:
            public_json(item);ident(item.get('id'),'claim.id');text(item.get('statement'),'statement')
            if item['id'] in ids:raise RuntimeError('Duplicate claim ID')
            ids.add(item['id']);cites=item.get('evidence_ids')
            if not isinstance(cites,list) or not cites or any(e not in refs for e in cites):raise RuntimeError('Every fact/signal needs listed evidence')
            if field=='candidate_signals':text(item.get('alternative_explanation'),'alternative_explanation')
    for field in ('pricing_eligibility','benefit_evidence'):
        x=result.get(field)
        if not isinstance(x,dict):raise RuntimeError(field+' must be explicit')
        states={'blocked','unqualified','excluded','eligible_as_declared'} if field=='pricing_eligibility' else {'unresolved','no_evidence_in_acquired_records','documented_public_record'}
        if x.get('status') not in states:raise RuntimeError('Invalid '+field+' state')
        text(x.get('reason'),field+'.reason');cites=x.get('evidence_ids')
        if not isinstance(cites,list) or any(e not in refs for e in cites):raise RuntimeError('Invalid '+field+' evidence')
        if x['status'] in {'eligible_as_declared','documented_public_record'} and not cites:raise RuntimeError('Affirmative gate requires evidence')
    for field in ('unknowns','ordinary_alternatives'):
        if not isinstance(result.get(field),list):raise RuntimeError(field+' must be an array')
        for x in result[field]:text(x,field)
    if not result['ordinary_alternatives']:raise RuntimeError('At least one reasoned alternative or applicability explanation required')
    text(result.get('conclusion'),'conclusion')
    if result.get('next_record') is not None:text(result['next_record'],'next_record')
    return result


def submit_result(db,task,owner,token,result,repository=REPOSITORY,now=None):
    at=now_value(now);owner=actor(owner)
    with transaction(db):
        old=prior_immutable(db,'results','id',result.get('result_id'),result)
        if old:
            if old['task_id']!=task or old['producer']!=owner or old['lease_token']!=token:raise RuntimeError('Result replay actor/lease mismatch')
            return {'result_id':old['id'],'sha256':old['sha256'],'idempotent':True}
        row=lease(db,task,owner,token,at)
        if actor(result.get('producer'))!=owner:raise RuntimeError('Result producer differs from lease owner')
        validate_result(db,row,result,repository)
        db.execute('INSERT INTO results VALUES(?,?,?,?,?,?)',(result['result_id'],task,owner,token,digest(result),canonical(result)))
        db.execute("UPDATE tasks SET status='awaiting_review',lease_until=NULL,current_result_id=? WHERE id=?",(result['result_id'],task))
        event(db,task,'result_submitted',owner,{'result_id':result['result_id'],'sha256':digest(result)},at)
    return {'result_id':result['result_id'],'sha256':digest(result),'idempotent':False,'status':'awaiting_review'}


def review(db,receipt,repository=REPOSITORY,now=None):
    public_json(receipt);ident(receipt.get('review_id'),'review_id');reviewer=actor(receipt.get('reviewer'));at=now_value(now)
    with transaction(db):
        old=prior_immutable(db,'reviews','id',receipt['review_id'],receipt)
        if old:return {'review_id':old['id'],'idempotent':True}
        result=db.execute('SELECT * FROM results WHERE id=?',(receipt.get('result_id'),)).fetchone()
        if not result:raise RuntimeError('Unknown result')
        row=task_row(db,result['task_id'])
        if row['status']!='awaiting_review' or row['current_result_id']!=result['id']:raise RuntimeError('Result is not the current review target')
        if reviewer==result['producer']:raise RuntimeError('Producer cannot independently review its own packet')
        if receipt.get('result_sha256')!=result['sha256']:raise RuntimeError('Review must pin exact result digest')
        if receipt.get('decision') not in {'accepted','needs_more_evidence','rejected'}:raise RuntimeError('Unsupported review decision')
        checks=receipt.get('checks')
        if not isinstance(checks,dict) or set(checks)!=REVIEW_CHECKS or any(not isinstance(v,str) or not v.strip() for v in checks.values()):raise RuntimeError('Review requires reasoned provenance/comparability/alternatives/amount/privacy checks')
        text(receipt.get('reason'),'review.reason')
        if receipt['decision']!='accepted':text(receipt.get('required_record'),'required_record')
        validate_result(db,row,json.loads(result['payload']),repository)
        db.execute('INSERT INTO reviews VALUES(?,?,?,?,?)',(receipt['review_id'],result['id'],reviewer,digest(receipt),canonical(receipt)))
        state={'accepted':'accepted','needs_more_evidence':'blocked','rejected':'rejected'}[receipt['decision']]
        db.execute('UPDATE tasks SET status=?,blocked_record=? WHERE id=?',(state,receipt.get('required_record'),row['id']))
        event(db,row['id'],'reviewed',reviewer,{'review_id':receipt['review_id'],'decision':receipt['decision']},at)
    return {'review_id':receipt['review_id'],'status':state,'idempotent':False,'meaning':'Packet acceptance is not benchmark eligibility, innocence, loss or a misconduct finding'}


def block(db,task,owner,token,required_record,reason,now=None):
    text(required_record,'required_record');text(reason,'reason');at=now_value(now)
    with transaction(db):
        row=lease(db,task,owner,token,at);c=counts(db,task);state='exhausted' if c['attempts']>=definition(row)['max_attempts'] else 'blocked'
        db.execute('UPDATE tasks SET status=?,blocked_record=?,lease_until=NULL WHERE id=?',(state,required_record,task))
        event(db,task,'blocked',actor(owner),{'required_record':required_record,'reason':reason,'status':state},at)
    return {'task_id':task,'status':state,'required_record':required_record}


def reopen(db,task,owner,trigger,repository=REPOSITORY,now=None):
    owner=actor(owner);at=now_value(now);public_json(trigger)
    ident(trigger.get('reopen_id'),'reopen_id');text(trigger.get('reason'),'reason');text(trigger.get('addresses_required_record'),'addresses_required_record')
    with transaction(db):
        row=task_row(db,task);d=definition(row);plan=task_plan(db,row)
        old=prior_immutable(db,'reopens','id',trigger['reopen_id'],trigger)
        if old:
            if old['task_id']!=task or old['actor']!=owner:raise RuntimeError('Reopen replay actor/task mismatch')
            return {'task_id':task,'idempotent':True}
        if row['status'] not in {'blocked','rejected','exhausted'}:raise RuntimeError('Only blocked/rejected/exhausted work may be reopened; accepted packets need new task versions')
        if trigger['addresses_required_record']!=row['blocked_record']:raise RuntimeError('Trigger must identify the exact blocked record')
        if row['reopen_count']>=d['max_reopens']:raise RuntimeError('Reopen budget exhausted')
        if counts(db,task)['attempts']>=d['max_attempts'] or row['claim_count']>=d.get('max_claims',d['max_attempts']+d['max_reopens']+1):raise RuntimeError('Work budget exhausted; reopening never resets it')
        evidence=trigger.get('evidence');artifact(evidence,repository,d['allowed_source_hosts'],plan['evidence_mode'])
        prior_ids={r['id'] for r in db.execute('SELECT id FROM evidence')}
        prior_ids|={json.loads(r['payload'])['evidence']['id'] for r in db.execute('SELECT payload FROM reopens')}
        if evidence['id'] in prior_ids:raise RuntimeError('Reopen trigger evidence ID must be new and unambiguous')
        prior_hashes={json.loads(e['payload'])['sha256'] for e in db.execute('SELECT payload FROM evidence WHERE task_id=?',(task,))}
        prior_hashes|={r['artifact_sha256'] for r in db.execute('SELECT artifact_sha256 FROM reopens WHERE task_id=?',(task,))}
        if evidence['sha256'] in prior_hashes:raise RuntimeError('Reopen requires newly supplied artifact bytes, not a repeated reason or old evidence')
        db.execute('INSERT INTO reopens VALUES(?,?,?,?,?,?)',(trigger['reopen_id'],task,owner,evidence['sha256'],digest(trigger),canonical(trigger)))
        db.execute("UPDATE tasks SET status='queued',owner=NULL,lease_token=NULL,lease_until=NULL,reopen_count=reopen_count+1 WHERE id=?",(task,))
        event(db,task,'reopened',owner,{'reopen_id':trigger['reopen_id'],'trigger_evidence_id':evidence['id'],'artifact_sha256':evidence['sha256']},at)
    return {'task_id':task,'status':'queued','idempotent':False,'trigger_evidence_id':evidence['id'],'remaining_attempts':d['max_attempts']-counts(db,task)['attempts']}


def status(db,now=None):
    at=now_value(now);rows=[]
    for row in db.execute('SELECT * FROM tasks ORDER BY id'):
        d=definition(row);c=counts(db,row['id']);deps=dependency_blockers(db,row)
        acquisition_exhausted=c['attempts']>=d['max_attempts']
        claim_exhausted=row['claim_count']>=d.get('max_claims',d['max_attempts']+d['max_reopens']+1)
        exhausted=acquisition_exhausted or claim_exhausted
        available=row['status'] in {'queued','claimed'} and (row['status']!='claimed' or row['lease_until']<=at) and not deps and not claim_exhausted
        reused=sum(json.loads(x['payload'])['method']=='LOCAL_CAPTURE_REUSE' for x in db.execute('SELECT payload FROM attempts WHERE task_id=?',(row['id'],)))
        rows.append({'task_id':row['id'],'plan_id':row['plan_id'],'agent_role':d['agent_role'],'status':row['status'],'owner':row['owner'],'lease_active':row['status']=='claimed' and row['lease_until']>at,'claim_count':row['claim_count'],'reopen_count':row['reopen_count'],'attempts':c['attempts'],'local_capture_reuse_attempts':reused,'remote_attempt_reservations':c['attempts']-reused,'attempts_remaining':d['max_attempts']-c['attempts'],'evidence_count':c['evidence'],'dependency_blockers':deps,'budget_exhausted':exhausted,'available':available,'available_work_mode':'closeout_only' if acquisition_exhausted else 'research','effective_status':'closeout_ready' if available and acquisition_exhausted else 'exhausted' if claim_exhausted and not (row['status']=='claimed' and row['lease_until']>at) and row['status'] in {'queued','claimed','blocked'} else row['status'],'required_record':row['blocked_record'],'current_result_id':row['current_result_id']})
    return {'schema_version':SCHEMA,'tasks':rows,'model_execution':'not_provided_by_this_runtime','distributed_lock':False}


def export(db,repository=REPOSITORY,now=None):
    # Recheck retained evidence so an old accepted receipt cannot hide modified files.
    for e in db.execute('SELECT * FROM evidence'):
        row=task_row(db,e['task_id']);artifact(json.loads(e['payload']),repository,definition(row)['allowed_source_hosts'],task_plan(db,row)['evidence_mode'])
    for trigger in db.execute('SELECT task_id,payload FROM reopens'):
        row=task_row(db,trigger['task_id']);artifact(json.loads(trigger['payload'])['evidence'],repository,definition(row)['allowed_source_hosts'],task_plan(db,row)['evidence_mode'])
    result={'schema_version':SCHEMA,'status':status(db,now),'graph_promotion':'requires_separate_publication_review','truth_authentication':'not_provided','tables':{}}
    for table in IMMUTABLE:
        records=[]
        for row in db.execute(f'SELECT * FROM {table}'):
            x=dict(row);x.pop('lease_token',None)
            if 'payload' in x:x['payload']=json.loads(x['payload'])
            records.append(x)
        result['tables'][table]=records
    return result


def load(path):
    p=Path(path)
    if p.stat().st_size>8*1024*1024:raise RuntimeError('Input JSON exceeds8MiB')
    return json.loads(p.read_text())


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--db',required=True);p.add_argument('--repository',default=str(REPOSITORY));sub=p.add_subparsers(dest='command',required=True)
    for command in ('init','import-plan'):
        a=sub.add_parser(command);a.add_argument('--plan',required=True)
    for command in ('status','next','export'):sub.add_parser(command)
    for command in ('claim','start-attempt','finish-attempt','append-evidence','submit-result','block','reopen'):
        a=sub.add_parser(command);a.add_argument('--task',required=True);a.add_argument('--owner',required=True)
        if command=='claim':a.add_argument('--lease-seconds',type=int,default=1800)
        elif command=='reopen':a.add_argument('--json',required=True)
        else:
            a.add_argument('--lease-token',required=True)
            if command=='block':a.add_argument('--required-record',required=True);a.add_argument('--reason',required=True)
            else:a.add_argument('--json',required=True)
    a=sub.add_parser('review');a.add_argument('--json',required=True)
    args=p.parse_args(argv)
    try:
        if args.command!='init' and not Path(args.db).is_file():raise RuntimeError('Database does not exist; run init first')
        if args.command=='init':Path(args.db).parent.mkdir(parents=True,exist_ok=True)
        db=connect(args.db)
        try:
            c=args.command
            if c in {'init','import-plan'}:result=import_plan(db,load(args.plan))
            elif c=='claim':result=claim(db,args.task,args.owner,args.lease_seconds)
            elif c=='start-attempt':result=start_attempt(db,args.task,args.owner,args.lease_token,load(args.json),repository=args.repository)
            elif c=='finish-attempt':result=finish_attempt(db,args.task,args.owner,args.lease_token,load(args.json))
            elif c=='append-evidence':result=append_evidence(db,args.task,args.owner,args.lease_token,load(args.json),args.repository)
            elif c=='submit-result':result=submit_result(db,args.task,args.owner,args.lease_token,load(args.json),args.repository)
            elif c=='review':result=review(db,load(args.json),args.repository)
            elif c=='block':result=block(db,args.task,args.owner,args.lease_token,args.required_record,args.reason)
            elif c=='reopen':result=reopen(db,args.task,args.owner,load(args.json),args.repository)
            elif c=='export':result=export(db,args.repository)
            else:
                result=status(db)
                if c=='next':result['tasks']=[x for x in result['tasks'] if x['available']]
        finally:db.close()
        print(json.dumps(result,indent=2,sort_keys=True));return 0
    except (RuntimeError,sqlite3.Error,OSError,ValueError,KeyError,TypeError) as exc:
        print('runtime error: '+str(exc),file=sys.stderr);return 2


if __name__=='__main__':raise SystemExit(main())
