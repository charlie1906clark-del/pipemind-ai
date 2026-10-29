# Healthcare public-funds research foundation

Researched: 2026-10-29. Scope: United States federal/state healthcare payments and public provider records.

## What this research actually establishes

This is a source-led research and detector-design foundation: 31 official source records, 10 existing enforcement/audit examples, and 9 healthcare workstreams. No bulk claims dataset has yet been ingested, no new case of fraud has been established, and no universal buyer/owner inventory has been completed. Public reimbursement data can support ranked questions; most clinical necessity, consent, delivery, intent and bank-transfer questions require further lawfully obtained evidence.

Every existing case here is a historical reference or calibration example. Settled allegations, specific admitted facts, charges, convictions, administrative exclusions and audit recommendations remain separate. An announcement of intended loss, a submitted charge, an agreed settlement, a restitution order and collected money are different financial measures.

## Recommended order

1. **DME supplier/service longitudinal pilot:** bound to one code family and 2–3 verified comparable years; start with national provider cohorts to avoid presuming a region is guilty. Rank abrupt billing changes, then resolve only the top reviewed entities.
2. **Medicaid provider-month pilot:** first retrieve HHS dictionaries and payment definitions. Include state, payment method and revision controls before using a growth score.
3. **Post-acute ownership pilot:** reconcile dated PECOS enrollment/ownership snapshots and produce a provenance-complete owner chain for a bounded provider cohort.
4. **Laboratory billing pilot:** public aggregates may identify concentration; same-patient/same-day test combinations and medical necessity remain blocked pending authorized records.
5. **MA, PBM and VA contract research:** high materiality but weaker public transaction visibility. Build policy/contract evidence and documented ownership paths before claiming detection coverage.

## Role and identity rules

- Government procuring office, healthcare payer, plan administrator, billing provider, rendering clinician, referring practitioner, wholesaler and manufacturer are different node roles.
- NPI identifies a healthcare provider record. It does not verify licensure, prove ownership, identify a bank account or serve as a universal corporate identifier. [HC-S06]
- PECOS ENROLLMENT ID, provider ASSOCIATE ID, owner ASSOCIATE ID, NPI and CCN are different keys. Use supported enrollment crosswalks; never join all-owner rows directly on an assumed NPI column. [HC-S09]
- Separate supplier and referring-provider aggregates do not expose a direct referral-to-supplier transaction. A shared HCPCS code is not an edge.
- Match exact official IDs first. Name/address similarities create candidate links with review state, not accepted identity or ownership facts.
- Preserve effective dates and observation dates on ownership, exclusion, enrollment and corporate changes. Current owner/status cannot be backdated.
- Keep public professional identity only as necessary for the business role. Do not ingest patient identities, SSNs, personal bank details or residential locations.

## Current evidence examples

| ID | Published record | Status | Amount meaning |
|---|---|---|---|
| HC-C01 | Eleven DMEPOS suppliers precluded by CMS | administrative_preclusion; suspected_billing_not_adjudicated | $3,400,000,000 suspected_billed_amount |
| HC-C02 | 2025 National Health Care Fraud Takedown / Operation Gold Rush | criminal_charges_alleged; aggregate_not_convictions | $14,600,000,000 aggregate_alleged_intended_loss |
| HC-C03 | Labcorp urine drug test-panel settlement | civil_settlement_with_specified_admitted_facts | $14,500,000 settlement_agreed |
| HC-C04 | Aetna risk-adjustment settlement | civil_settlement_resolving_allegations | $117,700,000 settlement_agreed |
| HC-C05 | Physicians Toxicology Laboratory and owners | civil_settlement_no_liability_determination | $4,425,000 settlement_agreed |
| HC-C06 | Creative Hospice entities referral settlement | civil_settlement_of_allegations | $9,200,000 settlement_paid_as_reported |
| HC-C07 | Opnet / P & P Health Care Services owner sentenced | jury_conviction_and_sentence_reported | $400,000 billed_amount_over; $360,000 paid_amount_over |
| HC-C08 | Labelle Home Health owner sentenced | jury_conviction_and_sentence_reported | $5,700,000 restitution_ordered |
| HC-C09 | VA Community Care Network outpatient and dental audit | audit_control_and_contract_findings_not_fraud_determination | $108,900,000 questioned_costs_metadata; $980,300,000 better_use_of_funds_metadata |
| HC-C10 | Walgreens controlled-substance settlement | civil_settlement_no_liability_determination | $300,000,000 base_settlement_agreed; $50,000,000 conditional_additional_settlement |

