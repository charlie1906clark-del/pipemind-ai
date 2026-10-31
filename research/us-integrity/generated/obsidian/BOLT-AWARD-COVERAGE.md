---
id: "BOLT-AWARD-COVERAGE"
type: "dataset_cohort"
title: "All seven declared historical PIIDs resolved in the bounded official search"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# All seven declared historical PIIDs resolved in the bounded official search

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "coverage": {
    "missing_keys": [],
    "requested_keys": [
      "SPE4A626V138W",
      "SPE4A626P5931",
      "SPE4A625V346U",
      "SPE4A625V252D",
      "SPE4A625V208Q",
      "SPE4A625PK654",
      "SPE4A625V4508"
    ],
    "returned_keys": [
      "SPE4A625PK654",
      "SPE4A625V208Q",
      "SPE4A625V252D",
      "SPE4A625V346U",
      "SPE4A625V4508",
      "SPE4A626P5931",
      "SPE4A626V138W"
    ],
    "scope": "Seven exact PIID search keys; not nationwide/recipient history; award summary and latest contract transaction are not invoices or contract line items.",
    "terminal_page_empty": true
  },
  "nationwide_coverage": false,
  "no_fraud_ranking": true,
  "total_observation_count": 7,
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-exact-award-search]]
- [[BOLT-SRC-exact-award-terminal]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- includes_award_observation: [[BOLT-AWARD-SPE4A626V138W]] — documented_fact (BOLT-E-3d5c71ceea42ed563253); sources: [[BOLT-SRC-award-SPE4A626V138W]]
- includes_award_observation: [[BOLT-AWARD-SPE4A625V208Q]] — documented_fact (BOLT-E-4ac051d762bafd390a9a); sources: [[BOLT-SRC-award-SPE4A625V208Q]]
- includes_award_observation: [[BOLT-AWARD-SPE4A625V346U]] — documented_fact (BOLT-E-70041fe0f6709e1f7538); sources: [[BOLT-SRC-award-SPE4A625V346U]]
- includes_award_observation: [[BOLT-AWARD-SPE4A625V4508]] — documented_fact (BOLT-E-7b70a113a7ccce01bf1f); sources: [[BOLT-SRC-award-SPE4A625V4508]]
- includes_award_observation: [[BOLT-AWARD-SPE4A626P5931]] — documented_fact (BOLT-E-7cce4335c50dbce93380); sources: [[BOLT-SRC-award-SPE4A626P5931]]
- includes_award_observation: [[BOLT-AWARD-SPE4A625V252D]] — documented_fact (BOLT-E-e0bdcb40dd8297c8b1ce); sources: [[BOLT-SRC-award-SPE4A625V252D]]
- includes_award_observation: [[BOLT-AWARD-SPE4A625PK654]] — documented_fact (BOLT-E-f5f02e7b975e9c01d9d0); sources: [[BOLT-SRC-award-SPE4A625PK654]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-51ed2382d300b19d2d7f); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-exact-award-search]] — documented_fact (edge-5fdf17352a246c2957ae); sources: [[BOLT-SRC-exact-award-search]]
- cites: [[BOLT-SRC-exact-award-terminal]] — documented_fact (edge-971ff43608dccefc4c34); sources: [[BOLT-SRC-exact-award-terminal]]

## Backlinks

- [[BOLT-BREV-F02]]: assesses_evidence — documented_fact (BOLT-E-310c0e39fe64237fa7a9)
- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-a622f4c484b9daefa510)
- [[BOLT-BREV-F10]]: assesses_evidence — documented_fact (BOLT-E-b33e3f89ea523f5a0131)
