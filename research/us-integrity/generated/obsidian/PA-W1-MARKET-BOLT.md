---
id: "PA-W1-MARKET-BOLT"
type: "research_task_definition"
title: "Qualify independent bolt offers"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Qualify independent bolt offers

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-MARKET",
    "allowed_source_hosts": [
      "www.fastenersuperstore.com",
      "www.mfsupply.com",
      "aspdotnetstorefront.coxhardware.com",
      "dibbs2.bsm.dla.mil"
    ],
    "depends_on": [
      "PA-W1-SPEC-BOLT"
    ],
    "disconfirmation_tests": [
      "The low price is a test page, obsolete offer, unavailable stock or inaccessible quantity tier.",
      "Necessary services and accepted conditions differ materially."
    ],
    "expected_output": [
      "seller-specific price tiers",
      "full-pack outlay",
      "stock/date/terms",
      "source-independence groups",
      "benchmark interval and exclusions"
    ],
    "id": "PA-W1-MARKET-BOLT",
    "independent_review_required": true,
    "invalid_inference": "Seller profit disclosure is not mandatory; do not infer a fair price by assuming a markup.",
    "max_attempts": 8,
    "max_evidence": 16,
    "max_reopens": 2,
    "question": "Which prior seller candidates, if any, satisfy exact item, quantity, date and government supply terms?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "maximum_sellers": 3,
      "need": "Feasible full-order outlay, source grouping, date/stock/terms; no supplier contacts.",
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "reuse": "Read the three prior captures; Cox test-site/stock exclusion remains unless new evidence changes it."
    },
    "stop_and_reopen": "Stop at bounded seller/source search; reopen with dated acceptable terms or an actually available independent offer.",
    "title": "Qualify independent bolt offers"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-MARKET]] — planned (PA-E-7f1380f08c0f3e35f9746e7f); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- requires_accepted_packet: [[PA-W1-SPEC-BOLT]] — planned (PA-E-8242d699b52b5a5a90a08349); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-84b4709117d41c3f11f5); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-e4d2d6af6be909f6e2ff); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-51719609ecd02d65294b1bc3)
- [[PA-RUNSTATE-PA-W1-MARKET-BOLT]]: observes_task_state — documented_fact (PA-E-96f6f03b0c6a6756bc38bf66)
- [[PA-W1-PRICE-BOLT]]: requires_accepted_packet — planned (PA-E-bdc18160e2fad93b0fe3cb6c)
