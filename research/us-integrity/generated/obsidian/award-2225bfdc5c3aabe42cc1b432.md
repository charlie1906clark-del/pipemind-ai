---
id: "award-2225bfdc5c3aabe42cc1b432"
type: "award"
title: "36C10G24N0114"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 36C10G24N0114

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_36C10G24N0114_3600_36C10G24D0048_3600/latest",
  "money": {
    "amount": "37763890.87",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "36C10G24N0114",
    "Awarding Agency": "Department of Veterans Affairs",
    "Awarding Agency Code": "036",
    "Awarding Sub Agency": "Department of Veterans Affairs",
    "Awarding Sub Agency Code": "3600",
    "Description": "PATIENT VIDEO TABLET DATA MAINTENANCE SUPPORT (PVT-DMS)",
    "End Date": "2027-08-31",
    "PSC": {
      "code": "6515",
      "description": "MEDICAL AND SURGICAL INSTRUMENTS, EQUIPMENT, AND SUPPLIES"
    },
    "Place of Performance State Code": "VA",
    "Recipient UEI": "PULLHCE2VM13",
    "Start Date": "2024-09-01",
    "Total Outlays": null,
    "agency_slug": "department-of-veterans-affairs",
    "awarding_agency_id": 561,
    "generated_internal_id": "CONT_AWD_36C10G24N0114_3600_36C10G24D0048_3600",
    "internal_id": 279976983,
    "recipient_id": "028e2d7f-cbff-9566-abcd-0fa8199499cc-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-medical-supplies]]

## Outgoing relationships

- reported_recipient: [[uei-PULLHCE2VM13]] — documented_fact (edge-13c45c7a1b24b8cd04c0); sources: [[src-live-medical-supplies]]
- cites: [[src-live-medical-supplies]] — documented_fact (edge-1c86fcc4c63069fbf7ce); sources: [[src-live-medical-supplies]]
- place_of_performance: [[geo-us-VA]] — documented_fact (edge-a2d14ff23902eb63baae); sources: [[src-live-medical-supplies]]

## Backlinks

- [[agency-036]]: awards — documented_fact (edge-76d946e88e3d1509aaed)
- [[cohort-medical-supplies]]: includes_award — documented_fact (edge-a6b50481085eeafbf6ff)
