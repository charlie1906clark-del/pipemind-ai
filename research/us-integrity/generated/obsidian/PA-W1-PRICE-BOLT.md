---
id: "PA-W1-PRICE-BOLT"
type: "research_task_definition"
title: "Test actual and repeated price differences"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Test actual and repeated price differences

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-PRICE",
    "allowed_source_hosts": [
      "dibbs2.bsm.dla.mil",
      "www.fastenersuperstore.com",
      "www.mfsupply.com"
    ],
    "depends_on": [
      "PA-W1-MARKET-BOLT"
    ],
    "disconfirmation_tests": [
      "Material term adjustments explain the difference.",
      "Cheaper lines, credits, changed mix or full-pack outlay remove the pattern."
    ],
    "expected_output": [
      "input hashes",
      "signed per-line differences",
      "quantity-weighted totals",
      "base and gross denominators",
      "eligible/blocked coverage",
      "period and sensitivity"
    ],
    "id": "PA-W1-PRICE-BOLT",
    "independent_review_required": true,
    "invalid_inference": "A price difference is not a kickback or loss; preserve negative differences and never annualize estimates.",
    "max_attempts": 4,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Is there any qualified price comparison; if not, which exact gate prevents the calculation?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "calculator": "investigations/dla-bolt-trace-2026-10-30/price-controls/premium_audit.py",
      "data_origin": "public_observation",
      "niin": "016864912",
      "nsn": "5306016864912",
      "null_policy": "An accepted unresolved upstream packet does not qualify a benchmark.",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "recurring_pattern": "No recurring result until distinct comparable transactions and a predeclared universe exist."
    },
    "stop_and_reopen": "Stop with null comparison when qualification fails; reopen after a new qualified source or corrected calculation.",
    "title": "Test actual and repeated price differences"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-PRICE]] — planned (PA-E-5d79d2b24d2178c99662e469); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- requires_accepted_packet: [[PA-W1-MARKET-BOLT]] — planned (PA-E-bdc18160e2fad93b0fe3cb6c); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-413bcc5ef0a2ad2e96fb); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-d960657602aa24899da2); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-RUNSTATE-PA-W1-PRICE-BOLT]]: observes_task_state — documented_fact (PA-E-10d025586ea33d9bd2dbaa98)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-265e8be95668064ba40fc848)
- [[PA-W1-REVIEW-BOLT]]: requires_accepted_packet — planned (PA-E-dfa21fc975791d62a9c86ec4)
