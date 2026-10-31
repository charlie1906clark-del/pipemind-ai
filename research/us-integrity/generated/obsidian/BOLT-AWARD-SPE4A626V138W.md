---
id: "BOLT-AWARD-SPE4A626V138W"
type: "award_observation"
title: "SPE4A626V138W: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626V138W: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2026-05-26",
    "description": "8512122584!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A626V138W_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A626V138W",
    "recipient_name_as_reported": "BUTT FAREED AHMAD",
    "recipient_uei": "GWEEKJ2PNL45",
    "solicitation_identifier": "SPE4A626T52U3",
    "source_reports_competition": "COMPETED UNDER SAP",
    "source_reports_offers": "3",
    "source_reports_pricing": "FIRM FIXED PRICE",
    "total_outlay": null
  },
  "source_scope": "Award summary and latest contract transaction, not priced line item or invoice",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A626V138W]]

## Outgoing relationships

- reports_obligation: [[BOLT-OBLIGATION-SPE4A626V138W]] — documented_fact (BOLT-E-09ea5f11d2c1315a5389); sources: [[BOLT-SRC-award-SPE4A626V138W]]
- source_reports_award_recipient: [[BOLT-SUPPLIER-6ZF42]] — documented_fact (BOLT-E-a88cfe78940bd2c61d1f); sources: [[BOLT-SRC-award-SPE4A626V138W]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- history_reports_cage: [[DISC-CAGE-6ZF42]] — documented_fact (BOLT-E-b6d2a52ec9ab8765bca9); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A626V138W]] — documented_fact (edge-904ea742494dfedf3f6d); sources: [[BOLT-SRC-award-SPE4A626V138W]]

## Backlinks

- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-3d5c71ceea42ed563253)
- [[BOLT-RECONCILIATION-SPE4A626V138W]]: checks_award — documented_fact (BOLT-E-d40d807bdba40eca1eac)
