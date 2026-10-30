---
id: "PA-W1-MARKET-DLA-PILOT"
type: "research_task_definition"
title: "Find an independently evidenced equivalent pilot-part offer"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Find an independently evidenced equivalent pilot-part offer

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-MARKET",
    "allowed_source_hosts": [
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "publogstorage.blob.core.windows.net",
      "www.boeing.com",
      "aerobasegroup.com",
      "www.aehiinc.com"
    ],
    "depends_on": [
      "PA-W1-SPEC-DLA-PILOT"
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
    "id": "PA-W1-MARKET-DLA-PILOT",
    "independent_review_required": true,
    "invalid_inference": "Seller profit disclosure is not mandatory; do not infer a fair price by assuming a markup.",
    "max_attempts": 8,
    "max_evidence": 20,
    "max_reopens": 2,
    "question": "Is a dated compliant offer available for exact part39-8820-501 and feasible quantity, with first-article and quality scope resolved?",
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
    "stop_and_reopen": "Stop at bounded seller/source search; reopen with dated acceptable terms or an actually available independent offer.",
    "title": "Find an independently evidenced equivalent pilot-part offer"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- requires_accepted_packet: [[PA-W1-SPEC-DLA-PILOT]] — planned (PA-E-1b6cd2ef6db638430a3538df); sources: [[PA-SRC-CURRENT-PLAN]]
- assigned_role: [[PA-ROLE-MARKET]] — planned (PA-E-4751611eac45266a70df6492); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-6cb7497769f59f7389b8); sources: [[PA-SRC-CURRENT-PLAN]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-9c53e625cb05b27331ee); sources: [[PA-SRC-ROLE-CONTRACTS]]

## Backlinks

- [[PA-W1-PRICE-DLA-PILOT]]: requires_accepted_packet — planned (PA-E-21c0ebd189306ecf95df3ef3)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-29e2a95ad479ea8e7ec4d08f)
- [[PA-RUNSTATE-PA-W1-MARKET-DLA-PILOT]]: observes_task_state — documented_fact (PA-E-b1158f7f28c9341975ba2c32)
