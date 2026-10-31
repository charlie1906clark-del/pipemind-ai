---
id: "DISC-PRICE-HISTORY-06"
type: "historical_price_observation"
title: "SPE4A625PK654: printed history unit cost 1.44000"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625PK654: printed history unit cost 1.44000

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "current_terms_not_backfilled": true,
  "missing_terms_are_unknown": true,
  "no_overpricing_verdict": true,
  "record": {
    "award_date": "2025-03-24",
    "cage": "51Y73",
    "comparable_price_verified": false,
    "contract_number": "SPE4A625PK654",
    "currency_explicit_in_history_table": null,
    "evidence_kind": "solicitation_disclosed_procurement_history",
    "historical_delivery_terms": null,
    "historical_nonrecurring_costs": null,
    "historical_pack_quantity": null,
    "historical_revision": null,
    "historical_unit_of_issue": null,
    "invoice_or_payment_verified": false,
    "nsn": "5306016864912",
    "quantity_as_printed": "240.000",
    "source_page": 8,
    "surplus_material_flag": "N",
    "unit_cost_as_printed": "1.44000"
  },
  "source_record": "pricing/snapshots/selected_evidence.json",
  "visibility": "public"
}
```

## Sources

- [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Outgoing relationships

- reports_supplier_identifier: [[DISC-CAGE-51Y73]] — documented_fact (DISC-E-371e26693069bd90673d); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- references_item: [[DISC-NSN-5306016864912]] — documented_fact (DISC-E-89042b589b4e76bf3a75); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]] — documented_fact (edge-eb78ea5e181b10196d15); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]

## Backlinks

- [[BOLT-RECONCILIATION-SPE4A625PK654]]: checks_prior_history_row — documented_fact (BOLT-E-3f9dbcf9b90c5bb65af6)
- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-e8fc2e26abc8e456fc17)
