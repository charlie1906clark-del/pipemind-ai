---
id: "PA-W1-COHORT-VA"
type: "research_task_definition"
title: "VA finite official award sample"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# VA finite official award sample

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
    "id": "PA-W1-COHORT-VA",
    "independent_review_required": true,
    "invalid_inference": "Do not turn cumulative obligations into line prices or annual paid spend.",
    "max_attempts": 6,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Can the declared request be reproduced with exact keys and honest coverage? ",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "agency": "Department of Veterans Affairs",
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
    "title": "VA finite official award sample"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- records_result_packet: [[PA-RUNRESULT-PA-W1-COHORT-VA-RESULT-01]] — documented_fact (PA-E-29cf372609ac9e378a7647aa); sources: [[PA-SRC-LOCAL-RUN]]
- assigned_role: [[PA-ROLE-ACQUIRE]] — planned (PA-E-2cc54451db7378f834a51a6d); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-303c3ed646562ff15684); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-ce59cb4996e0b0442429); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-W1-LINE-VA]]: requires_accepted_packet — planned (PA-E-39f1c0c5b8f151c6cb3051b5)
- [[PA-RUNSTATE-PA-W1-COHORT-VA]]: observes_task_state — documented_fact (PA-E-56163d2c22b21d2155c50e25)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-c40b44cea6f54c6c3d5909f9)
