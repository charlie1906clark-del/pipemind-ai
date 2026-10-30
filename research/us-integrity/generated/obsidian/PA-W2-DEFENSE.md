---
id: "PA-W2-DEFENSE"
type: "gated_sector_design"
title: "Defense consumables and spares"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Defense consumables and spares

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "activation_rules": [
    "Create a new immutable runtime plan for one named agency/commodity/date cohort; select actual PSC/NAICS codes from official source definitions before querying.",
    "Demonstrate acquisition of a priced line and its terms, or explicitly document why that sector cannot yet support a price test.",
    "Use a complete declared population when claiming repeated pattern prevalence; a first page supports only sample observations.",
    "Verify an independent source route and comparison requirements before expanding volume.",
    "Reserve a separate independent reviewer and explicit source budgets.",
    "Retain an explained/no-support control and report blocked coverage; expansion does not require finding fraud."
  ],
  "definition": {
    "agency_scope": "DLA and service procurement offices",
    "candidate_sources": "DIBBS original lines; public FLIS/PUB LOG; supplier catalogs",
    "critical_control": "Certification, traceability, supply urgency and aircraft/weapon-system-specific requirements can destroy a retail match.",
    "first_selection": "FSC5306 first, then a separately reviewed commodity code",
    "id": "W2-DEFENSE",
    "match_key": "NSN + revision + unit/pack + manufacturer part",
    "sector": "Defense consumables and spares",
    "status": "not_executed"
  },
  "nationwide_work_executed": false,
  "runtime_imported": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LATER-WAVES]]

## Outgoing relationships

- cites: [[PA-SRC-LATER-WAVES]] — documented_fact (edge-915f69353f37a7d17b52); sources: [[PA-SRC-LATER-WAVES]]

## Backlinks

- [[PA-SYSTEM-20261030]]: proposes_gated_wave — planned (PA-E-d41a7f9380c89ed76ce1c56a)
