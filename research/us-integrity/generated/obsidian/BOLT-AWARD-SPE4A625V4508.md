---
id: "BOLT-AWARD-SPE4A625V4508"
type: "award_observation"
title: "SPE4A625V4508: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V4508: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2024-12-04",
    "description": "8511055897!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A625V4508_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A625V4508",
    "recipient_name_as_reported": "KAREN CARLISLE",
    "recipient_uei": "KJGWN783BNB5",
    "solicitation_identifier": "SPE4A625T131Y",
    "source_reports_competition": "COMPETED UNDER SAP",
    "source_reports_offers": "4",
    "source_reports_pricing": "FIRM FIXED PRICE",
    "total_outlay": null
  },
  "source_scope": "Award summary and latest contract transaction, not priced line item or invoice",
  "visibility": "public"
}
```

## Sources

- [[BOLT-SRC-award-SPE4A625V4508]]

## Outgoing relationships

- reports_obligation: [[BOLT-OBLIGATION-SPE4A625V4508]] — documented_fact (BOLT-E-b488b607c018fd668b13); sources: [[BOLT-SRC-award-SPE4A625V4508]]
- source_reports_award_recipient: [[BOLT-SUPPLIER-8A1E8]] — documented_fact (BOLT-E-d30f6e359e59ee0d3714); sources: [[BOLT-SRC-award-SPE4A625V4508]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- history_reports_cage: [[DISC-CAGE-8A1E8]] — documented_fact (BOLT-E-eb0a1e163c768f5a84d7); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V4508]] — documented_fact (edge-e597946baeba1ab9e674); sources: [[BOLT-SRC-award-SPE4A625V4508]]

## Backlinks

- [[BOLT-RECONCILIATION-SPE4A625V4508]]: checks_award — documented_fact (BOLT-E-0b862981970a42c3864d)
- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-7b70a113a7ccce01bf1f)
