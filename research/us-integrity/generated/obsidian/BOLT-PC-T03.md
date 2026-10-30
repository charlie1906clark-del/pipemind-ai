---
id: "BOLT-PC-T03"
type: "audit_protocol"
title: "Repeated 12 percent hypothesis"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Repeated 12 percent hypothesis

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "execution_status": "Protocol defined; complete real-data test not established",
  "legal_fraud_threshold": false,
  "named_adverse_inference": false,
  "protocol": {
    "guard": "Thresholds are analyst-selected screening settings, not official fraud cutoffs. Multiple lines under one solicitation are not independent repetitions. Seven incomplete history rows cannot establish this test.",
    "id": "PC-T03",
    "inputs": [
      "qualified rows",
      "declared rate and tolerance",
      "solicitation/date strata",
      "benchmark intervals"
    ],
    "name": "Repeated 12 percent hypothesis",
    "output": "observed repetition and coverage, not a kickback probability",
    "test": "Before reading outcomes, declare 0.12 as a hypothesis, tolerance (for example 0.01), minimum independent solicitations/periods and complete eligible universe. Count rows and baseline-weighted amount within the band, report all residuals and benchmark sensitivity. Split exploratory and held-out periods; do not round values into a 12 percent pattern."
  },
  "visibility": "public"
}
```

## Sources

- [[BOLT-PC-MECH-S01]]
- [[BOLT-PC-MECH-S02]]
- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- cites: [[BOLT-PC-MECH-S01]] — documented_fact (edge-50b778002d49f907aa9b); sources: [[BOLT-PC-MECH-S01]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-6358fc8d1fde70acc652); sources: [[BOLT-PC-METHOD-S01]]
- cites: [[BOLT-PC-MECH-S02]] — documented_fact (edge-7326bfd2bb72c301702c); sources: [[BOLT-PC-MECH-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-b03e8451a7f9378c3940); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-c6dc6bdf4e31a9ad8922); sources: [[BOLT-PC-METHOD-S02]]

## Backlinks

- [[BOLT-PRICE-FAIRNESS-AUDIT]]: specifies_test — planned (BOLT-E-f10328458bf320359c0f)
