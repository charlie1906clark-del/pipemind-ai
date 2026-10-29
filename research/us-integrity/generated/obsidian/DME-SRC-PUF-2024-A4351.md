---
id: "DME-SRC-PUF-2024-A4351"
type: "source"
title: "CMS supplier detail: 2024 A4351"
status: "source"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2024 A4351

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "fc9f23b0aee3de42889120080b60a71bbd6158faad9c5930f407895f738168f7",
  "dataset_uuid": "1746a83e-bb65-4300-8e02-21edbab77c6b",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2024",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2024_A4351.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data?filter%5BHCPCS_Cd%5D=A4351&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-INV-20261029]]: cites — documented_fact (edge-03c138e0d7c1818cb3f9)
- [[DME-FALS-17]]: cites — documented_fact (edge-135cdcbb0a6e5e86cbc4)
- [[DME-COHORT-2024-A4351-money-allowed]]: cites — documented_fact (edge-1a3557e1acbe93d96be3)
- [[DME-COHORT-2024-A4351-money-submitted]]: cites — documented_fact (edge-200c8c81f31427678c4e)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-2e107c7673a53ba8f479)
- [[DME-REVOCATION-CROSSCHECK-2024-ALL_THREE_CODES]]: cites — documented_fact (edge-37f465485cc652386c92)
- [[DME-COHORT-2024-A4351-money-standardized_payment]]: cites — documented_fact (edge-41312e4f6e55cd96a56c)
- [[DME-REVOCATION-CROSSCHECK-2024-A4351]]: cites — documented_fact (edge-4986abd11ce2659971fe)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-552f9f299ca8d146ee84)
- [[DME-FALS-18]]: cites — documented_fact (edge-6c3d4104f9dca970a731)
- [[DME-COHORT-2024-A4351-money-puf_payment]]: cites — documented_fact (edge-6fadcd52a584bc4a2cd0)
- [[DME-NATIONAL-CHECK-2024-A4351]]: cites — documented_fact (edge-7d42f78d8c2c86d4dde5)
- [[DME-COHORT-2024-A4351]]: cites — documented_fact (edge-9d557e0e987fbdda14ed)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-aa8963768d8b633ed84e)
- [[DME-CHANGE-2023-2024-A4351]]: cites — documented_fact (edge-d294e4a9ed3f734e9a8f)
- [[DME-FALS-20]]: cites — documented_fact (edge-fa208632d2b044200037)