These examples are already publicly reported. They must not be represented as newly discovered, summed across parent/component cases, or used to imply guilt for other entities sharing a sector or location.

## Workstreams and specialist auditor contracts

### HC-01 — Original Medicare Part B and medical practice billing

**Money and commercial path:** CMS Medicare trust funds → Medicare Administrative Contractor → enrolled billing practitioner/group → rendering practitioner or downstream laboratory/supplier.

The federal payer reimburses care; the patient is not the federal procurement buyer. Rendering and billing identities can differ.

**Join plan**

- Retain NPI as a ten-character string and validate check digit. Keep Type 1 individual and Type 2 organization separate.
- Join NPI to the same observation-period NPPES snapshot; retain taxonomy and professional practice state.
- Compare by HCPCS, place of service, specialty, calendar year, regional payment conditions and available risk/case-mix proxies.
- Resolve group ownership through explicit enrollment/registry evidence; never infer ownership from a shared practice address.

**Candidate tests and refutation**

- **Signal:** Abrupt rise in units or paid amount for a narrow HCPCS family. **Benign explanations:** practice acquisition; new specialist service; coding or fee-schedule changes; demand/case-mix shift. **Evidence needed:** Prior-year records, dictionary comparability, paid-vs-submitted amount, enrollment history and a validated peer cohort.
- **Signal:** Provider appears on exclusion data and billing aggregates. **Benign explanations:** same-name different person; reinstatement; service dates predate exclusion; payment adjustment after permitted service. **Evidence needed:** Exact identity, exclusion effective/reinstatement dates and actual dates of service; annual aggregates alone cannot prove prohibited billing.

**Limits**

- No patient-level identity or clinical record in public aggregates.
- Part B FFS is not the full US health market.
- Annual aggregates cannot establish impossible daily workloads, forged signatures or deliberate misrepresentation.

**Specialist role:** Claims-methodology auditor: reject invalid cohorts, enforce amount semantics and flag only reproducible aggregate anomalies.

**Sources:** HC-S05, HC-S06, HC-S17, HC-S18.

### HC-02 — DMEPOS, catheters, orthotics and medical supply distribution

**Money and commercial path:** CMS FFS through MAC OR MA plan → DMEPOS billing supplier → commercial wholesaler/distributor → device manufacturer.

A billed supplier is not necessarily the manufacturer or federal contract vendor. Reimbursement does not expose its wholesale purchase invoice.

**Join plan**

- Use supplier NPI + HCPCS + rental indicator + service year as aggregate grain.
- Create separate records for referring-provider and supplier datasets. They are marginal aggregates; shared HCPCS does not establish a direct referrer-to-supplier transaction.
- Use NPI business identity and explicit corporate filings to trace registered entity/parents. Record each unsupported upstream manufacturer or beneficial-owner link as unknown.
- Version enrollment, deactivation, revocation and exclusion as different statuses with effective dates. A billing transition to another payer requires payer-specific data.

**Candidate tests and refutation**

- **Signal:** New or acquired supplier shows an extreme catheter billing increase relative to peers. **Benign explanations:** valid acquisition; consolidated billing; coding changes; new service territory. **Evidence needed:** Longitudinal supplier rows, valid acquisition source, product mix, beneficiary-count denominator and payer-specific data.
- **Signal:** Several suppliers share an officer/address and similar billing shocks. **Benign explanations:** legitimate chain; shared billing service; mailing office; registered agent. **Evidence needed:** Explicit ownership/control records and distinct contemporaneous entities; cluster is a lead, not conspiracy proof.

**Limits**

