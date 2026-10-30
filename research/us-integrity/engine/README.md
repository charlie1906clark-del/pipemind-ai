# Evidence graph engine

Offline Python 3.10+ tooling using only the standard library. It records the supplied evidence and its uncertainty; it does not independently establish fraud, acquire data, call an AI service, submit reports, or run unattended agents.

From the repository root:

```bash
python research/us-integrity/engine/integrity.py validate research/us-integrity/data/graph.json --public
python research/us-integrity/engine/integrity.py build research/us-integrity/data/graph.json --output /tmp/us-integrity-build --tasks research/us-integrity/architecture/tasks.json
python research/us-integrity/engine/integrity.py search --db /tmp/us-integrity-build/graph.sqlite "Medicare"
python -m unittest discover -s research/us-integrity/engine -v
```

Open `/tmp/us-integrity-build/obsidian` as an Obsidian vault. Each graph node becomes one note named by stable ID, with properties, source links, outgoing relationships and backlinks. No Obsidian plugin is needed. Copy the generated public notes into the existing PipeMind vault only after review; this engine does not operate the desktop application or sync it.

## Canonical input contract

```json
{
  "version": "1.0",
  "as_of": "2026-10-29",
  "nodes": [
    {
      "id": "SRC-EXAMPLE",
      "type": "source",
      "title": "Official document title",
      "status": "source",
      "source_ids": [],
      "properties": {
        "url": "https://example.gov/document",
        "accessed_at": "2026-10-29",
        "retrieval_method": "browser_read",
        "visibility": "public"
      }
    },
    {
      "id": "FACT-EXAMPLE",
      "type": "finding",
      "title": "Precisely bounded statement from the document",
      "status": "documented_fact",
      "source_ids": ["SRC-EXAMPLE"],
      "properties": {"visibility": "public"}
    }
  ],
  "edges": [
    {
      "id": "EDGE-EXAMPLE",
      "type": "supports",
      "source": "SRC-EXAMPLE",
      "target": "FACT-EXAMPLE",
      "status": "documented_fact",
      "source_ids": ["SRC-EXAMPLE"],
      "properties": {}
    }
  ]
}
```

Node types and relationship types are extensible strings. Node and edge IDs share a unique namespace, must begin with a letter, may contain letters, digits, `_`, `-` and `.`, and may not contain `..`. A name alone never merges entities. Use identifiers such as UEI, CAGE, NPI and state registration number in properties, with temporal validity and source references. Keep ambiguous matches as separate nodes and proposed relationships.

The accepted evidence status vocabulary is:

`source`, `documented_fact`, `published_case`, `allegation`, `settlement`, `conviction`, `audit_finding`, `hypothesis`, `planned`, `unknown`, `verified`, `disputed`, `closed`, `disproved`.

All documented nodes and edges require at least one `source_ids` entry pointing to an actual source node. Only `hypothesis`, `planned`, and `unknown` records may be unsourced. Source nodes require a public HTTP(S) URL and ISO `accessed_at` date or timezone-qualified datetime. This proves graph referential integrity, **not** the truth of the document or that its URL was independently fetched.

Case nodes require `properties.legal_status`. Supported values are `allegation`, `charged`, `indicted`, `complaint`, `pending`, `settlement`, `settled`, `conviction`, `convicted`, `guilty_plea`, `sentenced`, `acquitted`, `dismissed`, `audit_finding`, `audit`, `unknown`, `civil_settlement`, `administrative_action`, `mixed`, `judgment`, `published_case`. A `conviction` evidence label cannot accompany a merely charged legal status. Public case/person/lead nodes additionally require `properties.public_record=true`. That flag must describe the underlying record; it is not a permission to turn a novel hypothesis into a public accusation.

Money can be recorded as:

```json
{"money":{"amount":"1000000.00","currency":"USD","kind":"settlement","period":"2026","basis":"Official settlement announcement"}}
```

`amount`, three-letter uppercase `currency` and `kind` are required when `money` exists. Optional `qualifier` preserves bounds such as `greater_than` or `approximately`; optional `period`, `basis`, and `condition` retain timing, measurement context and conditional-payment triggers. These fields are also included in `money.csv`. Keep obligations, outlays, alleged loss, improper payments, settlement, recovery, avoided future costs and reward separate. No savings or reward calculation is performed. Structured properties remain in JSON and CSV exports.

