# Pilot validation

Validation run: 2026-10-30. The checks below concern this pilot's captures and derivations. They do not establish price fairness, delivery, a cash payment or absence of misconduct. The separately maintained `parties/` package has its own validation.

- **11 offline tests passed.** Original capture hashes and selected-source hashes replay; 30 exact award IDs remain unique; API date, agency, PSC, pagination and finite-amount rules hold. Negative or zero original-award quantities, negative prices, duplicate IDs, nonfinite amounts and mismatched line arithmetic are rejected.
- **Three samples remain partial.** Each has 10 rows and `hasNext:true`. The common `new_awards_only` window is validated against `Base Obligation Date`; a different performance start does not silently invalidate or change the date basis.
- **DLA arithmetic independently reproducible.** 2,243 × $272.99 = $612,316.57; adding the separately typed $3,500 first-article line gives $615,816.57. The one EA test requirement and two actual test articles are not added to production quantity. Adjustments/credits are not supported by this positive-original-award validator and would require a separate type.
- **Price bases remain distinct.** Award obligations have null award-level unit prices and null estimated losses. Two original CLINs reside in their own typed records. Two unrelated catalog entries remain rejected comparisons. No matched independent benchmark or cash payment has been verified.
- **Source visual checks completed.** Page 4 and the page-5 test-line crop were compared visually to the extracted values; page 11 was visually checked for the inserted two-article/400-day/180-day terms. Selected text retains the originating page and explicitly labels address omissions.
- **Graph integrity checked.** The pilot graph contains 65 nodes and 42 edges. Every edge endpoint and source identifier resolves. These are award/recipient/office/parent and awarded-line relationships, not payment transfers.
- **Canonical note generation retained.** Local duplicate per-award notes were removed before freeze; the parent integration generates notes from the canonical graph. Pilot local Markdown links resolve.
- **Public artifact scope checked.** No email address was found in the public text artifacts. Contact and street-address blocks were manually excluded from selected PDF excerpts; the two published source images contain no such blocks. The full original PDF is ignored by git and is not a public artifact. The selected officer record is limited to a printed professional name, title and date.
- **Research limits respected.** This subtask issued 12 search queries and 23 API/document retrieval operations. Failed/partial retrievals are recorded, including 404 price-list URLs and the SAM JavaScript shell. The three candidates were not replaced to conceal unavailable sources. The `parties/` and independent-review work have separate budgets.

Reproduce with:

```bash
python research/us-integrity/investigations/federal-price-pilot-2026-10-30/analyze.py
python -m unittest discover -s research/us-integrity/investigations/federal-price-pilot-2026-10-30 -p test_pilot.py -v
```

`bundle_manifest.json` hashes this pilot's public files, excluding itself, ignored originals/cache files and the separately owned `parties/` package. Capture manifests distinguish original-wire hashes from saved selected-response hashes. Web catalog facts are selected transcriptions; no original HTML-body hash is claimed. Hashes pin captured content, not the continuing availability or truth of a live website.
