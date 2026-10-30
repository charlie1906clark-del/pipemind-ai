---
id: "BOLT-PRICE-EVIDENCE-CONTRACT"
type: "evidence_schema"
title: "Required evidence fields separate price, decision roles and actual benefits"
status: "planned"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Required evidence fields separate price, decision roles and actual benefits

Evidence status: **planned**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "field_groups": {
    "action_identity": [
      "agency",
      "awarding_office_code",
      "funding_office_code",
      "solicitation_id",
      "piid",
      "parent_piid",
      "order_id",
      "modification_id",
      "clin",
      "subclin",
      "action_date",
      "effective_date",
      "line_status",
      "cancelled_quantity",
      "superseded_by"
    ],
    "benchmark": [
      "benchmark_id",
      "benchmark_source_type",
      "quoted_at",
      "valid_until",
      "historical_or_current",
      "exact_product_match",
      "specification_match_evidence",
      "quantity_tier_match",
      "pack_normalization_evidence",
      "available_quantity",
      "deliverable_by_required_date",
      "compliance_accepted",
      "seller_independence_status",
      "upstream_manufacturer",
      "landed_unit_price_low",
      "landed_unit_price_central",
      "landed_unit_price_high",
      "adjustment_records",
      "qualification_decision",
      "excluded_reason"
    ],
    "benefit_nexus": [
      "benefit_record_id",
      "record_type",
      "dated_authoritative_source",
      "allegation_or_admission_or_finding",
      "benefit_provider_entity_id",
      "beneficiary_public_role_id_if_necessary",
      "benefit_type",
      "amount_if_source_established",
      "currency",
      "transaction_date",
      "procurement_decision_id",
      "nexus_evidence",
      "alternative_explanation",
      "legal_status_as_of",
      "underlying_records_examined"
    ],
    "bid_and_decision": [
      "bidder_uei",
      "bidder_cage",
      "submission_id",
      "submitted_at",
      "offered_clin_price",
      "quoted_delivery",
      "technical_acceptability",
      "withdrawal_date",
      "evaluation_criteria",
      "evaluation_score_or_reason",
      "award_rationale",
      "price_reasonableness_record",
      "sole_source_reason",
      "bid_document_hash",
      "native_metadata_if_lawfully_available",
      "role_assignment_id",
      "role_start",
      "role_end",
      "delegated_authority",
      "decision_timestamp"
    ],
    "commercial_terms": [
      "currency",
      "price_unit",
      "units_per_price_unit",
      "units_per_pack",
      "ordered_quantity_ea",
      "invoice_quantity_ea",
      "accepted_quantity_ea",
      "paid_quantity_ea",
      "unit_price",
      "extended_line_amount",
      "discount",
      "rebate",
      "credit",
      "return",
      "freight_responsibility",
      "freight_amount",
      "insurance",
      "tax",
      "duty",
      "minimum_order",
      "quantity_tier",
      "stock_at_quote",
      "lead_time",
      "delivery_due",
      "delivery_location_business_region",
      "payment_terms",
      "warranty",
      "first_article_or_nonrecurring_cost"
    ],
    "product": [
      "nsn",
      "approved_part_number",
      "manufacturer_part_number",
      "drawing_id",
      "drawing_revision",
      "specification_revision",
      "diameter",
      "length",
      "thread_series",
      "thread_class",
      "thread_hand",
      "head_style",
      "material",
      "grade",
      "finish_specification",
      "origin_requirement",
      "traceability_requirement",
      "sampling_plan",
      "test_report_requirement",
      "certificate_requirement"
    ],
    "professional_entity_links": [
      "link_id",
      "subject_public_business_id",
      "object_public_business_id",
      "relation_type",
      "role_name",
      "valid_from",
      "valid_to",
      "date_precision",
      "source_filed_at",
      "source_retrieved_at",
      "identity_join_method",
      "conflicting_evidence",
      "link_is_reported_or_verified",
      "professional_role_only"
    ],
    "provenance": [
      "record_id",
      "source_id",
      "source_url",
      "document_title",
      "document_date",
      "retrieved_at",
      "locator",
      "original_sha256_if_available",
      "saved_artifact_sha256",
      "hash_scope",
      "public_replay_path",
      "extraction_method",
      "source_claim_or_inference",
      "reviewer",
      "review_status"
    ]
  },
  "schema_not_populated_personal_data": true,
  "visibility": "public"
}
```

## Sources

- [[BOLT-PC-METHOD-S01]]
- [[BOLT-PC-METHOD-S02]]
- [[BOLT-PC-METHOD-S03]]

## Outgoing relationships

- cites: [[BOLT-PC-METHOD-S02]] — documented_fact (edge-1dd3b5830b75a07450c9); sources: [[BOLT-PC-METHOD-S02]]
- cites: [[BOLT-PC-METHOD-S03]] — documented_fact (edge-4cf07e019a2b8e8c7a54); sources: [[BOLT-PC-METHOD-S03]]
- cites: [[BOLT-PC-METHOD-S01]] — documented_fact (edge-67f2d093577da4e6003a); sources: [[BOLT-PC-METHOD-S01]]

## Backlinks

- [[BOLT-TRACE-20261030]]: records_finding — planned (BOLT-E-75b9fcb11dd235434caa)
