---
id: "DISC-PRICE-ELIGIBILITY-GATE"
type: "finding"
title: "All 21 candidate history-row pairs fail the comparison gate"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# All 21 candidate history-row pairs fail the comparison gate

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "gate_limit": "Software checks completeness and declared evidence flags; it cannot independently authenticate arbitrary provenance or prove fraud",
  "gate_result": {
    "blocked_pairs": 21,
    "eligible_pairs": 0,
    "new_fraud_case_claimed": false,
    "observations": 7,
    "possible_pairs": 21,
    "potential_savings_usd": null,
    "representative_block_reasons": [
      "left: missing unit_of_issue, pack_quantity, item_revision, condition, delivery_terms, inspection_acceptance, warranty_basis, nonrecurring_cost_treatment, currency, unit_conversion_evidence",
      "left: amount is not a verified award CLIN or invoice line price",
      "right: missing unit_of_issue, pack_quantity, item_revision, condition, delivery_terms, inspection_acceptance, warranty_basis, nonrecurring_cost_treatment, currency, unit_conversion_evidence",
      "right: amount is not a verified award CLIN or invoice line price",
      "unresolved economic differences: quantity, price_date"
    ],
    "scope": "One purposively selected public solicitation; not a representative procurement cohort",
    "suspect_scores_generated": 0
  },
  "source_record": "pricing/eligibility_result.json",
  "visibility": "public"
}
```

## Sources

- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- [[DISC-PRICE-SRC-FAR-15-404-1]]

## Outgoing relationships

- cites: [[DISC-PRICE-SRC-FAR-15-404-1]] — documented_fact (edge-c7bd6e6fe8c003556a2c); sources: [[DISC-PRICE-SRC-FAR-15-404-1]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-d506a09da4dfc3936b4c); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Backlinks

- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-8e9f7da7684f303faa41)
