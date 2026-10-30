# Supplier-name investigation: testing Amazon versus Amazon.

**30 October 2026.** This is an executed public-data test of a proposed discovery method. It does not accuse Amazon, AWS, their affiliates or any other supplier of fraud. The observed punctuation difference is a useful identity-resolution example, but the acquired records do not establish a fake company or a new false claim.

## What was actually acquired

Nineteen public USAspending requests retrieved two literal-keyword contract-recipient searches, two FY2026 prime-contract award searches, before/after award counts, explicit terminal empty pages and six recipient profiles. The acquisition used contract types A–D and the award-search window 1 October 2025–30 September 2026. No private payment system, SAM login, bank information or company contact information was accessed.

| Literal search input | Contract recipient profile rows | Distinct profile UEIs | FY2026-window contract awards | Completion evidence |
|---|---:|---:|---:|---|
| `Amazon` | 6 | 3 | 150 | Counts agree before/after; unique award IDs; terminal pages empty |
| `Amazon.` | 2 | 1 | 12 | Counts agree before/after; unique award IDs; terminal pages empty |

All 12 awards from the second query occur in the first query. The union therefore contains **150 awards, not 162**. The 138-award difference is an observed **query-behavior difference**, not evidence of 138 fake records or a literal list of company names ending in a period. The narrower award query includes eleven Amazon.com Services awards and one AWS award whose displayed recipient name has no terminal period. Recipient-profile and award-search outputs should not be assumed to apply identical name-history matching.

The complete selected query results, exact POST bodies, retrieval times and hashes are in [capture-2026-10-30](capture-2026-10-30/manifest.json). Completeness applies to these bounded queries at retrieval, not all federal vendors, all aliases, all award types, every year or every transaction. USAspending's default award-search date semantics do not turn this into a census of transactions made during FY2026. [NAMES-S01–S04]

## The exact punctuation pair and identity checks

| Raw reported recipient name | Exact UEI | Profile state | FY2026-window awards in broad query | Child profile's reported parent UEI |
|---|---|---|---:|---|
| AMAZON.COM SERVICES LLC | TMKBFBRHFKH3 | WA | 11 | G5F2C46HBCM3 |
| AMAZON WEB SERVICES, INC | H6S2VKM5U6C5 | VA | 1 | G5F2C46HBCM3 |
| AMAZON WEB SERVICES, INC. | NQEWN6C1LSU5 | WA | 138 | G5F2C46HBCM3 |

The three child profiles all report **AMAZON.COM, INC.** with parent UEI **G5F2C46HBCM3**. This is a benign consistency fact in USAspending's reported hierarchy. It is not independently authenticated beneficial ownership or proof that each registration's historical details are correct. The two AWS identifiers remain distinct in the analysis; a normalized-name match never merges them. A UEI count is also not necessarily a count of ultimate corporate groups.

Each UEI appears twice in the recipient query: once at parent level `P` and once at child level `C`. Parent-level profiles report themselves as parent; child-level profiles report the above parent. Thus six profile rows are **three identifier pairs**, not six independently discovered companies. The selected profile responses retain raw names, UEIs, DUNS, profile level, reported parent fields, business types and state/country. Nested parent arrays, street addresses and contact fields are omitted. [NAMES-S03, NAMES-S05–S10]

The three raw names retain distinct identifiers in all 150 award rows; no award lacks a UEI. No same-UEI/multiple-name variation was observed in this bounded set. The AWS pair is a **same comparison key, different UEIs** observation, with a common reported parent, rather than a proved impersonation. Neither punctuation nor a missing period is a sufficient escalation trigger.

## Why a naive detector would fail here

1. **Counting profiles as companies:** `P`/`C` duplicates would double the apparent population and can duplicate the same underlying monetary measure.
2. **Treating query text as a legal-name test:** adding a period changed the returned award population substantially; the result was not a literal suffix filter.
3. **Collapsing names after punctuation removal:** the AWS pair would collapse despite different UEIs and source-reported locations. This destroys identity evidence.
4. **Calling distinct UEIs fraudulent:** separate identifiers require source/registration and timing checks, not an assumption that one is counterfeit.
5. **Treating a UEI as current eligibility:** SAM allows UEI-only records; a UEI's existence does not establish completed active registration, historical eligibility or absence of exclusions. [NAMES-S11]
6. **Treating money fields as losses:** the recipient API describes its amount as a trailing-12-month transaction aggregate. Award search returns an award-level amount with a different basis. No amounts are added or classified as losses by this audit. [NAMES-S01, NAMES-S03]

A preliminary all-award recipient search returned many unrelated businesses and individual DBA entries. That broader result was unsuitable for the specific procurement comparison and was not retained as a public candidate list. The completed captures are restricted to contract-recipient queries and the stated award window.

## Executable discovery rules

