---
id: "award-ed38c68a3bf481f2ec741d60"
type: "award"
title: "SPRPA119FE31N"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# SPRPA119FE31N

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_SPRPA119FE31N_9700_N0001915G0026_9700/latest",
  "money": {
    "amount": "876631383.68",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "SPRPA119FE31N",
    "Awarding Agency": "Department of Defense",
    "Awarding Agency Code": "097",
    "Awarding Sub Agency": "Defense Logistics Agency",
    "Awarding Sub Agency Code": "97AS",
    "Description": "COMPUTER,RADAR DATA",
    "End Date": "2029-05-13",
    "PSC": {
      "code": "1680",
      "description": "MISCELLANEOUS AIRCRAFT ACCESSORIES AND COMPONENTS"
    },
    "Place of Performance State Code": "FL",
    "Recipient UEI": "PK8PM2GNVMP8",
    "Start Date": "2019-09-23",
    "Total Outlays": null,
    "agency_slug": "department-of-defense",
    "awarding_agency_id": 1173,
    "generated_internal_id": "CONT_AWD_SPRPA119FE31N_9700_N0001915G0026_9700",
    "internal_id": 343243903,
    "recipient_id": "a398e5f8-3381-5983-2fb6-c60a3f701eb4-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-defense-parts]]

## Outgoing relationships

- place_of_performance: [[geo-us-FL]] — documented_fact (edge-aee09d1bb0ef457fd508); sources: [[src-live-defense-parts]]
- cites: [[src-live-defense-parts]] — documented_fact (edge-c291df31f8cb58316009); sources: [[src-live-defense-parts]]
- reported_recipient: [[uei-PK8PM2GNVMP8]] — documented_fact (edge-fc27971b853fa5081874); sources: [[src-live-defense-parts]]

## Backlinks

- [[agency-097]]: awards — documented_fact (edge-85b1f7d45cd05719ac9b)
- [[cohort-defense-parts]]: includes_award — documented_fact (edge-b0d4b1ff0784ec28eb73)
