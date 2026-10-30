---
id: "DISC-NAME-SRC-amazon-count-before"
type: "source"
title: "USAspending captured request: amazon-count-before"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# USAspending captured request: amazon-count-before

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
  "request_path": "investigations/discovery-policy-2026-10-30/names/capture-2026-10-30/requests/amazon-count-before.json",
  "request_sha256": "e616166942a437db4f3da9116a1a08e8c66f0dafe7de19b0fac4959c6f6a87c6",
  "retrieved_at": "2026-10-30T10:50:18.244334+00:00",
  "selection": "JSON reformatted only",
  "selection_note": null,
  "snapshot_path": "investigations/discovery-policy-2026-10-30/names/capture-2026-10-30/snapshots/amazon-count-before.json",
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

- [[DISC-NAME-GROUP-1]]: cites — documented_fact (edge-37745e6dd1de1407e870)
- [[DISC-NAME-COHORT-amazon]]: cites — documented_fact (edge-597cc5bd99093ae78933)
- [[DISC-20261030]]: cites — documented_fact (edge-5e4d4d3a3f3a6af4427a)
- [[DISC-RV-F01]]: cites — documented_fact (edge-74b0796329af7e79de63)
- [[DISC-NAME-ANALYSIS]]: cites — documented_fact (edge-a15ec9d9df1f9beb8e6d)
- [[DISC-NAME-GROUP-2]]: cites — documented_fact (edge-c1824ed636769e34417e)
- [[DISC-NAME-INDEPENDENT-REVIEW]]: cites — documented_fact (edge-ceff9ec9622929e97b21)
- [[DISC-RV-F02]]: cites — documented_fact (edge-fd3709b91f81e997843a)