## Publication boundary

Every build is a **public** export. There is deliberately no `--include-restricted` option. The engine rejects restricted visibility, declared sensitive-person/private-information flags, selected private-field names (including SSN, bank account, home address and patient identifiers), nonpublic novel leads, and nonpublic cases/persons. Business addresses are not rejected merely for being addresses. These are structured-data checks, **not a free-text PII detector or a substitute for a human publication review**. Do not place private evidence into this repository or into graph properties.

`validate` checks the graph contract; add `--public` to exercise the publication boundary. `build` always exercises it before creating outputs. CSV text fields beginning with spreadsheet formula characters are prefixed with an apostrophe.

Source `content_sha256`, when supplied, must be a 64-character lower-case hex digest of actually acquired bytes. The engine does not invent or fetch source hashes. `manifest.json` instead records `graph_sha256`, the digest of the canonical supplied JSON, and states that scope explicitly. Notes and JSON/CSV output are deterministic for identical graph input. SQLite bytes are not promised deterministic, especially because task leases and audit events are operational state.

## Two-model work queue

Import an array of tasks or an object with a `tasks` array using `build --tasks PATH`. A task has `id`, `title`, optional `status` (`queued` or `blocked` on initial import), `depends_on` (task IDs), and additional descriptive fields such as acceptance criteria. All task dependencies must exist and be acyclic. Restricted tasks cannot be imported into this public build.

```bash
python research/us-integrity/engine/integrity.py claim-task --db /tmp/us-integrity-build/graph.sqlite --task TASK-EXAMPLE --owner chatgpt-research-session-A --lease-seconds 1800
python research/us-integrity/engine/integrity.py complete-task --db /tmp/us-integrity-build/graph.sqlite --task TASK-EXAMPLE --owner chatgpt-research-session-A --lease-token TOKEN_FROM_SUCCESSFUL_CLAIM --result "Reviewed source ID, recorded dated evidence path and reviewer decision."
```

Use the actual task IDs in the imported manifest. Claims use SQLite `BEGIN IMMEDIATE`, so two simultaneous workers cannot both obtain an unexpired task lease. Repeating a claim by its current owner returns the existing lease. Other owners must wait for expiry; expired owners must reacquire before completing. Each new claim returns a fencing `lease_token`; completion requires that exact token, so an expired worker cannot complete a reclaimed task even when an owner label is reused. Use a unique owner per worker session. Completion is idempotent only for the same token, owner and identical result. Every new claim and completion appends an audit event. A dependent task remains unavailable until all dependencies are completed. Rebuilding the graph with unchanged task definitions preserves claims and results; changing an imported definition requires a new versioned task ID and rolls back the graph/database update. Blocked tasks require a reviewed new task definition/ID before work resumes.

Both assistants must reach the **same local SQLite file** through one coordinator. Committing a SQLite file to Git does not provide a distributed lock, and separate cloud sessions do not share a queue automatically. Use a single operator or implement an authenticated central coordinator before claiming cross-session concurrency. A task completion is a worker report, not independent evidence acceptance. The manifest/agent instructions must assign a separate reviewer.

## Outputs and verification limits

- `graph.sqlite`: queryable nodes, edges, metadata, tasks and append-only task events; FTS5 search where available, literal `LIKE` fallback otherwise.
- `exports/graph.json`, `nodes.csv`, `edges.csv`, `money.csv`: portable public graph.
- `obsidian/ID.md`: one generated note per node. Only stale files bearing the engine generation marker are removed; handwritten notes are preserved.
- `manifest.json`: counts and input digest, without a fabricated source-content verification claim.

The meaningful tests exercise provenance/reference failures, legal-status conflicts, public-export refusal, privacy false positives, path/symlink safety, entity-name ambiguity, search injection, monetary units, deterministic exports/backlinks, task import preservation and rollback, ownership/dependencies/expiry/idempotency, lease fencing, and a concurrent claim race. No network, model runtime, legal eligibility, fraud accuracy or installed Obsidian session is tested by these checks.
