---
id: "DISC-NAME-COHORT-amazon-dot"
type: "dataset_cohort"
title: "Literal keyword Amazon.: bounded contract-query cohort"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Literal keyword Amazon.: bounded contract-query cohort

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
    "after_count": 12,
    "award_rows": 12,
    "award_terminal_empty_page": true,
    "before_count": 12,
    "complete_for_bounded_query": true,
    "keyword": "Amazon.",
    "recipient_profiles": 2,
    "recipient_terminal_empty_page": true,
    "unique_awards": true
  },
  "scope": "Two literal recipient keywords, contract recipients and FY2026 prime contracts; no national entity census",
  "visibility": "public"
}
```

## Sources

- [[DISC-NAME-SRC-amazon-dot-awards-1]]
- [[DISC-NAME-SRC-amazon-dot-awards-2]]
- [[DISC-NAME-SRC-amazon-dot-count-after]]
- [[DISC-NAME-SRC-amazon-dot-count-before]]
- [[DISC-NAME-SRC-amazon-dot-recipients-1]]
- [[DISC-NAME-SRC-amazon-dot-recipients-2]]

## Outgoing relationships

- cites: [[DISC-NAME-SRC-amazon-dot-awards-1]] — documented_fact (edge-13b2d4a1ac5c0e9f073c); sources: [[DISC-NAME-SRC-amazon-dot-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-before]] — documented_fact (edge-237e2ad71581763781b6); sources: [[DISC-NAME-SRC-amazon-dot-count-before]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-after]] — documented_fact (edge-371b27c868cb6019c95d); sources: [[DISC-NAME-SRC-amazon-dot-count-after]]
- cites: [[DISC-NAME-SRC-amazon-dot-awards-2]] — documented_fact (edge-745d78fa51cc91cb9a62); sources: [[DISC-NAME-SRC-amazon-dot-awards-2]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-1]] — documented_fact (edge-9a2478ba50b3ce5c217a); sources: [[DISC-NAME-SRC-amazon-dot-recipients-1]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-2]] — documented_fact (edge-d37426a29aa024d229b9); sources: [[DISC-NAME-SRC-amazon-dot-recipients-2]]

## Backlinks

- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-e8e1bb4bde3c965c7f0d)
