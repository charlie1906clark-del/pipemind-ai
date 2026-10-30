#!/usr/bin/env python3
"""Build a bounded, dated public-business role graph from selected evidence."""
import hashlib,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
P=R.parent
DAY='2026-10-30'
def load(p):return json.loads((R/p).read_text())
def write(p,obj):
 (R/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
award=load('../detail-capture/detail-SPE4A626PW775.json')
profiles={c:load('profile-'+c+'-selected.json') for c in ['745V4','27624']}
source_specs=[
 ('TP-S-ORDER-ROLE','DLA original order page 1 printed officer role','https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF','../selected/dla-award-page1-role-selected.txt','Official DD1155 page 1 block 24 area; selected printed professional name, role and date only; not independently authenticated signature or price-selection/payment authority'),
 ('TP-S-ORDER','DLA original order page 2','https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF','../selected/dla-award-page2.txt','Official contract; selected page-2 text; stated intended source, not proof of delivery'),
 ('TP-S-AWARD','USAspending exact award','https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE4A626PW775_9700_-NONE-_-NONE-/','../detail-capture/detail-SPE4A626PW775.json','Official award selected fields; obligations and recipient, not payment ledger'),
 ('TP-S-CAGE-DON','DLA CAGE exact search 745V4','https://cage.dla.mil/Search','cage-745V4-selected.json','Exact CAGE/name/UEI strings returned together in a single-result search; registration-status detail page not read'),
 ('TP-S-CAGE-SPS','DLA CAGE exact search 27624','https://cage.dla.mil/Search','cage-27624-selected.json','Exact CAGE/name/UEI strings returned together in a single-result search; registration-status detail page not read'),
 ('TP-S-PROFILE-DON','USAspending Don child recipient profile','https://api.usaspending.gov/api/v2/recipient/'+profiles['745V4']['recipient_id']+'/','profile-745V4-selected.json','Selected public business identifiers, federal reported parent, state and country'),
 ('TP-S-QUERY-SPS','USAspending exact UEI recipient query','https://api.usaspending.gov/api/v2/recipient/','sps-recipient-query.json','POST keyword E6KFWWNKEQ49; one exact UEI child result; query payload reproduced in acquire_parties.py'),
 ('TP-S-PROFILE-SPS','USAspending SPS child recipient profile','https://api.usaspending.gov/api/v2/recipient/'+profiles['27624']['recipient_id']+'/','profile-27624-selected.json','Selected public business identifiers, federal reported parent, state and country')]
sources=[]
for sid,title,url,path,scope in source_specs:
 sources.append({'id':sid,'title':title,'url':url,'accessed_on':DAY,'authority':'official_public_record','snapshot_path':path,'snapshot_sha256':sha(R/path),'snapshot_scope':scope,'original_wire_bytes_archived':False})
write('sources.json',{'as_of':DAY,'sources':sources,'source_hash_note':'Snapshot SHA-256 values authenticate retained selected extracts only. Original-wire hashes for direct registry requests are in acquisition_log.json; wire bytes are not archived. Original order hash is in ../selected_manifest.json.'})
company_url='https://donindustrialgroup.com/about'
fl_url='https://search.sunbiz.org/Inquiry/corporationsearch/SearchResultDetail?aggregateId=flal-l10000120053-f1f6ee9a-e912-456e-8731-47dcc778c29f&directionType=ForwardList&inquirytype=EntityName&listNameOrder=DONIM+S545370&searchNameOrder=DONINDUSTRIALGROUP+L100001200530&searchTerm=DONIS+TRANSPORT+INC.'
web_notes=[
 {'id':'TP-COMPANY-DON','url':company_url,'publisher':'Don Industrial Group','retrieval_scope':'Full page opened; analyst-selected paraphrase only','accessed_on':DAY,'selected_facts':['Site displays CAGE 745V4 and describes distribution of aerospace/defense parts, custom packaging and long-term fixed prices.'],'limits':'Company marketing does not establish supplier cost, discount or shipment on this order.'},
 {'id':'TP-COMPANY-PB','url':'https://www.pccfasteners.com/companies/pcc-fasteners/pb-fasteners.html','publisher':'PCC Fasteners','retrieval_scope':'Full page opened; analyst-selected paraphrase only','accessed_on':DAY,'selected_facts':['PCC Fasteners lists PB Fasteners as a company and describes airframe structural nuts and bolts in Gardena, California.'],'limits':'No CAGE on the retained page observation; PB Fasteners has not been joined into the award graph by a unique identifier.'},
 {'id':'TP-CANDIDATE-FL','url':fl_url,'publisher':'Florida Division of Corporations','retrieval_scope':'Official search-index extract used; subsequent open response not used for facts because the tool output was unavailable after truncation','accessed_on':DAY,'selected_facts':['Florida document L10000120053 names DON INDUSTRIAL GROUP LLC.','Filing and effective date 2010-11-18; name-change event 2016-06-23.','Search-index extract shows active status and annual report dates 2024-04-25, 2025-04-29 and 2026-04-30.','Public authorized-person role: REINIER HERNANDEZ, title MGR.'],'limits':'Candidate state-filing entity remains separate. No retained official federal-ID/state-document crosswalk. Manager is not asserted to be owner, buyer, signatory, price evaluator or beneficiary. Role start/end and role at 2026-07-09 are unknown. No personal contact or address fields retained.'},
 {'id':'TP-COMPANY-BERKSHIRE','url':'https://www.berkshirehathaway.com/subs/sublinks.html','publisher':'Berkshire Hathaway','retrieval_scope':'Official search-index extract used; subsequent open response not used after output truncation','accessed_on':DAY,'selected_facts':['The issuer subsidiary directory lists Precision Castparts Corp.'],'limits':'Not used to fill missing SPS-to-PCC legal-chain edges or to assert any percentage ownership on the award date.'}]
write('context-notes.json',web_notes)
nodes=[];edges=[]
def node(i,t,title,sids,props,status='documented_fact'):
 nodes.append({'id':i,'type':t,'title':title,'status':status,'source_ids':sids,'properties':props})
def edge(i,t,s,tgt,sids,props,status='documented_fact'):
 edges.append({'id':i,'type':t,'source':s,'target':tgt,'status':status,'source_ids':sids,'properties':props})
for s in sources:node(s['id'],'source',s['title'],[],{'url':s['url'],'accessed_at':DAY,'snapshot_path':s['snapshot_path'],'snapshot_sha256':s['snapshot_sha256']},'source')
node('TP-AWARD-W775','award','DLA purchase order SPE4A626PW775',['TP-S-ORDER','TP-S-AWARD'],{'piid':award['piid'],'signed_date':award['date_signed'],'solicitation_identifier':'SPE4A626Q0688','actual_payee':None,'delivery_verified':False,'fraud_conclusion':None})
for cage,tag in [('745V4','DON'),('27624','SPS')]:
 d=profiles[cage]
 node('TP-ORG-'+tag,'organization',d['name'],['TP-S-CAGE-'+tag,'TP-S-PROFILE-'+tag],{'cage':cage,'uei':d['uei'],'recipient_id':d['recipient_id'],'alternate_names':d['alternate_names'],'profile_location':d['location'],'profile_observed_on':DAY,'location_scope':'Recipient profile state/country; not delivery, production origin, or individual residence','beneficial_owner':None})
node('TP-ORG-BERKSHIRE','organization','BERKSHIRE HATHAWAY INC.',['TP-S-PROFILE-SPS'],{'uei':'UU26FKF1MML6','role':'reported parent in SPS federal recipient profile','observed_on':DAY,'ownership_percentage':None,'beneficial_owner':None})
node('TP-OFFICE-DLA-AVIATION','government_office','DLA AVIATION',['TP-S-AWARD'],{'subtier_name':'Defense Logistics Agency','subtier_code':'97AS','toptier_name':'Department of Defense','toptier_code':'097','individual_buyer':None})
node('TP-PERSON-OFFICER-W775','person','Joseph Felhauer — printed contracting/ordering officer',['TP-S-ORDER-ROLE'],{'public_record':True,'professional_role':'CONTRACTING/ORDERING OFFICER','role_date':'2026-07-09','identity_scope':'Printed name on this instrument only; no cross-record or same-name person merge','signature_execution_authenticated':False,'price_selection_authority_verified':False,'payment_authority_verified':False,'personal_benefit':None})
node('TP-PART-39-8820-501','part','P/N 39-8820-501',['TP-S-ORDER'],{'part_number':'39-8820-501','technical_equivalence_to_other_parts':None})
edge('TP-E-PRINTED-OFFICER','printed_contracting_ordering_officer','TP-AWARD-W775','TP-PERSON-OFFICER-W775',['TP-S-ORDER-ROLE'],{'effective_date':'2026-07-09','document_locator':'DD1155 page 1 block 24 area','signature_execution_authenticated':False,'price_selection_authority_verified':False,'payment_authority_verified':False,'personal_benefit':None})
edge('TP-E-DEALER','named_dealer','TP-AWARD-W775','TP-ORG-DON',['TP-S-ORDER'],{'effective_date':'2026-07-09','role_scope':'Contract names dealer; does not establish actual disbursement'})
edge('TP-E-RECIPIENT','public_award_recipient','TP-AWARD-W775','TP-ORG-DON',['TP-S-AWARD','TP-S-CAGE-DON'],{'effective_date':'2026-07-09','recipient_uei':'XN9HKU6LUM59','actual_payee_verified':False})
edge('TP-E-MANUFACTURER','contractually_intended_manufacturer','TP-AWARD-W775','TP-ORG-SPS',['TP-S-ORDER','TP-S-CAGE-SPS'],{'effective_date':'2026-07-09','part_number':'39-8820-501','delivery_verified':False,'supplier_invoice_verified':False})
edge('TP-E-SUPPLY','contractually_intended_supply_from','TP-ORG-DON','TP-ORG-SPS',['TP-S-ORDER'],{'award':'SPE4A626PW775','effective_date':'2026-07-09','part_number':'39-8820-501','actual_commercial_transaction_verified':False})
edge('TP-E-PART','stated_material','TP-AWARD-W775','TP-PART-39-8820-501',['TP-S-ORDER'],{'effective_date':'2026-07-09'})
edge('TP-E-OFFICE','awarding_and_funding_office','TP-AWARD-W775','TP-OFFICE-DLA-AVIATION',['TP-S-AWARD'],{'individual_price_selector':None,'individual_signatory':None,'payment_authorizer':None})
edge('TP-E-PARENT-SPS','federally_reported_parent','TP-ORG-SPS','TP-ORG-BERKSHIRE',['TP-S-PROFILE-SPS'],{'observed_on':DAY,'effective_start':None,'effective_end':None,'ownership_percentage':None,'beneficial_ownership_verified':False,'direct_intermediate_chain_verified':False})
edge('TP-E-PARENT-DON','federally_reported_self_parent','TP-ORG-DON','TP-ORG-DON',['TP-S-PROFILE-DON'],{'observed_on':DAY,'ownership_percentage':None,'beneficial_ownership_verified':False,'interpretation':'Self-parent reporting does not identify natural-person owners or show absence of affiliates.'})
write('graph.json',{'version':'1.0','as_of':DAY,'nodes':nodes,'edges':edges})
write('timeline.json',[
 {'date':'2026-07-09','event':'USAspending signed date for purchase order SPE4A626PW775; DLA contract names dealer and intended manufacturer.','source_ids':['TP-S-AWARD','TP-S-ORDER','TP-S-ORDER-ROLE'],'printed_officer':'Joseph Felhauer, CONTRACTING/ORDERING OFFICER; printed role only','temporal_limit':'Intended supply and obligation, not fulfillment or payment evidence.'},
 {'date':DAY,'event':'Exact CAGE searches connect both dealer/manufacturer names to their distinct UEIs.','source_ids':['TP-S-CAGE-DON','TP-S-CAGE-SPS'],'temporal_limit':'Observed registry state; not a complete registration history.'},
 {'date':DAY,'event':'USAspending profiles show Don self-parent and SPS reporting Berkshire Hathaway as parent.','source_ids':['TP-S-PROFILE-DON','TP-S-PROFILE-SPS'],'temporal_limit':'No ownership percentage or historical-effective interval supplied.'},
 {'date':'2028-04-10','event':'Reported period-of-performance end in the award record.','source_ids':['TP-S-AWARD'],'temporal_limit':'Scheduled performance date, not evidence that delivery or acceptance occurred.'}])
write('unresolved.json',{
 'beneficial_ownership':{'don':None,'sps':None,'reason':'Self-parent and federal reported-parent fields do not disclose a complete beneficial-owner chain or ownership percentages.'},
 'actual_payee':None,'actual_supplier_invoice_party':None,'actual_manufacturing_site':None,'actual_delivery_location':None,'invoice_unit_cost':None,'credits_rebates_discounts':None,'shipping_and_insurance_cost':None,'gross_margin':None,'kickback_or_personal_benefit':None,'printed_officer_role':'Joseph Felhauer, CONTRACTING/ORDERING OFFICER, printed date 2026-07-09; source TP-S-ORDER-ROLE; signature execution and price/payment authority unknown','buyer_employee':None,'contract_signatory':None,'price_evaluator':None,'payment_authorizer':None,
 'required_to_test_cost_markup':['Contemporaneous dealer purchase order and supplier invoice tied to the part, revision and order','Quantity/lead-time/first-article/packaging/freight reconciliation','Credits, returns and rebates tied to the same purchase','Government invoice, receiving/acceptance and payment records','Documented professional decision authority only if needed to interpret actual approvals'],
 'state_filing_candidate':{'document_number':'L10000120053','status':'not_merged','reason':'Exact name is insufficient without a retained authoritative state-to-federal identifier crosswalk. Profile state TX and candidate state filing FL are different scopes and not an identity contradiction or fraud signal.'},
 'unsupported_conclusions':['No proven 12% markup','No proven overpayment','No proof of kickback, fabricated supplier, impersonation or personal benefit','Printed professional officer role creates no allegation, price-selection inference or personal-benefit association']})
write('identity-decisions.json',[
 {'decision':'join','keys':['CAGE 745V4','UEI XN9HKU6LUM59'],'basis':['TP-S-ORDER','TP-S-CAGE-DON','TP-S-AWARD','TP-S-PROFILE-DON'],'limit':'Role is named dealer and public award recipient, not proven payment recipient.'},
 {'decision':'join','keys':['CAGE 27624','UEI E6KFWWNKEQ49'],'basis':['TP-S-ORDER','TP-S-CAGE-SPS','TP-S-QUERY-SPS','TP-S-PROFILE-SPS'],'limit':'Intended manufacturer for this order. Do not substitute another SPS site/CAGE.'},
 {'decision':'preserve_reported_relation','keys':['E6KFWWNKEQ49','UU26FKF1MML6'],'basis':['TP-S-PROFILE-SPS'],'limit':'Federal reported parent observed 2026-10-30, not beneficial-owner or payment-flow conclusion.'},
 {'decision':'do_not_merge','keys':['Florida L10000120053','CAGE 745V4'],'basis':['context-notes.json TP-CANDIDATE-FL'],'limit':'State filing remains candidate; no person from it is inserted into the award graph.'},
 {'decision':'do_not_merge','keys':['PB Fasteners','CAGE 27624'],'basis':['context-notes.json TP-COMPANY-PB'],'limit':'Issuer product/brand page lacks a retained identifier crosswalk; marketing name is not a substitute for contract identity.'},
 {'decision':'do_not_infer_ownership','keys':['DON INDUSTRIAL GROUP LLC','XN9HKU6LUM59'],'basis':['TP-S-PROFILE-DON'],'limit':'Self-parent does not identify beneficial owners.'}])
queries=[
 '"745V4" "Don Industrial" official',
 '"27624" "SPS" site:precast.com OR site:pccfasteners.com OR site:sec.gov',
 '"SPS Technologies" "Precision Castparts" site:pccfasteners.com',
 '"PB Fasteners" site:pccfasteners.com',
 '"SPS Technologies" "subsidiaries" site:sec.gov/Archives/edgar/data',
 '"Don Industrial Group" "owner"',
 '"DON INDUSTRIAL GROUP LLC" site:search.sunbiz.org',
 '"Precision Castparts" site:berkshirehathaway.com/2025ar']
opens=[
 {'url':company_url,'result':'opened; selected paraphrase retained'},
 {'url':'https://www.pccfasteners.com/companies/sps-technologies.php','result':'inaccessible; no fact adopted'},
 {'url':'https://www.spsfasteners.com/about/','result':'timeout; no current ownership fact adopted'},
 {'url':'https://www.pccfasteners.com/companies/pcc-fasteners/pb-fasteners.html','result':'opened; selected paraphrase retained'},
 {'url':'https://www.sec.gov/Archives/edgar/data/79958/000119312510130580/dex21.htm','result':'opened; target fact not inspected in rendered excerpt; no ownership fact adopted'},
 {'url':fl_url,'result':'open requested; output unavailable after truncation; official search-index observation only'},
 {'url':'https://www.berkshirehathaway.com/subs/sublinks.html','result':'open requested; output unavailable after truncation; official search-index observation only'}]
write('research-budget.json',{'as_of':DAY,'web_queries':queries,'web_query_count':len(queries),'web_open_attempts':opens,'web_open_count':len(opens),'direct_requests':len(load('acquisition_log.json')['requests']),'public_read_attempt_count':len(opens)+len(load('acquisition_log.json')['requests']),'max_web_queries':8,'max_public_reads':15,'counting_note':'Includes failed opens and ordinary CAGE consent/form requests. Existing parent local captures are reused without new public reads. No automatic retries.'})
try:commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
except Exception:commit=None
write('finding.json',{'task_id':'federal-price-pilot-parties-SPE4A626PW775','agent_id':'transaction_parties','input_commit':commit,'cohort':['SPE4A626PW775'],'source_ids':[s['id'] for s in sources],'direct_findings':['Exact official identifier chain connects named dealer Don to UEI XN9HKU6LUM59 and intended manufacturer SPS CAGE 27624 to UEI E6KFWWNKEQ49.','USAspending reports Berkshire Hathaway UEI UU26FKF1MML6 as parent of this SPS recipient profile; Don reports itself as parent.','DLA AVIATION is the public awarding/funding office.','Original order page 1 prints Joseph Felhauer as CONTRACTING/ORDERING OFFICER dated 2026-07-09; signature execution and price/payment authority are unverified.'],'inferences':[],'contradictions':[],'benign_alternatives_tested':['SPS comma/no-comma punctuation appears as a profile alternate name tied to the same UEI; no impersonation inference.','A dealer supplying an approved manufacturer is expressly described in the order; an intermediary alone does not establish wrongdoing.','Different state registry/profile geography can represent jurisdiction or location scope; no name-only merge.'],'missing_data':[k for k in load('unresolved.json') if k!='printed_officer_role'],'method':'Bounded original-order → exact CAGE → exact UEI → recipient-profile join; separate reported parents and candidate state filing. Selected captures hashed; original bytes not archived.','visibility':'public_business_role_evidence_no_novel_allegation','legal_status_if_case':'not_a_case_or_allegation','next_step':'Obtain cost/quantity/terms-matched invoice, credits, acceptance and payment evidence through an authorized source before assessing supplier markup or benefit.','review_status':'pending_independent_review'})
(R/'REPORT.md').write_text('''# SPE4A626PW775: documented parties and unresolved money trail

The award names a dealer and an intended manufacturer. Exact DLA CAGE searches independently connect both to federal UEIs. This establishes who the public records identify; it does not establish a hidden markup, improper payment or personal benefit.

| Role | Documented entity | Identifier | Evidence and date |
|---|---|---|---|
| Named dealer | DON INDUSTRIAL GROUP LLC | CAGE 745V4; UEI XN9HKU6LUM59 | DLA order page 2, signed date 2026-07-09; exact CAGE search observed 2026-10-30 |
| Public award recipient | DON INDUSTRIAL GROUP LLC | Recipient 516cae19-6195-34c1-0e8f-71a1fd4f3702-C | Exact USAspending award and recipient profile |
| Contractually intended manufacturer | SPS TECHNOLOGIES LLC | CAGE 27624; UEI E6KFWWNKEQ49 | DLA order page 2 states source for P/N 39-8820-501; exact CAGE/UEI match |
| Reported parent of SPS recipient | BERKSHIRE HATHAWAY INC. | UEI UU26FKF1MML6 | USAspending child profile observed 2026-10-30; no historical ownership interval or percentage established |
| Awarding/funding office | DLA AVIATION | DLA 97AS; DoD 097 | Exact USAspending award |
| Actual government payee | Unknown | — | Obligation/recipient data is not a disbursement ledger |
| Actual invoice supplier | Unknown | — | Contractually intended manufacturer is not an invoice or delivery record |
| Printed contracting/ordering officer | Joseph Felhauer | Role limited to this instrument | DD1155 page 1 block 24 area; printed date 2026-07-09; signature execution not independently authenticated |
| Individual price selector, authenticated signer or payment approver | Unknown | — | Printed officer role does not establish these decisions or authorities |

Don's profile reports Don itself as parent. That does not identify an owner or demonstrate that no affiliates exist. SPS's reported-parent relationship is preserved with its source and observation date; it is not expanded into an unsupported beneficial-owner chain. The SPS comma/no-comma name variation is explicitly reported as an alias under the same UEI.

The Florida filing L10000120053 is an unmerged candidate. An official search-index extract identifies a manager, but the state document has no retained federal-identifier crosswalk and the manager's transaction-date role is unverified. The candidate stays outside the award graph. No residential addresses, personal contacts, family relationships or private financial profiles are retained.

The supplier-cost test still requires the dealer's actual supplier invoice, matching quantity and specifications, credits/rebates, packaging/freight and first-article obligations. Government invoice, receiving/acceptance and payment records would establish whether the scheduled supply became an actual payment. No price margin or benefit is computed from a corporate-parent field.

The machine-readable evidence is in [graph.json](graph.json), [sources.json](sources.json), [identity-decisions.json](identity-decisions.json), [timeline.json](timeline.json) and [unresolved.json](unresolved.json). [Context notes](context-notes.json) distinguish inspected company pages from search-index-only candidate observations. [Research budget](research-budget.json) records eight queries and fifteen public-read attempts, including consent and failed requests. [Acquisition log](acquisition_log.json) pins direct response hashes; retained selected extracts have separate hashes. Original source bytes are not claimed to be archived.

Reproduce local checks with `python3 validate_parties.py` from this directory. A fresh acquisition is deliberately blocked from overwriting evidence; a later authorized run should use a new dated output directory. The CAGE form requests follow ordinary public consent, without retaining cookies or form tokens.
''')
# Pin all locally retained inputs/outputs except manifest and validation outputs.
items=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and p.name not in {'manifest.json','validation.json'}:
  items.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
write('manifest.json',{'as_of':DAY,'hash_scope':'Exact bytes of retained local artifacts, not a claim to archive full websites or original PDF','files':items,'upstream_source_files':[{'path':s['snapshot_path'],'sha256':s['snapshot_sha256']} for s in sources if s['snapshot_path'].startswith('../')]})
print(json.dumps({'sources':len(sources),'nodes':len(nodes),'edges':len(edges),'retained_files':len(items)}))
