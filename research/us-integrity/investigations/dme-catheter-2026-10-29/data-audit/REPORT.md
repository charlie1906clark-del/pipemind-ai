# Catheter supplier data audit, 2022–2024

**Status:** completed descriptive acquisition and analysis; no new fraud determination. Retrieved 29 October 2026. Scope: CMS Medicare fee-for-service DME supplier/service and national geography/service public data for A4351, A4352 and A4353. This is a bounded national cohort, not a census of every US medical-supply transaction or buyer.

The strongest result is a reproducible structural break in A4353, concentrated in NPIs newly visible for that code. The publicly available supplier detail's reconstructed Medicare-payment measure increased from **$39.18 million in 2022 to $3.057 billion in 2023**, then declined to **$1.154 billion in 2024**. This supports prioritising the documented catheter problem for deeper reconciliation. It does **not** establish that these amounts were released in cash, represent unrecovered losses, or belong to previously unidentified fraudsters.

## Acquisition actually completed

- Nine complete **available public** supplier/code/year cohorts: **6,870 rows**. Each query's filtered `found_rows` matched the rows acquired; an explicit request at the next offset returned an empty page.
- Exact longitudinal keys: supplier NPI string, service year, HCPCS, rental indicator. No fuzzy-name joins. Every acquired catheter row has rental indicator `N`.
- Fifteen columns selected by CMS before transfer. Supplier names, streets, cities, ZIPs, contact details and patient records are absent from the retained cohorts. NPI is retained as the exact public professional/business identifier; no new named anomaly ranking is published.
- Three JSON dictionaries, current catalogue period mappings, resource links, and the linked PDF dictionary/methodology were inspected. Selected-response, canonical-row, local-snapshot and schema hashes have explicit scopes in the manifests. A selected response hash is **not** a hash of the full original CMS CSV.
- Nine national code/year rows acquired independently from the geography/service table, providing a comparison that includes records absent from supplier detail.
- Offline validation passed for hashes, row counts, key uniqueness, selected schema, minimum claim count, terminal pages and aggregate coverage. Live catalogue validation confirmed all six supplier/national dataset-year mappings.

## Measures and supplier-detail results

The dictionary prescribes `Tot_Suplr_Srvcs × Avg_*` to reconstruct totals. Calculations use decimal arithmetic and round only the final display. Submitted charges are billing amounts. Allowed amounts include Medicare, beneficiary and third-party responsibility. The payment field is the dataset's Medicare-payment measure. Standardised payment adjusts geography. These are different measures and are never added together.

Amounts below are **millions of USD**, reconstructed from published averages. Supplier counts refer to visible rows for each code; the same NPI may appear in several codes and years.

| Year | Code | Visible suppliers | Services/units | Submitted | Allowed | PUF payment | Standardised payment |
|---|---|---:|---:|---:|---:|---:|---:|
| 2022 | A4351 | 1,483 | 72,681,873 | 332.620 | 152.106 | 114.823 | 121.171 |
| 2022 | A4352 | 567 | 46,266,852 | 478.564 | 341.169 | 265.585 | 281.648 |
| 2022 | A4353 | 322 | 6,004,669 | 77.287 | 51.240 | 39.177 | 39.037 |
| 2023 | A4351 | 1,382 | 78,751,615 | 443.456 | 179.360 | 135.455 | 143.518 |
| 2023 | A4352 | 586 | 111,301,088 | 1,130.958 | 905.158 | 705.045 | 740.387 |
| 2023 | A4353 | 332 | 429,227,298 | 4,082.796 | 3,904.855 | 3,057.363 | 3,131.913 |
| 2024 | A4351 | 1,297 | 68,738,868 | 426.310 | 160.150 | 120.819 | 128.281 |
| 2024 | A4352 | 569 | 29,730,699 | 356.667 | 245.161 | 188.688 | 200.514 |
| 2024 | A4353 | 332 | 156,793,666 | 1,559.220 | 1,483.828 | 1,153.543 | 1,165.228 |

A4351 is a straight intermittent catheter; A4352 is the curved-tip variant; A4353 includes insertion supplies. The precise source descriptions are retained in every cohort. Their prices and units are not interchangeable.

## What changes after matching exact suppliers

For each adjacent year pair:

`Total change = change among matched rows + current amount in newly visible rows − prior amount in no-longer-visible rows`.

This identity reconciles exactly before display rounding. New visibility means appearance in this published code cohort, **not** incorporation, first Medicare participation, ownership change or business opening.

