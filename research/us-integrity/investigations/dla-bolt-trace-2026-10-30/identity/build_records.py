#!/usr/bin/env python3
"""Build neutral identity observations from frozen primary-source selections.
No network, entity guessing, fraud score, loss estimate or beneficial-owner inference.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json
ROOT=Path(__file__).resolve().parent
INV=ROOT.parent
BASE=INV.parent/'discovery-policy-2026-10-30'
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def main():
 manifest=read(ROOT/'capture_manifest.json')
 for req in manifest['requests']:
  for kind in ['request','snapshot']:
   if kind+'_path' in req:
    p=(ROOT/req[kind+'_path']).resolve()
    if not p.is_relative_to(ROOT):raise ValueError('Path escapes identity evidence directory')
    if digest(p)!=req[kind+'_sha256']:raise ValueError('Capture hash mismatch: '+str(p))
 for req in manifest.get('cage_captures',[]):
  if digest(ROOT/req['snapshot_path'])!=req['snapshot_sha256']:raise ValueError('CAGE snapshot hash mismatch')
 award_manifest=read(INV/'awards/capture-success/manifest.json')
 for rec in award_manifest:
  if rec.get('snapshot') and digest(INV/'awards/capture-success'/rec['snapshot'])!=rec['snapshot_sha256']:raise ValueError('Award snapshot hash mismatch')
 history=read(BASE/'pricing/snapshots/selected_evidence.json')
 groups=defaultdict(list)
 for row in history['observations']:groups[row['cage']].append(row)
 entities=[];edges=[];sources=[];joins=[];input_artifacts=[]
 def source(sid,title,url,path,scope,authority='official_public_record'):
  p=Path(path)
  source_path=str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(Path(__import__('os').path.relpath(p,ROOT)))
  sources.append({'id':sid,'title':title,'url':url,'accessed_on':'2026-10-30','authority':authority,'snapshot_path':source_path,'snapshot_sha256':digest(p),'snapshot_scope':scope,'original_wire_bytes_archived':False})
  input_artifacts.append({'path':source_path,'sha256':digest(p)})
 source('BI-S-HISTORY','Original DLA solicitation selected procurement-history table',history['source_url'],BASE/'pricing/snapshots/selected_evidence.json','Selected extraction; original PDF separately archived in prior investigation')
 for cage,rows in sorted(groups.items()):
  query=read(ROOT/'snapshots'/f'{cage}-recipient-page-1.json');terminal=read(ROOT/'snapshots'/f'{cage}-recipient-page-2.json')
  if terminal['results'] or query['page_metadata']['total']!=len(query['results']):raise ValueError('Incomplete recipient query')
  if len({r['id'] for r in query['results']})!=len(query['results']):raise ValueError('Duplicate recipient profiles')
  profile=read(ROOT/'snapshots'/f'{cage}-profile.json');selected=read(ROOT/'snapshots'/f'cage-{cage}-selected.json')
  uei=profile['uei'];name=profile['name']
  if not any(r['id']==profile['recipient_id'] and r['uei']==uei and r['name']==name for r in query['results']):raise ValueError('Profile/query mismatch')
  details=[l for l in selected['result_links'] if '/Search/Details?' in l['href']]
  if len(details)!=1 or selected['query']!=cage or any(selected['selected_text'].count(v)!=1 for v in [cage,uei,name]):raise ValueError('Ambiguous/mismatched CAGE registry selection')
  regid='BI-S-CAGE-'+cage;pid='BI-S-PROFILE-'+cage
  source(regid,'DLA CAGE public exact-code result '+cage,selected['source_url'],ROOT/'snapshots'/f'cage-{cage}-selected.json','Selected identifier/name text from one result row; no form tokens, address or contacts')
  source(pid,'USAspending child recipient profile '+uei,'https://api.usaspending.gov/api/v2/recipient/'+profile['recipient_id']+'/',ROOT/'snapshots'/f'{cage}-profile.json','Selected name, identifiers, aliases, reporting-parent, legal structure, state/country; demographic and contact fields omitted')
  entityid='BI-ENTITY-'+cage;hlinks=[];sids=[regid,pid,'BI-S-HISTORY']
  for h in rows:
   piid=h['contract_number'];path=INV/'awards/capture-success'/('award-'+piid+'.json');award=read(path)
   if award['piid']!=piid or award['recipient']['recipient_uei']!=uei or award['date_signed']!=h['award_date']:raise ValueError('Historical award/identity mismatch: '+piid)
   aid='BI-S-AWARD-'+piid
   source(aid,'USAspending exact award '+piid,'https://api.usaspending.gov/api/v2/awards/'+award['generated_unique_award_id']+'/',path,'Selected official award response; exact PIID, signed date, recipient UEI/name; original CAGE is supplied by the distinct DLA history source')
   link={'contract_number':piid,'cage':cage,'uei':uei,'award_date':h['award_date'],'rfq_source_page':h['source_page'],'recipient_name_as_reported':award['recipient']['recipient_name'],'exact_contract_and_date_match':True,'method':'DLA history PIID+CAGE joined to USAspending exact PIID+signed date+UEI; CAGE is not an award-API field','source_ids':['BI-S-HISTORY',aid]}
   hlinks.append(link);joins.append(link);sids.append(aid)
   edges.append({'id':'BI-REL-AWARD-'+piid,'source':piid,'target':entityid,'relationship':'source_reports_award_recipient','effective_date':h['award_date'],'status':'documented_source_relationship','source_ids':['BI-S-HISTORY',aid],'ownership_inferred':False})
  ent={'id':entityid,'cage':cage,'uei':uei,'legal_business_name':name,'recipient_record_type':'sole_proprietor_business_record' if 'sole_proprietorship' in profile['business_structure_types'] else 'corporate_business_record','business_structure_types':profile['business_structure_types'],'reported_aliases':profile['alternate_names'],'alias_effective_dates':None,'profile_location':profile['location'],'current_registry_as_of':'2026-10-30','current_registry_crosswalk_verified':True,'current_registry_result_rows':1,'historical_award_links':hlinks,'reporting_parent':{'name':profile['parent_name'],'uei':profile['parent_uei'],'same_uei_as_child':profile['parent_uei']==uei,'source_ids':[pid],'meaning':'Current USAspending reporting hierarchy; not authenticated beneficial ownership or historical control'},'beneficial_owners':None,'historical_registration_status':None,'sam_active_registration_verified':False,'status':'neutral_identity_consistency_observation','source_ids':sids,'fraud_assessment':False}
  entities.append(ent)
  edges.append({'id':'BI-REL-CAGE-'+cage,'source':'CAGE:'+cage,'target':'UEI:'+uei,'relationship':'current_registry_crosswalk','observed_on':'2026-10-30','status':'documented_source_relationship','source_ids':[regid],'historical_validity_inferred':False})
  edges.append({'id':'BI-REL-PARENT-'+cage,'source':entityid,'target':'UEI:'+profile['parent_uei'],'relationship':'source_reports_parent','observed_on':'2026-10-30','status':'source_reported_reporting_hierarchy','source_ids':[pid],'beneficial_ownership_inferred':False})
  for idx,alias in enumerate(profile['alternate_names'],1):
   edges.append({'id':f'BI-REL-ALIAS-{cage}-{idx}','source':entityid,'target':alias,'relationship':'source_reports_alternate_name','observed_on':'2026-10-30','effective_date':None,'status':'source_reported_alias','source_ids':[pid],'independent_legal_name_history_verified':False})
 output={'schema_version':'1.0','as_of':'2026-10-30','scope':'Five CAGEs from seven historical rows for NSN5306016864912; current registry corroboration and exact historical-award joins','entities':entities,'summary':{'entities':len(entities),'cages':len(groups),'ueis':len({e['uei'] for e in entities}),'historical_award_joins':len(joins),'current_cage_registry_matches':len(entities),'recipient_query_profiles':sum(len(read(ROOT/'snapshots'/f'{c}-recipient-page-1.json')['results']) for c in groups),'aliases':sum(len(e['reported_aliases']) for e in entities),'unresolved_beneficial_ownership_records':len(entities),'identifier_mismatches_observed':0,'new_fraud_findings':0,'money_aggregation_performed':False},'input_artifacts':input_artifacts}
 write(ROOT/'entity_records.json',output);write(ROOT/'relationships.json',{'schema_version':'1.0','as_of':'2026-10-30','relationships':edges});write(ROOT/'sources.json',{'schema_version':'1.0','as_of':'2026-10-30','sources':sources})
 print(json.dumps(output['summary'],indent=2))
if __name__=='__main__':main()
