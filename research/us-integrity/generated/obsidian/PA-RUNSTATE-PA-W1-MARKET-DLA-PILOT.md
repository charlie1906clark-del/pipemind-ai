---
id: "PA-RUNSTATE-PA-W1-MARKET-DLA-PILOT"
type: "task_execution_observation"
title: "PA-W1-MARKET-DLA-PILOT: queued"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-MARKET-DLA-PILOT: queued

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-MARKET",
    "attempts": 0,
    "attempts_remaining": 8,
    "available": false,
    "available_work_mode": "research",
    "budget_exhausted": false,
    "claim_count": 0,
    "current_result_id": null,
    "dependency_blockers": [
      "PA-W1-SPEC-DLA-PILOT"
    ],
    "effective_status": "queued",
    "evidence_count": 0,
    "lease_active": false,
    "local_capture_reuse_attempts": 0,
    "owner": null,
    "plan_id": "PA-WAVE-20261030-01",
    "remote_attempt_reservations": 0,
    "reopen_count": 0,
    "required_record": null,
    "status": "queued",
    "task_id": "PA-W1-MARKET-DLA-PILOT"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-MARKET-DLA-PILOT]] — documented_fact (PA-E-b1158f7f28c9341975ba2c32); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-37c1e08e25268a5ed55d); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-4edcb77db3f1ac9c0ae824c4)
