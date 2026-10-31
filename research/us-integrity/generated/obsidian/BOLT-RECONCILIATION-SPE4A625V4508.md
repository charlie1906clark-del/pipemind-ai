---
id: "BOLT-RECONCILIATION-SPE4A625V4508"
type: "finding"
title: "SPE4A625V4508: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V4508: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A625V4508",
  "history_quantity": "536.000",
  "history_unit_cost": "1.92000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "1029.12",
  "product": "1029.12000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V4508]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_award: [[BOLT-AWARD-SPE4A625V4508]] — documented_fact (BOLT-E-0b862981970a42c3864d); sources: [[BOLT-SRC-award-SPE4A625V4508]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_prior_history_row: [[DISC-PRICE-HISTORY-07]] — documented_fact (BOLT-E-e577436fd44c25e0aa73); sources: [[BOLT-SRC-award-SPE4A625V4508]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-7d861a8dc18816976428); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V4508]] — documented_fact (edge-d661f1b0b1efafad7448); sources: [[BOLT-SRC-award-SPE4A625V4508]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-a69c892126dd7f84373d)
