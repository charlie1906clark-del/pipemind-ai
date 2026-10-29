# Enrollment-status audit — 29 October 2026

The current CMS revocation extract independently confirms administrative actions against both suppliers in the already published criminal cases. This is an enrollment-status finding; it does not establish a new criminal finding or calculate a recoverable loss.

| Official legal business name | Exact NPI | Enrollment ID | Revocation effective | Re-enrollment bar expiration |
|---|---|---|---|---|
| ND MEDICAL SOLUTIONS LLC | 1790533503 | O20241216000744 | 2025-04-23 | 2035-04-22 |
| CENTENNIAL MED SUPPLY LLC | 1609626167 | O20240710000183 | 2025-10-24 | 2035-10-23 |

Both records report `424.535(A)(8)(Ii) Abuse Of Billing Privileges: Pattern Or Practice`, and `MULTIPLE_NPI_FLAG=N`. The precise server-selected responses are in [known_case_matches.json](snapshots/known_case_matches.json); exact requests, retrieval times and response hashes are in [acquisition_manifest.json](acquisition_manifest.json). The independently verified NPPES/LEIE records are in the sibling `../identity/` investigation. An active NPI identifies a provider; it does not itself establish active Medicare billing eligibility. A revocation record does not establish an individual's criminal guilt.

## Freshness and source selection

