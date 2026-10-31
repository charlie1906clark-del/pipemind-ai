---
id: "BOLT-RECONCILIATION-SPE4A626P5931"
type: "finding"
title: "SPE4A626P5931: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626P5931: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A626P5931",
  "history_quantity": "706.000",
  "history_unit_cost": "1.00000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "706.0",
  "product": "706.00000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A626P5931]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_prior_history_row: [[DISC-PRICE-HISTORY-02]] — documented_fact (BOLT-E-8e68bdd19d910e9641a0); sources: [[BOLT-SRC-award-SPE4A626P5931]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_award: [[BOLT-AWARD-SPE4A626P5931]] — documented_fact (BOLT-E-a1d2385782d25057612b); sources: [[BOLT-SRC-award-SPE4A626P5931]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A626P5931]] — documented_fact (edge-29a4d5d7f6a52deca2c2); sources: [[BOLT-SRC-award-SPE4A626P5931]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-de5158773b010ff4ef19); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-d6c5166607ffa6616ee2)
