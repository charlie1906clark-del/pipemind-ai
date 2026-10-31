---
id: "PA-W1-SPEC-DLA-PILOT"
type: "research_task_definition"
title: "Resolve exact pilot bolt specification and supply scope"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Resolve exact pilot bolt specification and supply scope

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-SPEC",
    "allowed_source_hosts": [
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "publogstorage.blob.core.windows.net",
      "www.boeing.com"
    ],
    "depends_on": [
      "PA-W1-LINE-DLA"
    ],
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
    "id": "PA-W1-SPEC-DLA-PILOT",
    "independent_review_required": true,
    "invalid_inference": "A similar product description or generic standard is not an exact NSN match.",
    "max_attempts": 10,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "What authoritative unrestricted attributes, approved source/part requirements and applicable revisions define CLIN0001?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "PIID": "SPE4A626PW775",
      "acquired_line": "2,243 EA at USD272.99, extended612316.57; separately priced first-article test CLIN0002 is3500.00.",
      "benchmark_status": "No qualified benchmark supplied by the acquisition pilot.",
      "clin": "0001",
      "comparison_boundary": "Exact listed part/drawing revisions, origin inspection/acceptance, packaging and first-article scope must be considered. Do not use generic commercial bolts.",
      "economic_priority": "Larger documented priced line, not a fraud likelihood assessment.",
      "manufacturer_part": "39-8820-501",
      "new_host_gate": "Current host scope permits the primary record and official manufacturer information. A specific new seller domain needs a coordinated versioned successor task before acquisition.",
      "nsn": "5306004457358",
      "selected_primary_artifacts": [
        "investigations/federal-price-pilot-2026-10-30/selected/dla-award-page4.txt",
        "investigations/federal-price-pilot-2026-10-30/selected/dla-award-page5-selected.txt",
        "investigations/federal-price-pilot-2026-10-30/selected_manifest.json"
      ],
      "source_discovery": "Search for precise public sources, preserve candidate URLs, and qualify them before adding source-host access.",
      "source_url": "https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF",
      "timing": "Required delivery2028-04-10; no payment conclusion."
    },
    "stop_and_reopen": "Stop comparison on unresolved critical fields; reopen with authoritative characteristics or a reviewed crosswalk.",
    "title": "Resolve exact pilot bolt specification and supply scope"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-LINE-DLA]] — planned (PA-E-376b4332edf2f07357f7d8be); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-SPEC]] — planned (PA-E-644b003c4a493a13a0333f2a); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-33908ce44136ebf75248); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-9618b898c655caba8200); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-0d50bac1703d1b0aae8fc2b0)
- [[PA-W1-MARKET-DLA-PILOT]]: requires_accepted_packet — planned (PA-E-1b6cd2ef6db638430a3538df)
- [[PA-RUNSTATE-PA-W1-SPEC-DLA-PILOT]]: observes_task_state — documented_fact (PA-E-1edec6d33e5ee6bc3428e4de)
