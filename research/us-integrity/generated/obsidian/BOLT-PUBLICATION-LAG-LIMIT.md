---
id: "BOLT-PUBLICATION-LAG-LIMIT"
type: "finding"
title: "Three empty public queries and two HTTP 503 failures do not show award absence or concealment"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Three empty public queries and two HTTP 503 failures do not show award absence or concealment

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "inference_status": "Plausible normal lag; exact cause unverified",
  "observation": {
    "delay_source_id": "BOLT-CUR-S03",
    "failed_503_queries": [
      "order-exact",
      "idv-exact"
    ],
    "false_absence_inference_prohibited": true,
    "interpretation": "Observed empty responses are compatible with normal publication lag; exact cause is unverified. HTTP503 is a failed retrieval, not an empty result.",
    "order_age_days": 11,
    "parent_age_days": 43,
    "publication_delay_days": 90,
    "success_queries": [
      "order-search",
      "order-id-filter",
      "idv-id-filter"
    ],
    "zero_result_queries": 3
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-CUR-S03]]
- [[BOLT-CUR-S04]]
- [[BOLT-SRC-CURRENT-QUERY-idv-exact]]
- [[BOLT-SRC-CURRENT-QUERY-idv-id-filter]]
- [[BOLT-SRC-CURRENT-QUERY-order-exact]]
- [[BOLT-SRC-CURRENT-QUERY-order-id-filter]]
- [[BOLT-SRC-CURRENT-QUERY-order-search]]

## Outgoing relationships

- cites: [[BOLT-SRC-CURRENT-QUERY-idv-id-filter]] — documented_fact (edge-136a39ad4e6e6ab53e94); sources: [[BOLT-SRC-CURRENT-QUERY-idv-id-filter]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-1d3b8db1335cdeb0dbfb); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-SRC-CURRENT-QUERY-order-exact]] — documented_fact (edge-31a77408c2542b438509); sources: [[BOLT-SRC-CURRENT-QUERY-order-exact]]
- cites: [[BOLT-SRC-CURRENT-QUERY-order-search]] — documented_fact (edge-3eb1e9dbdac795b0bfa8); sources: [[BOLT-SRC-CURRENT-QUERY-order-search]]
- cites: [[BOLT-SRC-CURRENT-QUERY-order-id-filter]] — documented_fact (edge-7a6214914693609ecec6); sources: [[BOLT-SRC-CURRENT-QUERY-order-id-filter]]
- cites: [[BOLT-SRC-CURRENT-QUERY-idv-exact]] — documented_fact (edge-929a5a82bc55cb813f73); sources: [[BOLT-SRC-CURRENT-QUERY-idv-exact]]
- cites: [[BOLT-CUR-S04]] — documented_fact (edge-bb693c648ea86bdbe385); sources: [[BOLT-CUR-S04]]
- cites: [[BOLT-CUR-S03]] — documented_fact (edge-bd3eecc5ce05e6a606ad); sources: [[BOLT-CUR-S03]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-ce0ddafeb7a3d7dc6832); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-644749577104e5e4a589)
- [[BOLT-BREV-F09]]: assesses_evidence — documented_fact (BOLT-E-65798f7b30036f1c0f31)
