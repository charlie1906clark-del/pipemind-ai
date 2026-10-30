---
id: "PA-W1-COHORT-DLA"
type: "research_task_definition"
title: "DLA finite official award sample"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# DLA finite official award sample

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-ACQUIRE",
    "allowed_source_hosts": [
      "api.usaspending.gov",
      "www.usaspending.gov"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "A purported repeated pattern disappears after duplicate/modification reconciliation.",
      "The sample is too incomplete for the proposed population claim."
    ],
    "expected_output": [
      "request/response hashes",
      "unique award keys",
      "coverage and truncation",
      "included/excluded/failed rows"
    ],
    "id": "PA-W1-COHORT-DLA",
    "independent_review_required": true,
    "invalid_inference": "Do not turn cumulative obligations into line prices or annual paid spend.",
    "max_attempts": 6,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Can the declared request be reproduced with exact keys and honest coverage? ",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "agency": "Defense Logistics Agency",
      "agency_level": "subtier",
      "artifact_root": "investigations/federal-price-pilot-2026-10-30/",
      "claim": "No company is designated suspect by selection.",
      "coverage": "bounded first-page sample; not random or complete",
      "date_type": "new_awards_only",
      "end_date": "2026-07-31",
      "limit": 10,
      "maximum_deep_trace_records": 1,
      "page": 1,
      "psc": "5306",
      "reuse_existing_captures_before_network": true,
      "sort": "Award Amount descending",
      "start_date": "2026-07-03"
    },
    "stop_and_reopen": "Stop at declared page/request limits; reopen with an identified missing page or corrected query, never a new hidden selection.",
    "title": "DLA finite official award sample"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-ACQUIRE]] — planned (PA-E-be4730cf663e01f39dfefffb); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- records_result_packet: [[PA-RUNRESULT-PA-W1-COHORT-DLA-RESULT-01]] — documented_fact (PA-E-c4ccb49f64a44c8ff5ec92fa); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-50fe3e5b501529e3e8d0); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-7b6e9bf2f4cf4684a7a6); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-RUNSTATE-PA-W1-COHORT-DLA]]: observes_task_state — documented_fact (PA-E-07bedbe39a10af1475283b88)
- [[PA-W1-LINE-DLA]]: requires_accepted_packet — planned (PA-E-10b46f156fe6ab3e9ce877a1)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-8a95b59a470bf42d7bea03fd)
