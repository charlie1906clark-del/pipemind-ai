---
id: "PA-W1-CURATE"
type: "research_task_definition"
title: "Publish reviewed outcomes and the next evidence frontier"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Publish reviewed outcomes and the next evidence frontier

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-GRAPH",
    "allowed_source_hosts": [
      "github.com",
      "www.usaspending.gov",
      "www.acquisition.gov"
    ],
    "depends_on": [
      "PA-W1-LINE-DLA",
      "PA-W1-LINE-VA",
      "PA-W1-LINE-HHS",
      "PA-W1-NOVELTY-BOLT",
      "PA-W1-PRICE-DLA-PILOT"
    ],
    "disconfirmation_tests": [
      "A source lacks the necessary locator or record hash scope.",
      "A named adverse claim, private field or synthetic value would be promoted improperly."
    ],
    "expected_output": [
      "additive digest-pinned extension",
      "Obsidian notes",
      "typed money/temporal edges",
      "immutable earlier evidence",
      "handoff receipt"
    ],
    "id": "PA-W1-CURATE",
    "independent_review_required": true,
    "invalid_inference": "Repository artifacts are not a live cross-model connection or global distributed lock.",
    "max_attempts": 4,
    "max_evidence": 32,
    "max_reopens": 2,
    "question": "Can accepted public packets be integrated without losing provenance, unknowns or monetary distinctions?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "destination": "research/us-integrity/",
      "external_submission": false,
      "graph_policy": "Add a separate reviewed extension; never mutate prior captured evidence.",
      "input_commit": "d535e545adf362c17e43337e1147a0b2f6c7c18a",
      "source_hash_scope": "Selected extracts, original bytes and canonical graph hashes remain distinct."
    },
    "stop_and_reopen": "Stop graph promotion on missing review/provenance; reopen after a corrected reviewed packet.",
    "title": "Publish reviewed outcomes and the next evidence frontier"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-PRICE-DLA-PILOT]] — planned (PA-E-07400e540fd52f08f6bf034d); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-GRAPH]] — planned (PA-E-20124fc03b7958bbb3ae775f); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- requires_accepted_packet: [[PA-W1-LINE-HHS]] — planned (PA-E-994b723839b4754fc3454792); sources: [[PA-SRC-CURRENT-PLAN]]
- requires_accepted_packet: [[PA-W1-NOVELTY-BOLT]] — planned (PA-E-cc462ff4ae395dd2530979ed); sources: [[PA-SRC-CURRENT-PLAN]]
- requires_accepted_packet: [[PA-W1-LINE-DLA]] — planned (PA-E-e0758ae65c191d32bb5fe551); sources: [[PA-SRC-CURRENT-PLAN]]
- requires_accepted_packet: [[PA-W1-LINE-VA]] — planned (PA-E-e8db20f796b6012cab5e0c0e); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-4f82ad7b4e993e5d3507); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-a8c807a49a6dcf30de12); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-05baf9187c91e0851b4f0a0d)
- [[PA-RUNSTATE-PA-W1-CURATE]]: observes_task_state — documented_fact (PA-E-0900873146e14e0c80ba9d06)