- Public aggregate data cannot establish delivery, beneficiary death, consent or medical necessity.
- Commercial supplier-to-wholesaler/manufacturer sales are usually not public.
- 2026 suspected billing cannot be confirmed with a 2024 aggregate dataset.

**Specialist role:** DME coding and network auditor: compare product-specific longitudinal cohorts and distinguish NPI/provider enrollment changes from legal-entity ownership changes.

**Sources:** HC-S01, HC-S02, HC-S03, HC-S04, HC-S05, HC-S06, HC-S17.

### HC-03 — Medicaid/CHIP, managed care, behavioural health and home/community services

**Money and commercial path:** Federal/state Medicaid funds → state Medicaid agency → FFS provider OR capitated managed-care organization → billing/servicing provider → staffing or other subcontractor.

State expenditure, MCO capitation, provider reimbursement and managed-care encounter value are different measures and must not be summed as independent spending.

**Join plan**

- Retrieve HHS HCPCS, NDC and enrollment extracts, schema, suppression and revision documentation before querying.
- Preserve billing NPI, servicing NPI and prescribing NPI as distinct roles. Add state, month and code-system version where fields support it.
- Validate cross-state/method comparability and managed-care encounter amount definitions; do not assume an encounter paid amount equals a state payment.
- Join provider enrollment segments temporally, keeping state-specific enrollment identifiers and spans.

**Candidate tests and refutation**

- **Signal:** Rapid provider-month growth in behavioural health or personal-care units. **Benign explanations:** expanded state eligibility; rate increase; new covered benefit; backlogged submissions; MCO reporting changes. **Evidence needed:** State benefit/rate chronology, claim revisions, enrollment spans, code dictionaries and comparable states/regions.
- **Signal:** Same provider has apparent high hours per month. **Benign explanations:** group NPI billing many staff; unit duration differs; institutional bundled payments. **Evidence needed:** Provider role, unit semantics, staffing evidence and appropriately authorized service records; public aggregate totals cannot prove impossible individual hours.

**Limits**

- T-MSIS is state-submitted and has completeness/comparability limitations.
- Suppression prevents reconstructing small cells.
- No patient identities; do not attempt reidentification or deceased-beneficiary joins.
- Managed-care subcontract and staffing contracts may be unavailable.

**Specialist role:** Medicaid state-policy auditor: condition every rule on state, year, programme and payment method; route missing definitions to blocked-data status.

**Sources:** HC-S11, HC-S12, HC-S13, HC-S17, HC-S29.

### HC-04 — Pharmaceutical supply, Part D prescribing, PBMs and rebates

**Money and commercial path:** CMS Part D subsidies and other payer contributions → Part D plan sponsor → PBM and affiliated group purchasing organization → dispensing pharmacy → wholesaler → manufacturer.

Drug acquisition, dispensing reimbursement, prescribing and rebate flows are distinct. Public Part D drug cost is not net federal spending, pharmacy revenue or manufacturer realized price.

**Join plan**

- Use prescribing NPI + brand/generic drug + year for Part D; NDC-bearing Medicaid data has a different grain.
- Preserve NDC format and package/product meaning; do not coerce away leading zeros or infer drug equality from string similarity.
- Use explicit corporate evidence for PBM/plan/pharmacy/manufacturer ownership and effective dates.
- Open Payments linking needs the current file layout and validated recipient crosswalk; do not assume every release exposes NPI. Keep payments, research and ownership as separate relations.

**Candidate tests and refutation**

- **Signal:** Very high brand share or spend per standardized fill in matched peers. **Benign explanations:** specialty patient mix; clinical contraindication; formulary requirements; different dosage/packaging; gross-vs-net price differences. **Evidence needed:** Drug identity, days supply, specialty, formulary/year and rebate limitations.
- **Signal:** Payment relationship and unusual prescribing co-occur. **Benign explanations:** lawful research; consulting; education; common specialty manufacturer relationship. **Evidence needed:** Actual agreement, timing, services and a legally supported inducement theory. Correlation is insufficient.

**Limits**

- Manufacturer rebates, PBM spread contracts and net prices often confidential.
- Part D prescriber tables do not identify every dispensing pharmacy transaction.
- FTC competition proceedings are not automatically criminal or FCA findings.