| Code | Years | Total PUF-payment change | Matched rows | Newly visible rows | No longer visible rows | Median growth among matched suppliers with prior payment ≥$100,000 |
|---|---|---:|---:|---:|---:|---:|
| A4351 | 2022→2023 | +17.97% | 1,197 | 185 | 286 | +3.50% |
| A4352 | 2022→2023 | +165.47% | 468 | 118 | 99 | +3.97% |
| A4353 | 2022→2023 | +7,704.07% | 249 | 83 | 73 | +0.30% |
| A4351 | 2023→2024 | −10.80% | 1,126 | 171 | 256 | −1.14% |
| A4352 | 2023→2024 | −73.24% | 460 | 109 | 126 | +5.38% |
| A4353 | 2023→2024 | −62.27% | 277 | 55 | 55 | −4.24% |

For **A4353, 2022→2023**, the exact decomposition in USD is:

- Total increase: **$3,018,186,282.67**.
- Matched-row increase: **$1,592,634.97**.
- Current amount in 83 newly visible rows: **$3,017,853,044.53**.
- Prior amount in 73 no-longer-visible rows: **$1,259,396.83**.

The newly visible contribution is 99.99% of the net increase; this is a decomposition, not a causal attribution. Of those 83 NPIs, **44 were already visible in A4351 or A4352 in 2022**, accounting for $157,010,549.98 of their 2023 A4353 measure. The remaining 39 were absent from all three prior code cohorts and account for $2,860,842,494.55. They may still have had other services or suppressed prior activity.

For **A4353, 2023→2024**, newly visible rows contribute **$719,886,501.97**, matched rows decrease **$335,602,355.73**, and disappearing rows had **$2,288,103,681.56** in 2023. Of the 55 newly visible NPIs, 33 had another comparator code in 2023; the other 22 account for $719,223,542.69. These observations warrant dated ownership and claim-status checks, not a public accusation.

## Concentration and comparator checks

| Year | Code | Median supplier PUF payment | Largest 5 suppliers' share | Largest 10 suppliers' share | Rows with suppressed beneficiary count |
|---|---|---:|---:|---:|---:|
| 2022 | A4351 | $6,356.10 | 51.63% | 60.91% | 1,092 |
| 2022 | A4352 | $20,300.19 | 73.21% | 80.03% | 398 |
| 2022 | A4353 | $24,320.40 | 35.13% | 46.88% | 235 |
| 2023 | A4351 | $7,099.09 | 52.47% | 63.35% | 997 |
| 2023 | A4352 | $21,722.93 | 84.13% | 90.51% | 405 |
| 2023 | A4353 | $31,997.54 | 62.80% | 92.65% | 230 |
| 2024 | A4351 | $7,797.89 | 52.83% | 61.80% | 899 |
| 2024 | A4352 | $25,248.94 | 59.77% | 68.28% | 376 |
| 2024 | A4353 | $30,382.05 | 70.44% | 96.88% | 236 |

Alternative explanations were tested as follows:

1. **General inflation or a price-only change:** A4353 units grew 7,048.23% in 2023, while its weighted PUF-payment amount per service grew 9.17%. A rate increase alone cannot explain the reconstructed increase. Unit coding, modifiers and actual delivery still require claim/product documentation.
2. **Broad growth in ordinary catheter demand:** A4351 grew 17.97%, and matched A4353 suppliers above the stated baseline had median growth of 0.30%. These comparisons make uniform sector growth a poor explanation for the aggregate break. They cannot rule out legitimate specialised entrants, product migration, referral concentration or acquisitions at particular firms.
3. **A4352 as a clean negative control:** rejected. Its 165.47% increase and concentration change show it is also affected. It is retained as an adjacent-code comparator, not labelled unaffected or legitimate merely because it is a comparator.
4. **Suppression as the main explanation:** the independent national table retains the enormous A4353 increase. Supplier-detail payment coverage changes from 95.84% to 99.94%, far too little to explain the scale. Small suppliers and hidden fields remain unobservable.
5. **A general surge in units per beneficiary:** medians among rows with disclosed beneficiaries are 1,075.98, 1,033.45 and 1,049.58 services per beneficiary for A4353 in 2022–2024. This is a limited consistency check: most rows have suppressed beneficiary counts, and clinical appropriateness cannot be inferred.
6. **New-code visibility as proof of a new company:** rejected by the exact cross-code matches above. NPI continuity and code-entry must be distinguished from legal entity and ownership history.

## National totals and missingness

The national geography/service table is a separate aggregation of underlying claims; it includes suppliers whose detailed rows are withheld. It is therefore the appropriate comparator for suppression, while the supplier table is needed for exact longitudinal matching.

