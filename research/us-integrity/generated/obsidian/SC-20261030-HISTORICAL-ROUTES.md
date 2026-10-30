---
id: "SC-20261030-HISTORICAL-ROUTES"
type: "acquisition_observation"
title: "Historical document routes failed; award existence remains established separately"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Historical document routes failed; award existence remains established separately

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "actual_losing_bids_or_evaluation_records_acquired": 0,
  "alternate_public_award_record_opens": 2,
  "alternate_route_documents_acquired": 0,
  "alternate_route_lineage": "Two alternate public award-record routes derived from observed current-record URL pattern and exact historical PIIDs",
  "automatic_redirect_hops_separately_counted": false,
  "awards_missing_or_concealed_inferred": false,
  "history_lane_attempted_piids": [
    "SPE4A626P5931",
    "SPE4A625PK654"
  ],
  "history_lane_opener_operations": 4,
  "history_lane_results": [
    {
      "error_type": "TimeoutError",
      "piid": "SPE4A626P5931",
      "result": "failed_no_retry",
      "url_lineage": "Derived from exact published PIID/date and prior observed official path pattern; not a clicked award hyperlink"
    },
    {
      "error_type": "ValueError",
      "piid": "SPE4A625PK654",
      "result": "failed_no_retry",
      "url_lineage": "Derived from exact published PIID/date and prior observed official path pattern; not a clicked award hyperlink"
    }
  ],
  "latest_other_attempt": "SPE4A626V138W date-derived PDF route returned file-not-found text",
  "new_historical_original_pdfs": 0,
  "visibility": "public"
}
```

## Sources

- [[SC-20261030-SRC-HISTORY-ALT-RECEIPT]]
- [[SC-20261030-SRC-HISTORY-RECEIPT]]
- [[SC-20261030-SRC-SCB-S03]]

## Outgoing relationships

- cites: [[SC-20261030-SRC-HISTORY-RECEIPT]] — documented_fact (edge-12b3f23510aee5ef02c3); sources: [[SC-20261030-SRC-HISTORY-RECEIPT]]
- cites: [[SC-20261030-SRC-HISTORY-ALT-RECEIPT]] — documented_fact (edge-93dcf305f9df065b3519); sources: [[SC-20261030-SRC-HISTORY-ALT-RECEIPT]]
- cites: [[SC-20261030-SRC-SCB-S03]] — documented_fact (edge-995eac01f065c23f9eac); sources: [[SC-20261030-SRC-SCB-S03]]

## Backlinks

- [[SC-20261030-CASE]]: includes_observation — documented_fact (SC-20261030-E-cd8e41af8a9d6ca92af8)
