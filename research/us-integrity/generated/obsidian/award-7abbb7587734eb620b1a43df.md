---
id: "award-7abbb7587734eb620b1a43df"
type: "award"
title: "36C10X26K0559"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# 36C10X26K0559

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/CONT_AWD_36C10X26K0559_3600_36C10X23D0032_3600/latest",
  "money": {
    "amount": "82387714.43",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Award ID": "36C10X26K0559",
    "Awarding Agency": "Department of Veterans Affairs",
    "Awarding Agency Code": "036",
    "Awarding Sub Agency": "Department of Veterans Affairs",
    "Awarding Sub Agency Code": "3600",
    "Description": "EXPRESS REPORT: MEDICAL SURGICAL PRIME VENDOR EXPENDITURES FOR THE MONTH OF AUG 2026",
    "End Date": "2026-08-31",
    "PSC": {
      "code": "6515",
      "description": "MEDICAL AND SURGICAL INSTRUMENTS, EQUIPMENT, AND SUPPLIES"
    },
    "Place of Performance State Code": "IL",
    "Recipient UEI": "DMPAKJ9N9K66",
    "Start Date": "2026-08-01",
    "Total Outlays": null,
    "agency_slug": "department-of-veterans-affairs",
    "awarding_agency_id": 561,
    "generated_internal_id": "CONT_AWD_36C10X26K0559_3600_36C10X23D0032_3600",
    "internal_id": 362600239,
    "recipient_id": "e69126ba-ae4e-13a4-4552-7eae9f4ad09d-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-medical-supplies]]

## Outgoing relationships

- reported_recipient: [[uei-DMPAKJ9N9K66]] — documented_fact (edge-156329f99f3694ee4480); sources: [[src-live-medical-supplies]]
- place_of_performance: [[geo-us-IL]] — documented_fact (edge-555ca46907cd40dbe392); sources: [[src-live-medical-supplies]]
- cites: [[src-live-medical-supplies]] — documented_fact (edge-d8872db121efb8d174d9); sources: [[src-live-medical-supplies]]

## Backlinks

- [[agency-036]]: awards — documented_fact (edge-3722311f086e52c3f2ad)
- [[cohort-medical-supplies]]: includes_award — documented_fact (edge-38ac9b11b9baafa83d12)
