---
id: "PA-W1-BIDS-BOLT"
type: "research_task_definition"
title: "Recover actual competition and selection evidence"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Recover actual competition and selection evidence

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-COMPETE",
    "allowed_source_hosts": [
      "api.usaspending.gov",
      "www.usaspending.gov",
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "sam.gov",
      "www.acquisition.gov"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "Independent dated competitive quotations and documented acceptability explain selection.",
      "Apparent rotation vanishes after lot, capacity, eligibility or specialization controls."
    ],
    "expected_output": [
      "bid prices and timestamps",
      "withdrawals/exclusions",
      "winner sequence with denominator",
      "common-template/upstream alternatives"
    ],
    "id": "PA-W1-BIDS-BOLT",
    "independent_review_required": true,
    "invalid_inference": "Prior winners are not automatically losing bidders and reported offers do not prove independence.",
    "max_attempts": 10,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Do released quote or evaluation records explain the actual price selection independently of offer counts?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "historical_scope": "Seven exact PIIDs and associated solicitations in prior awards/observations.json",
      "niin": "016864912",
      "no_submission": "Only search already public records; prepare precise missing-record descriptions, do not send requests.",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "records": [
        "quote abstract",
        "technical acceptability",
        "award rationale",
        "price-reasonableness determination"
      ]
    },
    "stop_and_reopen": "Stop if only an offer count is available; reopen with an actual bid record.",
    "title": "Recover actual competition and selection evidence"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-COMPETE]] — planned (PA-E-d6e1b206bc488b5157cfe493); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-26be4017b82f3b4fe3a8); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-703910108d2b12a3e31d); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-3e8dbef80798b341871a76a0)
- [[PA-RUNSTATE-PA-W1-BIDS-BOLT]]: observes_task_state — documented_fact (PA-E-7da4c4a828c6b055192028a7)
- [[PA-W1-REVIEW-BOLT]]: requires_accepted_packet — planned (PA-E-9b094a51c3ef7bac3374da2e)
