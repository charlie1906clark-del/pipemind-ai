---
id: "BOLT-RECONCILIATION-SPE4A625V252D"
type: "finding"
title: "SPE4A625V252D: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V252D: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A625V252D",
  "history_quantity": "665.000",
  "history_unit_cost": "1.10000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "731.5",
  "product": "731.50000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V252D]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_award: [[BOLT-AWARD-SPE4A625V252D]] — documented_fact (BOLT-E-07b969d79a364342dc60); sources: [[BOLT-SRC-award-SPE4A625V252D]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_prior_history_row: [[DISC-PRICE-HISTORY-04]] — documented_fact (BOLT-E-d5cc712773a58d7c658f); sources: [[BOLT-SRC-award-SPE4A625V252D]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V252D]] — documented_fact (edge-3bc7b089017bbdb580d7); sources: [[BOLT-SRC-award-SPE4A625V252D]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-af95af6b50f03e48f14c); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-5b1d371bc1d348a3f829)
