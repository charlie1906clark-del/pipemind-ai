#!/usr/bin/env python3
"""Offline verification of retained seven-key award evidence and arithmetic.
This validates provenance and joins. It does not verify invoices, CLINs, delivery,
original terms, registration, beneficial ownership, misrepresentation or fraud.
"""
from pathlib import Path
from decimal import Decimal
import hashlib,json
ROOT=Path(__file__).resolve().parent
HISTORY=ROOT.parents[1]/'discovery-policy-2026-10-30/pricing/snapshots/selected_evidence.json'
def load(p):return json.loads(p.read_text(),parse_float=Decimal)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(capture=ROOT/'capture-success',history=HISTORY):
 if digest(history)!='052d394c9aeca30e9220436b70fe40a3518233b1f4aabf36a97dd7c6b9c958d8':raise ValueError('Historical seed digest mismatch')
 manifest=load(capture/'manifest.json')
 for m in manifest:
  if m.get('error'):raise ValueError('Successful-capture registry contains failed request')
  if m.get('http_status')!=200:raise ValueError('Missing successful status')
  if digest(capture/m['snapshot'])!=m['snapshot_sha256']:raise ValueError('Snapshot digest mismatch')
  if m.get('request_file') and digest(capture/m['request_file'])!=m['request_sha256']:raise ValueError('Request digest mismatch')
 search=load(capture/'exact-award-search.json');terminal=load(capture/'exact-award-terminal.json')
 req=load(capture/'exact-award-search.request.json');req2=load(capture/'exact-award-terminal.request.json')
 rows=search['results'];hist={r['contract_number']:r for r in load(history)['observations']}
 if len(rows)!=len(hist) or {r['Award ID'] for r in rows}!=set(hist):raise ValueError('Exact seven-key population mismatch')
 if req['filters'].get('award_ids')!=list(hist) or req2!=dict(req,page=2):raise ValueError('Search scope mismatch')
 if req.get('page')!=1 or req.get('subawards')is not False or terminal['results'] or terminal['page_metadata']['page']!=2 or terminal['page_metadata']['hasNext']:raise ValueError('Terminal page not proven')
 findings=[]
 for row in sorted(rows,key=lambda x:x['Award ID']):
  key=row['Award ID'];h=hist[key];d=load(capture/('award-'+key+'.json'))
  if d['piid']!=key or d['generated_unique_award_id']!=row['generated_internal_id']:raise ValueError('Detail identifier mismatch')
  if d['recipient']['recipient_uei']!=row['Recipient UEI'] or d['recipient']['recipient_name']!=row['Recipient Name']:raise ValueError('Recipient join mismatch')
  if d['date_signed']!=h['award_date']:raise ValueError('History date mismatch')
  if d['total_obligation']!=row['Award Amount']:raise ValueError('Search/detail amount mismatch')
  for key_to_omit in ['location','business_categories','email','phone','address_line1']:
   if key_to_omit in d['recipient']:raise ValueError('Irrelevant profile field retained')
  c=d['latest_transaction_contract_data'];product=Decimal(h['quantity_as_printed'])*Decimal(h['unit_cost_as_printed'])
  findings.append({'id':'BOLT-AWARD-'+key,'contract_number':key,'nsn_from_history':h['nsn'],'history_cage':h['cage'],'recipient_name':d['recipient']['recipient_name'],'recipient_uei':d['recipient']['recipient_uei'],'recipient_hash':d['recipient']['recipient_hash'],'source_ids':['BOLT-AWD-HISTORY','BOLT-AWD-SEARCH','BOLT-AWD-'+key],'date_signed':d['date_signed'],'history_date_matches':True,'award_type':d['type_description'],'awarding_agency':d['awarding_agency'],'solicitation_identifier':c.get('solicitation_identifier'),'number_of_offers_received':c.get('number_of_offers_received'),'competition':c.get('extent_competed_description'),'contract_pricing':c.get('type_of_contract_pricing_description'),'set_aside':c.get('type_set_aside_description'),'psc':c.get('product_or_service_code'),'performance_period':d['period_of_performance'],'award_obligation_usd':str(d['total_obligation']),'amount_basis':'Current cumulative obligation in official award summary; not payment','history_quantity_as_printed':h['quantity_as_printed'],'history_unit_cost_as_printed':h['unit_cost_as_printed'],'arithmetic_product':str(product),'product_equals_award_obligation':product==d['total_obligation'],'arithmetic_limit':'Numeric reconciliation only; does not authenticate purchased units, complete price scope or payment','cage_uei_join_basis':'Historical RFQ PIID/CAGE + exact official award PIID/UEI and matching date; not a direct SAM registration crosswalk','historical_clin_verified':False,'historical_unit_verified':False,'historical_pack_verified':False,'historical_delivery_terms_verified':False,'invoice_or_payment_verified':False,'fraud_finding':False})
 return {'schema_version':'1.0','as_of':'2026-10-30','observations':findings,'summary':{'exact_contracts':len(findings),'exact_date_matches':len(findings),'arithmetic_matches':sum(x['product_equals_award_obligation'] for x in findings),'distinct_ueis':len({x['recipient_uei'] for x in findings}),'sum_current_award_obligations_usd':str(sum(Decimal(x['award_obligation_usd']) for x in findings)),'aggregate_scope':'Seven distinct purchase-order PIIDs only; not spend for the NSN, invoices, loss, recovery or savings','original_priced_awards_acquired':0,'fraud_cases_established':0,'reward_estimate':None}}
if __name__=='__main__':
 out=verify();(ROOT/'observations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['summary']))
