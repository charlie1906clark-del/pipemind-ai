# CMS catheter data audit

Read [REPORT.md](REPORT.md) for the completed 2022–2024 audit: 6,870 supplier rows, nine national comparator rows, exact-key growth decomposition, concentration, missingness and cash-status limits.

Reproduce from retained snapshots and verify provenance:

```sh
python audit_catheters.py
python -m unittest discover -s . -p "test_audit_contract.py" -v
```

The network refresh command is documented in the report. `source_registry.json` indexes primary-source captures, and `agent_result.json` is the structured handoff. `validation.json` records actual hash, count, schema, grain and paging checks.
