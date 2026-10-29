---
id: "award-debf039f96875372dbdcd6a1"
type: "award"
title: "36C24824C0045"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 36C24824C0045

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_36C24824C0045_3600_-NONE-_-NONE-/latest",
  "money": {
    "amount": "22544138.28",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "36C24824C0045",
    "Awarding Agency": "Department of Veterans Affairs",
    "Awarding Agency Code": "036",
    "Awarding Sub Agency": "Department of Veterans Affairs",
    "Awarding Sub Agency Code": "3600",
    "Description": "SCOPE LEASE PROGRAM",
    "End Date": "2027-09-30",
    "PSC": {
      "code": "6515",
      "description": "MEDICAL AND SURGICAL INSTRUMENTS, EQUIPMENT, AND SUPPLIES"
    },
    "Place of Performance State Code": "FL",
    "Recipient UEI": "FLWQVLFLMEL3",
    "Start Date": "2024-04-01",
    "Total Outlays": null,
    "agency_slug": "department-of-veterans-affairs",
    "awarding_agency_id": 561,
    "generated_internal_id": "CONT_AWD_36C24824C0045_3600_-NONE-_-NONE-",
    "internal_id": 280152746,
    "recipient_id": "a757e8e0-8720-428e-64bc-1d025227406d-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-medical-supplies]]

## Outgoing relationships

- place_of_performance: [[geo-us-FL]] — documented_fact (edge-1602bca82373dc13adcd); sources: [[src-live-medical-supplies]]
- cites: [[src-live-medical-supplies]] — documented_fact (edge-ad323aa175511bf912d8); sources: [[src-live-medical-supplies]]
- reported_recipient: [[uei-FLWQVLFLMEL3]] — documented_fact (edge-b9a53a1f1f039017d487); sources: [[src-live-medical-supplies]]

## Backlinks

- [[agency-036]]: awards — documented_fact (edge-67281e788e6023aecd67)
- [[cohort-medical-supplies]]: includes_award — documented_fact (edge-fffff68cc661b22ad816)
