---
id: "award-a82096c27d8d6aadeb4bf502"
type: "award"
title: "FA863425CB002"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# FA863425CB002

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_FA863425CB002_9700_-NONE-_-NONE-/latest",
  "money": {
    "amount": "348142000.41",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "FA863425CB002",
    "Awarding Agency": "Department of Defense",
    "Awarding Agency Code": "097",
    "Awarding Sub Agency": "Department of the Air Force",
    "Awarding Sub Agency Code": "5700",
    "Description": "F-15 EAGLE ACTIVE PASSIVE WARNING SURVIVABILITY SYSTEM (EPAWSS) FULL-RATE PRODUCTION (FRP)",
    "End Date": "2030-12-31",
    "PSC": {
      "code": "1680",
      "description": "MISCELLANEOUS AIRCRAFT ACCESSORIES AND COMPONENTS"
    },
    "Place of Performance State Code": "MO",
    "Recipient UEI": "MF2LE5RK6L84",
    "Start Date": "2025-01-06",
    "Total Outlays": null,
    "agency_slug": "department-of-defense",
    "awarding_agency_id": 1173,
    "generated_internal_id": "CONT_AWD_FA863425CB002_9700_-NONE-_-NONE-",
    "internal_id": 298560109,
    "recipient_id": "241d908a-e5e9-f275-b625-6b1f76859002-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-defense-parts]]

## Outgoing relationships

- place_of_performance: [[geo-us-MO]] — documented_fact (edge-3be759c4a604742a3200); sources: [[src-live-defense-parts]]
- reported_recipient: [[uei-MF2LE5RK6L84]] — documented_fact (edge-95810dcd0e02f7cda35c); sources: [[src-live-defense-parts]]
- cites: [[src-live-defense-parts]] — documented_fact (edge-d2359eedc54a027afec4); sources: [[src-live-defense-parts]]

## Backlinks

- [[agency-097]]: awards — documented_fact (edge-8020a542f145f62305a9)
- [[cohort-defense-parts]]: includes_award — documented_fact (edge-d6801103b08499acfc9e)
