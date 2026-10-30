---
id: "award-98a33037f9dafbcbfe6f43ed"
type: "award"
title: "36C79126N0016"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 36C79126N0016

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_36C79126N0016_3600_36C79121D0007_3600/latest",
  "money": {
    "amount": "44587943.3",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "36C79126N0016",
    "Awarding Agency": "Department of Veterans Affairs",
    "Awarding Agency Code": "036",
    "Awarding Sub Agency": "Department of Veterans Affairs",
    "Awarding Sub Agency Code": "3600",
    "Description": "POSITIVE AIRWAY PRESSURE DEVICES 90 DAY DELIVERY.",
    "End Date": "2026-05-14",
    "PSC": {
      "code": "6515",
      "description": "MEDICAL AND SURGICAL INSTRUMENTS, EQUIPMENT, AND SUPPLIES"
    },
    "Place of Performance State Code": "FL",
    "Recipient UEI": "Z3BPH2N9K1L9",
    "Start Date": "2026-02-14",
    "Total Outlays": 44480419.2,
    "agency_slug": "department-of-veterans-affairs",
    "awarding_agency_id": 561,
    "generated_internal_id": "CONT_AWD_36C79126N0016_3600_36C79121D0007_3600",
    "internal_id": 356476327,
    "recipient_id": "48b0e8ee-5d59-6197-6d43-8871927ecab0-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-medical-supplies]]

## Outgoing relationships

- place_of_performance: [[geo-us-FL]] — documented_fact (edge-059d5e3d9a2bdafc0032); sources: [[src-live-medical-supplies]]
- reported_recipient: [[uei-Z3BPH2N9K1L9]] — documented_fact (edge-aff26cb904ef4486a651); sources: [[src-live-medical-supplies]]
- cites: [[src-live-medical-supplies]] — documented_fact (edge-ca4ccd56a473afe035ec); sources: [[src-live-medical-supplies]]

## Backlinks

- [[cohort-medical-supplies]]: includes_award — documented_fact (edge-c5fa1bdf5cf3eb2ce3fa)
- [[agency-036]]: awards — documented_fact (edge-f05665c6c9e1bc9ff0ad)
