---
id: "BOLT-AWARD-SPE4A625V346U"
type: "award_observation"
title: "SPE4A625V346U: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V346U: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2025-06-16",
    "description": "8511447838!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A625V346U_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A625V346U",
    "recipient_name_as_reported": "SUBURBAN BOLT & SUPPLY CO",
    "recipient_uei": "JE5NG1MWNU77",
    "solicitation_identifier": "SPE4A625T99L1",
    "source_reports_competition": "COMPETED UNDER SAP",
    "source_reports_offers": "5",
    "source_reports_pricing": "FIRM FIXED PRICE",
    "total_outlay": null
  },
  "source_scope": "Award summary and latest contract transaction, not priced line item or invoice",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V346U]]

## Outgoing relationships

- reports_obligation: [[BOLT-OBLIGATION-SPE4A625V346U]] — documented_fact (BOLT-E-24a596ac16abc410da0b); sources: [[BOLT-SRC-award-SPE4A625V346U]]
- history_reports_cage: [[DISC-CAGE-7W108]] — documented_fact (BOLT-E-2d36d6b5adea7c54173c); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- source_reports_award_recipient: [[BOLT-SUPPLIER-7W108]] — documented_fact (BOLT-E-7ba3f9d10355b2000936); sources: [[BOLT-SRC-award-SPE4A625V346U]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V346U]] — documented_fact (edge-94b8e9689fbd76deaf8d); sources: [[BOLT-SRC-award-SPE4A625V346U]]

## Backlinks

- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-70041fe0f6709e1f7538)
- [[BOLT-RECONCILIATION-SPE4A625V346U]]: checks_award — documented_fact (BOLT-E-76b8d06397c54afe8f27)
