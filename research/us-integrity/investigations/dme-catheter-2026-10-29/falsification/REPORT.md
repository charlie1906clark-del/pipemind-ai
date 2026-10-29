# DME catheter investigation: independent falsification review

Review date: 2026-10-29. Role: independent methodology and disconfirmation reviewer. Scope: public records; no beneficiary records, private payer ledgers, restricted CMS files, or investigative access were obtained. This review does not establish a new fraud case or identify an uncharged supplier as fraudulent.

## Decision

Continue the reproducible 2022–2024 supplier cohort analysis as a **screening and data-quality exercise**, and use published enforcement cases to test its coverage. An abrupt A4353 increase is a reason to investigate, not a fraud determination. The latest eleven precluded suppliers are a poor public-data identification target: CMS does not name them in the September 2026 release, their cited billing starts after the current supplier data period, and the Preclusion List is not public. The Gold Rush secondary-payer mechanism is specific and documented, but already known to government; its continuing existence after new controls is unproved.

The strongest actionable research question is: **Does an exact-identifier supplier trend remain unexplained after release, suppression, code-mix, payment-basis, ownership-timing, and known-enforcement checks?** No answer should be forced to be positive.

## Source findings that constrain the hypothesis

**F01 — Claims are not a cash ledger.** GAO reports that suspended claims can appear approved downstream while payment is withheld. GAO found at least $196,000 of combined federal/state Medicaid cost sharing paid to fifteen suppliers during 2023–2024 suspensions; private-payer estimates were not exact. Suspension-report sharing began in December 2025/January 2026. Consequently, the historical sharing failure is supported; a present October 2026 failure is an open question. [S1, section “CMS Has Begun to Inform Supplemental Payers of Payment Suspensions,” paragraphs 1–8.]

**F02 — An official correction matters.** CMS’s final rule clarified that payments had been stopped, so previously described recoupments were unnecessary. Suspended approved amounts could still affect ACO calculations. The rule removes all relevant A4352/A4353 amounts from specified CY2023 Shared Savings Program calculations. It does not determine every supplier fraudulent or state that these records were removed from the public supplier file. [S2, PDF p.5 footnotes 1–2; p.32 response to “across all suppliers”; §425.670.]

**F03 — The historical spike was already investigated.** CMS’s case study reports fifteen suppliers with recent ownership changes, more than 99% of suspect payments stopped, and over $4.2 billion prevented as of July 6, 2024. Its determination used order, delivery, and beneficiary evidence absent from the public aggregate file. Rediscovering that spike is not discovering a new recoverable loss. [S3, pp.1–2.]

**F04 — Ownership opacity is real, but not an adverse finding about a particular owner.** OIG describes difficulty detecting unreported ownership changes and imperfect state data. Appendix A repeats allegations about over thirty purchased suppliers and $941 million received from Medicare **and** secondary payers in Gold Rush. Do not label that entire sum federal loss or assume the fifteen historical suppliers, thirty-plus charged-network suppliers, and eleven 2026 suppliers are identical sets. [S4, printed pp.4–5 and 16 (PDF pp.5–6 and 18).]

**F05 — Recent, specific, but not publicly identified.** CMS’s September 8, 2026 release describes eleven suppliers, more than $3.4 billion of suspected 2025–2026 billing, and a Florida catheter example whose payments were stopped. No company names or NPIs appear. CMS’s FAQ states that the Preclusion List is not public. Public exclusion, enrollment, and NPI files are different populations and cannot fill that identity gap by assumption. [S5, paragraphs beginning “As part” and “All 11”; S6, Q44.]

The Preclusion List restriction is not a statement that every revocation record is private. The companion enrollment review is checking the newer public revoked-provider dataset. A public revoked-provider record can establish the record's stated administrative status; it does not by itself match a supplier to the unnamed eleven.

**F06 — Improper payment and fraud differ.** OIG’s catheter audit concerns July 2021–June 2022 and documentation/coverage compliance. It found 15 sample errors, 88 compliant items and two non-reviewed items treated as non-errors. This supports testing orders, delivery, eligibility and refill documentation; it does not supply intent evidence against a new supplier. [S7, “What OIG Found.”]

**F07 — The newer $72 million preclusion audit is not $72 million of established fraud.** OIG A-02-24-01013 examines 2022–2024 plan payments associated with 249 of 1,017 revoked NPIs. Its $72,004,603 total includes $42,021,169 for twelve pharmacy NPIs where current rules did not prohibit filling eligible prescriptions. The remaining table categories concern timing/errors and organizational ownership rules. This is a separate vulnerability analysis, not evidence identifying the eleven catheter/DME suppliers. The report also notes a reinstatement-check procedure introduced in March 2024. [S10, printed pp.6–8 (PDF pp.8–10), table and footnote 32.]

