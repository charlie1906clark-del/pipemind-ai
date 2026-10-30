---
id: "DISC-WP-DLA-BOLTS-001"
type: "research_task"
title: "Next bounded cohort: 30 public DLA bolt RFQs"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Next bounded cohort: 30 public DLA bolt RFQs

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "claude_executed": false,
  "completed_seed_rfqs": 1,
  "definition": {
    "acceptance": [
      "All cohort documents accounted for including failed/empty records",
      "All retained observations have primary source hash and page",
      "All comparisons pass eligibility gate or are explicitly blocked",
      "All candidate claims have alternative explanation and novelty review",
      "No savings estimated without verified paid quantities and defensible counterfactual",
      "A null finding completes the work package"
    ],
    "claim_ladder": [
      "source observation",
      "comparable price difference",
      "unexplained price-review lead",
      "corroborated misrepresentation/nonperformance evidence",
      "reviewed referral; legal determination belongs to competent authority"
    ],
    "external_models": {
      "Claude": "not invoked by this work package",
      "Grok": "not invoked by this work package",
      "exchange": "same source/evidence schema and critic gates; model identity and run provenance required"
    },
    "id": "WP-DLA-BOLTS-001",
    "price_gate": "eligibility.py; verified award CLIN or invoice price plus complete unit/item/terms evidence; source history alone cannot pass",
    "private_candidate_contract": {
      "candidate_names_and_allegations": "outside public repository",
      "public_identifiers_in_pilot": "neutral faithful source transcription only, not candidate ranking",
      "public_output": "methods, neutral source evidence, aggregate coverage and missing-data status"
    },
    "prohibited": [
      "credential guessing",
      "access-control circumvention",
      "sending allegations or agency messages without explicit authorization",
      "publishing unreviewed candidate dossiers",
      "claiming exhaustive coverage or undiscovered status from a limited search"
    ],
    "required_negative_controls": [
      "No ceiling divided by estimate",
      "No obligation divided by assumed quantity",
      "No retail price without equivalent product and terms",
      "No automatic same-unit assumption",
      "No high price to fraud inference",
      "No OIG/DOJ case repackaged as new"
    ],
    "roles": [
      {
        "id": "public_source_acquirer",
        "output": "raw source, source registry, inclusion/exclusion log",
        "task": "Acquire official public RFQ and linked award/order documents with hashes and access logs; stop at authentication or access denial"
      },
      {
        "id": "item_and_unit_specialist",
        "output": "item equivalence and units matrix; null for unknowns",
        "task": "Validate NSN, part/revision, condition, UI, QUP and conversion evidence from each historical order independently"
      },
      {
        "id": "price_terms_auditor",
        "output": "eligibility.py inputs, term adjustments and reviewer evidence",
        "task": "Distinguish ceiling, obligation, CLIN price, invoice and payment; account for quantity, date, delivery, warranty, quality and nonrecurring costs"
      },
      {
        "id": "data_integrity_checker",
        "output": "extraction corrections with provenance",
        "task": "Independently inspect source pages; reconcile duplicates, split lines, revisions and modifications"
      },
      {
        "id": "alternative_explanations_reviewer",
        "output": "counterevidence, unresolved facts and rejection reasons",
        "task": "Try to disprove each price lead using ordinary procurement explanations and missing data"
      },
      {
        "id": "novelty_reviewer",
        "output": "dated query log; bounded not-found status; known-case matches",
        "task": "Search DOJ, DoD/DLA OIG, GAO, agencies and court disclosures by verified identifiers and mechanism"
      },
      {
        "id": "human_evidence_reviewer",
        "output": "review decision; no automated accusation or referral",
        "task": "Approve evidence completeness and any next records/referral step"
      }
    ],
    "scope": {
      "family": "non-sensitive common machine bolts",
      "not_population_estimate": true,
      "sampling": "purposive recent official public RFQ cohort; 90-day issue-date window fixed before collection",
      "seed_completed_rfqs": 1,
      "target_rfqs": 30
    },
    "status": "reviewable_next_work_package_not_executed",
    "stop_conditions": [
      "30 RFQs processed or documented source-access limit reached",
      "Missing historical units/terms cannot be resolved from authorized sources",
      "Authentication, terms restrictions, restricted technical data or unavailable credentials encountered",
      "No supported lead remains after counterevidence review"
    ]
  },
  "execution_status": "not_executed",
  "grok_executed": false,
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

- assigns_planned_role: [[DISC-ROLE-price-terms-auditor]] — planned (DISC-E-293d127df6a03e591ae8); sources: 
- assigns_planned_role: [[DISC-ROLE-novelty-reviewer]] — planned (DISC-E-2f78891ff1f10259e721); sources: 
- assigns_planned_role: [[DISC-ROLE-public-source-acquirer]] — planned (DISC-E-368298eb71fe61e7636b); sources: 
- assigns_planned_role: [[DISC-ROLE-item-and-unit-specialist]] — planned (DISC-E-6e79161761150355fddd); sources: 
- assigns_planned_role: [[DISC-ROLE-data-integrity-checker]] — planned (DISC-E-a8731cbb864da692ee41); sources: 
- assigns_planned_role: [[DISC-ROLE-alternative-explanations-reviewer]] — planned (DISC-E-ec681ab26397fc1fbb55); sources: 
- assigns_planned_role: [[DISC-ROLE-human-evidence-reviewer]] — planned (DISC-E-f714267663aa7b97ec76); sources: 

## Backlinks

- [[DISC-20261030]]: defines_followup — planned (DISC-E-5772b34e7fe35c80b271)
- [[DISC-RV-F06]]: supports_followup_design — documented_fact (DISC-E-59d250aedf2cc40ebfe5)
