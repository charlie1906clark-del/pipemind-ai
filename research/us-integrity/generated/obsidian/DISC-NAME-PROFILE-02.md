---
id: "DISC-NAME-PROFILE-02"
type: "recipient_profile"
title: "AMAZON.COM SERVICES LLC — C profile"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# AMAZON.COM SERVICES LLC — C profile

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "no_fraud_determination": true,
  "observed_at": "2026-10-30",
  "parent_field_is_not_ultimate_ownership": true,
  "profile_is_not_separate_company": true,
  "record": {
    "alternate_names": [
      "AMAZON.COM  INC."
    ],
    "business_types": [
      "category_business",
      "corporate_entity_not_tax_exempt",
      "limited_liability_corporation",
      "other_than_small_business",
      "special_designations",
      "us_owned_business"
    ],
    "duns": "128990418",
    "location": {
      "country_code": "USA",
      "state_code": "WA"
    },
    "name": "AMAZON.COM SERVICES LLC",
    "parent_duns": "884745530",
    "parent_id": "5fdd1c86-6551-bc97-900c-426613b1ba66-P",
    "parent_name": "AMAZON.COM, INC.",
    "parent_uei": "G5F2C46HBCM3",
    "recipient_id": "06d55b8d-0bcb-c654-8213-1001f38dd3d2-C",
    "recipient_level": "C",
    "uei": "TMKBFBRHFKH3"
  },
  "visibility": "public"
}
```

## Sources

- [[DISC-NAME-SRC-profile-02]]

## Outgoing relationships

- reports_recipient_uei: [[DISC-UEI-TMKBFBRHFKH3]] — documented_fact (DISC-E-f1ab0d1e8d0019cabd5e); sources: [[DISC-NAME-SRC-profile-02]]
- reports_parent_profile_reference: [[DISC-PARENT-UEI-G5F2C46HBCM3]] — documented_fact (DISC-E-f5610f9c476eecf00d62); sources: [[DISC-NAME-SRC-profile-02]]
- cites: [[DISC-NAME-SRC-profile-02]] — documented_fact (edge-daa21e145c76f66692c2); sources: [[DISC-NAME-SRC-profile-02]]

## Backlinks

- [[DISC-NAME-ANALYSIS]]: includes_profile — documented_fact (DISC-E-8a2fd6598b3df9a87b39)
