# Durable price-investigation work runtime

This is executable coordination for targeted research agents using the existing Python standard-library stack. It records finite work, preserves evidence and resumes blocked questions when a specified new record arrives. ChatGPT/Claude researchers perform the reasoning and source work; this program does not invoke a model, authenticate their identities, crawl the internet, deploy an unattended service or determine wrongdoing.

The runtime reuses the existing graph engine's canonical serialization, ID/date checks and structured public-data checks. Its separate ledger adds review, attempt accounting, evidence integrity and reopen transitions without changing the foundation task ledger. One shared SQLite file provides local concurrency. Separate copies on different computers do not provide distributed exclusivity; use a coordinator and versioned repository receipts between sessions.

## Reproduce the implemented behavior

From repository root, Python 3.10+:

```bash
python -m unittest discover -s research/us-integrity/price-agents/runtime -p 'test_*.py' -v
python research/us-integrity/price-agents/runtime/demo.py
python research/us-integrity/price-agents/runtime/agent_runtime.py --db /tmp/price-agent-demo.sqlite init --plan research/us-integrity/price-agents/runtime/fixtures/plan.json
python research/us-integrity/price-agents/runtime/agent_runtime.py --db /tmp/price-agent-demo.sqlite next
```

`demo.py` uses three separate database connections to demonstrate blocked work, a new artifact trigger, a new fenced lease, result submission and separate review. The old worker is rejected, and a dependent task stays unavailable until review accepts the correctly limited packet. It uses a simulated clock, invented artifacts and zero network/model calls. [demo-output.json](demo-output.json) is the deterministic checked result; it is not a government investigation or a deployed agent. Existing output files are not overwritten by `--output`.

The [price-check adapter](price_check.py) executes the existing hash-pinned premium engine without replacing its rules:

```bash
python research/us-integrity/price-agents/runtime/price_check.py research/us-integrity/investigations/dla-bolt-trace-2026-10-30/price-controls/scenarios/dla-current-no-qualified-benchmark.json
```

The actual DLA comparison remains blocked. This adapter returns input/code hashes, makes no network call, and neither completes a task nor approves a graph entry. Calculator flags and arithmetic cannot authenticate a source, benchmark, payment or buyer benefit.

## Plan contract

`init --plan PATH` creates a ledger and imports a plan. `import-plan --plan PATH` adds another immutable plan to an existing ledger. [fixtures/plan.json](fixtures/plan.json) is a complete synthetic example.

```json
{
  "schema_version": "1.0",
  "plan_id": "PRICE-WAVE-V1",
  "base_commit": "d535e545adf362c17e43337e1147a0b2f6c7c18a",
  "evidence_mode": "public",
  "tasks": [{
    "id": "PRICE-SPEC-001",
    "title": "Resolve the exact item specification",
    "agent_role": "Technical equivalence auditor",
    "question": "Which primary record establishes the applicable item characteristics?",
    "scope": {"nsn": "5306016864912", "period": "2026-09-17 through 2026-10-30"},
    "depends_on": [],
    "allowed_source_hosts": ["api.usaspending.gov", "www.dla.mil"],
    "max_attempts": 12,
    "max_evidence": 12,
    "max_reopens": 2
  }]
}
```

Additional JSON fields are retained and hashed. Task IDs are globally unique; all dependencies must be in the same imported plan and acyclic. Changing any existing plan/task definition requires a new versioned ID. `max_claims` is optional and defaults to `max_attempts + max_reopens + 1`. The commit is an exact declared baseline; this runtime does not authenticate its remote repository provenance. Evidence hashes and the separate repository result-review protocol provide additional checks.

Public and synthetic plans are separate. A synthetic fixture cannot enter a public plan. The runtime rejects structured private fields and common credential fields, unsafe artifact paths, symlinks, changed file hashes, malformed URLs, URL credentials, fragments and credential-like query keys. These checks are not a free-text privacy detector or proof that every source is public; a publication reviewer must still inspect the actual packet.

## Work and persistence contract

Global `--db PATH` and optional `--repository PATH` precede the command. `--repository` identifies the checkout containing retained evidence; by default it is this repository.