`audit_names.py` preserves raw strings and creates a comparison key using Unicode NFKC, case folding, punctuation-to-space and whitespace collapse. It retains legal suffixes, DBA text and subsidiary words. It does not transliterate Cyrillic/Greek lookalikes into Latin or automatically merge organizations. Mixed-script text can be described for review; this alone establishes no deception.

The output distinguishes:

- Same reported UEI with multiple observed names: possible formatting/history issue; preserve dates and source records.
- Same comparison key with different UEIs: unresolved identity relationship; keep separate entities and inspect dated registries/parent assertions.
- Missing or malformed UEI: unresolved identifier; never fill it from a name match.
- Same UEI at `P` and `C` profile levels: profile hierarchy duplication; no duplicate-company inference or amount summing.
- Different full names containing the same brand token: keyword discovery only; DBA, reseller, affiliate and unrelated-name explanations remain available.

The script deliberately emits no fraud score, estimated loss, guilt label, automatic entity merge or inferred owner. These constraints are part of the output contract, not a claim that a suspicious identifier can never exist.

## A stronger search for new impersonation cases

Advance a name variant only when it has an independent contradiction. A useful sequence is:

1. Resolve exact UEI, CAGE, award identifier, legal/trade name and relevant service/award dates. Preserve distinct namespaces; CAGE and UEI are different systems.
2. Compare dated SAM/entity records and published corporate filings against the contracting record. Verify role and control as of the transaction, not merely today's registered agent or officer.
3. Check publicly documented exclusions, registration effective periods, assignment/novation records and legitimate reseller arrangements.
4. If the discrepancy survives, seek the original award/solicitation record, invoice/delivery evidence and any published payment confirmation. A suspicious name does not prove money reached a different payee.
5. Search prior OIG/DOJ/GAO/court publications for the exact identifiers to determine whether the specific allegation is already public. Keep novelty separate from anomaly size.
6. Have a separate reviewer test benign explanations before escalation. Keep an unresolved new named theory out of this public repository until its evidence and publication implications are reviewed.

The best new lead would be a **dated identifier or control contradiction tied to a particular representation and payment**, not a high-volume list of punctuation differences. Many decisive records are not exposed in aggregate public APIs. No claim of universal coverage or an authenticated beneficial-ownership chain is made here.

## Reproduce and validate

From the repository root:

```bash
python research/us-integrity/investigations/discovery-policy-2026-10-30/names/audit_names.py
python -m unittest discover -s research/us-integrity/investigations/discovery-policy-2026-10-30/names -p 'test_*.py' -v
```

Default execution makes no network calls. It checks all captured snapshot/request hashes, re-reads the two actual count responses, proves contiguous pages ending empty, checks profile and award uniqueness, and binds derived files to the retained snapshots. Sixteen tests passed, including altered-parent data, wrong count summaries, missing terminal pages, tampering, Unicode lookalikes, DBA preservation, distinct identifiers and profile-level duplicates.

For a new deliberately bounded capture, use `--acquire /path/to/new-directory`. Existing capture directories are rejected. Requests have 20-second timeouts, a 4 MiB response cap, at most 20 pages per query and no automatic retries. Every refreshed dataset must receive a fresh date and evidence review; the current report describes only this captured run.

`analysis.json` contains computed results. `sources.json` and `evidence_records.json` provide claim-level references for graph ingestion. Original HTTP-response hashes are retained, but the archived JSON responses are selected/reformatted snapshots, not original wire bytes. The manifest labels those digest scopes separately.

**Result:** the proposed name screen has been tested against real public contracting data. It exposes query and identity pitfalls and produces a reproducible method. It has established **zero new fraud cases and no recoverable loss**.

[NAMES-S01]: https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award.md
[NAMES-S02]: https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/search_filters.md
[NAMES-S03]: https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/contracts/v2/recipient.md
[NAMES-S04]: https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award_count.md
[NAMES-S05]: https://api.usaspending.gov/api/v2/recipient/06d55b8d-0bcb-c654-8213-1001f38dd3d2-P/
[NAMES-S06]: https://api.usaspending.gov/api/v2/recipient/06d55b8d-0bcb-c654-8213-1001f38dd3d2-C/
[NAMES-S07]: https://api.usaspending.gov/api/v2/recipient/fd132ca2-1539-c208-cb18-0d8f8cfe0618-P/
[NAMES-S08]: https://api.usaspending.gov/api/v2/recipient/fd132ca2-1539-c208-cb18-0d8f8cfe0618-C/
[NAMES-S09]: https://api.usaspending.gov/api/v2/recipient/645df5f2-66e3-8d2b-a612-3bff6ed3da30-C/
[NAMES-S10]: https://api.usaspending.gov/api/v2/recipient/645df5f2-66e3-8d2b-a612-3bff6ed3da30-P/
[NAMES-S11]: https://sam.gov/entity-registration
