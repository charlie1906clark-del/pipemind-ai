---
id: "PA-W1-PRICE-DLA-PILOT"
type: "research_task_definition"
title: "Review the pilot line against any qualified benchmark"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Review the pilot line against any qualified benchmark

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-PRICE",
    "allowed_source_hosts": [
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "publogstorage.blob.core.windows.net",
      "www.boeing.com",
      "aerobasegroup.com",
      "www.aehiinc.com"
    ],
    "depends_on": [
      "PA-W1-MARKET-DLA-PILOT"
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
    "id": "PA-W1-PRICE-DLA-PILOT",
    "independent_review_required": true,
    "invalid_inference": "A price difference is not a kickback or loss; preserve negative differences and never annualize estimates.",
    "max_attempts": 4,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Does an independently accepted benchmark support a signed price comparison while keeping the separate first-article line and payment status explicit?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "PIID": "SPE4A626PW775",
      "acquired_line": "2,243 EA at USD272.99, extended612316.57; separately priced first-article test CLIN0002 is3500.00.",
      "admission_is_not_qualification": "No qualified quote has been obtained: Aerobase direct opens timed out twice; AEHI is a historical indexed catalog pointer. Exact technical, quantity, date, first-article and procurement-term gates remain unchanged.",
      "benchmark_status": "No qualified benchmark supplied by the acquisition pilot.",
      "clin": "0001",
      "comparison_boundary": "Exact listed part/drawing revisions, origin inspection/acceptance, packaging and first-article scope must be considered. Do not use generic commercial bolts.",
      "economic_priority": "Larger documented priced line, not a fraud likelihood assessment.",
      "host_admission_record": "price-agents/plans/host-admissions.json",
      "manufacturer_part": "39-8820-501",
      "new_host_gate": "The two exact seller hosts in host-admissions.json are admitted for the observed exact-part sources. Unlisted hosts require a recorded coordinator admission and, after import, a new immutable plan/task version. No wildcard crawling.",
      "nsn": "5306004457358",
      "selected_primary_artifacts": [
        "investigations/federal-price-pilot-2026-10-30/selected/dla-award-page4.txt",
        "investigations/federal-price-pilot-2026-10-30/selected/dla-award-page5-selected.txt",
        "investigations/federal-price-pilot-2026-10-30/selected_manifest.json"
      ],
      "seller_source_budget": "Market task: at most two requests per admitted seller host and four combined within its existing eight-attempt cap, including redirects/retries. Price task reuses accepted market artifacts; any fresh verification still counts against its existing four-attempt cap and needs a separately bounded tracer input.",
      "source_discovery": "Use the recorded exact URLs and the preserved search/source lineage. These are candidate seller sources, not asserted approved-source, price, inventory or equivalence evidence.",
      "source_url": "https://dibbs2.bsm.dla.mil/Downloads/Awards/09JUL26/SPE4A626PW775.PDF",
      "timing": "Required delivery2028-04-10; no payment conclusion."
    },
    "stop_and_reopen": "Stop with null comparison when qualification fails; reopen after a new qualified source or corrected calculation.",
    "title": "Review the pilot line against any qualified benchmark"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-MARKET-DLA-PILOT]] — planned (PA-E-21c0ebd189306ecf95df3ef3); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-PRICE]] — planned (PA-E-415474f48c82ac9b5196ff72); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-2928b2e2a6d697636271); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-6e2310ad7d861c21d640); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-W1-CURATE]]: requires_accepted_packet — planned (PA-E-07400e540fd52f08f6bf034d)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-0ba702f2f6ee8dbd9ff86ef4)
- [[PA-RUNSTATE-PA-W1-PRICE-DLA-PILOT]]: observes_task_state — documented_fact (PA-E-456e5ccf31e6b7b4ffab2902)
