---
id: "BOLT-AWARD-SPE4A626P5931"
type: "award_observation"
title: "SPE4A626P5931: official award observation"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPE4A626P5931: official award observation

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_adverse_inference": true,
  "observation": {
    "cash_payment_verified": false,
    "date_signed": "2025-11-14",
    "description": "8511753268!BOLT,MACHINE",
    "generated_award_id": "CONT_AWD_SPE4A626P5931_9700_-NONE-_-NONE-",
    "historical_clin_acquired": false,
    "instrument": "PURCHASE ORDER",
    "piid": "SPE4A626P5931",
    "recipient_name_as_reported": "DIALOGIC CORP",
    "recipient_uei": "JEJSN59MQVK3",
    "solicitation_identifier": "SPE4A626T8303",
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

- [[BOLT-SRC-award-SPE4A626P5931]]

## Outgoing relationships

- source_reports_award_recipient: [[BOLT-SUPPLIER-0NFB8]] — documented_fact (BOLT-E-2dc5ccd766638163e877); sources: [[BOLT-SRC-award-SPE4A626P5931]], [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- history_reports_cage: [[DISC-CAGE-0NFB8]] — documented_fact (BOLT-E-3144cde92e35c48ade15); sources: [[DISC-PRICE-SRC-DLA-SPE4A626U3619]]
- reports_obligation: [[BOLT-OBLIGATION-SPE4A626P5931]] — documented_fact (BOLT-E-3e341ff924321a1ac85e); sources: [[BOLT-SRC-award-SPE4A626P5931]]
- cites: [[BOLT-SRC-award-SPE4A626P5931]] — documented_fact (edge-55c6fd703b69afa57f33); sources: [[BOLT-SRC-award-SPE4A626P5931]]

## Backlinks

- [[BOLT-AWARD-COVERAGE]]: includes_award_observation — documented_fact (BOLT-E-7cce4335c50dbce93380)
- [[BOLT-RECONCILIATION-SPE4A626P5931]]: checks_award — documented_fact (BOLT-E-a1d2385782d25057612b)
