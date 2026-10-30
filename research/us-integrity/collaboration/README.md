# Claude, Grok and the PipeMind research exchange

Prepared 30 October 2026. **Two research packets are ready; neither has been dispatched to Claude or Grok.** The repository is the shared evidence store. It does not itself open another chat, invoke a model, share a live database lock or train model weights.

## Current connection state

[CONNECTION-STATUS.json](CONNECTION-STATUS.json) records the root coordinator's verified discovery results. Native GitHub is available. Grok authorization was initiated and is awaiting the user; no Grok model call has run. The Claude administrator connection was rejected by automatic approval review for excessive organizational permissions. A separate inference-only gateway connection was rejected because its routing, account and billing scope had not been explicitly approved. No Claude model call has run. Further authorization attempts are outside this packet.

Existing Claude or Grok chat accounts can use the **manual repository handoff** below without a new model-API integration. Whether a particular chat can read or write GitHub depends on that chat's actual connection. A supplied repository URL alone does not grant write access. If it can only read, return the result file to the coordinator for review and commit.

On the inspected research branch, the existing `.claude/agents/x-*.md` files concern X drafting. They are not research dispatchers and are not modified by this work. Older daily-research documents describe a manually initiated workflow; their statements about training must not be read as evidence of updated model weights or permanent cross-provider memory. This exchange persists evidence that each worker must explicitly reload.

## Concrete assignments

| Packet | Intended worker | Bounded question | State |
|---|---|---|---|
| [CLAUDE-PRICE-001](tasks/CLAUDE-PRICE-001.json) | Claude | Can one official, simple-item procurement record support a comparable unit-price test and a correctly scoped defective-pricing inquiry? | Queued, not dispatched |
| [GROK-IDENTITY-001](tasks/GROK-IDENTITY-001.json) | Grok | Does a bounded Amazon/Amazon. recipient query produce aliases, affiliates, separate identifiers or an unresolved identity conflict? | Queued, not dispatched |

The name example is a test of entity matching, not an allegation against Amazon or any similarly named business. High prices, punctuation and absent search results do not establish fraud. Published enforcement matters are comparison material and must not be relabeled discoveries.

Each packet permits one finite research result, at most 12 public search requests and 20 public document/API reads. The packet authorizes no purchase, paid API execution, message to a third party, tip submission or unattended loop. The existing user request authorizes preparation of this collaboration; actual API execution still requires an active, appropriately scoped connection and an approved route. Root also inspected the integration and agent-governance branch trees, which contain additional hydrogen agent documents and CI tests. No live bridge was verified in those inspected sources; this is not a claim that no external integration exists anywhere.

## Manual handoff that can be used now

1. Open the intended existing Claude or Grok session. Supply the repository branch/commit containing this packet and the relevant entrypoint: [`CLAUDE.md`](../CLAUDE.md) or [`GROK.md`](../GROK.md).
2. Supply the exact task JSON. Its research inputs are pinned to baseline commit `55fa8ab8cb7a60b243884f22f8655503009ccda4`. The task packet is created later; it is delivered alongside that baseline. Do not pretend the new task file existed at the baseline commit.
3. Assign the task through one coordinator and record its task-specification digest. Read `QUEUE.json` as a dispatch record, not a distributed lock. Use the proposed task-specific branch only after checking it does not already contain someone else's work. No shared-branch overwrites or force pushes.
4. Read the seven pinned input files from that exact baseline. Their byte hashes are included in the task. New public sources are allowed within the budget, but their dates, queries, coverage and limitations must be captured in the returned result.
5. Return the JSON result described in [RESULT-CONTRACT.md](RESULT-CONTRACT.md), with the actual model and session identifier. The research result starts as `submitted`, awaiting independent review. A null result or a disproved hypothesis is valid.
6. The coordinator validates the result, obtains a separate review and then decides whether to add findings to the public graph. A model response is not an authoritative source and a successful schema check is not a fraud finding.

Copy this dispatch text, substituting the actual delivery commit and packet:

> Work only on the attached PipeMind US Integrity task packet. Read the scoped entrypoint and preserve the task's exact input commit and input-file hashes. Use official public evidence within the finite budget. Seek a new supportable observation without assuming fraud must be found. Return a JSON result under `RESULT-CONTRACT.md`, including counterevidence, failed access and the exact unresolved edge. Do not change the canonical graph, merge a PR, contact a target, submit a report or publish a new named suspicion. Record the actual model/session and return your result to the coordinator for independent review.

## API execution after an authorized connection exists

The root coordinator must first verify the connection is Active and inspect the complete current inference-tool schema. Use the exact discovered tool, provider model and approved budget. Supply only the public task packet and selected public evidence; do not transmit unrelated repository secrets or private candidate identities. A single bounded call is sufficient to test the integration.

Record provider, tool, model, request time, task digest, input commit and actual provider response ID in a dispatch receipt. Preserve the response as a content-addressed artifact. An unsuccessful or ambiguous write must be checked before retrying; no speculative duplicate execution. A discovered capability, connection initiation or task file is not a successful model invocation.

No API runner, GitHub Action, secret, webhook, bot mention or background worker is installed by this package. It therefore creates no new inference billing or automatic publication path. Authorization links and credentials are intentionally excluded from Git.

## Validate and preserve a returned result

From repository root:

```sh
python research/us-integrity/collaboration/validate_result.py \
  research/us-integrity/collaboration/tasks/GROK-IDENTITY-001.json \
  /path/to/returned-result.json \
  --verify-inputs .

python research/us-integrity/collaboration/validate_result.py \
  research/us-integrity/collaboration/tasks/GROK-IDENTITY-001.json \
  /path/to/returned-result.json \
  --review /path/to/independent-review.json \
  --verify-inputs . \
  --archive /path/to/reviewed-public-results

python -m unittest discover -s research/us-integrity/collaboration -p 'test_*.py' -v
```

Use the Claude task filename for a Claude result. `--verify-inputs` reads baseline Git blobs locally, checks their hashes and performs no fetch. `--archive` writes canonical JSON under its SHA-256 filename, allows an identical replay and rejects changed bytes at that filename. This is an append-only convention with tamper detection, not an operating-system write lock. Reviewer receipts should be retained separately and identified by their own digest.

The validator rejects the wrong task or baseline, changed task specification, missing citations/locators, declared private output, new named adverse hypotheses, self-acceptance/self-review, unsupported money relabeling and unit-price comparisons without required terms. It cannot authenticate the claimed model identity, inspect every source, detect all sensitive text or prove an independent review actually happened. The coordinator must verify receipts and inspect content.

## Coordination and acceptance

Use disjoint task branches. The coordinator is the only writer of the public approval manifest and canonical graph. A task completion does not automatically approve its findings. No shared SQLite claim exists across separate machines; the existing [engine's fenced leases](../engine/README.md) apply only when workers use the same actual database through one coordinator.

Keep task specifications immutable. Change the scope by issuing a new task version/ID and digest. Dispatch state belongs in [QUEUE.json](QUEUE.json); each state change needs a real receipt. A proposed result carries `task_spec_sha256` and `input_commit`, so a response to an older assignment cannot be silently accepted for a revised one. Review decisions are separately bound to `result_sha256`. Narrowed findings require a new result and review rather than rewriting an already accepted artifact.

When adding new research inputs, publish that research first and verify its actual commit. The prepared [version-2 input plan](reissue-plan-v2.json) lists the 30 October policy, name-audit and pricing artifacts. `reissue_tasks.py --input-commit PUBLISHED_40_CHARACTER_SHA` previews a reissue using only committed Git blobs; `--apply` preserves prior packets and updates the queued assignments. It refuses missing evidence and any already-dispatched assignment. The script does not verify remote publication or fetch the commit, so the coordinator must do that first. Never attach hashes of uncommitted files to an older commit. Rerun the handoff tests and pinned-input checks after reissue.

For evidence conflicts, preserve both sourced assertions and their dates. Request the exact observation that would distinguish them. For unsupported novelty, say only “not found in this bounded search”; no public search can certify that government investigators or another whistleblower have never seen a fact.

Public findings enter the graph only through the existing reviewed investigation-extension mechanism. Candidate names, private financial records and unreported adverse theories stay outside this public repository. The current packets are setup artifacts, not model research results.
