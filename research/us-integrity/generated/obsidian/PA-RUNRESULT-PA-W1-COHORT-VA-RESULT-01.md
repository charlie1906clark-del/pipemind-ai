---
id: "PA-RUNRESULT-PA-W1-COHORT-VA-RESULT-01"
type: "accepted_research_packet"
title: "PA-W1-COHORT-VA: accepted scoped observation packet"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-COHORT-VA: accepted scoped observation packet

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "external_truth_authentication": false,
  "new_fraud_established": false,
  "packet": {
    "benefit_evidence": {
      "evidence_ids": [],
      "reason": "These source selections do not establish buyer influence or a personal benefit",
      "status": "unresolved"
    },
    "candidate_signals": [],
    "conclusion": "Narrow public observations only. A completed and accepted packet does not establish price fairness, buyer independence, loss or fraud.",
    "data_origin": "public",
    "evidence_ids": [
      "PA-W1-COHORT-VA-E1"
    ],
    "facts": [
      {
        "evidence_ids": [
          "PA-W1-COHORT-VA-E1"
        ],
        "id": "PA-W1-COHORT-VA-FACT-1",
        "statement": "The declared July3–31,2026 new-awards query retained ten unique award summaries for this stratum."
      },
      {
        "evidence_ids": [
          "PA-W1-COHORT-VA-E1"
        ],
        "id": "PA-W1-COHORT-VA-FACT-2",
        "statement": "The response reports hasNext:true; this is an incomplete first-page sample sorted by cumulative award amount, not a random or nationwide cohort."
      },
      {
        "evidence_ids": [
          "PA-W1-COHORT-VA-E1"
        ],
        "id": "PA-W1-COHORT-VA-FACT-3",
        "statement": "Cumulative obligations are not unit prices, period spending or paid cash."
      }
    ],
    "input_commit": "d535e545adf362c17e43337e1147a0b2f6c7c18a",
    "next_record": "Original priced line and applicable procurement terms for the selected exact award.",
    "ordinary_alternatives": [
      "Award summaries and source availability do not indicate misconduct; supply terms and separately priced services can explain differences."
    ],
    "outcome": "observations",
    "pricing_eligibility": {
      "evidence_ids": [
        "PA-W1-COHORT-VA-E1"
      ],
      "reason": "No independently qualified equivalent benchmark or complete paid-value evidence",
      "status": "unqualified"
    },
    "producer": "codex-evidence-coordinator",
    "result_id": "PA-W1-COHORT-VA-RESULT-01",
    "schema_version": "1.0",
    "supplemental_input_scope": "New source selections acquired after the plan base commit, identified by evidence hashes; not represented as existing at that baseline.",
    "task_id": "PA-W1-COHORT-VA",
    "unknowns": [
      "Original priced lines are not established by these summary rows.",
      "Full population coverage and payment are not established."
    ]
  },
  "result_sha256": "ab30f52fc729e86e301abe588119af17021e75c33570a3fd873f78e2c1f40227",
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-f8548a0b5fe6807c23fa); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-W1-COHORT-VA]]: records_result_packet — documented_fact (PA-E-29cf372609ac9e378a7647aa)
