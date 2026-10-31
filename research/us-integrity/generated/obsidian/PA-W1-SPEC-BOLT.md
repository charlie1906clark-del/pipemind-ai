---
id: "PA-W1-SPEC-BOLT"
type: "research_task_definition"
title: "Resolve the exact primary bolt specification"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Resolve the exact primary bolt specification

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-SPEC",
    "allowed_source_hosts": [
      "www.dla.mil",
      "publogstorage.blob.core.windows.net",
      "dibbs2.bsm.dla.mil"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "A material grade, finish, certification, traceability, pack or revision mismatch invalidates comparison.",
      "The catalog product lacks the required condition or configuration."
    ],
    "expected_output": [
      "attribute-by-attribute match matrix",
      "critical mismatch list",
      "revision applicability",
      "qualified/rejected/unresolved match"
    ],
    "id": "PA-W1-SPEC-BOLT",
    "independent_review_required": true,
    "invalid_inference": "A similar product description or generic standard is not an exact NSN match.",
    "max_attempts": 12,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Can authoritative NIIN characteristics and relevant revision establish the retail item match?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "followup_artifact_root": "investigations/bolt-spec-followup-2026-10-30/",
      "max_selected_items": 1,
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "requirement": "Use actual published public record routes; record missing critical fields."
    },
    "stop_and_reopen": "Stop comparison on unresolved critical fields; reopen with authoritative characteristics or a reviewed crosswalk.",
    "title": "Resolve the exact primary bolt specification"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-SPEC]] — planned (PA-E-6032c55b5d07c43820db5098); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- documents_specification_gap: [[PA-SPEC-FOLLOWUP-20261030]] — documented_fact (PA-E-e5dfb6dbb55dd8abf61693fd); sources: [[PA-SPEC-SRC-BSF-S01]], [[PA-SPEC-SRC-BSF-S02]], [[PA-SPEC-SRC-BSF-S03]], [[PA-SPEC-SRC-BSF-S04]], [[PA-SPEC-SRC-BSF-S05]], [[PA-SRC-SPEC-FOLLOWUP]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-8efa9aed88927af9ab6a); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-9a8edd39f27ff3acf216); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-718db464b29274e7131f7614)
- [[PA-RUNSTATE-PA-W1-SPEC-BOLT]]: observes_task_state — documented_fact (PA-E-7aa9ac22a867298f722b93ce)
- [[PA-W1-MARKET-BOLT]]: requires_accepted_packet — planned (PA-E-8242d699b52b5a5a90a08349)
