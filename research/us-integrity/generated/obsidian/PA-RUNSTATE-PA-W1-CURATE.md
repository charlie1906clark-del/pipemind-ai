---
id: "PA-RUNSTATE-PA-W1-CURATE"
type: "task_execution_observation"
title: "PA-W1-CURATE: queued"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-CURATE: queued

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-GRAPH",
    "attempts": 0,
    "attempts_remaining": 4,
    "available": false,
    "available_work_mode": "research",
    "budget_exhausted": false,
    "claim_count": 0,
    "current_result_id": null,
    "dependency_blockers": [
      "PA-W1-LINE-VA",
      "PA-W1-LINE-HHS",
      "PA-W1-NOVELTY-BOLT",
      "PA-W1-PRICE-DLA-PILOT"
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
    "task_id": "PA-W1-CURATE"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-CURATE]] — documented_fact (PA-E-0900873146e14e0c80ba9d06); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-66c3958b25b3783d02fb); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-c8abbe988b179aaea7228cf3)
