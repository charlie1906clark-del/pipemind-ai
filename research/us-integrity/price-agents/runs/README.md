# Actual retained-evidence task run

This run imports the current 20-task plan and revalidates previously acquired public pilot evidence. Its acquisitions are recorded in the [pilot manifests](../../investigations/federal-price-pilot-2026-10-30/REPORT.md). It does not backdate runtime reservations or represent local reuse as a fresh download. Every attempt has `method: LOCAL_CAPTURE_REUSE`, the original observation time, selected-artifact hash and `new_network_requests: 0`.

`replay_pilot.py` submits the three cohort packets, waits for separately authored independent review receipts, then submits the DLA line packet only after its dependency has been accepted. The producer script never creates or approves its own review. The runtime verifies packet hashes and evidence files again. Review accepts narrowly worded observations; price eligibility remains unqualified and buyer benefit unresolved.

The run deliberately blocks the prior bolt's primary specification and bid questions, the VA and HHS order-line questions, and the new DLA item's exact technical/comparator gate. Those blocks identify the next record; they do not imply that the named recipient did anything wrong. Other queued tasks remain unexecuted.

Use a new database outside Git to reproduce the recorded stages from repository root:

```bash
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase cohorts
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase review --review-receipts research/us-integrity/price-agents/review/cohort-receipts.json
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase line
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase review --review-receipts research/us-integrity/price-agents/review/line-receipts.json
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase block-known-gaps
python research/us-integrity/price-agents/runs/replay_pilot.py --db /tmp/price-run.sqlite --out /tmp/price-run-export --phase export
```

Retained review receipts are historical independent decisions about exact hashes, not new reviews by whoever replays them. Current evidence mutations cause validation failure; changed results require new review. Times, event IDs, leases and run-state hashes can differ in a reproduction. The result packets and evidence content are deterministic. Snapshot exports omit lease tokens, and the operational SQLite file is not committed.

The plan's baseline is commit `d535e545adf362c17e43337e1147a0b2f6c7c18a`. Supplemental source selections acquired later are identified separately by exact hashes. They are not represented as content already present at that baseline. [Current run](current-run/) and [independent review](../review/) preserve the actual sequence.
