---
id: "PA-RUNSTATE-PA-W1-COHORT-DLA"
type: "task_execution_observation"
title: "PA-W1-COHORT-DLA: accepted"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-COHORT-DLA: accepted

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-ACQUIRE",
    "attempts": 1,
    "attempts_remaining": 5,
    "available": false,
    "available_work_mode": "research",
    "budget_exhausted": false,
    "claim_count": 1,
    "current_result_id": "PA-W1-COHORT-DLA-RESULT-01",
    "dependency_blockers": [],
    "effective_status": "accepted",
    "evidence_count": 1,
    "lease_active": false,
    "local_capture_reuse_attempts": 1,
    "owner": "codex-evidence-coordinator",
    "plan_id": "PA-WAVE-20261030-01",
    "remote_attempt_reservations": 0,
    "reopen_count": 0,
    "required_record": null,
    "status": "accepted",
    "task_id": "PA-W1-COHORT-DLA"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-COHORT-DLA]] — documented_fact (PA-E-07bedbe39a10af1475283b88); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-ffb397feca3550801044); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-830db0b0bfa1d65befb9d0f6)