| Command | Required data | Effect |
|---|---|---|
| `claim` | `--task`, `--owner`, optional `--lease-seconds` | Atomically acquires a lease; returns its fencing token |
| `start-attempt` | task, owner, token, `--json REQUEST` | Reserves one finite logical work attempt before work |
| `finish-attempt` | task, owner, token, `--json COMPLETION` | Appends success, failure or unavailable outcome |
| `append-evidence` | task, owner, token, `--json EVIDENCE` | Checks an actual retained artifact and appends an immutable source receipt |
| `submit-result` | task, owner, token, `--json RESULT` | Pins a structured result and moves work to review |
| `review` | `--json REVIEW` | Separate actor reviews the exact result digest |
| `block` | task, owner, token, `--required-record`, `--reason` | Saves the exact missing record without discarding earlier evidence |
| `reopen` | task, owner/coordinator, `--json TRIGGER` | New exact artifact can reopen a blocked/rejected task within remaining budgets |
| `status` / `next` | database | Reports all tasks or currently available work |
| `export` | database and repository | Rechecks retained evidence and reopen-trigger bytes; emits a token-free audit snapshot |

Successful requests, failed requests and abandoned reservations all consume work budget. A last-attempt crash does not prevent an unresolved closeout: a later worker may obtain a **closeout-only** lease, but cannot reserve another acquisition. Claims themselves are bounded. Reopening never resets attempt or claim counters; once those budgets cannot support new work, a coordinator must define a new reviewed task/version. Accepted packets remain immutable and also require a new task/version for follow-up.

A blocked record is a precise artifact requirement, such as an applicable item export or dated bid abstract. Repeating a reason, URL or old artifact digest cannot reopen the task. A trigger must identify the exact blocked record and provide new retained bytes, a unique evidence ID, provenance and an actual SHA256. The program checks newness and integrity, not whether the record substantively resolves the question. The next researcher and reviewer make that judgment. A reopen trigger is not automatically accepted evidence.

Actor IDs are case-normalized and cannot contain whitespace. Producer self-review under case variants is rejected. Actor strings do not authenticate real people or independent model sessions; the coordinator must assign and verify them. Lease tokens fence stale workers and are omitted from exports, but a local file owner could alter program/database access. This is a local coordination boundary, not a hardened multi-tenant authentication system.

## Attempt and evidence payloads

A request contains `attempt_id`, `task_id`, `url`, `method`, and `purpose`. Read methods are `GET`, `HEAD`, `POST_READONLY`, `PUBLIC_TOOL_READ`, or `LOCAL_CAPTURE_REUSE`. A completion contains `attempt_id`, `outcome` (`success`, `failure`, `unavailable`) and `detail`. A reservation is not proof a network request was sent; actual network semantics belong to the acquisition adapter's manifest. This runtime does not make the request or prevent unregistered external activity.

The tracing adapter has its own bounded request log and currently has no automatic runtime-reservation bridge. Do not retrospectively describe an already completed acquisition as having run under a new reservation. Reuse its retained manifest honestly through the local-capture method below. A failed trace manifest is evidence of that failed attempt, never evidence that its target page was acquired.

Evidence fields:

- `id`, `task_id`, `attempt_id`: exact stable IDs; the task attempt must have completed successfully.
- `source_url`, `source_kind`: exact approved HTTPS host; kind is `official_record`, `seller_catalog`, `corporate_filing`, `court_record`, `methodology`, `selected_public_record`, or `synthetic`.
- `observed_at`, `event_date`: source retrieval/observation date and optional separate event date; event date may be null.
- `artifact_path`, `sha256`: repository-relative retained file and actual byte digest; files must remain inside the checkout with no private/hidden/symlink path.
- `hash_scope`: `selected_extract`, `raw_response`, `render`, `metadata`, or `synthetic_fixture`. A selected extract hash does not authenticate an original page.
- `locator`, `claim_scope`, `visibility:"public"`, `synthetic:false`: precise source location and limits; synthetic plans instead require synthetic kind/scope/flag.