**Specialist role:** Drug-pricing and formulary auditor: normalize drug/packaging/payment measures and challenge gross-cost versus net-cost mistakes.

**Sources:** HC-S13, HC-S14, HC-S15, HC-S16, HC-S30, HC-S31.

### HC-05 — Clinical laboratories, urine drug tests and genetic testing

**Money and commercial path:** CMS/MAC or Medicaid/MCO → billing laboratory → ordering practitioner and potential marketer/MSO → reference lab or testing subcontractor.

An ordering physician is not automatically an owner or procurement buyer; an advertised test brand does not uniquely identify the billing laboratory.

**Join plan**

- Resolve NPI and CLIA certificate separately, using explicit crosswalk or corroborated location/legal name and certificate dates.
- Compare CPT/HCPCS families with site-of-service and year-specific billing rules; preserve modifiers when available.
- Record marketers/MSOs only if documented; never convert a co-located company into a financial intermediary.

**Candidate tests and refutation**

- **Signal:** High same-family test intensity or spending concentration. **Benign explanations:** specialist addiction/toxicology practice; legitimate confirmatory testing; reference-lab referrals. **Evidence needed:** Coverage policy, ordering data, actual test panel, medical record and patient-specific indication under lawful access.
- **Signal:** Ownership distributions correlated with referrals. **Benign explanations:** bona fide investment returns; actual services under compliant arrangement. **Evidence needed:** Contract/distribution/referral evidence and legal review; public association alone cannot establish a kickback.

**Limits**

- Aggregate NPI/code totals cannot show same-patient same-day testing combinations.
- CLIA certificate quality status is not Medicare billing approval or fraud determination.
- Medical necessity and intent require additional records.

**Specialist role:** Laboratory coding and CLIA auditor: require precise panel/code/date evidence and separate admitted facts from settlement allegations.

**Sources:** HC-S01, HC-S18, HC-S19, HC-S24, HC-S26.

### HC-06 — Telehealth, lead generation and remote prescribing

**Money and commercial path:** Medicare/Medicaid or plan → billed practitioner/lab/DME supplier → telehealth platform → marketing/lead generation vendor → owners/management.

The platform can be a vendor, a clinical group or a billing entity; never assume these roles are interchangeable.

**Join plan**

- Preserve practitioner NPI, platform legal entity, billed supplier and marketer as distinct nodes.
- Use only explicit contracts/case records to connect lead seller and provider.
- Version telehealth place-of-service/payment rules and distinguish authorized telehealth expansion from misconduct.

**Candidate tests and refutation**

- **Signal:** DME/lab billing growth accompanies remote ordering concentration. **Benign explanations:** lawful remote care programme; centralized specialty service; changes to coverage. **Evidence needed:** Validated ordering linkage, encounter evidence and consent documentation; marginal aggregates cannot prove a path.
- **Signal:** Unusual volume associated with a new telehealth group. **Benign explanations:** group NPI/many clinicians; seasonal volume; acquisition. **Evidence needed:** Role-correct numerator, denominator and clinician capacity evidence.

**Limits**

- Call recordings, patient consent, identity theft and AI-generated consent records are not available in public spending tables.
- No scraping patient/social accounts or trying to impersonate beneficiaries.

**Specialist role:** Telehealth rule and consent-evidence auditor: distinguish legal remote care from source-supported conduct; block unsupported consent conclusions.

**Sources:** HC-S01, HC-S02, HC-S06, HC-S18.

### HC-07 — Hospice, home health and skilled nursing ownership networks

**Money and commercial path:** CMS Part A / Medicaid / other programme → enrolled facility or home-care agency → staffing/management company → parent/chain/investor.

Patient referral, agency enrollment, facility operation and real-estate ownership are separate relations.

**Join plan**

