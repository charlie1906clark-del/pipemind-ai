---
id: "BOLT-AWARD-SPE4A625V252D"
type: "award_observation"
title: "SPE4A625V252D: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V252D: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2025-05-16",
    "description": "8511387851!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A625V252D_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A625V252D",
    "recipient_name_as_reported": "KAREN CARLISLE",
    "recipient_uei": "KJGWN783BNB5",
    "solicitation_identifier": "SPE4A625T61G7",
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

- [[BOLT-SRC-award-SPE4A625V252D]]

## Outgoing relationships

- history_reports_cage: [[DISC-CAGE-8A1E8]] — documented_fact (BOLT-E-69421516fbce64029704); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- source_reports_award_recipient: [[BOLT-SUPPLIER-8A1E8]] — documented_fact (BOLT-E-70e61424364a14bbbdbb); sources: [[BOLT-SRC-award-SPE4A625V252D]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- reports_obligation: [[BOLT-OBLIGATION-SPE4A625V252D]] — documented_fact (BOLT-E-b0393c09d5471dca046f); sources: [[BOLT-SRC-award-SPE4A625V252D]]
- cites: [[BOLT-SRC-award-SPE4A625V252D]] — documented_fact (edge-9ea05bdfb7730a3d2766); sources: [[BOLT-SRC-award-SPE4A625V252D]]

## Backlinks

- [[BOLT-RECONCILIATION-SPE4A625V252D]]: checks_award — documented_fact (BOLT-E-07b969d79a364342dc60)
- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-e0bdcb40dd8297c8b1ce)
