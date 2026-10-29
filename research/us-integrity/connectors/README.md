# Bounded USAspending acquisition

`usaspending.py` uses only Python's standard library. Running it issues at most three public POST requests in parallel, one first page per configured cohort. Each request has a 20-second timeout and 4 MiB response cap. It does not retry or follow result pagination. Importing the module does not issue requests. Each run receives a new directory, and an existing cohort directory cannot be overwritten.

```bash
python research/us-integrity/connectors/usaspending.py
python -m unittest discover -s research/us-integrity/connectors -p 'test_usaspending.py' -v
```

For a single acquisition use `--cohort medical-supplies`, `--cohort defense-parts` or `--cohort nih-grants`. A later run produces a separate snapshot; it does not update the earlier evidence.

## Observed acquisition

Run `snapshots/20261029T183534Z-e5a42676` completed on 29 October 2026, 18:35:39–18:35:40 UTC. The service returned HTTP 200 for all three requests. Eight offline tests passed, including exact response-byte preservation, failure manifests, byte caps, no retry and overwrite prevention.

| Cohort | Award filters | Limit / records received | Agency labels checked in response |
|---|---|---:|---|
| medical-supplies | Contract types A–D; PSC 6515 | 25 / 25 | Multiple agencies; no agency filter |
| defense-parts | Contract types A–D; PSC 1680 | 20 / 20 | Department of Defense, awarding top tier |
| nih-grants | Grant types 02–05 | 20 / 20 | NIH awarding sub tier, HHS top tier |

All use `2025-10-01` through `2026-09-30`. Each response reports `hasNext: true`, so **all three are truncated samples**. All 65 records contain Recipient UEIs; generated award IDs are unique within each cohort. Capture hashes were independently recomputed after acquisition and matched all three manifests. The service returned an informational earliest-search-date message, retained in each manifest.

## Interpret the sample correctly

The API returns awards selected by its award-search date filters. The default `date_type` is omitted: according to the official filter contract, default comparisons use latest action for the start bound and base transaction date for the end bound. This is not a list of all FY2026 transactions or an FY2026 spending aggregate.

Results are the largest **cumulative award amounts** returned in descending order, not a random sample, a complete population, contract ceilings or a fraud ranking. Do not sum these amounts and describe the result as FY2026 expenditure or loss. NIH grants are a research-focused proxy; no research-only assistance-listing filter was applied. PSC 6515 and 1680 are narrow procurement slices, not their complete sectors.

No selected company or award is implicated in wrongdoing by appearing here. No anomaly rule, ownership verification, sales analysis or beneficiary-tracing result has been applied to these snapshots.

## Provenance and identity

Each cohort contains:

- `request.json`: exact UTF-8 request bytes sent.
- `response.json`: exact received JSON response bytes; never pretty-printed or normalized.
- `manifest.json`: SHA256 hashes, timestamps, HTTP status, limits, pagination, API messages, scope and validation outcome.

`run-manifest.json` combines cohort outcomes. Failed/oversized responses have explicitly labelled error or partial files; a failed validation never becomes a successful acquisition. SHA256 checks detect later file modification; they are not a third-party timestamp or independent certification of upstream truth.

Use `generated_internal_id` to identify an award, UEI for recipient identity when present, and `recipient_id` as the API recipient reference. Do not merge organizations solely by names. Awarding agencies represent government buyers; recipients represent prime vendors/grantees. Neither establishes ultimate beneficial ownership or downstream customers. Requested location detail is state only; street addresses, telephone numbers and email fields are not requested.

## Official API sources

Contracts checked 29 October 2026:

- [Spending by award API contract](https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award.md)
- [Search filter contract](https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/search_filters.md)

The API contracts are source documentation, not data completeness guarantees. Their upstream `master` URLs may change; exact requests and received response bytes are retained in this run.
