# Seven historical DLA bolt awards: exact record trace

Checked **30 October 2026**. All seven contract numbers in the original RFQ's history table now match official USAspending award records. All seven dates agree, and each printed history quantity multiplied by its printed cost equals the corresponding current cumulative award obligation. The records report three to five offers and firm-fixed-price purchase orders under simplified acquisition. This is useful corroboration of the history table. It establishes **no new fraud, paid-invoice verification, recoverable loss or reward**.

This lane deliberately follows one item, **NSN 5306016864912**, and seven predefined historical PIIDs. Claude's separate pricing assignment and the coordinator's current IDC/order investigation remain separate. The seven-award sample is inherited from one solicitation's history table; it is not a complete population of purchases, modifications, transactions or suppliers for the NSN.

## What the official records show

| Historical award | Signed date | Current award obligation, USD | Offers reported | Related solicitation |
|---|---|---:|---:|---|
| SPE4A626V138W | 2026-05-26 | 1,127.16 | 3 | SPE4A626T52U3 |
| SPE4A626P5931 | 2025-11-14 | 706.00 | 4 | SPE4A626T8303 |
| SPE4A625V346U | 2025-06-16 | 470.40 | 5 | SPE4A625T99L1 |
| SPE4A625V252D | 2025-05-16 | 731.50 | 4 | SPE4A625T61G7 |
| SPE4A625V208Q | 2025-04-30 | 552.24 | 3 | SPE4A625T52K8 |
| SPE4A625PK654 | 2025-03-24 | 345.60 | 4 | SPE4A625T825F |
| SPE4A625V4508 | 2024-12-04 | 1,029.12 | 4 | SPE4A625T131Y |

Source IDs `BOLT-AWD-<PIID>` resolve in [sources.json](sources.json), with archived selected responses and their exact hashes. Each record reports DLA Aviation as the awarding office. The seven distinct order obligations sum to **$4,962.02**. That aggregate is only the current obligation for this selected set: it is not cash paid, all spending on the NSN, or a possible recovery. It would be a weak basis for prioritizing this seed as a large financial fraud opportunity.

The API's performance-period dates vary, but are award-summary fields; they are not authenticated original delivery clauses or acceptance evidence. The reported offer counts do not identify the bidders or establish independent competition. The simplified-acquisition and fixed-price fields likewise describe reported award characteristics, not an independently audited procurement file. All seven report no set-aside in their latest contract data; this must not be transferred to the separate current IDC or assumed to describe every earlier solicitation version.

## Exact identity joins, with their limits

The seven records contain five UEIs. Each reported recipient agrees between the award-search response and its detail response. The original DLA history supplies PIID and CAGE; USAspending supplies the same PIID, matching signed date, reported recipient name and UEI. That is a defensible **cross-source association**, not a direct SAM registration or beneficial-ownership verification. USAspending's detail response used here does not expose a CAGE field.

The [structured observations](observations.json) preserve each historical CAGE, exact PIID, recipient UEI and source-reported name. A name in a public sole-proprietor award remains a business-role observation, not an allegation about that individual. All recipient location/contact fields and demographic business categories have been excluded from retained detail snapshots. Source-reported corporate relationships and registration dates require the identity specialist's separate evidence.

## Why arithmetic agreement is insufficient for a price verdict

For example, the printed 1,212 quantity and 0.93000 cost produce 1,127.16000000, numerically matching the API's $1,127.16 cumulative obligation. Equivalent checks pass for every row, including the single 472-quantity history entry. This strengthens the case that the table and award summary refer to the same award amount. It does not identify the historical purchased unit, package size, revision, warranty, freight allocation, nonrecurring charges, delivered quantity or payment.

The raw historical table does not explicitly label currency or historical unit of issue. Matching a USD award obligation is corroborative arithmetic, not permission to silently fill every historical unit/currency field. Original order lines and terms remain the decisive source for a comparable unit-price calculation. A current order's `EA` designation cannot retrospectively establish all seven older orders' units.

Neither a three-offer record nor a lower nominal price proves absence of misconduct. Conversely, the seven records do not support bid-rigging, supplier impersonation, false billing or defective-pricing allegations. The result narrows uncertainty and supports returning this seed to a control/calibration role unless new transaction-specific evidence changes the assessment.

## What happened when seeking original order documents

Seven public DLA document URLs were derived from the known award dates and exact PIIDs using the observed dated award-file route. **The date folder was not independently verified as the posting date.** Six attempts timed out during the ordinary notice-consent flow; one returned HTML rather than a PDF after consent. No historical priced award was acquired. A further attempt at the most recent linked RFQ, SPE4A626T52U3, timed out. The [attempt manifest](dla-attempts/manifest.json) distinguishes successful HTTP responses from failed attempts; an HTTP200 notice page is not a successfully downloaded award.

These results do not prove that the documents were deleted, withheld, or unavailable by every public route. In particular, the DLA's April2026 supplier newsletter states a normal PO/DO retention period of 120 days after posting, extended by later modifications. Its official search-indexed text was available, while full PDF retrieval returned403; that limitation is preserved in source `BOLT-AWD-RETENTION`. Retention begins from posting/latest modification, not automatically the signed date. All seven signed dates predate the current date by more than120 days, so routine retention is a plausible explanation to investigate, not an established explanation for these timeouts or derived-URL failures.

No login, restricted drawing access, credential guessing, supplier contact or external records request occurred. The coordinator's newer current-order trace may have better document availability and must be assessed from its own evidence.

## Acquisition and reproducibility

A first seven-key query using quoted IDs returned503, as did its terminal-page request. A simpler single-key diagnostic succeeded. A subsequent unquoted seven-key query succeeded and was **post-filtered by exact PIID**, then followed by an explicit empty second page and seven detail GETs. The archived successful capture therefore contains nine requests, allHTTP200, seven exact requested award matches, no extra award and an empty terminal page. The failed earlier requests remain in `capture/`; they are not silently replaced. No cause for the503 responses is asserted.

[Capture manifest](capture_manifest.json) accounts for **33 logical document/API reads** against a limit of35, plus11 web search queries against a limit of14. The retained successful API registry distinguishes original search-response bytes from selected/reformatted detail snapshots. A wire-response digest is not a claim that those original bytes were archived. Unarchived diagnostics and the failed supporting-document reads are recorded explicitly.

Run the offline checks from the repository root:

```sh
python research/us-integrity/investigations/dla-bolt-trace-2026-10-30/awards/analyze.py
python -m unittest discover -s research/us-integrity/investigations/dla-bolt-trace-2026-10-30/awards -p 'test_*.py'
```

Seven tests cover the pinned historical seed, retained-evidence integrity, wrong PIIDs, changed recipients, terminal-page failure, irrelevant profile fields and the distinction between an obligation and a verified payment. `acquire_awards.py --output NEW_DIRECTORY` makes a fresh bounded capture; changes require a dated review rather than overwriting this evidence. `acquire_public_documents.py` repeats only the seven stated derived URLs and ordinary notice flow; it cannot certify that those paths are the original posting paths.

The next discriminating input is an original historical order/CLIN and its modification history, or a properly documented newer comparison cohort. Further broad searches for the same names would add little without that transaction-level evidence.
