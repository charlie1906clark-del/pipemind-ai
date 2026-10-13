# Tenant-private audit integrity (v0.3)

The system maintains one append-only SQLite audit chain for all tenants.
Previously `/api/v1/audit/verify` exposed the **global event count and head hash**
to any tenant auditor. That leaked cross-customer platform activity metadata.

The endpoint now verifies every hash internally and responds with only:
- an integrity boolean and the caller's own event count;
- a fingerprint calculated solely over the caller's event hashes;
- no cross-tenant records, global head or sequence position.

The internal store can still verify its whole chain and return the global
head to a properly separated host-level anchoring job. **No external
anchoring job is deployed or configured yet**. The local fingerprint is not
cryptographic evidence that an operator with full database access cannot
rewrite an entire history. An independent WORM/time-stamped audit anchor and
backup/restore verification remain release gates.

Mixed tenant history corruption fails closed but discloses no position or
which customer triggered it.
