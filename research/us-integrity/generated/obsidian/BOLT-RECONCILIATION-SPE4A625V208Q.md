---
id: "BOLT-RECONCILIATION-SPE4A625V208Q"
type: "finding"
title: "SPE4A625V208Q: printed quantity × cost equals reported obligation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V208Q: printed quantity × cost equals reported obligation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "dates_match": true,
  "exact_contract_key": "SPE4A625V208Q",
  "history_quantity": "472.000",
  "history_unit_cost": "1.17000",
  "inference_limit": "Arithmetic and date agreement corroborate record consistency; they do not establish historical units, priced CLINs, delivery, invoicing or cash disbursement",
  "obligation_usd": "552.24",
  "product": "552.24000000",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V208Q]]
- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- checks_award: [[BOLT-AWARD-SPE4A625V208Q]] — documented_fact (BOLT-E-172a741cd5ae739fc803); sources: [[BOLT-SRC-award-SPE4A625V208Q]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- checks_prior_history_row: [[DISC-PRICE-HISTORY-05]] — documented_fact (BOLT-E-51188664a49e286aa68e); sources: [[BOLT-SRC-award-SPE4A625V208Q]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-5e562b4fc94c99b6d94d); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V208Q]] — documented_fact (edge-96d9d91dffd31768ec1f); sources: [[BOLT-SRC-award-SPE4A625V208Q]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — documented_fact (BOLT-E-7a6e72d40c1b6cae3855)
