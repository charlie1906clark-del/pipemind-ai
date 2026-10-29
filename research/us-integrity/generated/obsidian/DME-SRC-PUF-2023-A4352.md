---
id: "DME-SRC-PUF-2023-A4352"
type: "source"
title: "CMS supplier detail: 2023 A4352"
status: "source"
visibility: public
as_of: "2026-10-29"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2023 A4352

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "ed518fed359be3b20b529dddd2e19f66ab26d50ea9dcbe61e41b89357f07f891",
  "dataset_uuid": "44235fd3-6cf9-487f-928d-12998cd84071",
  "hash_scope": "Saved selected/normalized JSON bytes; not the complete upstream dataset or original HTTP wire response",
  "period": "2023",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2023_A4352.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/44235fd3-6cf9-487f-928d-12998cd84071/data?filter%5BHCPCS_Cd%5D=A4352&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-FALS-18]]: cites — documented_fact (edge-4551aa3f02d9b44e6347)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-501c66c633e18069f67d)
- [[DME-COHORT-2023-A4352]]: cites — documented_fact (edge-5de5bfc07c0f3a53dedb)
- [[DME-REVOCATION-CROSSCHECK-2023-ALL_THREE_CODES]]: cites — documented_fact (edge-65dcb782dd96c106a760)
- [[DME-NATIONAL-CHECK-2023-A4352]]: cites — documented_fact (edge-6c65526bbf88e88c31b5)
- [[DME-INV-20261029]]: cites — documented_fact (edge-77eddb1dbca7cb82a116)
- [[DME-COHORT-2023-A4352-money-allowed]]: cites — documented_fact (edge-78e6876016971d870c59)
- [[DME-FALS-20]]: cites — documented_fact (edge-7fa5827b17a19dff2065)
- [[DME-COHORT-2023-A4352-money-standardized_payment]]: cites — documented_fact (edge-83ef13504b8c53c46c69)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-8487e0bd8ec6eef6da64)
- [[DME-CHANGE-2022-2023-A4352]]: cites — documented_fact (edge-97d8f5d453fc1a617f2f)
- [[DME-COHORT-2023-A4352-money-puf_payment]]: cites — documented_fact (edge-9fe491d5f14b0833c426)
- [[DME-FALS-17]]: cites — documented_fact (edge-a7b64cb6bb0aa266978c)
- [[DME-CHANGE-2023-2024-A4352]]: cites — documented_fact (edge-cf76d8505055b91eb7aa)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-dd08679030ba8cfb972e)
- [[DME-REVOCATION-CROSSCHECK-2023-A4352]]: cites — documented_fact (edge-ed01d584f1895f307fc5)
- [[DME-COHORT-2023-A4352-money-submitted]]: cites — documented_fact (edge-f32d61a4d9c7629e3fc1)
- [[DME-ENTRY-CONTROL-2023-2024]]: cites — documented_fact (edge-f5a65b808406e40eb113)