## What the public supplier file can establish

The current linked methodology covers final-action FFS DME-MAC claims and separate supplier/referrer aggregates. Its demographics are from NPPES at the end of the year following the service year. It excludes Medicare Advantage, is not risk adjusted, retains statistical outliers, and warns about claim errors, suppressed small cells and cross-file timing. Its suppression descriptions differ: §3 says small beneficiary groups are excluded, whereas the limitations/dictionary distinguish small claim rows and suppressed beneficiary counts. Preserve this ambiguity. [S8, §§1–5.]

| Public field or grain | Permitted analytical use | Unsupported conclusion |
|---|---|---|
| `Suplr_NPI` with reporting year | Match an exact identifier across releases | Same historical owner, criminal controller, or all related companies |
| `HCPCS_CD`, `Suplr_Rentl_Ind` | Compare like codes and rental status | Same clinical indication or complete modifier mix |
| `Tot_Suplr_Clms`, `Tot_Suplr_Srvcs` | Compare counts and units separately | One service equals one claim, visit, shipment or person |
| `Tot_Suplr_Benes` | Denominator where reported | Missing value equals zero; sum across codes equals unique people |
| Average submitted charge | Multiply by service units for reconstructed charge measure | Government expenditure, cash transferred, or loss |
| Average allowed amount | Reconstruct allowed measure | Medicare alone paid the whole amount |
| Average Medicare payment | Reconstruct the dictionary’s Medicare payment measure | Bank settlement, unrecovered loss, liability, or reward value |
| Average standardized amount | Geography-adjusted comparison | Actual revenue or a real remittance amount |
| Name, city, state, ZIP | Identify the recorded business location | Place of every service, residential location, common owner or conspiracy |

Dictionary locations and exact multiplication definitions: [S9, pp.1–3]. Do not multiply the average payment by claim count. Preserve decimal precision and label multiplied results as reconstructed aggregates. The dictionary describes its payment variable as paid; GAO alone does **not** establish that every PUF payment value is withheld. The file has no suspension, disbursement, refund, recoupment, or ultimate-loss reconciliation fields.

The public schema has no beneficiary identifiers, individual service dates, physician-order documents, delivery proof, bank flows, purchase invoices, secondary insurer/payment records or ownership percentages. Supplier and referring-provider tables are separate marginal aggregates: matching code, ZIP and year does not create a referral or transaction edge. Manufacturer sales and trading cannot be inferred from Medicare reimbursement totals.

## Falsification tests required before escalation

| Alternative explanation | Concrete test | Result that reduces suspicion |
|---|---|---|
| Threshold crossing or missing page | Verify API count, pagination, duplicates, rental key, and null semantics; preserve raw files | Apparent new entrant was suppressed or omitted earlier |
| Wrong amount or denominator | Recompute average × services; compare charges, allowed, payment and standardized separately | Large charges with modest allowed/payment or unit-count mistake |
| Legitimate acquisition or consolidation | Exact NPI/entity identifiers plus dated corporate filings and public acquisition disclosures | Growth follows documented transfer of an existing customer base |
| Code substitution or patient-mix change | Compare A4351/A4352/A4353 units, beneficiaries and share together; consult contemporaneous code rules | Family-level totals stable while code mix changes |
| Price/geography/modifier change | Compare standardized and actual measures, rate-year and geographic cohort; note unobserved modifiers | Growth mainly price/mix rather than extra utilization |
| Revised claims or release corrections | Compare same-year snapshots and release metadata, not just service years | Spike changes materially with release version |
| Already stopped or charged activity | Exact identifier match to dated official cases, suspensions and judgments | Pattern reproduces a known intervention, not a new lead |
| An innocent coding/documentation error | Seek published correction, audit or adjudication; retain alternative explanation | Error established without deceptive intent |

Tests are analytical proposals, not findings that a benign explanation has occurred. Conversely, inability to find a public explanation is not proof that none exists. A small business may legitimately lack SEC disclosures. Mail-order supply can separate business and beneficiary geography. Corporate registered agents are not automatically owners. Current NPPES contacts cannot establish ownership during prior service years.

