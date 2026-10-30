# Fixed pilot selection and replay

Observed 2026-10-30. Base repository commit `d535e545adf362c17e43337e1147a0b2f6c7c18a`.

This is a finite discovery sample with three fixed strata. It is not a nationwide census, a random sample, a list of suspicious companies, or a measure of fraud prevalence.

| Stratum | Awarding-agency filter | Commodity |
|---|---|---|
| `dla-bolts` | Defense Logistics Agency, awarding subtier of Department of Defense | PSC 5306 |
| `va-medical` | Department of Veterans Affairs, awarding toptier | PSC 6515 |
| `hhs-medical` | Department of Health and Human Services, awarding toptier | PSC 6515 |

For each stratum, request contract types A/B/C/D, `subawards:false`, page 1, limit 10, descending `Award Amount`. The common filter is 2026-07-03 through 2026-07-31 inclusive, explicitly `date_type:new_awards_only`. Exact requests are in `capture/*.request.json`; `acquire.py` constructs them. No additional pages were fetched. Every response reported `hasNext:true`; ten is a retrieved count, not the population size. No silent date-window or stratum substitution occurred.

The official API's [date-filter documentation](https://raw.githubusercontent.com/fedspendingtransparency/usaspending-api/master/usaspending_api/api_contracts/search_filters.md) defines this mode using the base transaction date. The retrieved `Base Obligation Date`, not performance `Start Date`, is validated against the window. A `date_signed` value is separately available for three detailed records. Express reports can have an earlier performance period and aggregate multiple purchases; five VA results contain express-report wording. No row is treated as a July-only payment, item quantity or unit price.

All 30 rows are retained, including express reports. Detail selection was then fixed in `detail-selection.json` before original-document tracing:

1. DLA `SPE4A626PW775`: highest-obligation sampled ordinary bolt purchase order.
2. VA `36C79126F0030`: highest-obligation sampled non-express-report medical-device order.
3. HHS `75N98026F00268`: discrete defibrillator goods with a traceable FSS parent. The higher-obligation custom freezer system and broad medical-supply funding record were excluded from this *document-priority pass*, not from the 30-row cohort.

These choices favor economic exposure and tractable item documentation. They do not rank recipient honesty or identify likely fraud. This purposive choice also limits generalization. The exact generated award identifier controls joins; a similar or punctuated company name is insufficient identity evidence. UEIs label reported recipients, not beneficial ownership.

For each candidate, fetch the official award detail endpoint, follow exact parent/solicitation identifiers, and search for the original order or governing price list. The DLA original award was obtained through its ordinary public notice. Two GSA price-list URLs returned 404; one received a single alternate web retrieval that also returned 404. The SAM notice opened as a JavaScript shell. Accessible catalog items were evaluated on exact item identity and explicitly rejected when mismatched. Neither blocked documents nor missing prices imply absence of an issue.

`request_ledger.json` records 12 search queries and 23 API/document retrieval operations, including failures and repeated web opens, within limits of 12 and 30. It counts issued retrieval operations; hidden search-backend transport and automatic redirects are not observable. Independent reviewer and parent-agent research have separate logs. Search stopping rules have been reached; remaining work is expressed as named tasks rather than an unbounded crawl. `document_links.json` inventories eight visible URL references in the DLA PDF and explicitly distinguishes unvisited technical references and generic system links from award-specific transaction evidence. External nested links and restricted technical data packages were not acquired.

## Evidence handling

API manifests preserve request hashes, original-response hashes and selected-response hashes separately. Original wire bytes were not archived; selected business-award JSON is reformatted and hashable. Do not claim a selected snapshot reproduces original wire bytes. The DLA original PDF has a recorded hash and byte count. The full PDF contains contact/address blocks and is excluded from the public repository; reviewed text selections and source-page/crop PNGs have their own hashes in `selected_manifest.json`.

Source page 4 was rendered at 110 dpi with `pdftoppm`, and page 5's first-article section was cropped at the same resolution (`-x 0 -y 1000 -W 935 -H 210`). These images were visually compared with the extracted line text. The first-article clause on page 11 was also visually inspected; its selected text marks the testing-facility address omission. Pages 1, 2, 3, 6 and 7 supply selected role, item, scope and timing text. A printed professional officer name/role is not an authenticated signature or proof of a personal price-selection decision.

## Replay

From the repository root, offline normalization and validation require Python's standard library:

```bash
python research/us-integrity/investigations/federal-price-pilot-2026-10-30/analyze.py
python -m unittest discover -s research/us-integrity/investigations/federal-price-pilot-2026-10-30 -p test_pilot.py -v
```

Live replays create new directories and may return updated data. They do not overwrite the observed cohort:

```bash
python research/us-integrity/investigations/federal-price-pilot-2026-10-30/acquire.py --output /tmp/federal-price-new-capture
python research/us-integrity/investigations/federal-price-pilot-2026-10-30/acquire.py --details research/us-integrity/investigations/federal-price-pilot-2026-10-30/detail-selection.json --output /tmp/federal-price-new-detail
python research/us-integrity/investigations/federal-price-pilot-2026-10-30/acquire_dla_document.py --output /tmp/federal-price-new-original
```

The parent BPA replay uses the same `Capture` and `select_detail` helper with `https://api.usaspending.gov/api/v2/awards/CONT_IDV_36C79123A0003_3600/`; its exact observed request is recorded in `parent-capture/manifest.json`. No authenticated system is needed for these acquisitions. Re-run public-data selection before publishing a refreshed original document or API response.
