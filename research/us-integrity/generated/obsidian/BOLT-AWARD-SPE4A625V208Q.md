---
id: "BOLT-AWARD-SPE4A625V208Q"
type: "award_observation"
title: "SPE4A625V208Q: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625V208Q: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2025-04-30",
    "description": "8511353398!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A625V208Q_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A625V208Q",
    "recipient_name_as_reported": "BUTT FAREED AHMAD",
    "recipient_uei": "GWEEKJ2PNL45",
    "solicitation_identifier": "SPE4A625T52K8",
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

- [[BOLT-SRC-award-SPE4A625V208Q]]

## Outgoing relationships

- reports_obligation: [[BOLT-OBLIGATION-SPE4A625V208Q]] — documented_fact (BOLT-E-1e43ca3178f02708e192); sources: [[BOLT-SRC-award-SPE4A625V208Q]]
- source_reports_award_recipient: [[BOLT-SUPPLIER-6ZF42]] — documented_fact (BOLT-E-ac6de1c184e8dcb381db); sources: [[BOLT-SRC-award-SPE4A625V208Q]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- history_reports_cage: [[DISC-CAGE-6ZF42]] — documented_fact (BOLT-E-ae4ea67a860b0d1493f2); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625V208Q]] — documented_fact (edge-6f7a866c97135ca5df8b); sources: [[BOLT-SRC-award-SPE4A625V208Q]]

## Backlinks

- [[BOLT-RECONCILIATION-SPE4A625V208Q]]: checks_award — documented_fact (BOLT-E-172a741cd5ae739fc803)
- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-4ac051d762bafd390a9a)
