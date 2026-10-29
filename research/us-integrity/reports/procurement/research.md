---
title: Procurement, defense, logistics and foreign-assistance research foundation
as_of: 2026-10-29
status: source_led_research_and_agent_specifications
new_fraud_cases_established: 0
---

# Procurement research foundation

This pack contains 37 primary-source records, eight published enforcement/audit benchmarks, one neutral buyer–award–vendor–parent trace, and 11 specialist-agent specifications. It does not claim to enumerate every buyer, vendor, invoice, shareholder or beneficial owner. Public data does not expose that universe. The benchmarks are already-public matters for validating research methods, not newly discovered reward opportunities.

## What is worth building first

The first useful product is a reproducible procurement evidence service: a bounded award universe; time-aware entity joins; source-backed relationships; anomaly explanations; and independent disconfirmation. A national accusation engine would amplify missing data, mismatched prices and ambiguous identities. A good first pilot asks one narrow question, such as whether publicly documented purchases of the same identifiable spare part show price differences that survive specification and contract-term review.

The order below is an engineering prioritization based on public observability, not a ranking of fraud prevalence:

| Track | First question | First obtainable evidence | Major stopping point |
|---|---|---|---|
| Standardized supplies and spares | Are comparable part purchases priced differently? | Public award actions, solicitations, PUB LOG item records | No line prices, incomparable configuration or controlled specifications |
| Set-aside eligibility and control | Do award-time eligibility and documented roles agree? | Award fields, SBA profiles, dated corporate records | Current profile cannot establish past control |
| Construction and maintenance | Are repeated bidding/variation patterns unexplained? | Public solicitations, bid tabs where released, modifications | Missing losing bids and approved-change detail |
| Services and IT | Do public commitments and accepted delivery evidence align? | Clauses, task orders, deliverable records where published | Internal time records and security evidence unavailable |
| Logistics and fuel | Are route/product/service equivalents comparable? | Public lots, shipment/tender documents where available | Shipment-level performance and authentication private |
| Foreign assistance | Can prime and reported subrecipient chains reconcile? | Public awards, reported subawards, OIG audits | Lower tiers, local records, security constraints |
| Major weapon/aerospace systems | Are pricing representations supportable? | Public contracts and enforcement disclosures | Proprietary cost data and engineering comparability |

## Current source changes that affect implementation

