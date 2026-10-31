---
id: "PA-W1-ENTITY-BOLT"
type: "research_task_definition"
title: "Resolve dated business control without speculative merges"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Resolve dated business control without speculative merges

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-ENTITY",
    "allowed_source_hosts": [
      "cage.dla.mil",
      "sam.gov",
      "www.sec.gov",
      "data.sec.gov",
      "api.usaspending.gov"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "A supposed shell or alias is an ordinary legal name/DBA or separate valid entity.",
      "A registered agent or reported parent does not support the claimed owner relationship."
    ],
    "expected_output": [
      "exact and unresolved identity edges",
      "legal entity/DBA/parent roles",
      "ownership evidence and effective dates",
      "missing beneficial-owner fields"
    ],
    "id": "PA-W1-ENTITY-BOLT",
    "independent_review_required": true,
    "invalid_inference": "Current registrations and securities holdings do not establish historical beneficial ownership.",
    "max_attempts": 8,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Which historical supplier/control assertions can be supported by exact identifiers and dated public filings?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "award_parent": "SPE4A626D61WS",
      "historical_cages": [
        "6ZF42",
        "0NFB8",
        "7W108",
        "8A1E8",
        "51Y73"
      ],
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "ownership_unknown_is_valid": true,
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "reuse": "Five official current crosswalks already verified; do not reacquire without discrepancy.",
      "state_registry_gate": "A specific observed state-registry URL/host needs a reviewed successor task; no wildcard domain grant."
    },
    "stop_and_reopen": "Stop a join on ambiguous names or unsupported control; reopen on authoritative identifier/ownership evidence.",
    "title": "Resolve dated business control without speculative merges"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-ENTITY]] — planned (PA-E-3fe0098b5ee77ca46a83d877); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-9556347e816b797fcd74); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-f62bae735e2a07ac640e); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-RUNSTATE-PA-W1-ENTITY-BOLT]]: observes_task_state — documented_fact (PA-E-6dc817fdec5d06ace8874e18)
- [[PA-W1-BENEFIT-BOLT]]: requires_accepted_packet — planned (PA-E-9a630ac424f45e76499d720e)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-dcb70d68c84afffb11a22562)
