---
id: "BOLT-MARKET-BENCHMARK-MATRIX"
type: "benchmark_review"
title: "Three provisional catalog candidates; zero qualified DLA price comparators"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Three provisional catalog candidates; zero qualified DLA price comparators

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "candidate_count": 3,
  "candidate_spec_origin": "Secondary NSNExplorer claim; exact primary NSN/spec association not acquired. See spec-crosswalk.json.",
  "conclusion": "Further price research is warranted; no fraud, improper margin or buyer-side payment established.",
  "independent_market_price_verified": false,
  "no_new_named_adverse_inference": true,
  "price_fairness_established": false,
  "qualified_comparison": {
    "eligible": false,
    "eligible_comparator_count": 0,
    "kickback_amount": null,
    "loss_amount": null,
    "overcharge_amount": null,
    "price_premium": null,
    "reason": "Primary NSN/specification crosswalk and comparable accepted supply conditions are missing."
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-CUR-S01]]
- [[BOLT-CUR-S02]]
- [[BOLT-MKT-SRC-COX]]
- [[BOLT-MKT-SRC-FSS]]
- [[BOLT-MKT-SRC-FSS-FAQ]]
- [[BOLT-MKT-SRC-FSS-FINISH]]
- [[BOLT-MKT-SRC-FSS-STYLE]]
- [[BOLT-MKT-SRC-FSS-TERMS]]
- [[BOLT-MKT-SRC-MF]]
- [[BOLT-MKT-SRC-MF-SHIPPING]]
- [[BOLT-MKT-SRC-MF-TERMS]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]

## Outgoing relationships

- screens_candidate: [[BOLT-MKT-MF-HH38FX3-4G8ZY]] — documented_fact (BOLT-E-1a372d4813fdb776149f); sources: [[BOLT-MKT-SRC-MF]], [[BOLT-MKT-SRC-MF-SHIPPING]], [[BOLT-MKT-SRC-MF-TERMS]]
- keeps_fairness_question_open: [[BOLT-PRICE-FAIRNESS-UNKNOWN]] — documented_fact (BOLT-E-2773c96e97d7ca74e39b); sources: [[BOLT-CUR-S01]], [[BOLT-CUR-S02]], [[BOLT-MKT-SRC-COX]], [[BOLT-MKT-SRC-FSS]], [[BOLT-MKT-SRC-FSS-FAQ]], [[BOLT-MKT-SRC-FSS-FINISH]], [[BOLT-MKT-SRC-FSS-STYLE]], [[BOLT-MKT-SRC-FSS-TERMS]], [[BOLT-MKT-SRC-MF]], [[BOLT-MKT-SRC-MF-SHIPPING]], [[BOLT-MKT-SRC-MF-TERMS]], [[BOLT-PC-METHOD-S01]], [[BOLT-PC-METHOD-S02]]
- screens_candidate: [[BOLT-MKT-FSS-191377]] — documented_fact (BOLT-E-383e51b346d01bcdb21b); sources: [[BOLT-MKT-SRC-FSS]], [[BOLT-MKT-SRC-FSS-FAQ]], [[BOLT-MKT-SRC-FSS-TERMS]]
- screens_candidate: [[BOLT-MKT-COX-HB8F38-34]] — documented_fact (BOLT-E-d34bee7117c86978c06c); sources: [[BOLT-MKT-SRC-COX]]
- requires_resolved_crosswalk: [[BOLT-NSN-SPEC-CROSSWALK-GAP]] — planned (BOLT-E-f54bffbe15b6d3b7d5fa); sources: [[BOLT-CUR-S01]], [[BOLT-SPEC-R01]], [[BOLT-SPEC-R02]], [[BOLT-SPEC-R03]], [[BOLT-SPEC-R04]], [[BOLT-SPEC-R05]], [[BOLT-SRC-BR-S02]]
- cites: [[BOLT-MKT-SRC-FSS-TERMS]] — documented_fact (edge-1b0748c6052c99b937e2); sources: [[BOLT-MKT-SRC-FSS-TERMS]]
- cites: [[BOLT-CUR-S02]] — documented_fact (edge-28dc704703d6a4357ae0); sources: [[BOLT-CUR-S02]]
- cites: [[BOLT-MKT-SRC-MF]] — documented_fact (edge-3e50899721f509a65b48); sources: [[BOLT-MKT-SRC-MF]]
- cites: [[BOLT-MKT-SRC-FSS-FINISH]] — documented_fact (edge-53dddd3ce855c1b446df); sources: [[BOLT-MKT-SRC-FSS-FINISH]]
- cites: [[BOLT-MKT-SRC-COX]] — documented_fact (edge-5e002faf013c7f4373ac); sources: [[BOLT-MKT-SRC-COX]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-8311c2fdba257ea25720); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-87c3f27e8b6f42319cf4); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-CUR-S01]] — documented_fact (edge-ba667e8eeb76e3021940); sources: [[BOLT-CUR-S01]]
- cites: [[BOLT-MKT-SRC-FSS-STYLE]] — documented_fact (edge-cf80e0d27aba3ee1a6b1); sources: [[BOLT-MKT-SRC-FSS-STYLE]]
- cites: [[BOLT-MKT-SRC-FSS]] — documented_fact (edge-eba6fd9cac48207090d0); sources: [[BOLT-MKT-SRC-FSS]]
- cites: [[BOLT-MKT-SRC-FSS-FAQ]] — documented_fact (edge-f4160c8519ae736f5371); sources: [[BOLT-MKT-SRC-FSS-FAQ]]
- cites: [[BOLT-MKT-SRC-MF-TERMS]] — documented_fact (edge-f8867b5a6ae3326e8198); sources: [[BOLT-MKT-SRC-MF-TERMS]]
- cites: [[BOLT-MKT-SRC-MF-SHIPPING]] — documented_fact (edge-face26806826ac3afa21); sources: [[BOLT-MKT-SRC-MF-SHIPPING]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-a2c8a793e2a43766f0af)
- [[BOLT-SPEC-EXACT-ROW-GAP]]: blocks_qualified_comparison — planned (BOLT-E-e379c9a0ef9ebac17b3a)
- [[SC-20261030-MF-PACK]]: updates_pack_evidence_only — documented_fact (SC-20261030-E-903363caf524a60c1827)
