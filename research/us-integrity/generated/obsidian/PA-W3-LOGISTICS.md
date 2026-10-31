---
id: "PA-W3-LOGISTICS"
type: "gated_sector_design"
title: "Freight, storage and logistics"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Freight, storage and logistics

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
    "agency_scope": "DLA, military transport and civilian logistics offices",
    "candidate_sources": "Released rate schedules, orders and amendments",
    "critical_control": "Emergency transport, hazardous cargo, empty return, demurrage and accessorial services explain many differences.",
    "first_selection": "One lane, cargo type and service level",
    "id": "W3-LOGISTICS",
    "match_key": "Origin/destination commercial route + cargo + distance + timing + accessorials",
    "sector": "Freight, storage and logistics",
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

- cites: [[PA-SRC-LATER-WAVES]] — documented_fact (edge-144736cebc3396b4634c); sources: [[PA-SRC-LATER-WAVES]]

## Backlinks

- [[PA-SYSTEM-20261030]]: proposes_gated_wave — planned (PA-E-674b53daf40525f14d585ad7)
