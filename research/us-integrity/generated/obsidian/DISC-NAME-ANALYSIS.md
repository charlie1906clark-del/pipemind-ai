---
id: "DISC-NAME-ANALYSIS"
type: "finding"
title: "Neutral recipient-name and punctuation comparison"
status: "documented_fact"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# Neutral recipient-name and punctuation comparison

Evidence status: **documented_fact**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "calculation": {
    "as_of": "2026-10-30",
    "award_distinct_uei_count": 3,
    "award_groups": [
      {
        "automatic_entity_merge": false,
        "comparison_key": "amazon com services llc",
        "distinct_raw_names": [
          "AMAZON.COM SERVICES LLC"
        ],
        "distinct_valid_ueis": [
          "TMKBFBRHFKH3"
        ],
        "fraud_determination": false,
        "missing_or_invalid_uei_rows": 0,
        "observations": [],
        "profile_level_pair_count": 0,
        "record_count": 11
      },
      {
        "automatic_entity_merge": false,
        "comparison_key": "amazon web services inc",
        "distinct_raw_names": [
          "AMAZON WEB SERVICES, INC",
          "AMAZON WEB SERVICES, INC."
        ],
        "distinct_valid_ueis": [
          "H6S2VKM5U6C5",
          "NQEWN6C1LSU5"
        ],
        "fraud_determination": false,
        "missing_or_invalid_uei_rows": 0,
        "observations": [
          "name_format_variation",
          "shared_comparison_key_distinct_ueis"
        ],
        "profile_level_pair_count": 0,
        "record_count": 139
      }
    ],
    "award_missing_uei_rows": 0,
    "award_raw_name_count": 3,
    "award_rows": 150,
    "distinct_valid_recipient_ueis": 3,
    "fraud_scoring_performed": false,
    "keyword_variant_symmetric_difference_count": 138,
    "keyword_variants_return_identical_award_ids": false,
    "money_summed": false,
    "new_fraud_established": false,
    "profile_parent_uei_present_rows": 6,
    "query_scope": "Two literal recipient keywords, contract recipients and FY2026 prime contracts; no national entity census",
    "recipient_groups": [
      {
        "automatic_entity_merge": false,
        "comparison_key": "amazon com services llc",
        "distinct_raw_names": [
          "AMAZON.COM SERVICES LLC"
        ],
        "distinct_valid_ueis": [
          "TMKBFBRHFKH3"
        ],
        "fraud_determination": false,
        "missing_or_invalid_uei_rows": 0,
        "observations": [
          "same_uei_parent_and_child_profile_levels"
        ],
        "profile_level_pair_count": 1,
        "record_count": 2
      },
      {
        "automatic_entity_merge": false,
        "comparison_key": "amazon web services inc",
        "distinct_raw_names": [
          "AMAZON WEB SERVICES, INC",
          "AMAZON WEB SERVICES, INC."
        ],
        "distinct_valid_ueis": [
          "H6S2VKM5U6C5",
          "NQEWN6C1LSU5"
        ],
        "fraud_determination": false,
        "missing_or_invalid_uei_rows": 0,
        "observations": [
          "name_format_variation",
          "shared_comparison_key_distinct_ueis",
          "same_uei_parent_and_child_profile_levels"
        ],
        "profile_level_pair_count": 2,
        "record_count": 4
      }
    ],
    "recipient_levels": {
      "C": 3,
      "P": 3
    },
    "recipient_profile_rows": 6,
    "same_uei_multiple_raw_names_count": 0,
    "scope_limitations": [
      "Comparison keys do not merge legal entities, beneficial owners or liabilities.",
      "Recipient P/C/R profile levels are not separate companies; amounts must not be summed across them.",
      "Recipient amounts are trailing-12-month transaction aggregates; award amounts are cumulative award measures, not FY2026 cash or fraud loss.",
      "Award date filter uses documented default award-search timing; this is not a list of every FY2026 transaction.",
      "Keyword matching is an index search, not an exact legal-name search; these queries exclude other sectors and aliases without this token.",
      "Parent links are source-reported profile relationships, not verified ultimate beneficial ownership.",
      "No name variation establishes a fake company, false claim, improper payment or reward eligibility."
    ]
  },
  "no_fraud_determination": true,
  "source_record": "names/analysis.json",
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

