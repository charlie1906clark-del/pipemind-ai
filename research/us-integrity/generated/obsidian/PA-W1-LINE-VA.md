---
id: "PA-W1-LINE-VA"
type: "research_task_definition"
title: "VA original transaction-line trace"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# VA original transaction-line trace

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-TRACE",
    "allowed_source_hosts": [
      "api.usaspending.gov",
      "www.usaspending.gov",
      "sam.gov",
      "www.vendorportal.ecms.va.gov",
      "department.va.gov"
    ],
    "depends_on": [
      "PA-W1-COHORT-VA"
    ],
    "disconfirmation_tests": [
      "The linked document belongs to another award, time, item or superseded revision.",
      "The apparent price comes from a ceiling, estimate or duplicate snapshot."
    ],
    "expected_output": [
      "URL frontier with parent and relationship",
      "original line/CLIN locators",
      "amendment chronology",
      "inaccessible record ledger"
    ],
    "id": "PA-W1-LINE-VA",
    "independent_review_required": true,
    "invalid_inference": "Never invent document URLs or treat a search result as acquired content.",
    "max_attempts": 10,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Does one source-available selected award expose a priced line, exact item and applicable order terms?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "access_scope": "Public records only; no login/key recovery or external requests.",
      "agency": "Department of Veterans Affairs",
      "agency_level": "toptier",
      "artifact_root": "investigations/federal-price-pilot-2026-10-30/",
      "claim": "No company is designated suspect by selection.",
      "coverage": "bounded first-page sample; not random or complete",
      "date_type": "new_awards_only",
      "end_date": "2026-07-31",
      "limit": 10,
      "line_limit": 3,
      "maximum_deep_trace_records": 1,
      "page": 1,
      "psc": "6515",
      "required_join": [
        "agency namespace",
        "PIID",
        "parent/order",
        "modification",
        "CLIN",
        "source locator"
      ],
      "reuse_existing_captures_before_network": true,
      "selection": "Use pilot documented deterministic source-availability selection; disclose every skipped candidate.",
      "sort": "Award Amount descending",
      "start_date": "2026-07-03",
      "tracer_contract": "../tracing/"
    },
    "stop_and_reopen": "Stop at host/path/request limits or access controls; reopen on an actual published relevant URL or new public version.",
    "title": "VA original transaction-line trace"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-COHORT-VA]] — planned (PA-E-39f1c0c5b8f151c6cb3051b5); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-TRACE]] — planned (PA-E-c48a035643cfec25b3d93251); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-001863887d0fa2444ec1); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-40f97baf24693f2101d3); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-2b889f548fb32181ae4618c1)
- [[PA-RUNSTATE-PA-W1-LINE-VA]]: observes_task_state — documented_fact (PA-E-5edb52af42091d117f5d093b)
- [[PA-W1-CURATE]]: requires_accepted_packet — planned (PA-E-e8db20f796b6012cab5e0c0e)
