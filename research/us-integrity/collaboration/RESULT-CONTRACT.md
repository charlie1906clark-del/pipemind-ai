# Model research result and independent-review contract

Version 1.0. Every result is tied to one immutable task specification and one input commit. The actual executable checks are in `validate_result.py`; no third-party Python packages are required.

`task_spec_sha256` and `result_sha256` mean SHA-256 of JSON encoded as UTF-8 with sorted keys, compact `,`/`:` separators and `ensure_ascii=False`, **without** a trailing newline. They are not hashes of arbitrary pretty-printed files. Input-file hashes instead cover exact baseline Git blob bytes.

## Worker result shape

The example below is a template, not evidence or a received model response. Replace all placeholder values; empty claims or citations fail validation.

```json
{
  "schema_version": "1.0",
  "task_id": "EXACT_TASK_ID",
  "task_spec_sha256": "COMPUTED_TASK_DIGEST",
  "input_commit": "EXACT_TASK_INPUT_COMMIT",
  "created_at": "ACTUAL_TIME_WITH_TIMEZONE",
  "visibility": "public",
  "status": "submitted",
  "no_new_fraud_determination": true,
  "sensitive_material_included": false,
  "execution_mode": "manual_repo_handoff",
  "worker": {
    "provider": "xai",
    "agent_id": "ACTUAL_WORKER_ID",
    "model": "ACTUAL_MODEL",
    "session_id": "ACTUAL_DISTINCT_SESSION",
    "identity_basis": "self_reported"
  },
  "scope": "Exact cohort, query, period and question",
  "coverage_limit": "Complete available query or exact partial coverage",
  "limitations": ["What these records cannot establish"],
  "sources": [
    {
      "source_id": "S1",
      "url": "https://OFFICIAL_SOURCE",
      "title": "Source title",
      "publisher": "Publishing agency or issuer",
      "source_kind": "primary_official",
      "accessed_at": "ACTUAL_ISO_DATE",
      "publication_date": null,
      "retrieval_status": "read"
    }
  ],
  "claims": [
    {
      "claim_id": "C1",
      "statement": "One precisely bounded observation",
      "evidence_type": "derived_observation",
      "subject_scope": "aggregate",
      "adverse_inference": false,
      "named_subjects": [],
      "novelty": {
        "status": "not_found_in_bounded_search",
        "search_scope": "Exact identifiers, repositories and queries checked",
        "limitation": "Absence here does not prove undiscovered status"
      },
      "source_refs": [{"source_id": "S1", "locator": "Page, paragraph, table row or API record"}],
      "alternatives": ["Plausible legitimate explanation and the test performed"],
      "next_discriminating_evidence": "Specific missing observation or reason to close"
    }
  ],
  "amounts": []
}
```

For Claude, the assigned provider is `anthropic`; for Grok, `xai`. A manual session identity is self-reported until the coordinator verifies it. An `authorized_model_api` execution requires the actual `provider_response_id`; the validator does not authenticate that receipt with the provider. Do not invent model names or response IDs.

Allowed claim evidence types are `reported_fact`, `derived_observation`, `hypothesis`, `null_result`, `published_allegation` and `published_adjudication`. Allowed subject scopes are `aggregate`, `published_case`, `named_public_business` and `anonymous_candidate`. Keep neutral company identity observations separate from an adverse inference. A new named adverse inference is rejected; already published adverse facts need `legal_status`, `legal_status_date`, source locators and `novelty.status=known_public_case`. This structured declaration is not a substitute for reading the prose before publication.

A failed source access is recorded as `retrieval_status=unavailable`. It can support a bounded null/access result, not a substantive conclusion from unread material. When a source snapshot was actually retained, add `snapshot_sha256` and an explicit `hash_scope`; never hash a summary and label it the original source.

## Money shape

Every money record includes `amount_id`, decimal-string `value`, three-letter `currency`, `measure`, `source_measure`, `payer`, `period`, `basis`, `qualifier`, `source_ids` and `is_recoverable_loss=false`.

Allowed measures are `submitted_claims`, `contract_ceiling`, `obligations`, `outlays`, `invoiced`, `disbursed_cash`, `withheld_escrow`, `recovered_cash`, `unit_price`, `reference_unit_price`, `estimated_exposure` and `price_difference`. For direct amounts, `measure` must equal the source measure. Billing, obligations, cash and escrow cannot be relabeled. Derived exposure/difference requires `calculation`; a unit-price difference must derive from actual unit/reference-unit price evidence, not a ceiling or obligation.

A unit-price record also has `comparison_terms`. The Claude packet requires all of: `item_identifier`, `revision`, `unit_of_issue`, `pack_size`, `quantity`, `price_date`, `condition`, `delivery`, `warranty` and `included_scope`. Record unknown terms honestly and decline a comparison that depends on them. Passing the presence check does not establish that terms are equivalent. The independent reviewer must examine the source values and adjustments.

Do not sum prime/subaward amounts, repeated award snapshots, payment states or overlapping case measures. Do not label a price difference as fraud loss, savings, recovery or an award base. Reward eligibility is not decided by this contract.

## Separate reviewer receipt

```json
{
  "schema_version": "1.0",
  "task_id": "EXACT_TASK_ID",
  "result_sha256": "EXACT_RESULT_DIGEST",
  "reviewer": {
    "agent_id": "DIFFERENT_REVIEWER",
    "session_id": "DIFFERENT_SESSION"
  },
  "reviewed_at": "ACTUAL_TIME_WITH_TIMEZONE",
  "decision": "needs_more_evidence",
  "checked_claim_ids": ["C1"],
  "material_checks_reproduced": false,
  "reason": "Source and calculation checks performed, outcomes and limits"
}
```

Allowed decisions are `supported_as_worded`, `supported_with_narrowing`, `unsupported`, `contradicted` and `needs_more_evidence`. The receipt must account for every claim and bind to the exact result digest. `supported_as_worded` requires reproduced material checks and a different worker/session; it means the declared reviewer supports that wording, not that fraud has been proved. Every other decision requires revision or more evidence. The worker cannot include a self-acceptance field in its result.

The coordinator verifies the reviewer's identity and actual check artifacts. Even an accepted result requires a separate public-evidence review before graph ingestion; this validator does not mutate the graph or submit anything.