Evidence can support its own task and accepted transitive dependencies. It is rechecked before submission, review and export, so modifying a retained source cannot silently preserve an old accepted packet. SQL update/delete triggers protect ledger evidence, attempts, results, reviews and event rows from routine mutation; direct database-owner tampering is outside this trust model.

### Reuse captures acquired before the runtime existed

`LOCAL_CAPTURE_REUSE` is a finite local validation step, **not a new source download**. Its request additionally requires:

```json
{
  "new_network_requests": 0,
  "original_capture": {
    "artifact_path": "research/us-integrity/path/to/selected-capture.json",
    "sha256": "ACTUAL_64_CHARACTER_RETAINED_BYTE_DIGEST",
    "observed_at": "2026-10-30T12:00:00Z",
    "hash_scope": "selected_extract",
    "provenance_note": "Original capture manifest path and actual retrieval scope"
  }
}
```

The complete request still includes its attempt/task IDs, original source URL, method and purpose. The placeholder above must be replaced by the actual digest. Startup checks the existing file. Completion must explicitly state `new_network_requests:0`. Appended evidence must preserve the same original capture path, digest, observation timestamp and hash scope. Runtime event timestamps describe the later local inspection; they do not replace the original retrieval date.

Status reports `local_capture_reuse_attempts` separately from `remote_attempt_reservations`. Both consume finite logical work budget, but these counters must not be summed and described as actual HTTP requests.

## Result and independent review contracts

A result requires `schema_version`, `result_id`, `task_id`, `producer`, `input_commit` matching the plan, `data_origin` matching the plan, `outcome`, `evidence_ids`, `facts`, `candidate_signals`, `pricing_eligibility`, `benefit_evidence`, `unknowns`, `ordinary_alternatives`, `conclusion`, and optional `next_record`.

`facts` and `candidate_signals` are arrays of `{id,statement,evidence_ids}`. Each signal also needs `alternative_explanation`. References must identify retained evidence in this task or accepted dependencies. `outcome` is `observations`, `ordinary_explanation`, `unresolved`, or `unsupported_signal`; proving misconduct is never a required outcome.

`pricing_eligibility` has `{status,reason,evidence_ids}`, with status `blocked`, `unqualified`, `excluded`, or `eligible_as_declared`. `benefit_evidence` uses the same shape with status `unresolved`, `no_evidence_in_acquired_records`, or `documented_public_record`. Affirmative states need evidence references but still require substantive independent source review. An unexplained price difference never automatically becomes a benefit, loss or criminal finding. Do not equate absence in acquired records with proof no benefit exists.

A review requires `review_id`, `result_id`, `reviewer`, exact `result_sha256`, `decision`, `reason`, and `checks`. The five reasoned check entries are `provenance`, `comparability`, `alternative_explanations`, `amount_basis`, and `privacy`. Decision is `accepted`, `needs_more_evidence` or `rejected`; the latter two require `required_record`. The reviewer must differ from the producer. Full executable payloads are in [demo.py](demo.py) and its [export](demo-output.json).

An **accepted packet may correctly conclude that evidence is unresolved**. Acceptance completes that research task and can release dependencies; it does not qualify a benchmark, clear a buyer, establish a payment or authorize a public allegation. Dependent price workers must reapply the independent calculator and source-comparability gates. No result is automatically added to the canonical graph or sent outside the authorized repository.

## Validation and operating limits

The tests cover lease fencing/expiry and concurrent claims; immutable plan/evidence/result replay; failed and abandoned attempt accounting; closeout after exhaustion; budget preservation on reopen; exact new-artifact triggers; public/synthetic separation; unsafe URL/path rejection; independent review; dependency release; source modification detection; SQL append-only rows; token-free exports; prior-capture reuse; and the existing premium engine's real/synthetic gates.

The synthetic durable demo is reproducible across database restarts. A real research run must retain actual source provenance and a separately attributed review receipt. Neither passing tests nor a large graph demonstrates nationwide transaction coverage, access to private financial records, a deployed model worker or a fraud discovery. The successful research outcome is a source-supported conclusion with the remaining uncertainty made explicit.
