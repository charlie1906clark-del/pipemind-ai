---
id: "PA-RUNSTATE-PA-W1-LINE-VA"
type: "task_execution_observation"
title: "PA-W1-LINE-VA: blocked"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-LINE-VA: blocked

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-TRACE",
    "attempts": 0,
    "attempts_remaining": 10,
    "available": false,
    "available_work_mode": "research",
    "budget_exhausted": false,
    "claim_count": 1,
    "current_result_id": null,
    "dependency_blockers": [],
    "effective_status": "blocked",
    "evidence_count": 0,
    "lease_active": false,
    "local_capture_reuse_attempts": 0,
    "owner": "codex-evidence-coordinator",
    "plan_id": "PA-WAVE-20261030-01",
    "remote_attempt_reservations": 0,
    "reopen_count": 0,
    "required_record": "Original order36C79126F0030 priced device/accessory lines with model, quantity and accepted terms.",
    "status": "blocked",
    "task_id": "PA-W1-LINE-VA"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-LINE-VA]] — documented_fact (PA-E-5edb52af42091d117f5d093b); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-19c122ecefbf9ad8eb36); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-376627c9d1933eb9ed196896)
