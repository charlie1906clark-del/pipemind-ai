---
id: "BOLT-RECONCILIATION-SPE4A625V346U"
type: "finding"
title: "SPE4A625V346U: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V346U: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A625V346U",
  "history_quantity": "448.000",
  "history_unit_cost": "1.05000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "470.4",
  "product": "470.40000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V346U]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_prior_history_row: [[DISC-PRICE-HISTORY-03]] — documented_fact (BOLT-E-68ac1ff3842b387430b6); sources: [[BOLT-SRC-award-SPE4A625V346U]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_award: [[BOLT-AWARD-SPE4A625V346U]] — documented_fact (BOLT-E-76b8d06397c54afe8f27); sources: [[BOLT-SRC-award-SPE4A625V346U]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-2ddc8888effb0ec3abbb); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V346U]] — documented_fact (edge-b817159c8b534a27fb5a); sources: [[BOLT-SRC-award-SPE4A625V346U]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-cc728d9cb86b6195e2e8)
