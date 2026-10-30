---
id: "DISC-NAME-INDEPENDENT-REVIEW"
type: "finding"
title: "Independent reconstruction confirms bounded name-query results"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Independent reconstruction confirms bounded name-query results

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "method": "Independent reconstruction from saved responses; audit module not imported",
  "source_record": "review/name_data_review.json",
  "verification": {
    "amazon_awards": 150,
    "amazon_dot_awards": 12,
    "amazon_dot_recipient_profiles": 2,
    "amazon_recipient_profiles": 6,
    "award_intersection": 12,
    "award_only_amazon": 138,
    "award_only_amazon_dot": 0,
    "child_profile_count": 3,
    "distinct_recipient_ueis": 3,
    "distinct_reported_parent_ueis_among_child_profiles": 1,
    "distinct_uei_name_collisions": 1,
    "fraud_determination": false,
    "money_summed": false,
    "normalized_name_groups": 2,
    "parent_profiles_reporting_self_parent": 3,
    "profile_level_counts": {
      "C": 3,
      "P": 3
    },
    "same_uei_multiple_names": 0,
    "same_uei_parent_child_pairs": 3
  },
  "verification_scope": "Verifies captured-query consistency and calculations, not legal identity, beneficial ownership, fraud, cash loss or national coverage.",
  "visibility": "public"
}
```

## Sources

- [[DISC-NAME-SRC-amazon-awards-1]]
- [[DISC-NAME-SRC-amazon-awards-2]]
- [[DISC-NAME-SRC-amazon-awards-3]]
- [[DISC-NAME-SRC-amazon-count-after]]
- [[DISC-NAME-SRC-amazon-count-before]]
- [[DISC-NAME-SRC-amazon-dot-awards-1]]
- [[DISC-NAME-SRC-amazon-dot-awards-2]]
- [[DISC-NAME-SRC-amazon-dot-count-after]]
- [[DISC-NAME-SRC-amazon-dot-count-before]]
- [[DISC-NAME-SRC-amazon-dot-recipients-1]]
- [[DISC-NAME-SRC-amazon-dot-recipients-2]]
- [[DISC-NAME-SRC-amazon-recipients-1]]
- [[DISC-NAME-SRC-amazon-recipients-2]]
- [[DISC-NAME-SRC-profile-01]]
- [[DISC-NAME-SRC-profile-02]]
- [[DISC-NAME-SRC-profile-03]]
- [[DISC-NAME-SRC-profile-04]]
- [[DISC-NAME-SRC-profile-05]]
- [[DISC-NAME-SRC-profile-06]]

## Outgoing relationships

- cites: [[DISC-NAME-SRC-amazon-recipients-1]] — documented_fact (edge-1a9604e00ec81b74b576); sources: [[DISC-NAME-SRC-amazon-recipients-1]]
- cites: [[DISC-NAME-SRC-amazon-dot-awards-1]] — documented_fact (edge-1db7fa6aad31546ec81e); sources: [[DISC-NAME-SRC-amazon-dot-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-recipients-2]] — documented_fact (edge-3d6bfa37c8f3208eeb50); sources: [[DISC-NAME-SRC-amazon-recipients-2]]
- cites: [[DISC-NAME-SRC-amazon-dot-awards-2]] — documented_fact (edge-46bf963ff9b330a10f65); sources: [[DISC-NAME-SRC-amazon-dot-awards-2]]
- cites: [[DISC-NAME-SRC-profile-02]] — documented_fact (edge-5539d1769c684f2352c5); sources: [[DISC-NAME-SRC-profile-02]]
- cites: [[DISC-NAME-SRC-amazon-count-after]] — documented_fact (edge-63b8275dec9aab80c845); sources: [[DISC-NAME-SRC-amazon-count-after]]
- cites: [[DISC-NAME-SRC-profile-03]] — documented_fact (edge-691b4b3c47e2a9a0ace6); sources: [[DISC-NAME-SRC-profile-03]]
- cites: [[DISC-NAME-SRC-amazon-awards-1]] — documented_fact (edge-7d9e60f1484ac82b632b); sources: [[DISC-NAME-SRC-amazon-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-after]] — documented_fact (edge-849348644292650a8260); sources: [[DISC-NAME-SRC-amazon-dot-count-after]]
- cites: [[DISC-NAME-SRC-amazon-awards-3]] — documented_fact (edge-8c73d8687eedbf27e26e); sources: [[DISC-NAME-SRC-amazon-awards-3]]
- cites: [[DISC-NAME-SRC-profile-05]] — documented_fact (edge-90cd39495ae623412eaa); sources: [[DISC-NAME-SRC-profile-05]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-2]] — documented_fact (edge-9cd73b6345908c568a1d); sources: [[DISC-NAME-SRC-amazon-dot-recipients-2]]
- cites: [[DISC-NAME-SRC-profile-06]] — documented_fact (edge-9dac8fab5ff03a1c1805); sources: [[DISC-NAME-SRC-profile-06]]
- cites: [[DISC-NAME-SRC-profile-04]] — documented_fact (edge-b079d3555c09530a357c); sources: [[DISC-NAME-SRC-profile-04]]
- cites: [[DISC-NAME-SRC-amazon-awards-2]] — documented_fact (edge-ba7e460f85264339d8b2); sources: [[DISC-NAME-SRC-amazon-awards-2]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-before]] — documented_fact (edge-c78d6be0ba1a7209d389); sources: [[DISC-NAME-SRC-amazon-dot-count-before]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-1]] — documented_fact (edge-c8f6a7848fe49caf7352); sources: [[DISC-NAME-SRC-amazon-dot-recipients-1]]
- cites: [[DISC-NAME-SRC-amazon-count-before]] — documented_fact (edge-ceff9ec9622929e97b21); sources: [[DISC-NAME-SRC-amazon-count-before]]
- cites: [[DISC-NAME-SRC-profile-01]] — documented_fact (edge-f6f677f7a6e211e1b976); sources: [[DISC-NAME-SRC-profile-01]]

## Backlinks

- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-c65f50d1efb85d2d1084)
