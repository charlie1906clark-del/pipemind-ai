---
id: "PA-W1-PAYMENT-BOLT"
type: "research_task_definition"
title: "Separate order, delivery, invoice and payment"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Separate order, delivery, invoice and payment

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "definition": {
    "agent_role": "PA-ROLE-PAYMENT",
    "allowed_source_hosts": [
      "api.usaspending.gov",
      "www.usaspending.gov",
      "dibbs2.bsm.dla.mil",
      "www.dla.mil",
      "sam.gov"
    ],
    "depends_on": [],
    "disconfirmation_tests": [
      "A credit, quantity adjustment or cancelled order removes the supposed excess.",
      "The recorded value is an obligation or order rather than disbursed cash."
    ],
    "expected_output": [
      "separate amount-basis ledger",
      "quantity reconciliation",
      "credits/returns/cancellations",
      "payment-to-line match and gaps"
    ],
    "id": "PA-W1-PAYMENT-BOLT",
    "independent_review_required": true,
    "invalid_inference": "No assumption that an order was paid or that a contract maximum was spent.",
    "max_attempts": 6,
    "max_evidence": 12,
    "max_reopens": 2,
    "question": "Can released transaction records establish any net paid line amount for the current order?",
    "result_contract": "role-contracts.json#common_contract",
    "scope": {
      "amount_bases": [
        "ordered_value",
        "invoiced_value",
        "paid_cash"
      ],
      "award_parent": "SPE4A626D61WS",
      "current_state": "Delivery requirement is2027-01-04; actual delivery/payment unverified as of2026-10-30.",
      "niin": "016864912",
      "nsn": "5306016864912",
      "order": "SPE4A627F0588",
      "prior_evidence": "investigations/dla-bolt-trace-2026-10-30/",
      "prior_state": "0.91USD perEA ×906EA is documented ordered value; no qualified benchmark, actual payment or benefit established",
      "public_record_only": true,
      "unknown_is_not_zero": true
    },
    "stop_and_reopen": "Stop at absent invoice/payment records; reopen on a released specific transaction document.",
    "title": "Separate order, delivery, invoice and payment"
  },
  "execution_state_in_definition": false,
  "visibility": "public"
}
```

## Sources

- [[PA-SRC-CURRENT-PLAN]]
- [[PA-SRC-ROLE-CONTRACTS]]

## Outgoing relationships

- assigned_role: [[PA-ROLE-PAYMENT]] — planned (PA-E-ec2647ac094078df72de0e7d); sources: [[PA-SRC-CURRENT-PLAN]], [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-ROLE-CONTRACTS]] — documented_fact (edge-a0497b47a674e43456d8); sources: [[PA-SRC-ROLE-CONTRACTS]]
- cites: [[PA-SRC-CURRENT-PLAN]] — documented_fact (edge-feb4a7ae79aba7e6c1c9); sources: [[PA-SRC-CURRENT-PLAN]]

## Backlinks

- [[PA-RUNSTATE-PA-W1-PAYMENT-BOLT]]: observes_task_state — documented_fact (PA-E-52051d0ae9a493991b807f06)
- [[PA-W1-REVIEW-BOLT]]: requires_accepted_packet — planned (PA-E-66e19397674b17592e814a1c)
- [[PA-WAVE-20261030-01]]: includes_task — planned (PA-E-9f7ec2c4cb70aa34c1c53349)