- Use ENROLLMENT ID and ASSOCIATE ID to join PECOS ownership rows to the matching enrollment dataset; obtain NPI/CCN from that supported crosswalk.
- Keep owner ASSOCIATE ID distinct from provider ASSOCIATE ID and NPI.
- Represent ownership percentage, role, association date and snapshot date; sum percentages only where ownership layer and definitions permit.
- Recurse through evidenced organization owners; a self-reported intermediate owner is not proven ultimate beneficial ownership.

**Candidate tests and refutation**

- **Signal:** Rapid facility enrollment or ownership turnover and unusual service patterns. **Benign explanations:** legitimate chain acquisition; corporate restructuring; expansion to meet demand. **Evidence needed:** Snapshots/filings, provider operational dates, payment/quality denominators and explicit acquisition evidence.
- **Signal:** Hospice and separate provider payments may overlap. **Benign explanations:** unrelated condition or permitted separate benefit; adjustment timing. **Evidence needed:** Patient/service-level records and hospice coverage rules; aggregate overlap alone is not duplicate billing.

**Limits**

- Current ownership snapshot can misrepresent the historical owner.
- Self-reported ownership may be incomplete or late.
- Public service aggregates cannot establish terminal prognosis, homebound status, forged signatures or actual staff attendance.
- Enhanced-oversight states are control jurisdictions, not a list of culpable providers.

**Specialist role:** Post-acute ownership and eligibility auditor: version every ownership edge and require authorized clinical evidence before eligibility conclusions.

**Sources:** HC-S07, HC-S08, HC-S09, HC-S10, HC-S20, HC-S21, HC-S27, HC-S28.

### HC-08 — Medicare Advantage risk adjustment and delegated vendor networks

**Money and commercial path:** CMS risk-adjusted capitation → Medicare Advantage organization → delegated provider group / HRA or coding vendor → corporate parent.

Capitation is an insurer payment, not reimbursement for one specific billed clinical service; chart review and care delivery can be performed by different entities.

**Join plan**

- Keep contract/plan/year and parent organization effective dates; do not infer plan ownership from brand alone.
- Preserve diagnosis submission/deletion, HRA and encounter origins if lawfully available.
- Use public audits/settlements as typology evidence; do not pretend public NPI aggregates include underlying risk adjustment records.

**Candidate tests and refutation**

- **Signal:** Risk-adjustment payment rises without corresponding service pattern in authorized data. **Benign explanations:** true morbidity increase; benefit/coding/model change; care underuse; data incompleteness. **Evidence needed:** Validated diagnosis encounter histories, HCC model/year, deletion records and clinical documentation.

**Limits**

- Public sources rarely expose complete enrollee diagnosis chains or HRA-vendor contracts.
- OIG HRA-only payment estimates include alternative care-quality explanations and are not fraud loss estimates.

**Specialist role:** Risk-adjustment evidence auditor: require correct model/version, supported diagnosis/deletion facts and legal-status precision.

**Sources:** HC-S22, HC-S25.

### HC-09 — VA community care, prosthetics and medical procurement

**Money and commercial path:** VA/VHA → third-party administrator OR direct procurement vendor → community care provider / distributor → medical-device manufacturer / corporate parent.

CCN claim reimbursement and a VA purchase order are different procurement/payment paths. Contract-compliant margins can be a policy weakness without being fraud.

**Join plan**

- Identify CCN region, administrator contract, payment period and applicable rate hierarchy.
- Trace actual award identifiers via the procurement system separately from NPI-based community-provider records.
- Keep contract price, provider invoice and VA reimbursement measures separate; source the contract clause governing each.

**Candidate tests and refutation**

- **Signal:** VA reimbursement exceeds provider invoice. **Benign explanations:** contract expressly permits rate-based reimbursement; administration fees; different invoice scope. **Evidence needed:** Executed contract and modifications, governing fee schedule, invoice and payment reconciliation.
- **Signal:** Medical procurement price above catalogue/reference price. **Benign explanations:** sterility/quality specification; quantity; freight; emergency delivery; warranty; different unit. **Evidence needed:** Item/NSN/UDI if available, comparable terms, quantities and period; no price-only fraud conclusion.

**Limits**

- Patient-level VA claims and commercial upstream invoices usually restricted.
- Questioned costs and recommendations for better use of funds are not recoveries.
- 2025 audit found most outpatient payments accurate; selecting only negative findings would distort evidence.