No amount of annual aggregation establishes impossible daily workload. No shared street, name, code or lawyer independently establishes control. No public-data anomaly establishes that beneficiaries were deceased or that equipment was not delivered; those require separate source evidence.

## Avenue scores

Ordinal research judgments, 1 = weak and 5 = strong. “Novelty” means the prospect of a new, supportable fact from the available evidence, not likelihood of fraud. Scores are neither calibrated probabilities nor allegations.

| Avenue | Specificity | Public observability | Novelty | Actionability | Decision |
|---|---:|---:|---:|---:|---|
| Eleven suppliers precluded in 2026 | 3 | 1 | 1 | 2 | Track new named releases/appeals; do not guess identities from state and dollar totals |
| 2023–2024 supplier cohort, with 2022 baseline | 3 | 5 | 2 | 4 | Best reproducible public analytical pilot; quantify limits and test false positives |
| Published Gold Rush secondary-payer network | 5 | 3 | 1 | 3 | Best documented mechanism/case map; separate defendants, payers, allegations, dates and sums |

The cohort wins on immediate reproducibility, not novelty or guilt. The public network can validate whether a detector finds known cases, but this is not a sensitivity estimate unless the set of observable known suppliers is complete. Missing known cases may reflect coverage, suppression, dates or identifiers, not a successful concealment finding. A model tuned on Gold Rush must be evaluated on a separate cohort before claiming predictive performance.

## Workable next questions and stop conditions

1. Reproduce the same-year/code/rental totals and metadata. Record exact counts and discrepancy explanations before ranking entities.
2. Test the leading trend against at least two plausible alternatives. Use exact identifiers and dated public ownership evidence; label unresolved matches explicitly.
3. Cross-check whether named entities are already within government action. Store public novelty separately from anomaly severity and money size.
4. For the secondary-payer issue, search official material after January 2026 for actual implementation, timeliness, rejected crossovers and residual losses. New sharing is not proof of effectiveness, but historical failure is not proof of continuing failure.
5. Close or downgrade an unsupported lead when an alternative explains it. Escalate only a narrowly described unresolved question with source provenance, reproducible calculations and contradictory evidence preserved.

A submission-ready case would need evidence linking a specific false representation, accountable actor, payer, actual payment and unresolved loss. This review does not have that chain. Research should remain persistent about resolving questions, including exculpatory findings; it must not be persistent about producing a predetermined accusation.

## Independent check of the actual cohort analysis

I independently recalculated the saved 6,870 selected CMS rows without importing the audit script. All nine cohort payment totals, weighted unit averages, exact-key uniqueness checks and top-ten shares agree with `data-audit/analysis.json`. All six year-pair decompositions, two cross-code entry controls, and nine national payment reconciliations agree. Snapshot and final reviewed-script hashes plus results are in `data_review.json`.

For A4353, the reconstructed public payment measure is $39.18 million in 2022, $3.057 billion in 2023, and $1.154 billion in 2024. The 2022–2023 change separates into approximately $3.01785 billion for 83 newly visible NPI/code/rental rows, $1.59 million growth for 249 matched rows, minus $1.26 million for 73 no-longer-visible rows. This supports describing a concentrated change in the visible cohort. It does not establish 83 newly formed businesses or 83 fraudulent suppliers. The $100,000-baseline matched subgroup's median growth is 0.30%; that subgroup is selected and cannot describe every supplier.

The A4353 top-ten share rises from 46.88% in 2022 to 92.65% in 2023 and 96.88% in 2024. These shares describe the public cohort's reconstructed payment measure, not an industry-wide sales market or share of fraud. A4352's measure also grows sharply in 2023; together with CMS's rule, this rules it out as an unaffected negative control. A4351 is a useful adjacent-code comparison, not a validated causal control.

Of the 83 NPIs newly visible for A4353 in 2023, 44 already appeared in the previous year's A4351/A4352 cohorts. Of 55 newly visible in 2024, 33 previously appeared in those adjacent codes. This directly falsifies interpreting every new A4353 row as a new business. Supplier-detail A4353 payment coverage relative to the unsuppressed national table is 95.84%, 99.94% and 99.85% for 2022, 2023 and 2024 respectively. National and detail amounts are both reconstructed from rounded published averages.

The script properly uses service units rather than claims to reconstruct amounts, keeps monetary bases separate, avoids treating observed entries/exits as openings/closures, and does not sum beneficiary counts as unique people. No material arithmetic defect was found. Exact matching to known enforcement remains a separate workstream; these validated public aggregates cannot certify cash disbursement or original fraud discovery.

