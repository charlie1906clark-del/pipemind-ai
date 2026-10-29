#!/usr/bin/env python3
"""Assemble reviewed public registries and captured API samples into a neutral graph.

No remote calls, fraud scoring, fuzzy entity merging or ownership inference occurs.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from coverage import SECTORS
from investigation_extensions import load_approved_extensions

ROOT = Path(__file__).resolve().parents[1]
DAY = '2026-10-29'
nodes, edges, by_id, aliases, urls = [], [], {}, {}, {}

# Reviewed legal events, never inferred from keywords inside prose/negations.
CASE_LEGAL_STATUS = {
 'HC-C01':'administrative_action','HC-C02':'charged','HC-C03':'settlement',
 'HC-C04':'settlement','HC-C05':'settlement','HC-C06':'settlement',
 'HC-C07':'sentenced','HC-C08':'sentenced','HC-C09':'audit_finding','HC-C10':'settlement',
 'PROC-C001':'audit_finding','PROC-C002':'mixed','PROC-C003':'settlement',
 'PROC-C004':'settlement','PROC-C005':'settlement','PROC-C006':'guilty_plea',
 'PROC-C007':'settlement','PROC-C008':'mixed',
 'XS-C01':'settlement','XS-C02':'settlement','XS-C03':'conviction',
 'XS-C04':'sentenced','XS-C05':'guilty_plea','XS-C06':'sentenced',
 'XS-C07':'guilty_plea','XS-C08':'sentenced','XS-C09':'audit_finding',
 'XS-C10':'administrative_action',
}

def read(path):
    return json.loads(path.read_text())

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def node(ident, typ, title, status='planned', sources=(), **props):
    if ident in by_id:
        old = by_id[ident]
        old['source_ids'] = sorted(set(old['source_ids']) | set(sources))
        return ident
    record = dict(id=ident, type=typ, title=title, status=status,
                  source_ids=sorted(set(sources)), properties={'visibility':'public', **props})
    by_id[ident] = record
    nodes.append(record)
    return ident

def edge(typ, source, target, sources=(), status='documented_fact', **props):
    ident = 'edge-' + hashlib.sha256(f'{typ}|{source}|{target}'.encode()).hexdigest()[:20]
    if any(e['id'] == ident for e in edges): return
    edges.append(dict(id=ident,type=typ,source=source,target=target,status=status,
                      source_ids=sorted(set(sources)),properties={'visibility':'public',**props}))

def refs(ids):
    return sorted(set(aliases[x] for x in ids))

def canonical_url(url):
    s=urlsplit(url)
    q=[(k,v) for k,v in parse_qsl(s.query,keep_blank_values=True)
       if not (k.startswith('utm_') or k in {'trk','source','ref'})]
    return urlunsplit((s.scheme.lower(),s.netloc.lower(),s.path.rstrip('/'),urlencode(q),''))

def add_source(s):
    url=canonical_url(s['url'])
    if url in urls:
        ident=urls[url];aliases[s['id']]=ident
        by_id[ident]['properties'].setdefault('registry_aliases',[]).append(s['id'])
        return ident
    ident='src-'+s['id'];aliases[s['id']]=ident;urls[url]=ident
    props={k:v for k,v in s.items() if k not in {'id','title','url'}}
    props.setdefault('accessed_at',DAY)
    props.setdefault('source_bytes_archived',False)
    return node(ident,'source',s['title'],'source',url=url,registry_aliases=[s['id']],**props)

OWNERSHIP_SOURCES=[
 dict(id='OWN-S001',title='RTX Exhibit 21: subsidiary and affiliate listing at 2025-12-31',url='https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/exhibit212025-12x3110xk.htm',publisher='SEC EDGAR / RTX issuer filing',published_at='2026-02-06',summary='Raytheon Company appears in the dated issuer subsidiary/affiliate listing; not a full beneficial ownership chain.'),
 dict(id='OWN-S002',title='CVS Health Exhibit 21.1: subsidiaries at 2025-12-31',url='https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/exhibit211-2025.htm',publisher='SEC EDGAR / CVS issuer filing',published_at='2026-02-10',summary='Aetna Inc. is listed as a CVS Health subsidiary at this date; do not apply to every earlier transaction.'),
 dict(id='OWN-S003',title='RTX FY2025 Form 10-K',url='https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm',publisher='SEC EDGAR / RTX issuer filing',published_at='2026-02-06',summary='Dated corporate financial-reporting source. No revenue value has been extracted or reconciled to federal awards in this graph.'),
 dict(id='OWN-S004',title='CVS Health FY2025 Form 10-K',url='https://www.sec.gov/Archives/edgar/data/64803/000006480326000010/cvs-20251231.htm',publisher='SEC EDGAR / CVS issuer filing',published_at='2026-02-10',summary='Consolidated/segment accounting source, not a ledger of purchases or complete customer sales.'),
 dict(id='OWN-S005',title='DOJ Raytheon defective-pricing, bribery and export-control resolutions',url='https://www.justice.gov/archives/opa/pr/raytheon-company-pay-over-950m-connection-defective-pricing-foreign-bribery-and-export',publisher='DOJ',published_at='2024-10-16',summary='Published DPA and civil resolutions with admitted conduct; not a new lead or a conviction. Identifies Raytheon as RTX subsidiary and DoD procurement counterparty.'),
 dict(id='OWN-S006',title='GAO: limited beneficial ownership information available on awardees',url='https://www.gao.gov/products/gao-26-108174',publisher='GAO',published_at='2026-09-30',summary='Federal award and registry ownership information has substantial coverage limitations; listed officers and agents may not be beneficial owners.'),
]

def main():
    family_sources={}
    for family in ['reward','healthcare','procurement','cross_sector']:
        data=read(ROOT/'reports'/family/'sources.json')
        family_sources[family]=[add_source(s) for s in data]
    for s in OWNERSHIP_SOURCES:
        s.update(accessed_at=DAY,retrieval_status='web_open',source_bytes_archived=False)
        add_source(s)
    write(ROOT/'data/registries/ownership-sources.json',OWNERSHIP_SOURCES)

    for family,sources in family_sources.items():
        collection=node('bibliography-'+family,'research_collection',family+' source collection','planned',
                        scope='Discovery bibliography; membership does not establish every source supports every sector hypothesis')
        for src in sorted(set(sources)):edge('catalogues_source',collection,src,[src])

    for slug,title,family,path,test,alternative,gap in SECTORS:
        sec=node('sector-'+slug,'sector',title,'planned',scope=path,research_priority='catalogued_not_incidence_rank',
                 completeness='not_enumerated_nationwide',evidence_gap=gap)
        h=node('hyp-'+slug,'hypothesis',title+': bounded audit test','hypothesis',
               signal_to_test=test,benign_alternative=alternative,required_evidence=gap,
               conclusion='untested',no_fraud_determination=True)
        edge('has_research_hypothesis',sec,h,status='planned')
        edge('uses_discovery_bibliography',sec,'bibliography-'+family,status='planned')

    for family in ['healthcare','procurement','cross_sector']:
        for c in read(ROOT/'reports'/family/'cases.json'):
            source=refs(c['source_ids']); ident=c['id']
            detail=c.get('legal_status',c['status'])
            legal=CASE_LEGAL_STATUS[ident]  # unknown new case IDs require explicit review
            props={k:v for k,v in c.items() if k not in {'id','title','status','source_ids','legal_status','amount','amounts'}}
            node(ident,'case',c['title'],'published_case',source,legal_status=legal,
                 legal_status_detail=detail,public_record=True,novel_lead=False,
                 reward_eligibility='not_assessed',**props)
            es=c.get('entities',c.get('organizations',[]))
            for i,e in enumerate(es):
                name=e if isinstance(e,str) else e.get('name',str(e))
                eid=ident+'-entity-'+str(i+1)
                # Scoped identifiers intentionally avoid name-only cross-case merges.
                entity_type=e.get('type','organization') if isinstance(e,dict) else 'organization'
                node(eid,entity_type,name,'documented_fact',source,
                     public_record=True,identity_resolution='source_label_only_no_cross_case_merge',
                     role=e.get('role','mentioned_in_source') if isinstance(e,dict) else 'mentioned_in_source')
                edge('mentions',ident,eid,source,scope='Published source association; does not independently assign liability')
            amounts=c.get('amounts', [c['amount']] if isinstance(c.get('amount'),dict) else [])
            for i,a in enumerate(amounts):
                value=a.get('amount',a.get('value'))
                if value is None: continue
                measure=a.get('measure',a.get('type',a.get('category','unspecified_source_measure')))
                mid=ident+'-amount-'+str(i+1)
                node(mid,'money_measure',f'{c["title"]}: {measure}','documented_fact',source,
                     money={'amount':str(value),'currency':a.get('currency','USD'),'kind':measure,
                            'qualifier':a.get('qualifier',a.get('source_qualifier','as_reported')),
                            'comparator':a.get('comparator','not_specified'),
                            'period':a.get('period','not_specified'),
                            'basis':a.get('basis','published_source_measure'),
                            'condition':a.get('condition','none_reported')},
                     source_amount_details=a,source_reports_collection_verified=a.get('collection_verified',False),
                     independently_verified_collection=False,aggregation_permitted=False)
                edge('reports_amount',ident,mid,source)

    for s in read(ROOT/'reports/healthcare/sectors.json'):
        sid='workstream-'+s['id']
        source=refs(s['source_ids'])
        props={k:v for k,v in s.items() if k not in {'id','title','source_ids'}}
        node(sid,'workstream',s['title'],'planned',source,**props)
        for i,h in enumerate(s.get('hypotheses',[])):
            hid=sid+'-hyp-'+str(i+1)
            node(hid,'hypothesis',h['signal'],'hypothesis',source,**h)
            edge('has_research_hypothesis',sid,hid,status='planned')

    routes=read(ROOT/'reports/reward/rewards.json')['routes']
    for route in routes:
        source=refs(route['citations']); ident=route['id']
        props={k:v for k,v in route.items() if k not in {'id','name','status','citations'}}
        node(ident,'reward_route',route['name'],'documented_fact',source,
             programme_status=route['status'],eligibility_review_required=True,**props)

    ownership=read(ROOT/'reports/healthcare/ownership_examples.json')
    for n in ownership['nodes']:
        source=refs([s for e in ownership['edges'] if n['id'] in (e['subject'],e['object']) for s in e['source_ids']])
        node(n['id'],n['type'],n['name'],'documented_fact',source,public_record=True,
             role_scope=n.get('scope','Published corporate relationship; no inherited liability'))
    for e in ownership['edges']:
        edge(e['predicate'],e['subject'],e['object'],refs(e['source_ids']),
             time_basis=e['time_basis'],evidence_state=e['evidence_state'])

    for ident,name,source in [('entity-rtx','RTX Corporation','OWN-S001'),('entity-raytheon','Raytheon Company','OWN-S001'),
                              ('entity-cvs','CVS Health Corporation','OWN-S002'),('entity-aetna','Aetna Inc.','OWN-S002')]:
        node(ident,'organization',name,'documented_fact',refs([source]),public_record=True,
             source_dated_identity=True,ultimate_beneficial_owner='not_established')
    edge('reported_subsidiary_of','entity-raytheon','entity-rtx',refs(['OWN-S001','OWN-S005']),valid_at='2025-12-31',
         scope='2025 issuer listing; DOJ also describes subsidiary relationship in 2024; percentage/direct-parent chain not inferred')
    edge('reported_subsidiary_of','entity-aetna','entity-cvs',refs(['OWN-S002']),valid_at='2025-12-31',
         scope='Dated issuer disclosure; not a statement about liability or transaction-period ownership')
    for eid,sid in [('entity-rtx','OWN-S003'),('entity-cvs','OWN-S004')]:
        edge('has_financial_filing',eid,aliases[sid],refs([sid]),revenue_extraction='not_performed')
    trace=read(ROOT/'reports/procurement/neutral_trace.json')
    trace_ids={'PROC-ORG-RAYTHEON':'entity-raytheon','PROC-ORG-RTX':'entity-rtx'}
    for n in trace['nodes']:
        if n['id']=='PROC-C002': continue  # already represented once in case registry
        source=refs([s for e in trace['edges'] if n['id'] in (e['from'],e['to']) for s in e['source_ids']])
        props={k:v for k,v in n.items() if k not in {'id','name','type'}}
        node(trace_ids.get(n['id'],n['id']),'neutral_trace_'+n['type'].lower(),n['name'],
             'documented_fact',source,public_record=True,no_allegation_on_this_award=True,**props)
    for e in trace['edges']:
        edge(e['relation'],trace_ids.get(e['from'],e['from']),trace_ids.get(e['to'],e['to']),refs(e['source_ids']),
             observed_source_date=e['as_of'],assertion_type=e['assertion_type'],
             context='Neutral award trace. Historical legal matter is not connected to this PIID.')

    cohort_counts={}
    # Only reviewer-approved snapshots enter the public graph. New acquisitions
    # cannot silently replace evidence or collide with an earlier cohort ID.
    approved=read(ROOT/'data/approved-snapshots.json')['manifest_paths']
    seen_cohorts=set()
    for relative_path in approved:
        manifest_path=(ROOT/relative_path).resolve()
        if not manifest_path.is_relative_to((ROOT/'connectors/snapshots').resolve()):
            raise ValueError('Approved snapshot must be within connectors/snapshots')
        m=read(manifest_path); cohort=m['cohort']; folder=manifest_path.parent
        if cohort in seen_cohorts: raise ValueError('Only one approved observation per cohort in this version')
        seen_cohorts.add(cohort)
        if m.get('success') is not True or m.get('http_status')!=200:
            raise ValueError('Only successful reviewed HTTP200 captures can enter graph')
        if hashlib.sha256((folder/'request.json').read_bytes()).hexdigest()!=m['request_sha256']:
            raise ValueError('Snapshot request digest mismatch')
        body=(folder/'response.json').read_bytes()
        if hashlib.sha256(body).hexdigest()!=m['response_sha256']: raise ValueError('Snapshot digest mismatch')
        rows=json.loads(body)['results']
        if m['records_returned']!=len(rows):raise ValueError('Snapshot record count mismatch')
        cohort_counts[cohort]=len(rows)
        src='src-live-'+cohort
        node(src,'source','USAspending captured sample: '+cohort,'source',url=m['endpoint'],accessed_at=m['completed_at'],
             content_sha256=m['response_sha256'],source_bytes_archived=True,
             snapshot_path=str((folder/'response.json').relative_to(ROOT)),manifest_path=str(manifest_path.relative_to(ROOT)),
             request_path=str((folder/'request.json').relative_to(ROOT)),scope=m['scope'],sample_complete=False,
             pagination=m['page_metadata'],amount_semantics=m['amount_semantics'])
        cid=node('cohort-'+cohort,'cohort',cohort+' captured award sample','documented_fact',[src],
                 rows=len(rows),sample_complete=False,is_fraud_rank=False,ranking='largest cumulative award amount, descending',
                 remaining_pages=m['page_metadata']['hasNext'],claims_of_completeness=False)
        for r in rows:
            aid='award-'+hashlib.sha256(r['generated_internal_id'].encode()).hexdigest()[:24]
            rid='uei-'+r['Recipient UEI']; source=[src]
            node(rid,'organization',r['Recipient Name'],'documented_fact',source,uei=r['Recipient UEI'],
                 public_record=True,identity_resolution='Exact USAspending reported UEI; legal-registry corroboration pending',
                 ownership='not_traced',investigation_status='not_assessed_no_allegation')
            agency='agency-'+str(r['Awarding Agency Code'])
            node(agency,'agency',r['Awarding Agency'],'documented_fact',source,reported_code=r['Awarding Agency Code'])
            p={k:v for k,v in r.items() if k not in {'Award Amount','Recipient Name'}}
            node(aid,'award',r['Award ID'],'documented_fact',source,source_record=p,
                 money={'amount':str(r['Award Amount']),'currency':'USD','kind':'cumulative_award_amount_not_fy_spend'},
                 api_detail_url='https://www.usaspending.gov/award/'+r['generated_internal_id']+'/latest',
                 no_fraud_assessment=True,subaward_chain='not_acquired',ownership='not_traced')
            edge('includes_award',cid,aid,source)
            edge('awards',agency,aid,source)
            edge('reported_recipient',aid,rid,source)
            state=r.get('Place of Performance State Code')
            if state:
                gid=node('geo-us-'+state,'geography','US state/territory code '+state,'documented_fact',source,location_meaning='place_of_performance_not_owner_residence')
                edge('place_of_performance',aid,gid,source)

    agent_path=ROOT/'agents/agents.json'
    if agent_path.exists():
        ag=read(agent_path)
        for a in (ag if isinstance(ag,list) else ag['agents']):
            ident=a['id'] if a['id'].startswith('agent-') else 'agent-'+a['id']
            node(ident,'agent_specification',a.get('name',a.get('title',a['id'])),'planned',specification=a,runtime_active=False)
    tasks_path=ROOT/'architecture/tasks.json'
    if tasks_path.exists():
        ts=read(tasks_path)
        for t in (ts if isinstance(ts,list) else ts['tasks']):
            node('task-'+t['id'],'research_task',t['title'],'planned',definition=t,runtime_status='queued_definition_only')
        for t in (ts if isinstance(ts,list) else ts['tasks']):
            for dep in t.get('depends_on',[]):edge('depends_on','task-'+t['id'],'task-'+dep,status='planned')
    coverage=ROOT/'agents/coverage-map.json'
    if coverage.exists():
        mapping=read(coverage)
        for entry in mapping['coverage']:
            s=entry['sector_id']
            for role,ids in [('primary',[entry['primary_agent_id']]),('secondary',entry['secondary_agent_ids']),
                             ('reviewer',entry['mandatory_reviewers'])]:
                for a in ids:
                    if s not in by_id or a not in by_id:raise ValueError('Invalid sector agent coverage mapping')
                    edge('assigned_'+role+'_specification',s,a,status='planned',runtime_active=False)
    investigations = load_approved_extensions(ROOT, nodes, edges, DAY)
    by_id.update({n['id']: n for n in nodes})
    # Explicit provenance edges make the evidence bank navigable outside Obsidian.
    for n in list(nodes):
        for sid in n['source_ids']:edge('cites',n['id'],sid,[sid])
    nodes.sort(key=lambda n:n['id']);edges.sort(key=lambda e:e['id'])
    write(ROOT/'data/graph.json',dict(version='1.0',as_of=DAY,nodes=nodes,edges=edges))
    stats=dict(as_of=DAY,nodes=len(nodes),edges=len(edges),node_types=dict(Counter(n['type'] for n in nodes)),
               unique_source_urls=len({n['properties']['url'] for n in nodes if n['type']=='source'}),
               live_cohort_records=cohort_counts, approved_investigations=investigations,
               new_fraud_cases_identified=0,nationwide_buyer_coverage='not_complete',
               novel_named_leads_published=0,autonomous_agents_running=False)
    write(ROOT/'data/coverage-summary.json',stats)
    print(json.dumps(stats,indent=2))

if __name__=='__main__':main()