**Specialist role:** VA contract-rate auditor: reconstruct the contract/rate hierarchy and challenge false fraud labels for permitted terms.

**Sources:** HC-S23.

## Evidence-supported ownership examples

**PTL → Lund Capital Group:** DOJ expressly describes Lund Capital Group LLC as PTL’s grandparent. Store `has_grandparent`; do not invent the missing direct parent, ownership percentage or contemporary beneficial owner. [HC-S26]

**Paul Njoku → Opnet → P & P:** DOJ describes Njoku as owner/CEO of Opnet and Opnet as doing business as P & P Health Care Services. Store ownership and trade name as different relations and use the underlying conduct period. [HC-S28]

## Research acceptance gates

1. Dataset manifest contains actual vintage, grain, units, coverage, suppression, revision handling and a content digest of the fetched bytes. Catalogue availability alone does not pass ingestion.
2. Every accepted identity/ownership edge has an exact source locator and temporal scope; unresolved candidates remain unmerged.
3. Every detector emits an explanation, a peer definition, a counterexample/benign explanation and a required-evidence checklist.
4. Each high-scoring candidate undergoes independent refutation review before becoming a lead. A lead is not a legal finding.
5. Legal-status and financial-measure validation reject labels that turn suspected billing or better-use recommendations into proven fraud or recovered money.
6. Historical-case calibration uses known legal status as-of the model cutoff. No training/test leakage from later enforcement records.
7. No source-specific suppressed cells are reconstructed by differencing or joining; no patient reidentification.
8. No automatic complaints, accusations, contacts, filings or public publication. Separate reviewed evidence packages from raw anomaly ranking.

## Source index

