---
id: "DME-SRC-PUF-2022-A4352"
type: "source"
title: "CMS supplier detail: 2022 A4352"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2022 A4352

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "a7ddd5ca537c9d082656f4aeffcd671728e6f2e9f2cdb61c122e1103bdde55f8",
  "dataset_uuid": "dad703df-2e52-4ac6-a26f-51ecbf463d77",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2022",
  "request_manifest": "investigations/dme-catheter-2026-10-29/data-audit/acquisition_manifest.json",
  "selected_columns": [
    "Suplr_NPI",
    "Suplr_Prvdr_Ent_Cd",
    "Suplr_Prvdr_State_Abrvtn",
    "Suplr_Prvdr_Spclty_Cd",
    "Suplr_Prvdr_Spclty_Desc",
    "HCPCS_Cd",
    "HCPCS_Desc",
    "Suplr_Rentl_Ind",
    "Tot_Suplr_Benes",
    "Tot_Suplr_Clms",
    "Tot_Suplr_Srvcs",
    "Avg_Suplr_Sbmtd_Chrg",
    "Avg_Suplr_Mdcr_Alowd_Amt",
    "Avg_Suplr_Mdcr_Pymt_Amt",
    "Avg_Suplr_Mdcr_Stdzd_Amt"
  ],
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2022_A4352.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/dad703df-2e52-4ac6-a26f-51ecbf463d77/data?filter%5BHCPCS_Cd%5D=A4352&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-COHORT-2022-A4352-money-puf_payment]]: cites — documented_fact (edge-080a12735c999ea162a9)
- [[DME-COHORT-2022-A4352]]: cites — documented_fact (edge-0a37eeb3eff7156af076)
- [[DME-INV-20261029]]: cites — documented_fact (edge-152e32501ce9b51cdb09)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-286ac31f6c3626236990)
- [[DME-COHORT-2022-A4352-money-standardized_payment]]: cites — documented_fact (edge-58099fe225e0226c7f18)
- [[DME-NATIONAL-CHECK-2022-A4352]]: cites — documented_fact (edge-6f1b209a00d9d8fb9ca0)
- [[DME-FALS-17]]: cites — documented_fact (edge-71ebc66acd7b4d693d7a)
- [[DME-REVOCATION-CROSSCHECK-2022-ALL_THREE_CODES]]: cites — documented_fact (edge-84993ba925eae574b1fc)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-9125d69cd4c03859df30)
- [[DME-FALS-18]]: cites — documented_fact (edge-9328504cacdf5fbb1ec7)
- [[DME-ENTRY-CONTROL-2022-2023]]: cites — documented_fact (edge-97d766a67399253b16bd)
- [[DME-FALS-20]]: cites — documented_fact (edge-990be41938f450b78236)
- [[DME-CHANGE-2022-2023-A4352]]: cites — documented_fact (edge-9c6b81e585ef9de50621)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-aaa26648776cb4983369)
- [[DME-COHORT-2022-A4352-money-allowed]]: cites — documented_fact (edge-af2e325c105964886502)
- [[DME-REVOCATION-CROSSCHECK-2022-A4352]]: cites — documented_fact (edge-b2a950e79b2171d9b5a4)
- [[DME-COHORT-2022-A4352-money-submitted]]: cites — documented_fact (edge-f889f07ab29415b76573)
