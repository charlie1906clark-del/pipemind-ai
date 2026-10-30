---
id: "DME-SRC-PUF-2024-A4353"
type: "source"
title: "CMS supplier detail: 2024 A4353"
status: "source"
visibility: public
as_of: "2026-10-30"
---
<!-- generated-by: us-integrity-engine-v1 -->

# CMS supplier detail: 2024 A4353

Evidence status: **source**.
This note records supplied sources; it does not independently establish fraud.

## Properties

```json
{
  "accessed_at": "2026-10-29",
  "completion": "Filtered stats count matched; next offset returned an empty page.",
  "content_sha256": "228793c093d4bd6587db97d321887f907c04d673f12bdabb92198be197aafdfb",
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
  "snapshot_path": "investigations/dme-catheter-2026-10-29/data-audit/snapshots/suppliers_2024_A4353.json",
  "source_bytes_archived": true,
  "url": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data?filter%5BHCPCS_Cd%5D=A4353&column=Suplr_NPI%2CSuplr_Prvdr_Ent_Cd%2CSuplr_Prvdr_State_Abrvtn%2CSuplr_Prvdr_Spclty_Cd%2CSuplr_Prvdr_Spclty_Desc%2CHCPCS_Cd%2CHCPCS_Desc%2CSuplr_Rentl_Ind%2CTot_Suplr_Benes%2CTot_Suplr_Clms%2CTot_Suplr_Srvcs%2CAvg_Suplr_Sbmtd_Chrg%2CAvg_Suplr_Mdcr_Alowd_Amt%2CAvg_Suplr_Mdcr_Pymt_Amt%2CAvg_Suplr_Mdcr_Stdzd_Amt&sort=Suplr_NPI&size=5000&offset=0",
  "visibility": "public"
}
```

## Sources

No supporting source attached; treat as an unverified planning record.

## Outgoing relationships

None recorded.

## Backlinks

- [[DME-COHORT-2024-A4353-money-standardized_payment]]: cites — documented_fact (edge-01c25da19b71e734e20d)
- [[DME-FALS-17]]: cites — documented_fact (edge-248857c56647cd043c31)
- [[DME-COHORT-2024-A4353-money-puf_payment]]: cites — documented_fact (edge-271653eb3b7a87b71345)
- [[DME-ENTRY-CONTROL-2023-2024]]: cites — documented_fact (edge-28a341ce24fa0c5883e5)
- [[DME-REVOCATION-COHORT-OVERVIEW]]: cites — documented_fact (edge-352b3f7b9cfef3365d38)
- [[DME-NATIONAL-CHECK-2024-A4353]]: cites — documented_fact (edge-469ed055bee00eb004b1)
- [[DME-PUF-PRESENCE-centennial]]: cites — documented_fact (edge-7c0ae65c6e937eee53cc)
- [[DME-COHORT-2024-A4353]]: cites — documented_fact (edge-8546efa121e3da448ce9)
- [[DME-COHORT-2024-A4353-money-submitted]]: cites — documented_fact (edge-9fcb73910cb3ecb66adc)
- [[DME-FALS-18]]: cites — documented_fact (edge-a1ea1c92b072229ba506)
- [[DME-FALS-20]]: cites — documented_fact (edge-a6265b61aff89a571bec)
- [[DME-REVOCATION-CROSSCHECK-2024-ALL_THREE_CODES]]: cites — documented_fact (edge-b97f9044314c0b3d8f50)
- [[DME-COHORT-2024-A4353-money-allowed]]: cites — documented_fact (edge-be380fa85214624354f4)
- [[DME-REVOCATION-CROSSCHECK-2024-A4353]]: cites — documented_fact (edge-c4227548bbbe311836e6)
- [[DME-PUF-PRESENCE-nd-medical]]: cites — documented_fact (edge-cbc26c2f9c454fd0dfca)
- [[DME-INV-20261029]]: cites — documented_fact (edge-cedfbe7861987e2b0836)
- [[DME-CHANGE-2023-2024-A4353]]: cites — documented_fact (edge-d1be401d9306bfa3746a)
