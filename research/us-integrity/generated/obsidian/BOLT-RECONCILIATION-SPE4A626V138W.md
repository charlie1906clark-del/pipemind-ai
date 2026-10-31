---
id: "BOLT-RECONCILIATION-SPE4A626V138W"
type: "finding"
title: "SPE4A626V138W: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626V138W: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A626V138W",
  "history_quantity": "1212.000",
  "history_unit_cost": "0.93000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "1127.16",
  "product": "1127.16000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A626V138W]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_award: [[BOLT-AWARD-SPE4A626V138W]] — documented_fact (BOLT-E-d40d807bdba40eca1eac); sources: [[BOLT-SRC-award-SPE4A626V138W]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_prior_history_row: [[DISC-PRICE-HISTORY-01]] — documented_fact (BOLT-E-eeedfd677ca07ca6b6c8); sources: [[BOLT-SRC-award-SPE4A626V138W]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-3cdb11b7e4452a024f4a); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A626V138W]] — documented_fact (edge-7cce6209c7ca996df20c); sources: [[BOLT-SRC-award-SPE4A626V138W]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-06cf3e771f7778d40243)
