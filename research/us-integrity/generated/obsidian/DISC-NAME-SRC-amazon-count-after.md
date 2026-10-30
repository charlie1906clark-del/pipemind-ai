---
id: "DISC-NAME-SRC-amazon-count-after"
type: "source"
title: "USAspending captured request: amazon-count-after"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# USAspending captured request: amazon-count-after

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-30",
  "content_sha256": "83bee066c2edb37ddc1755e1d88b3617c82962d24dfe7338bc5db5e7fcf11d59",
  "hash_scope": "Wire hash covers actual HTTP response; retained snapshot hash covers selected/normalized JSON, not original wire bytes",
  "method": "POST",
  "original_wire_archived": false,
  "original_wire_sha256": "f9d32179281dcfcf7823a697a109657427c77b3eb8e7f032e84be7dea20e9db9",
  "request_manifest": "names/capture-2026-10-30/manifest.json",
  "request_path": "investigations/discovery-policy-2026-10-30/names/capture-2026-10-30/requests/amazon-count-after.json",
  "request_sha256": "e616166942a437db4f3da9116a1a08e8c66f0dafe7de19b0fac4959c6f6a87c6",
  "retrieved_at": "2026-10-30T10:50:40.923062+00:00",
  "selection": "JSON reformatted only",
  "selection_note": null,
  "snapshot_path": "investigations/discovery-policy-2026-10-30/names/capture-2026-10-30/snapshots/amazon-count-after.json",
  "source_bytes_archived": true,
  "url": "https://api.usaspending.gov/api/v2/search/spending_by_award_count/",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DISC-RV-F02]]: cites — documented_fact (edge-27f247fabf2f49c548fa)
- [[DISC-NAME-GROUP-1]]: cites — documented_fact (edge-31f9177ed48e9e1f80d6)
- [[DISC-RV-F01]]: cites — documented_fact (edge-4e47840eae1473edca88)
- [[DISC-NAME-INDEPENDENT-REVIEW]]: cites — documented_fact (edge-63b8275dec9aab80c845)
- [[DISC-NAME-ANALYSIS]]: cites — documented_fact (edge-77019f3ecf2c1780ff26)
- [[DISC-20261030]]: cites — documented_fact (edge-8f53f1b557084162ce46)
- [[DISC-NAME-GROUP-2]]: cites — documented_fact (edge-add18bcf084af9d72c0a)
- [[DISC-NAME-COHORT-amazon]]: cites — documented_fact (edge-bd378d2e5ce43f777d39)
