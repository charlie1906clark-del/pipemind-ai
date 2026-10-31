---
id: "PA-RUNSTATE-PA-W1-LINE-DLA"
type: "task_execution_observation"
title: "PA-W1-LINE-DLA: accepted"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-LINE-DLA: accepted

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-TRACE",
    "attempts": 3,
    "attempts_remaining": 7,
    "available": false,
    "available_work_mode": "research",
    "budget_exhausted": false,
    "claim_count": 1,
    "current_result_id": "PA-W1-LINE-DLA-RESULT-01",
    "dependency_blockers": [],
    "effective_status": "accepted",
    "evidence_count": 3,
    "lease_active": false,
    "local_capture_reuse_attempts": 3,
    "owner": "codex-evidence-coordinator",
    "plan_id": "PA-WAVE-20261030-01",
    "remote_attempt_reservations": 0,
    "reopen_count": 0,
    "required_record": null,
    "status": "accepted",
    "task_id": "PA-W1-LINE-DLA"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-LINE-DLA]] — documented_fact (PA-E-7203a3755fa9f9d7b14d80d0); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-b27dbe31f8af33db50a1); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-5c7313782adc651a173d0490)
