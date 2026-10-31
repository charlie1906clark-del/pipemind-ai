---
id: "PA-W2-VA"
type: "gated_sector_design"
title: "Healthcare equipment and consumables procurement"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Healthcare equipment and consumables procurement

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
    "agency_scope": "VA and HHS procurement offices",
    "candidate_sources": "VA CCST and authorized price lists; public solicitation/order attachments",
    "critical_control": "Schedule catalog price is not the transaction price; service, installation and training bundles matter.",
    "first_selection": "PSC6515; pick one exact product family",
    "id": "W2-VA",
    "match_key": "Manufacturer/catalog model + pack + sterile/reusable status + warranty",
    "sector": "Healthcare equipment and consumables procurement",
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

- cites: [[PA-SRC-LATER-WAVES]] — documented_fact (edge-705e8bc6b2bc14314e52); sources: [[PA-SRC-LATER-WAVES]]

## Backlinks

- [[PA-SYSTEM-20261030]]: proposes_gated_wave — planned (PA-E-315c34aa1bbe974bfdb4210c)
