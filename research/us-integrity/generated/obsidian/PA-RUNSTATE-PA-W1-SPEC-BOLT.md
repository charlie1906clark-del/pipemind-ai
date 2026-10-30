---
id: "PA-RUNSTATE-PA-W1-SPEC-BOLT"
type: "task_execution_observation"
title: "PA-W1-SPEC-BOLT: blocked"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# PA-W1-SPEC-BOLT: blocked

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "ledger_observation": {
    "agent_role": "PA-ROLE-SPEC",
    "attempts": 0,
    "attempts_remaining": 12,
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
    "required_record": "Authoritative unrestricted NIIN016864912 Characteristics and Reference exports, with source release and qualifiers.",
    "status": "blocked",
    "task_id": "PA-W1-SPEC-BOLT"
  },
  "scoped_to_retained_local_run": true,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-LOCAL-RUN]]

## Outgoing relationships

- observes_task_state: [[PA-W1-SPEC-BOLT]] — documented_fact (PA-E-7aa9ac22a867298f722b93ce); sources: [[PA-SRC-LOCAL-RUN]]
- cites: [[PA-SRC-LOCAL-RUN]] — documented_fact (edge-63956e91cb4c88952bfe); sources: [[PA-SRC-LOCAL-RUN]]

## Backlinks

- [[PA-RUN-LOCAL-20261030]]: includes_task_state — documented_fact (PA-E-70dfa152776d1def03ac2030)
