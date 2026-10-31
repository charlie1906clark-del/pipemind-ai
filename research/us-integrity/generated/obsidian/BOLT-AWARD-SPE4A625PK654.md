---
id: "BOLT-AWARD-SPE4A625PK654"
type: "award_observation"
title: "SPE4A625PK654: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A625PK654: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2025-03-24",
    "description": "8511261286!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A625PK654_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A625PK654",
    "recipient_name_as_reported": "CASCADE NUT & BOLT, INC",
    "recipient_uei": "US4BABY42KV8",
    "solicitation_identifier": "SPE4A625T825F",
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

- [[BOLT-SRC-award-SPE4A625PK654]]

## Outgoing relationships

- source_reports_award_recipient: [[BOLT-SUPPLIER-51Y73]] — documented_fact (BOLT-E-06b8f665184da581798e); sources: [[BOLT-SRC-award-SPE4A625PK654]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- reports_obligation: [[BOLT-OBLIGATION-SPE4A625PK654]] — documented_fact (BOLT-E-7c202a5cc86350333c0c); sources: [[BOLT-SRC-award-SPE4A625PK654]]
- history_reports_cage: [[DISC-CAGE-51Y73]] — documented_fact (BOLT-E-dfd53de605d939dc0d11); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- cites: [[BOLT-SRC-award-SPE4A625PK654]] — documented_fact (edge-1edc46fa9be45844bea2); sources: [[BOLT-SRC-award-SPE4A625PK654]]

## Backlinks

- [[BOLT-RECONCILIATION-SPE4A625PK654]]: checks_award — documented_fact (BOLT-E-d4ac4b5a30c456186235)
- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-f5f02e7b975e9c01d9d0)
