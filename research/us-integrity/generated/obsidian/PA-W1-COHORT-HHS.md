---
id: "PA-W1-COHORT-HHS"
type: "research_task_definition"
title: "HHS finite official award sample"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# HHS finite official award sample

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
    "id": "PA-W1-COHORT-HHS",
    "independent_review_required": true,
    "invalid_inference": "Do not turn cumulative obligations into line prices or annual paid spend.",
    "max_attempts": 6,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Can the declared request be reproduced with exact keys and honest coverage? ",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "agency": "Department of Health and Human Services",
      "agency_level": "toptier",
      "artifact_root": "investigations/federal-price-pilot-2026-10-30/",
      "claim": "No company is designated suspect by selection.",
      "coverage": "bounded first-page sample; not random or complete",
      "date_type": "new_awards_only",
      "end_date": "2026-07-31",
      "limit": 10,
      "maximum_deep_trace_records": 1,
      "page": 1,
      "psc": "6515",
      "reuse_existing_captures_before_network": true,
      "sort": "Award Amount descending",
      "start_date": "2026-07-03"
    },
    "stop_and_reopen": "Stop at declared page/request limits; reopen with an identified missing page or corrected query, never a new hidden selection.",
    "title": "HHS finite official award sample"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- records_result_packet: [[PA-RUNRESULT-PA-W1-COHORT-HHS-RESULT-01]] — documented_fact (PA-E-6ef0c9b413aff0c2019e4585); sources: [[PA-SRC-LOCAL-RUN]]
- assigned_role: [[PA-ROLE-ACQUIRE]] — planned (PA-E-7107104bd6976a3654e6a677); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-ad55262f064bc113e02b); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-c288462741d3c79c9fdd); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-W1-LINE-HHS]]: requires_accepted_packet — planned (PA-E-59bc64da4ebc8349ad46885f)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-6087baa9af0c0befb3a6a91d)
- [[PA-RUNSTATE-PA-W1-COHORT-HHS]]: observes_task_state — documented_fact (PA-E-e14f0d74119c67e12d9b05bd)
