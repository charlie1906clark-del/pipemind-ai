---
id: "DISC-NAME-COHORT-amazon"
type: "dataset_cohort"
title: "Literal keyword Amazon: bounded contract-query cohort"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Literal keyword Amazon: bounded contract-query cohort

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "all_nationwide_recipients": false,
  "amount_semantics": "Recipient trailing-twelve-month and award cumulative amounts have different scopes; no monetary sums made",
  "complete_for_bounded_query": true,
  "fraud_rank": false,
  "query": {
    "after_count": 150,
    "award_rows": 150,
    "award_terminal_empty_page": true,
    "before_count": 150,
    "complete_for_bounded_query": true,
    "keyword": "Amazon",
    "recipient_profiles": 6,
    "recipient_terminal_empty_page": true,
    "unique_awards": true
  },
  "scope": "Two literal recipient keywords, contract recipients and FY2026 prime contracts; no national entity census",
  "visibility": "public"
}
```

## Sources

- [[DISC-NAME-SRC-amazon-awards-1]]
- [[DISC-NAME-SRC-amazon-awards-2]]
- [[DISC-NAME-SRC-amazon-awards-3]]
- [[DISC-NAME-SRC-amazon-count-after]]
- [[DISC-NAME-SRC-amazon-count-before]]
- [[DISC-NAME-SRC-amazon-recipients-1]]
- [[DISC-NAME-SRC-amazon-recipients-2]]

## Outgoing relationships

- cites: [[DISC-NAME-SRC-amazon-awards-1]] — documented_fact (edge-334433cfffd3fab02544); sources: [[DISC-NAME-SRC-amazon-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-count-before]] — documented_fact (edge-597cc5bd99093ae78933); sources: [[DISC-NAME-SRC-amazon-count-before]]
- cites: [[DISC-NAME-SRC-amazon-awards-3]] — documented_fact (edge-9737bed3a6fb87e49668); sources: [[DISC-NAME-SRC-amazon-awards-3]]
- cites: [[DISC-NAME-SRC-amazon-count-after]] — documented_fact (edge-bd378d2e5ce43f777d39); sources: [[DISC-NAME-SRC-amazon-count-after]]
- cites: [[DISC-NAME-SRC-amazon-awards-2]] — documented_fact (edge-c1d9554212fe5f24af4f); sources: [[DISC-NAME-SRC-amazon-awards-2]]
- cites: [[DISC-NAME-SRC-amazon-recipients-2]] — documented_fact (edge-d57fa536b5c30284da17); sources: [[DISC-NAME-SRC-amazon-recipients-2]]
- cites: [[DISC-NAME-SRC-amazon-recipients-1]] — documented_fact (edge-f83754bb0ce6c418f39a); sources: [[DISC-NAME-SRC-amazon-recipients-1]]

## Backlinks

- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-a0ed2d433b3969fce613)
