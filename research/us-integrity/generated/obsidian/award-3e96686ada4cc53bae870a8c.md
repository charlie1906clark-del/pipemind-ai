---
id: "award-3e96686ada4cc53bae870a8c"
type: "award"
title: "P30CA008748"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# P30CA008748

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/ASST_NON_P30CA008748_075/latest",
  "money": {
    "amount": "263969535.79",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Assistance Listings": [
      {
        "cfda_number": "93.353",
        "cfda_program_title": "21ST CENTURY CURES ACT - BEAU BIDEN CANCER MOONSHOT"
      },
      {
        "cfda_number": "93.360",
        "cfda_program_title": "BIOMEDICAL ADVANCED RESEARCH AND DEVELOPMENT AUTHORITY (BARDA), BIODEFENSE MEDICAL COUNTERMEASURE DEVELOPMENT"
      },
      {
        "cfda_number": "93.394",
        "cfda_program_title": "CANCER DETECTION AND DIAGNOSIS RESEARCH"
      },
      {
        "cfda_number": "93.395",
        "cfda_program_title": "CANCER TREATMENT RESEARCH"
      },
      {
        "cfda_number": "93.397",
        "cfda_program_title": "CANCER CENTERS SUPPORT GRANTS"
      },
      {
        "cfda_number": "93.701",
        "cfda_program_title": "TRANS-NIH RECOVERY ACT RESEARCH SUPPORT"
      }
    ],
    "Award ID": "P30CA008748",
    "Awarding Agency": "Department of Health and Human Services",
    "Awarding Agency Code": "075",
    "Awarding Sub Agency": "National Institutes of Health",
    "Awarding Sub Agency Code": "7529",
    "Description": "CANCER CENTER SUPPORT GRANT",
    "End Date": "2026-03-31",
    "Place of Performance State Code": "NY",
    "Recipient UEI": "KUKXRCZ6NZC2",
    "Start Date": "1997-01-20",
    "Total Outlays": 64600674.96,
    "agency_slug": "department-of-health-and-human-services",
    "awarding_agency_id": 806,
    "generated_internal_id": "ASST_NON_P30CA008748_075",
    "internal_id": 269956119,
    "recipient_id": "b514fc3a-d769-87e9-75ea-7a6766afb5ee-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-nih-grants]]

## Outgoing relationships

- reported_recipient: [[uei-KUKXRCZ6NZC2]] — documented_fact (edge-0b5dbbb534a2932ed586); sources: [[src-live-nih-grants]]
- place_of_performance: [[geo-us-NY]] — documented_fact (edge-c5639ac701264f6afd45); sources: [[src-live-nih-grants]]
- cites: [[src-live-nih-grants]] — documented_fact (edge-e9bcef42538b2d0758fd); sources: [[src-live-nih-grants]]

## Backlinks

- [[cohort-nih-grants]]: includes_award — documented_fact (edge-2dbe3ca787af391b6c8d)
- [[agency-075]]: awards — documented_fact (edge-566094b7cd1dfb29be63)