- **HC-S01** [National Health Care Fraud Takedown Results in 324 Defendants Charged in Connection with Over $14.6 Billion in Alleged Fraud](https://www.justice.gov/index.php/opa/pr/national-health-care-fraud-takedown-results-324-defendants-charged-connection-over-146) — DOJ; accessed 2026-10-29. Charges and intended loss, not convictions or recoveries. Broad takedown record; do not double count its component cases.
- **HC-S02** [CMS Cracks Down on Massive $3.4 Billion Medical Equipment Supplier Fraud Scheme](https://www.cms.gov/newsroom/press-releases/cms-cracks-down-massive-3-4-billion-medical-equipment-supplier-fraud-scheme) — CMS; accessed 2026-10-29. Eleven suppliers precluded; suspected billed amounts. Source excerpt identifies no supplier names. Do not infer defendants or owners.
- **HC-S03** [Medicare Durable Medical Equipment, Devices & Supplies - by Supplier and Service](https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service) — CMS; accessed 2026-10-29. NPI, HCPCS, rental indicator; final-action FFS Part B claim aggregates. Small-count suppression. Search index and live JavaScript landing page differ in available detail; resolve version from metadata before ingestion.
- **HC-S04** [Medicare DME supplier and service official catalog metadata](https://catalog.data.gov/dataset/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service-da750) — HHS / Data.gov; accessed 2026-10-29. Catalog lists series endpoint https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data and coverage through 2024. Endpoint discovered, not fetched or validated in this research.
- **HC-S05** [NPPES Data Dissemination](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) — CMS; accessed 2026-10-29. Official monthly replacement and weekly incremental files; self-reported provider data; deactivation rules. Raw file exceeds 4GB uncompressed.
- **HC-S06** [NPPES NPI Registry](https://npiregistry.cms.hhs.gov/) — CMS; accessed 2026-10-29. NPI issuance is not license or credential verification. API and bulk alternatives. Current directory is not a historical ownership record.
- **HC-S07** [Hospital All Owners](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-all-owners) — CMS; accessed 2026-10-29. PECOS self-reported ownership names, roles and dates. Does not establish completeness of ultimate beneficial ownership.
- **HC-S08** [Home Health Agency All Owners](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners) — CMS; accessed 2026-10-29. PECOS self-reported ownership. Quarterly snapshots; preserve observed and effective dates.
- **HC-S09** [Home Health Agency All Owners API documentation](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners/api-docs) — CMS; accessed 2026-10-29. Search result lists ENROLLMENT ID, ASSOCIATE ID, ASSOCIATE ID - OWNER, role and percentage fields. Q4 2026 version identifier 87e65a9e-3695-4b48-bd5c-4d5f4dfc7f08. Live open returned JavaScript shell; latest version must be revalidated on fetch.
- **HC-S10** [Hospice All Owners official catalog metadata](https://catalog.data.gov/dataset/hospice-all-owners-2026-04-02) — HHS / Data.gov; accessed 2026-10-29. Ownership name/type/effective date; provider enrollment identifiers and data dictionary must be read before joins. Catalog snapshot has April 2026 version, not a guarantee of latest data.
- **HC-S11** [HHS Open Data provider catalogue](https://opendata.hhs.gov/dataset/medicaid-provider-spending) — HHS; accessed 2026-10-29. Observed catalogue lists Medicaid HCPCS spending (2018-2024), NDC spending, provider enrollment segments and revoked Medicare providers. Bulk download and exact schema still need retrieval.
- **HC-S12** [Medicaid Provider Spending by HCPCS](https://opendata.hhs.gov/datasets/medicaid-provider-spending/) — HHS; accessed 2026-10-29. Official catalogue describes provider/HCPCS/month aggregates covering FFS, managed care and CHIP. Detail page was JavaScript shell in retrieval. Validate definitions, revisions, negative adjustments and suppression before use.
- **HC-S13** [Medicaid Provider Spending by NDC](https://opendata.hhs.gov/datasets/medicaid-provider-spending-ndc/) — HHS; accessed 2026-10-29. Official catalogue describes billing NPI, prescribing NPI, NDC, claim month. It does not expose each patient, invoice, rebate or bank transfer.
- **HC-S14** [Medicare Part D Prescribers - by Provider and Drug](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug) — CMS; accessed 2026-10-29. Latest indexed year 2024. NPI/brand/generic aggregated fills and total drug cost. Total drug cost includes multiple payers; it is not solely federal expenditure.
- **HC-S15** [Medicare Part D Prescribers methodology](https://data.cms.gov/sites/default/files/2026-05/MUP_DPR_RY26_20260421_Methodology_508.pdf) — CMS; accessed 2026-10-29. Suppresses provider-drug records with 10 or fewer claims. Annual aggregation cannot show specific patient duplication or prescription validity.
- **HC-S16** [Open Payments Data Overview](https://www.cms.gov/priorities/key-initiatives/open-payments/data) — CMS; accessed 2026-10-29. General/research payments and physician ownership interests; reports lawful relationships too. A payment or holding alone is not a kickback. Some publication can be delayed.
- **HC-S17** [LEIE Database and Supplement Downloads](https://www.oig.hhs.gov/exclusions/leie-database-supplement-downloads/) — HHS OIG; accessed 2026-10-29. Monthly active exclusions; reinstated entries removed. Do not use name-only matches as confirmed identity or current status to infer historic exclusion.
- **HC-S18** [NPI/HCPCS/place-of-service practitioner aggregate metadata](https://catalog.data.gov/dataset/medicare-physician-other-practitioners-by-provider-and-service-f9cd9) — HHS / Data.gov; accessed 2026-10-29. Public NPI/service/place-of-service aggregates; catalog discovers endpoint https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data . Endpoint not yet fetched.
- **HC-S19** [CLIA Laboratory Performance](https://www.cms.gov/medicare/health-safety-standards/clinical-laboratory-improvement-amendments-clia/laboratory-performance) — CMS; accessed 2026-10-29. QCOR search by CLIA certificate/facility/location/type/expiry. CLIA certification and payment NPI are different identities; do not join by similar name alone.
- **HC-S20** [Hospice oversight portfolio](https://oig.hhs.gov/reports/featured/hospice/) — HHS OIG; accessed 2026-10-29. Summarizes care quality, enrollment and billing vulnerabilities. Portfolio is risk evidence, not a finding against every hospice.
- **HC-S21** [Hospice Medicare fee-for-service compliance](https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/medical-review-education/hospice) — CMS; accessed 2026-10-29. Enhanced oversight began in AZ CA NV TX; GA/OH added Dec 30 2025 according to current page. Geography is a programme control, not proof about providers or residents.
- **HC-S22** [Medicare Advantage health risk assessments evaluation OEI-03-23-00380](https://www.oig.hhs.gov/reports/all/2024/medicare-advantage-questionable-use-of-health-risk-assessments-continues-to-drive-up-payments-to-plans-by-billions/) — HHS OIG; accessed 2026-10-29. Estimated $7.5bn 2023 risk-adjusted payments linked to HRA-only/HRA-linked diagnoses; concern includes inaccurate diagnoses OR missing needed follow-up. Not a fraud loss estimate.
- **HC-S23** [VA Community Care outpatient payments audit 23-00748-28](https://www.vaoig.gov/reports/audit/community-care-network-outpatient-claim-payments-mostly-followed-contract-rates-and) — VA OIG; accessed 2026-10-29. Most outpatient payments followed rates. Estimated rate overpayments and dental reimbursement contract issue; distinguish questioned costs, better use of funds and legal contractual payments.
- **HC-S24** [Labcorp $14.5m FCA settlement](https://www.justice.gov/opa/pr/labcorp-agrees-pay-145m-resolve-false-claims-act-allegations) — DOJ; accessed 2026-10-29. Specified admissions about test-panel billing; settlement allegations and admitted conduct require separate claims. No newly discovered case.
- **HC-S25** [Aetna $117.7m FCA settlement](https://www.justice.gov/opa/pr/aetna-agrees-pay-1177-million-resolve-false-claims-act-allegations) — DOJ; accessed 2026-10-29. Risk adjustment diagnoses; settled allegations. Retrieve agreement for exact admissions, releases and payment allocation before any further legal characterization.
- **HC-S26** [Physicians Toxicology Laboratory and owners settlement](https://www.justice.gov/usao-wdmi/pr/2025_0103_physicians_toxicology_laboratory_settlement) — DOJ; accessed 2026-10-29. PTL/Lund Capital and former president/individual co-defendants; $4.425m; no determination of liability.
- **HC-S27** [Creative Hospice $9.2m kickback settlement](https://www.justice.gov/usao-ndga/pr/mahlega-abdsharafat-and-creative-hospice-settle-health-care-kickback-claims-92-million) — DOJ; accessed 2026-10-29. Settled referral compensation allegations. Ownership/role only as explicitly described by DOJ; no inference against other affiliates.
- **HC-S28** [Opnet home health agency owner sentenced](https://www.justice.gov/usao-sdtx/pr/home-health-agency-owner-sentenced-more-six-years-medicare-fraud-and-identity-theft) — DOJ; accessed 2026-10-29. Conviction and 75-month sentence; falsified medical records; stated billed and paid totals are separate.
- **HC-S29** [Labelle owner sentenced for Medicaid fraud](https://www.justice.gov/usao-sdoh/pr/home-health-care-companies-owner-sentenced-more-3-years-prison-57-million-medicaid) — DOJ; accessed 2026-10-29. Conviction, 42 months, $5.7m restitution ordered; not evidence restitution has been collected.
- **HC-S30** [Walgreens opioid and FCA settlement](https://www.justice.gov/usao-edny/pr/walgreens-agrees-pay-350-million-illegally-filling-unlawful-opioid-prescriptions-and) — DOJ; accessed 2026-10-29. Base $300m plus conditional $50m, ability-to-pay settlement; source explicitly states allegations only/no liability determination.
- **HC-S31** [FTC PBM insulin case docket 221-0114](https://www.ftc.gov/legal-library/browse/cases-proceedings/221-0114-caremark-rx-zinc-health-services-et-al-matter-insulin) — FTC; accessed 2026-10-29. Docket includes ESI Feb 2026 and Caremark July 2026 settlement materials. Competition/unfair practices case, not automatically FCA fraud. Proposal/final order status must be checked from underlying instrument.
