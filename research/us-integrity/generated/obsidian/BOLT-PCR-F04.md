---
id: "BOLT-PCR-F04"
type: "review_assessment"
title: "MF Supply's displayed box/piece prices and seven-box stock are supported; pack normalization remains unresolved."
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# MF Supply's displayed box/piece prices and seven-box stock are supported; pack normalization remains unresolved.

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "evidence_paths": [
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/market/benchmark_matrix.json",
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/market/captures/mkt-mf-hh38fx3-4g8zy.json",
    "research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-challenge/independent_market_observations.json"
  ],
  "limits": [
    "Do not infer pack count from price or weight ratios.",
    "Orders and special conditions require seller acceptance; no government-compliant executable quote established."
  ],
  "new_named_adverse_inference": false,
  "provenance_note": "External source links provide source facts or methodology; code execution and synthetic arithmetic are supported by the separately pinned local artifacts",
  "review_decision": "narrow",
  "synthetic_numeric_claim": false,
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S02]]
- [[BOLT-PC-MKT-S03]]
- [[BOLT-PC-MKT-S04]]

## Outgoing relationships

- assesses_evidence: [[BOLT-MKT-MF-HH38FX3-4G8ZY]] — documented_fact (BOLT-E-1d22e6aed7605323d5b7); sources: [[BOLT-CUR-S02]], [[BOLT-PC-MKT-S03]], [[BOLT-PC-MKT-S04]]
- cites: [[BOLT-PC-MKT-S03]] — documented_fact (edge-21cba07a9a47f806329c); sources: [[BOLT-PC-MKT-S03]]
- cites: [[BOLT-PC-MKT-S04]] — documented_fact (edge-31bdc3e30ee8196d71e0); sources: [[BOLT-PC-MKT-S04]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-3cabd18c902ef319bf35); sources: [[BOLT-CUR-S02]]

## Backlinks

- [[BOLT-PRICE-CHALLENGE-REVIEW]]: records_review_assessment — documented_fact (BOLT-E-2073b6a4d551683bc2ce)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-fa6965ba694745310dc2)