| Year | A4353 suppliers, national | A4353 beneficiaries, national | A4353 services, national | National reconstructed PUF payment | Detail payment coverage |
|---|---:|---:|---:|---:|---:|
| 2022 | 720 | 5,731 | 6,279,809 | $40,876,216.24 | 95.84% |
| 2023 | 703 | 518,185 | 429,493,441 | $3,059,163,823.61 | 99.94% |
| 2024 | 672 | 244,723 | 157,039,228 | $1,155,271,517.52 | 99.85% |

All three national rows are non-rental, so the beneficiary values above are taken directly from one row per year/code. **Do not sum national beneficiaries across codes or years.** Supplier-level beneficiary counts overlap as well: the 2023 disclosed A4353 supplier counts sum to 523,496, exceeding the national figure despite many hidden cells.

Across all nine supplier cohorts, **4,868 of 6,870 beneficiary-count fields are blank**. These blanks are unknown, not zero; monetary/service/claim fields needed for the calculations are present. The minimum disclosed claim count is 11 in every cohort. Per-column missingness is in `analysis.json`.

The linked June 2025 methodology contains inconsistent suppression wording: its population section refers to records with ten or fewer beneficiaries being excluded, while its limitations section refers to ten or fewer claims. The linked supplier dictionary instead specifies beneficiary-count suppression and exclusion for fewer than eleven claims. The observed blank-beneficiary rows with more than ten claims support using the latter operational interpretation, while preserving the source discrepancy. Absence still cannot be interpreted as zero activity.

## What this audit cannot establish

- The PUF is final-action FFS claims data, not a bank/escrow/refund ledger. Its dictionary calls the payment measure Medicare payments, but neither the inspected dictionary nor linked methodology supplies a claim suspension, cash-release, escrow, recoupment or net-loss field. [GAO-26-107799](https://files.gao.gov/reports/GAO-26-107799/index.html) describes approved processing under payment suspension. This audit therefore does not equate a processed payment measure with released or retained cash, or assume that every PUF payment was withheld.
- CMS's [urinary catheter case study](https://www.cms.gov/files/document/cpi-urinary-catheter-case-study.pdf) establishes an already-known enforcement context. Aggregate resemblance cannot identify its unnamed suppliers. This analysis is not discovery of that previously announced case.
- The linked methodology describes following-year-end NPPES demographics. A state in these files does not prove location or ownership on the service date. Ownership, buyers, bank transfers, invoices, referring-provider relationships, patient consent and delivery require distinct dated evidence.
- The files cover 2022–2024. They cannot test allegations about acquisitions, claims or transfers first occurring in 2025–2026, including ND Medical's reported 2025 acquisition.
- No probability of fraud is assigned to any supplier, and no amount here is designated recoverable loss or reward-eligible savings. Missing records remain missing.

## Reproduction and audit trail

From this directory, with Python 3 and no third-party packages:

```sh
python audit_catheters.py
```

This recomputes analysis and national reconciliation from retained snapshots and verifies their recorded hashes/counts. To refresh the public data deliberately:

```sh
python audit_catheters.py --fetch --fetch-national
```

Refreshing validates the dataset years against the live catalogue, rejecting a moving series UUID if it has switched periods. CMS may revise records; retain the existing commit/manifests before a refresh. The refresh needs public network access, uses 20-second request timeouts, bounded retries, and at most three supplier requests concurrently.

Key files:

- `acquisition_manifest.json`: nine supplier queries, filtered counts, page offsets, response and snapshot hashes, selected fields and schema hash.
- `national_acquisition_manifest.json`: nine national requests and hashes.
- `analysis.json`: all monetary measures, missingness, medians, concentration, exact-key decompositions and cross-code controls.
- `national_reconciliation.json`: all nine national/detail comparisons.
- `period_validation.json`, `catalog_selected_2022_2024.json`, `supporting_source_manifest.json`: dated source/period provenance and PDF hashes.
- `validation.json`: actual validation results, including all 6,870 supplier rows.
- `agent_result.json`: structured research handoff and limitations.

Supplier API UUIDs: 2022 `dad703df-2e52-4ac6-a26f-51ecbf463d77`; 2023 `44235fd3-6cf9-487f-928d-12998cd84071`; current 2024 series `1746a83e-bb65-4300-8e02-21edbab77c6b`. The current catalogue also lists year-specific 2024 API UUID `1dc6718a-e44b-403a-a735-ce01a6233822`; it was not substituted for the acquired series.

The next justified audit step is a **dated exact-NPI join to official ownership/enrolment and publicly documented enforcement, followed by claim-status and secondary-payer cash reconciliation where lawful evidence exists**. Public aggregate data cannot complete the latter step by itself.