SAM is the current home for public contract-award search; FPDS ezSearch was decommissioned on February 24, 2026. A connector should follow the new service documentation and retain legacy IDs for historical joins. [PROC-S005](https://sam.gov/fpds)

The SAM Contract Awards API distinguishes public revealed data from restricted unrevealed data. Public DoD records have a 90-day signing delay; some parent fields are withheld from the revealed response. Quotas vary by account, and result caps require partitions. Do not interpret recent missing awards as concealment, or attempt to obtain restricted responses. [PROC-S006](https://open.gsa.gov/api/contract-awards/)

DLA PUB LOG is the public bulk catalog route. Version the layouts: DLA removed several distributed fields starting April 1, 2026. WebFLIS has controlled authentication, and DIBBS technical-data links can lead to restricted material; these are not unrestricted public feeds. [PROC-S010](https://www.dla.mil/Information-Operations/FLIS-Data-Electronic-Reading-Room/PUBLOGFLISSearchDownloadInstr/) [PROC-S011](https://www.dla.mil/Information-Operations/Services/Applications/WebFLIS/) [PROC-S012](https://www.dla.mil/Small-Business/Resource-Center/Training-Resources/Details/Article/4408730/dla-troop-support-clothing-textiles-supplier-pathway/)

A material documentation conflict exists. Treasury's October 6, 2026 data guide still states a blanket $30,000 subaward threshold. Current procurement FAR 4.1403 displays $40,000; FAR 52.204-10 ties reporting to the threshold at subcontract award time and contains exceptions. Assistance terms in 2 CFR 170 use $30,000. Store award type, award date, incorporated clause, exception and rule version; a single governmentwide threshold is unsafe. [PROC-S004](https://www.usaspending.gov/data/about-the-data-download.pdf) [PROC-S019](https://www.acquisition.gov/far/52.204-10) [PROC-S020](https://www.acquisition.gov/far/4.1403) [PROC-S033](https://www.govinfo.gov/content/pkg/CFR-2026-title2-vol01/xhtml/CFR-2026-title2-vol01-subtitleA-chapI.html)

## Buyer and supply-chain graph

Represent buyer functions separately. The funding agency, awarding agency, contracting office, intended recipient country, end user and site of performance can differ. Likewise a prime contractor is buying from a subcontractor; that subcontractor's general supplier may not appear in first-tier reporting. A graph must preserve each role rather than collapsing all of them into “buyer.”

| Stage | Recommended node types | Join/identity keys | Relationship evidence |
|---|---|---|---|
| Funding | Agency, Bureau, FederalAccount, Program | Published agency/office code, TAS where available | Funding-agency field, source award action |
| Procurement | Solicitation, Lot, Award, IDV, Order, Modification | PIID plus agency and parent IDV context; modification number | Award/solicitation document, action record |
| Prime | Organization, Facility | UEI, CAGE, legacy DUNS with validity interval | Recipient record and public entity record |
| First tier | Subaward, Organization | Prime award key, prime-assigned subcontract ID, subrecipient UEI | Reported subaward, contract document |
| Lower tier | SupplierAgreement, Organization | Publicly documented contract/reference only | Specific lawful public disclosure; otherwise unknown |
| Ownership | Organization, OwnershipAssertion | Registry ID, CIK, CAGE/UEI crosswalk | Dated official filing or explicit source statement |
| Goods/services | Product, Part, Specification, ServiceCategory | NSN/NIIN, part number plus manufacturer CAGE, revision | Public solicitation/catalog; no inferred equivalence |
| Locations | OfficeLocation, FacilityLocation, PerformanceLocation | Role-tagged country/state/county/city | The specific address field's stated meaning |
| Sales | RevenueObservation, ObligationAction, PaymentObservation | Entity scope, period, accounting basis, currency | Financial filing or published transaction |
| Oversight | Audit, LegalMatter, Recommendation, Resolution | Report number, docket, agency identifier | Specific official report or court/resolution document |

USAspending's API supports scoped award, transaction, recipient, subaward and download operations. Preserve its generated award key in addition to the source PIID; use identifier fields rather than company-name equality. [PROC-S001](https://api.usaspending.gov/) [PROC-S002](https://api.usaspending.gov/docs/endpoints) [PROC-S003](https://www.usaspending.gov/federal-spending-guide)

CAGE is facility-oriented: one corporate group may have multiple facility codes. SAM's public entity API can support corporate-relationship checks, but absent or self-reported ownership detail is not proof of deception. [PROC-S009](https://www.dla.mil/Working-With-DLA/Applications/Details/Article/2920893/cage-code-commercial-and-government-entity-code/) [PROC-S007](https://open.gsa.gov/api/entity-api/)

GAO's September 2026 release confirms limited beneficial-owner visibility. Officers, directors, nominees and registered agents are not interchangeable with ultimate natural-person owners. Record “unknown” explicitly; do not manufacture complete ownership chains from names or addresses. [PROC-S015](https://www.gao.gov/products/gao-26-108174)

## Sector paths and verification playbooks

### Defense supplies, spares, clothing and medical procurement

Follow contracting office → solicitation/lot → award/action → prime UEI/CAGE → publicly reported subcontract → manufacturer CAGE/part → delivered specification, if public. Keep equipment acquisition separate from maintenance support and component replacement. Start by selecting a narrow item family, agency and fiscal period; inspect all records in that defined cohort, including ordinary observations.

Candidate checks: repeated identical-item outliers, unexplained switches in manufacturer identifiers, missing required traceability documents, duplicate-looking award actions, and inconsistent public origin/specification statements. Each is a question, not a finding of deceit. Benign alternatives include unit-of-issue conversions, minimum lots, first-article tests, warranties, emergency delivery, obsolescence and freight.

FAR price-analysis guidance requires adjusting historical comparisons for material changes in terms, quantities and market conditions and obtaining technical advice for similar items. An online retail listing is not automatically a military-part comparator. [PROC-S018](https://www.acquisition.gov/far/15.404-1)

The C-17 audit is an appropriate benchmark for evidence completeness: it identified nearly $1 million overpayment in reviewed parts, while other price comparisons could not be resolved. It is an audit, not a determination of criminal fraud. [PROC-S025](https://www.dodig.mil/DesktopModules/ArticleCS/Print.aspx?Article=3948604&ModuleId=2907&PortalId=48)

### Aerospace and major defense systems

Follow program/contracting office → prime contract → modifications → identifiable systems/configurations → source-backed suppliers → pricing representation and technical baseline. Candidate questions concern data disclosed at negotiation, change order basis, duplicated charges and origin/qualification representations. An expensive system or large profit margin is insufficient evidence.

Technical peers must first decide whether the compared systems are equivalent. Public award ceilings cannot disclose all engineering, sustainment, classified components or proprietary cost detail. The specialist must stop at the evidence boundary, rather than infer a false certification.

Raytheon's 2024 resolutions include DPAs with admissions and separate civil components. They are a published method-testing benchmark; their combined amount cannot be reused as a single procurement-loss number. [PROC-S024](https://www.justice.gov/archives/opa/pr/raytheon-company-pay-over-950m-connection-defective-pricing-foreign-bribery-and-export)

### Construction, infrastructure and base maintenance

Follow public owner/funding agency → site/project → bid lot → prime → trade subcontractor → variation → certified work/acceptance, where those documents are released. Build cohorts around equivalent scope and tender conditions. Search for repeated bidder rotation, lot allocation, unusually similar bid documents and unexplained variation sequences. The relevant evidence is the bid and correspondence record, not merely similar totals.

Disconfirm against legitimate specialization, regional travel cost, common software, shared estimating services, approved teaming, weather and unforeseen conditions. Construction cost differences require quantities, specifications, programme and change-control context.

A December 2025 guilty plea concerned cover bids in military maintenance procurements administered by DLA. The source identifies approximately $6 million attributable commerce; that is not established loss. The company is not named there and must not be guessed. [PROC-S028](https://www.justice.gov/opa/pr/executive-north-carolina-construction-company-pleads-guilty-multi-million-dollar-bid-rigging)

### IT, cybersecurity, software and professional services

Follow buyer → framework/IDV → task order → prime → reseller/subcontractor → licensed product or accepted deliverable. Separate licenses, hardware, labor hours and outcomes. Candidate checks include inconsistent license counts, unsupported labor categories, overlapping invoices, false public compliance representations and subcontract steering. Public staffing or office-location information cannot determine whether an employee worked billed hours.

A cyber research agent reads contracts and disclosures; it does not scan contractor systems. Check the exact incorporated clause, assessed environment, representation date and authorized remediation. A control deficiency alone does not establish a knowingly false material claim.

Honeywell Aerospace's September 2026 $2,042,518 resolution expressly settled allegations without a liability determination. Booz Allen's $15.875 million simulator settlement likewise preserved that civil distinction. [PROC-S023](https://www.justice.gov/opa/pr/honeywell-aerospace-inc-agrees-pay-over-2m-settle-false-claims-act-allegations-failing) [PROC-S027](https://www.justice.gov/archives/opa/pr/booz-allen-agrees-pay-15875m-settle-false-claims-act-allegations)

### Small-business set-asides and control

Follow award → applicable program/NAICS → recipient legal entity → certification at relevant date → joint venture/mentor-protege terms → actual work and control evidence. Never infer ineligibility from company size today, a founder's absence from a website, a common address or an acquisition without examining applicable rules and dates.

SBA's Small Business Search supports UEI/CAGE discovery and program checks. Preserve dated evidence: today's search result cannot prove award-time eligibility. [PROC-S013](https://search.certifications.sba.gov/) [PROC-S014](https://www.sba.gov/contracting-officials/)

The June 2026 Broadway/Cornerstone resolution includes specific conduct admissions about control and pass-through arrangements. It is a benchmark for examining work/control evidence, not a reason to label all teaming or joint ventures improper. [PROC-S026](https://www.justice.gov/opa/pr/government-contractor-and-executives-pay-213m-resolve-fraud-scheme-involving-service)

### Logistics, fuel, freight and moving

Follow procuring activity → route/lot/service window → transportation prime → delivery agent/carrier → fuel/product specification → delivered quantity and performance record, when public. Normalize distances, capacity, security, season, fuel indices, storage and service guarantees. Potential duplicate invoices and extreme routing differences require shipment-level evidence before conclusions.

Performance-score anomalies require authenticity evidence. Denali's 2025 $3.5 million settlement concerned alleged survey falsification in military-moving allocation; the release expressly says no determination of liability. A company's public performance score alone cannot reproduce the government's evidence. [PROC-S029](https://www.justice.gov/usao-sdil/pr/transportation-company-agrees-settle-allegations-impersonating-military-members-obtain)

### Foreign assistance, reconstruction and security assistance

Separate grant, procurement, government-to-government support and FMS channels. Follow funding agency/program → implementer → reported subrecipient → local delivery partner → documented recipient/output. Country allocation is not the same thing as an overseas recipient-company payment. Compare award purpose, performance evidence, audits and independent public delivery records.

Watch role changes between prime and subcontractor, duplicated project budgets and unresolved questioned costs; test currency, security and reporting explanations first. Do not convert reconstruction waste, abandoned projects or all contract volume into criminal-fraud totals.

The Vistant/Apprio official releases document individual guilty pleas, corporate DPAs and later individual debarments. Prime/subcontract roles changed over time. The more than $550 million contract volume is not a loss or recovery estimate. [PROC-S030](https://oig.usaid.gov/node/7877) [PROC-S034](https://www.justice.gov/opa/pr/usaid-official-and-three-corporate-executives-plead-guilty-decade-long-bribery-scheme)

SIGAR's final review and USAID OIG's case index are oversight discovery sources, not a substitute for specific case evidence. [PROC-S031](https://www.sigar.mil/Portals/147/Files/Reports/sigar-final-report.pdf) [PROC-S032](https://oig.usaid.gov/our-work/investigations)

## Neutral trace already recorded

`neutral_trace.json` records Army Contracting Command, Redstone Arsenal → contract W31P4Q-24-C-0003 → Raytheon Company → RTX. Modification P00002 was announced at $946,446,735, with $463,758,900 obligated from FMS Romania funds. The work location was Andover, Massachusetts. No fraud allegation attaches to this award. The historical enforcement benchmark is deliberately not connected to this PIID. [PROC-S037](https://www.defense.gov/News/Contracts/Contract/Article/4016173/)

The DOJ named the subsidiary relationship in 2024, and RTX's SEC-filed year-end 2025 list corroborates the legal entity. This remains a dated corporate relationship; no ultimate person is inferred. The UEI/CAGE crosswalk and lower-tier chain are unresolved. [PROC-S035](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/exhibit212025-12x3110xk.htm)

The October 2026 issuer filing reports a Navy administrative agreement, continuing government-contract eligibility and an independent monitor. Store this response beside the historic resolution. Do not infer an active exclusion from a prior prosecution. [PROC-S036](https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/rtx-20260930.htm)

## Reproducible ingestion and analysis

1. Define the universe in a run manifest: fiscal/calendar date interpretation, agency/office scope, award/action type, geography role, classification filters, selected dataset versions and exclusions.
2. Query the USAspending API/documented download service in bounded partitions; save request payloads and response metadata. Fetch each source once per snapshot, honor quotas and use bounded retries with backoff.
3. Store raw bytes outside ordinary Git history, with digest, retrieval timestamp, source URL, content type and licensing/access notes. This research pack currently stores reviewed source metadata and passages, not archived original bytes.
4. Normalize IDs and dated entity relationships; keep raw values. Quarantine uncertain name matches. Keep modifications and negative obligations; never sum IDV ceilings with child order obligations.
5. Join only identifier-confirmed records, or preserve explicit candidate matches. Reconcile subaward duplicates and links before generating an anomaly. Missing coverage gets a coverage status, not a zero or accusation.
6. Produce a peer cohort and method card for each comparison. Use explainable statistics and minimum sample rules chosen before inspecting entities; disclose multiple-comparison effects.
7. Route candidate observations to an independent skeptic. Require benign explanations, contradictions, missing records and a next verification step.
8. Export source, entity, relationship, case and lead notes to Obsidian. A note for a hypothesis must never masquerade as an adjudicated fact.

Exclusions are a separate dated legal/administrative record. Use identifier and period matching; a name-only hit remains unresolved. [PROC-S008](https://open.gsa.gov/api/exclusions-api/)

Company revenue, stock trading, contract obligations, invoices, cash payments and a contract ceiling are distinct measures. GSA SRP is a controlled vendor reporting portal, so public documentation cannot be treated as access to every line of private sales data. [PROC-S021](https://www.gsa.gov/sell-to-government/step-1-learn-about-government-contracting/how-to-access-contract-opportunities/help-with-mas-contracts-to-sell-to-government/transactional-data-reporting/help-with-tdr)

## Specialist-agent contracts

`agents.json` defines procurement-universe, defense-spares, aerospace-pricing, construction-integrity, cyber-compliance, services-labor, set-aside-control, logistics/fuel, foreign-assistance, temporal-ownership and skeptic roles. These are specifications, not deployed autonomous agents. Each must emit facts, inferences, contradictions, missing evidence, exact sources and next verification separately.

The same model cannot promote and approve its own lead. A human review queue must block all filings, subject contact, public accusations, requests for nonpublic records and reward claims. Legitimate public source acquisition and internal note creation can run within the declared scope.

Recommended acceptance checks:

- A 2024 owner edge cannot silently become current ownership.
- Different part revisions or units fail the price-comparability gate.
- A missing subcontract yields `coverage_unknown` until reporting obligations and source completeness are established.
- An audit finding never becomes `criminal_fraud` through summarization.
- A settlement without admission retains that status on every note and graph edge.
- A historical enforcement matter does not taint unrelated awards of the same vendor.
- Peer reports cite exact source IDs and record queries so another researcher can reproduce the result.
- Source duplicates cannot inflate amounts or corroboration counts.

GAO's fraud-risk work supports systematic control assessment; DOJ's Procurement Collusion Strike Force describes analytics as a way to find signs warranting investigation. Neither makes public-data outliers proof of fraud. [PROC-S016](https://files.gao.gov/reports/GAO-25-108500/index.html) [PROC-S017](https://www.gao.gov/products/gao-20-106) [PROC-S022](https://www.justice.gov/atr/procurement-collusion-strike-force)
