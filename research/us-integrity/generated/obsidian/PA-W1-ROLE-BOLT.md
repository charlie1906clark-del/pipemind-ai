---
id: "PA-W1-ROLE-BOLT"
type: "research_task_definition"
title: "Trace a documented professional decision role"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Trace a documented professional decision role

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-DECISION",
    "allowed_source_hosts": [
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "sam.gov",
      "www.gao.gov",
      "www.oversight.gov"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "The named signatory only processed or witnessed the document.",
      "A different official, office or effective period made the relevant choice."
    ],
    "expected_output": [
      "role-to-decision evidence",
      "signatory versus decision-maker distinction",
      "event/effective/observation dates",
      "unresolved authority edges"
    ],
    "id": "PA-W1-ROLE-BOLT",
    "independent_review_required": true,
    "invalid_inference": "No family, residence, social-friendship or surname profiling; a signature does not establish improper influence.",
    "max_attempts": 8,
    "max_evidence": 16,
    "max_reopens": 2,
    "question": "Which released record actually attributes the relevant supplier/price decision to an office or professional role?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "maximum_relevant_professional_roles": 3,
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "prohibited": "No residential, personal-contact, family or speculative friendship investigation.",
      "required": [
        "documented role",
        "specific decision",
        "effective/event dates",
        "source locator"
      ]
    },
    "stop_and_reopen": "Stop person linkage without dated professional evidence; reopen with the specific decision/assignment record.",
    "title": "Trace a documented professional decision role"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-DECISION]] — planned (PA-E-c799d8da9a636a5e1250eede); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-466cf5373069aafefcec); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-fd82a56f6f25044d0632); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-W1-BENEFIT-BOLT]]: requires_accepted_packet — planned (PA-E-06dfc675d66ebf9f5c7bbd6b)
- [[PA-RUNSTATE-PA-W1-ROLE-BOLT]]: observes_task_state — documented_fact (PA-E-24a034ae3059054695d398db)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-70859ddc324e1be1b4fede4e)
