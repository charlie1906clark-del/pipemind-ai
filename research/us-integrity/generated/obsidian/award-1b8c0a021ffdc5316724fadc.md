---
id: "award-1b8c0a021ffdc5316724fadc"
type: "award"
title: "36C10X26K0175"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 36C10X26K0175

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_36C10X26K0175_3600_36C10X23D0032_3600/latest",
  "money": {
    "amount": "77635361.93",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "36C10X26K0175",
    "Awarding Agency": "Department of Veterans Affairs",
    "Awarding Agency Code": "036",
    "Awarding Sub Agency": "Department of Veterans Affairs",
    "Awarding Sub Agency Code": "3600",
    "Description": "EXPRESS REPORT: MEDICAL SURGICAL PRIME VENDOR EXPENDITURES FOR THE MONTH OF MARCH 2026",
    "End Date": "2026-03-31",
    "PSC": {
      "code": "6515",
      "description": "MEDICAL AND SURGICAL INSTRUMENTS, EQUIPMENT, AND SUPPLIES"
    },
    "Place of Performance State Code": "IL",
    "Recipient UEI": "DMPAKJ9N9K66",
    "Start Date": "2026-03-01",
    "Total Outlays": null,
    "agency_slug": "department-of-veterans-affairs",
    "awarding_agency_id": 561,
    "generated_internal_id": "CONT_AWD_36C10X26K0175_3600_36C10X23D0032_3600",
    "internal_id": 357339907,
    "recipient_id": "e69126ba-ae4e-13a4-4552-7eae9f4ad09d-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-medical-supplies]]

## Outgoing relationships

- place_of_performance: [[geo-us-IL]] — documented_fact (edge-2359c578a78c9e0a38e9); sources: [[src-live-medical-supplies]]
- reported_recipient: [[uei-DMPAKJ9N9K66]] — documented_fact (edge-30a04a416ac1f1123cdb); sources: [[src-live-medical-supplies]]
- cites: [[src-live-medical-supplies]] — documented_fact (edge-76727263701257bb38b3); sources: [[src-live-medical-supplies]]

## Backlinks

- [[cohort-medical-supplies]]: includes_award — documented_fact (edge-3bb5b5db0fc5d1165aae)
- [[agency-036]]: awards — documented_fact (edge-dcf0d2a4616628ffc8f7)
