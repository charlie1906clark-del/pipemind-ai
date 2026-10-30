---
id: "award-f8c47e1ceba7feda93d6217f"
type: "award"
title: "P51OD010425"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# P51OD010425

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "api_detail_url": "https://www.usaspending.gov/award/ASST_NON_P51OD010425_075/latest",
  "money": {
    "amount": "201841608.0",
    "currency": "USD",
    "kind": "cumulative_award_amount_not_fy_spend"
  },
  "no_fraud_assessment": true,
  "ownership": "not_traced",
  "source_record": {
    "Assistance Listings": [
      {
        "cfda_number": "93.310",
        "cfda_program_title": "TRANS-NIH RESEARCH SUPPORT"
      },
      {
        "cfda_number": "93.351",
        "cfda_program_title": "RESEARCH INFRASTRUCTURE PROGRAMS"
      },
      {
        "cfda_number": "93.866",
        "cfda_program_title": "AGING RESEARCH"
      }
    ],
    "Award ID": "P51OD010425",
    "Awarding Agency": "Department of Health and Human Services",
    "Awarding Agency Code": "075",
    "Awarding Sub Agency": "National Institutes of Health",
    "Awarding Sub Agency Code": "7529",
    "Description": "WASHINGTON NATIONAL PRIMATE RESEARCH CENTER",
    "End Date": "2027-04-30",
    "Place of Performance State Code": "WA",
    "Recipient UEI": "HD1WMN6945W6",
    "Start Date": "1997-06-10",
    "Total Outlays": 58777981.81,
    "agency_slug": "department-of-health-and-human-services",
    "awarding_agency_id": 806,
    "generated_internal_id": "ASST_NON_P51OD010425_075",
    "internal_id": 270012924,
    "recipient_id": "8a022699-f7be-356a-f01a-3aa6f76016ef-C"
  },
  "subaward_chain": "not_acquired",
  "visibility": "public"
}
```

## Sources

- [[src-live-nih-grants]]

## Outgoing relationships

- place_of_performance: [[geo-us-WA]] — documented_fact (edge-6ad6407a7e4f20e38d31); sources: [[src-live-nih-grants]]
- reported_recipient: [[uei-HD1WMN6945W6]] — documented_fact (edge-9037cf2c1e24fb31630a); sources: [[src-live-nih-grants]]
- cites: [[src-live-nih-grants]] — documented_fact (edge-92e748fd9960cbd6fa72); sources: [[src-live-nih-grants]]

## Backlinks

- [[cohort-nih-grants]]: includes_award — documented_fact (edge-f492e5177ddfc9c53070)
- [[agency-075]]: awards — documented_fact (edge-ff1270a254fd9d338e0d)