- includes_profile: [[DISC-NAME-PROFILE-04]] — documented_fact (DISC-E-0fb66a03817cab4c8086); sources: [[DISC-NAME-SRC-profile-04]]
- includes_profile: [[DISC-NAME-PROFILE-05]] — documented_fact (DISC-E-22334ffd66ff2bd2b777); sources: [[DISC-NAME-SRC-profile-05]]
- includes_profile: [[DISC-NAME-PROFILE-06]] — documented_fact (DISC-E-2697737706e812284a31); sources: [[DISC-NAME-SRC-profile-06]]
- includes_profile: [[DISC-NAME-PROFILE-03]] — documented_fact (DISC-E-7aa8f13281918c3e26a4); sources: [[DISC-NAME-SRC-profile-03]]
- includes_profile: [[DISC-NAME-PROFILE-01]] — documented_fact (DISC-E-7ba943482b1cf6f5f4e2); sources: [[DISC-NAME-SRC-profile-01]]
- includes_profile: [[DISC-NAME-PROFILE-02]] — documented_fact (DISC-E-8a2fd6598b3df9a87b39); sources: [[DISC-NAME-SRC-profile-02]]
- cites: [[DISC-NAME-SRC-profile-01]] — documented_fact (edge-143580bdc9c628ce689f); sources: [[DISC-NAME-SRC-profile-01]]
- cites: [[DISC-NAME-SRC-amazon-dot-awards-2]] — documented_fact (edge-1abb710a9636e3f00848); sources: [[DISC-NAME-SRC-amazon-dot-awards-2]]
- cites: [[DISC-NAME-SRC-profile-05]] — documented_fact (edge-431d507ac9f3bd899ea7); sources: [[DISC-NAME-SRC-profile-05]]
- cites: [[DISC-NAME-SRC-profile-03]] — documented_fact (edge-4cd8fb4ec3500e6595a3); sources: [[DISC-NAME-SRC-profile-03]]
- cites: [[DISC-NAME-SRC-amazon-recipients-2]] — documented_fact (edge-6abd26bdef8d0d615e70); sources: [[DISC-NAME-SRC-amazon-recipients-2]]
- cites: [[DISC-NAME-SRC-amazon-awards-3]] — documented_fact (edge-6ad4a1d9d44d763aed9a); sources: [[DISC-NAME-SRC-amazon-awards-3]]
- cites: [[DISC-NAME-SRC-amazon-awards-2]] — documented_fact (edge-6c42860b2cf1270bf70a); sources: [[DISC-NAME-SRC-amazon-awards-2]]
- cites: [[DISC-NAME-SRC-profile-04]] — documented_fact (edge-711366c047516c2e390e); sources: [[DISC-NAME-SRC-profile-04]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-2]] — documented_fact (edge-7488157bd843df04b9b2); sources: [[DISC-NAME-SRC-amazon-dot-recipients-2]]
- cites: [[DISC-NAME-SRC-amazon-count-after]] — documented_fact (edge-77019f3ecf2c1780ff26); sources: [[DISC-NAME-SRC-amazon-count-after]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-after]] — documented_fact (edge-7ca78886ec30093d0c87); sources: [[DISC-NAME-SRC-amazon-dot-count-after]]
- cites: [[DISC-NAME-SRC-amazon-dot-count-before]] — documented_fact (edge-983a17ddd9099db84c23); sources: [[DISC-NAME-SRC-amazon-dot-count-before]]
- cites: [[DISC-NAME-SRC-amazon-count-before]] — documented_fact (edge-a15ec9d9df1f9beb8e6d); sources: [[DISC-NAME-SRC-amazon-count-before]]
- cites: [[DISC-NAME-SRC-profile-06]] — documented_fact (edge-b8de68660b54b9ad3210); sources: [[DISC-NAME-SRC-profile-06]]
- cites: [[DISC-NAME-SRC-amazon-dot-awards-1]] — documented_fact (edge-b97f514ef39ae656f057); sources: [[DISC-NAME-SRC-amazon-dot-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-awards-1]] — documented_fact (edge-daae6bd42ea892411881); sources: [[DISC-NAME-SRC-amazon-awards-1]]
- cites: [[DISC-NAME-SRC-amazon-recipients-1]] — documented_fact (edge-de20ce882887581f5426); sources: [[DISC-NAME-SRC-amazon-recipients-1]]
- cites: [[DISC-NAME-SRC-amazon-dot-recipients-1]] — documented_fact (edge-ece8dbb030570eff71f0); sources: [[DISC-NAME-SRC-amazon-dot-recipients-1]]
- cites: [[DISC-NAME-SRC-profile-02]] — documented_fact (edge-f31bf9c8c47e79545064); sources: [[DISC-NAME-SRC-profile-02]]

## Backlinks

- [[DISC-20261030]]: records_observation — documented_fact (DISC-E-b906456f67f392590059)