The live [CMS data catalog](https://data.cms.gov/data.json) selected on 29 October 2026 identifies `Revoked Medicare Providers and Suppliers : 2026-09-01`, modified **2026-10-21**, with temporal metadata **2026-07-01 through 2026-09-30**. The stable series ID is `a6496a7d-4e19-479a-a9ad-d4c0a49e07c3`; the version-specific ID retrieved is `66acd4b6-e9ca-47bb-a7d6-fbd7c2f56e93`. The resource calls the extract Q3 2026 and the CSV filename is `Revocation_Extract_2026.10.21.csv`. These are separate source labels; none is treated as real-time status on 29 October.

An indexed API-documentation result still pointed to Q1 2026 and 7,059 rows; the HHS Open Data derivative describes a 14 February 2026 snapshot. Neither was used for the current intersection. See [catalog_selected.json](catalog_selected.json), [resources.json](resources.json), and the [CMS source page](https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revoked-medicare-providers-and-suppliers).

The [current resource-linked methodology](https://data.cms.gov/sites/default/files/2026-03/887c55c7-3dc1-4b14-aee5-970021b3b194/Revoked%20Medicare%20Provider%20and%20Supplier%20Methodology.pdf) requires an active bar and a first-level appeal that was exhausted or not timely filed. It warns about appeal-related publication lag, later status changes and other active enrollments under the same TIN. Absence from the list proves neither current enrollment nor eligibility. This March 2026 methodology supersedes the indexed February version that described an all-enrollments-inactive condition. Inclusion is not a representation that every further appeal is exhausted. The public record does not provide each supplier's appeal docket or a complete history of enrollment actions.

## National cohort intersection

Acquisition reconciled **8,620 main rows** against the API count and an explicit terminal empty page. All main enrollment×NPI keys are unique. There are 128 blank primary NPIs. All **94 companion additional-NPI rows** link to the main enrollment table. Joining them yields **8,714 enrollment×NPI rows** including blanks, and **7,462 distinct nonblank NPIs**. Additional identifiers are not additional enforcement actions. The selected main snapshot omits individual and organization names and contact details; names are retained only for the two exact known-case queries above.

The separate catheter audit covers 1,976 distinct supplier NPIs across A4351, A4352 and A4353 during 2022–2024. **64** intersect the current revocation snapshot. That is a descriptive exact-identifier overlap, not a fraud rate: this current-bar snapshot is not a historical census of revoked suppliers.

| Service year | Catheter supplier NPIs | Match current snapshot | Effective before year | Effective during year | Effective after year |
|---|---:|---:|---:|---:|---:|
| 2022 | 1,616 | 39 | 3 | 1 | 35 |
| 2023 | 1,520 | 47 | 4 | 1 | 42 |
| 2024 | 1,440 | 34 | 2 | 6 | 26 |

The pre-year subgroup spans four unique NPIs across the three years. Their records require enrollment-level reconciliation before any adverse interpretation. In 2024, the two pre-year matches are associated with **$1,923,512.54 of reconstructed annual PUF payment measure**. This amount is not established improper payments, money received after revocation, cash lost, savings, or a reward base. The NPI join does not prove that the billed enrollment was the revoked enrollment. Annual data lack individual service dates, cash-release dates, and suspension/escrow detail. The same-state match does not resolve that problem. No newly named suspected party is published from this subgroup.

Relation buckets count an NPI once within each bucket; an NPI with several revoked enrollments can appear in multiple buckets. The current results happen to partition the yearly counts, but downstream code must not assume that relationship in future extracts. Full code-level aggregate tables, cohort input hashes and validation outcomes are in [crosscheck.json](crosscheck.json).

A bounded follow-up checked the two 2024 pre-year matches against the official Q1, Q3 and Q4 2026 Public Provider Enrollment Files. Neither appeared as a primary NPI in those three snapshots. **Candidate A** did appear in the Q4 additional-NPI file, linked to a different approved enrollment for **Part B mass immunization, roster billing only**. Its revoked record is for DME pharmacy enrollment. This demonstrates a different-enrollment explanation for an apparently active status; the immunization enrollment does not establish authority to bill catheters. **Candidate B** had no exact Q4 additional-NPI match. The latest approved-enrollment extract is labeled Q4 2026, modified 19 October, with a 29 September extract filename. None of these 2026 snapshots resolves the enrollment used for 2024 services. No conclusively matching DAB appeal decision or enforcement report was identified in bounded name-and-domain searches. Similar-name results were rejected. Notice dates, appeal outcomes, any retroactive adjustment and actual post-revocation cash remain unknown for both. See [candidate_followup_summary.json](candidate_followup_summary.json) for source URLs, query templates, response hashes, explicit nulls and required next evidence. Exact candidate identifiers and filtered responses are kept outside this public report.

ND Medical has one released 2024 A4353 supplier row. Its reconstructed annual payment measure is $88,034,901.04, and its service year **precedes** the 2025-04-23 revocation date. The service year also precedes [DOJ’s alleged February 2025 start of Gugava’s purported ownership](../case-trace/REPORT.md); this row cannot establish his conduct in 2024. This is not evidence of payments after that date and must not be combined with DOJ amounts for a different period or different payment concept. Centennial has no rows in this three-code, three-year public cohort. Suppression, the limited period and the selected codes make that absence insufficient to establish no billing.

## Independent evidence about a related control gap

HHS-OIG report **A-02-24-01013** was **issued 2026-09-28 and posted 2026-10-01**; its PDF cover says September 2026. It examined 1,017 revoked NPIs absent from the Preclusion List during 2022–2023 and identified $72 million in Part C/D payments associated with 249 of them during 2022–2024. Of that total, $42 million concerned 12 pharmacy NPIs: CMS lacked preclusion authority to prohibit payment solely for filling prescriptions from eligible prescribers. Separate exclusion-related duties still applied. The brief also describes timing/errors and organizations whose owners had adverse actions. It makes no specific recommendations. This documents a separate preclusion-control issue, not a finding about the catheter suppliers or proof that all $72 million was fraud. The public revocation file is not the restricted plan Preclusion List.

Sources: [official report page](https://oig.hhs.gov/reports/all/2026/medicare-advantage-organizations-and-prescription-drug-plans-paid-72-million-during-a-3-year-period-for-services-associated-with-excluded-providers-or-individuals-convicted-of-certain-felonies/) and [PDF](https://oig.hhs.gov/documents/audit/11934/A-02-24-01013.pdf). Retrieval hashes and source HTML date elements are preserved in [supporting_sources.json](supporting_sources.json).

## Tests and next discriminating evidence

`python audit_enrollment.py` reruns the reconciliation from the stored sanitized snapshots and sibling catheter cohort. `python audit_enrollment.py --validate` checks snapshot and input hashes, paging/count reconciliation, companion joins, exact known-case identity and date-boundary logic offline. `python audit_enrollment.py --acquire` refreshes the official catalog and current extract before reconciliation; a future refresh can legitimately select a newer version, so retain the versioned manifest with any output.

The highest-value unresolved test is whether the four pre-year NPI matches billed through the revoked enrollment, a different valid enrollment, a retroactively adjusted enrollment, or corrected/withheld claims. It needs enrollment-specific effective/appeal history and claim-level service, adjudication and cash-release records. Public annual PUFs and current NPPES status cannot answer it. Public DAB decisions or subsequent agency publications may resolve a subset; record a negative result rather than treating absent public evidence as proof of misconduct. Do not add patients, private contact details or allegations based only on this join.