## Primary-source register

- **S1:** GAO-26-107799, published March 30 / released April 21, 2026. [Full report](https://files.gao.gov/reports/GAO-26-107799/index.html). Locator: “CMS Has Begun to Inform Supplemental Payers of Payment Suspensions,” particularly paragraphs beginning “According to CMS officials, when providers,” “Prior to December 2025,” and “In addition, based on our analysis.”
- **S2:** CMS-1799-F, final rule scheduled September 27, 2024, effective October 15, 2024. [Official PDF](https://public-inspection.federalregister.gov/2024-22054.pdf). Locators: PDF p.5 footnotes 1–2; pp.21–22 section II.B; p.32 response to “across all suppliers”; final §425.670(c)–(e). [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/final-rule-mitigating-impact-significant-anomalous-and-highly-suspect-billing-activity-medicare).
- **S3:** CMS, “Urinary Catheter Case Study: CMS’ Swift Action Saves Billions.” [PDF](https://www.cms.gov/files/document/cpi-urinary-catheter-case-study.pdf). Locators: p.1 investigation, payment stops and revocations; p.2 beneficiary complaints. Amount cutoff July 6, 2024; publication date not independently established here.
- **S4:** HHS-OIG OEI-02-24-00311, August 2026, “The Nation’s Challenge to Combat Durable Medical Equipment Fraud in Medicare.” [PDF](https://oig.hhs.gov/documents/evaluation/11855/OEI-02-24-00311.pdf). Locators: Chapter 1 printed pp.4–5 (PDF pp.5–6); Appendix A printed p.16 (PDF p.18). Allegations in Appendix A are attributed to DOJ, not new findings by this project.
- **S5:** CMS, September 8, 2026. [Eleven-supplier release](https://www.cms.gov/newsroom/press-releases/cms-cracks-down-massive-3-4-billion-medical-equipment-supplier-fraud-scheme). Locators: first two substantive paragraphs; Florida and Texas examples. Status: administrative action and suspected billing, not a criminal judgment.
- **S6:** CMS, “Preclusion List Frequently Asked Questions,” updated March 21, 2025. [PDF](https://www.cms.gov/medicare/provider-enrollment-and-certification/medicareprovidersupenroll/downloads/preclusion_list_faqs.pdf). Locators: Q44 (public availability); Q34 (possible retroactive reinstatement); Q36 (identifier matching). [Current information page](https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/chain-ownership-system-pecos/preclusion-list).
- **S7:** HHS-OIG, “Medicare Improperly Paid Suppliers for Intermittent Urinary Catheters,” 2025. [Report page](https://oig.hhs.gov/reports/all/2025/medicare-improperly-paid-suppliers-for-intermittent-urinary-catheters/). Locators: “Why OIG Did This Audit”; “What OIG Found”; “What OIG Recommends.”
- **S8:** CMS, “Medicare Durable Medical Equipment, Devices & Supplies Methodology,” June 2025, linked in current 2024 dataset resources. [PDF](https://data.cms.gov/sites/default/files/2025-06/a837dcf7-3d06-4c1f-8d4a-82ee737b7932/MUP_DME_RY25_Methodology_20250617_508.pdf). Locators: p.3 §§1–3; p.4 §4.1; pp.5–6 §5. Dataset resource manifest retained by the data audit agent; document vintage is older than 2026 data release.
- **S9:** CMS supplier/service dictionary, footer June 18, 2025, linked in current dataset resources. [PDF](https://data.cms.gov/sites/default/files/2025-06/9d983215-a36b-4089-9683-c50b150dfef2/MUP_DME_RY25_Data-Dictionary_20250617_suphpr_508.pdf). Locators: p.1 identifier/location; p.2 rental and beneficiary fields; p.3 claims/services and monetary fields.
- **S10:** HHS-OIG A-02-24-01013, September 2026, “Medicare Advantage Organizations and Prescription Drug Plans Paid $72 Million During a 3-Year Period for Services Associated With Excluded Providers or Individuals Convicted of Certain Felonies.” [PDF](https://oig.hhs.gov/documents/audit/11934/A-02-24-01013.pdf). Locators: printed p.6 scope and pharmacy matching; printed p.7 payment table; printed p.8 footnote 32. Plan payments, federal capitation and provable recoverable fraud loss are distinct measures.

The companion `evidence_records.json` preserves discrete claims, exact locators, legal status and inference limits for graph ingestion. Numeric results are derived from the separate data-audit snapshots and independently recalculated as recorded above.
