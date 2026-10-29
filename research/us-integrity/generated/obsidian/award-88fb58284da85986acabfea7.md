---
id: "award-88fb58284da85986acabfea7"
type: "award"
title: "U10CA180886"
status: "documented_fact"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# U10CA180886

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/ASST_NON_U10CA180886_075/latest",
  "money": {
    "amount": "362114327.85",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Assistance Listings": [
      {
        "cfda_number": "93.360",
        "cfda_program_title": "BIOMEDICAL ADVANCED RESEARCH AND DEVELOPMENT AUTHORITY (BARDA), BIODEFENSE MEDICAL COUNTERMEASURE DEVELOPMENT"
      },
      {
        "cfda_number": "93.395",
        "cfda_program_title": "CANCER TREATMENT RESEARCH"
      }
    ],
    "Award ID": "U10CA180886",
    "Awarding Agency": "Department of Health and Human Services",
    "Awarding Agency Code": "075",
    "Awarding Sub Agency": "National Institutes of Health",
    "Awarding Sub Agency Code": "7529",
    "Description": "COG NCTN NETWORK GROUP OPERATIONS CENTER",
    "End Date": "2032-02-29",
    "Place of Performance State Code": "CA",
    "Recipient UEI": "Y8BQUVUFW8T6",
    "Start Date": "2014-04-11",
    "Total Outlays": 131387966.48,
    "agency_slug": "department-of-health-and-human-services",
    "awarding_agency_id": 806,
    "generated_internal_id": "ASST_NON_U10CA180886_075",
    "internal_id": 271681636,
    "recipient_id": "9fc8ae95-8621-4d46-35b5-a1fa62faa964-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-nih-grants]]

## Outgoing relationships

- reported_recipient: [[uei-Y8BQUVUFW8T6]] — documented_fact (edge-1d31732771a47a6abd3a); sources: [[src-live-nih-grants]]
- cites: [[src-live-nih-grants]] — documented_fact (edge-2283e4d3e1e30c2d5d7a); sources: [[src-live-nih-grants]]
- place_of_performance: [[geo-us-CA]] — documented_fact (edge-5bddf6397418121345a4); sources: [[src-live-nih-grants]]

## Backlinks

- [[cohort-nih-grants]]: includes_award — documented_fact (edge-068fc94a043cd14fb23a)
- [[agency-075]]: awards — documented_fact (edge-16da11753c6e34b33272)
