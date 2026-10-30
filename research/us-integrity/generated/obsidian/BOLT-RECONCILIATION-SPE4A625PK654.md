---
id: "BOLT-RECONCILIATION-SPE4A625PK654"
type: "finding"
title: "SPE4A625PK654: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625PK654: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A625PK654",
  "history_quantity": "240.000",
  "history_unit_cost": "1.44000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "345.6",
  "product": "345.60000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625PK654]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_prior_history_row: [[DISC-PRICE-HISTORY-06]] — documented_fact (BOLT-E-3f9dbcf9b90c5bb65af6); sources: [[BOLT-SRC-award-SPE4A625PK654]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_award: [[BOLT-AWARD-SPE4A625PK654]] — documented_fact (BOLT-E-d4ac4b5a30c456186235); sources: [[BOLT-SRC-award-SPE4A625PK654]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-074e2616100ba275ff16); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625PK654]] — documented_fact (edge-2613f84d1618a908d811); sources: [[BOLT-SRC-award-SPE4A625PK654]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-a361ad6836230c3b6aa9)
