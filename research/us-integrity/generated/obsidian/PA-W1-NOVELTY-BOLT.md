---
id: "PA-W1-NOVELTY-BOLT"
type: "research_task_definition"
title: "Check bounded prior disclosure without claiming government ignorance"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Check bounded prior disclosure without claiming government ignorance

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-NOVELTY",
    "allowed_source_hosts": [
      "www.acquisition.gov",
      "www.justice.gov",
      "www.gao.gov",
      "www.oversight.gov",
      "www.dla.mil"
    ],
    "depends_on": [
      "PA-W1-REVIEW-BOLT"
    ],
    "disconfirmation_tests": [
      "A matching prior case/audit already discloses the asserted novelty.",
      "The alleged legal outcome is merely a charge, not a finding."
    ],
    "expected_output": [
      "query ledger",
      "matching/nonmatching disclosures",
      "source-stated legal status/date",
      "coverage and uncertainty"
    ],
    "id": "PA-W1-NOVELTY-BOLT",
    "independent_review_required": true,
    "invalid_inference": "No public result does not prove that government investigators lack knowledge or establish reward eligibility.",
    "max_attempts": 6,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Does a matching published case/audit already disclose any surviving precisely stated transaction question?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "government_knowledge": "unknown",
      "maximum_exact_queries": 6,
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "search_scope": "Exact PIID/NSN and sourced legal-entity identifiers; official published cases/audits.",
      "skip_rule": "If no supported new transaction question survives, return not-applicable with evidence, rather than inventing one."
    },
    "stop_and_reopen": "Stop at declared search limits; reopen on a new exact identifier or release.",
    "title": "Check bounded prior disclosure without claiming government ignorance"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-REVIEW-BOLT]] — planned (PA-E-288d0845153e0dc803f5354f); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-NOVELTY]] — planned (PA-E-99ffd6383e18b7a5d9f86402); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-06673f0a3191956f69da); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-65531bd22606695310a3); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-34bda3fe9acac220fc5acad9)
- [[PA-RUNSTATE-PA-W1-NOVELTY-BOLT]]: observes_task_state — documented_fact (PA-E-c45904a8818dcc4bffb51475)
- [[PA-W1-CURATE]]: requires_accepted_packet — planned (PA-E-cc462ff4ae395dd2530979ed)
