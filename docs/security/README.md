# PipeMind security / deployment boundary

## Stages
- Development: manually chosen >=24 character bearer token, local storage only, synthetic data.
- Production deployment: require OIDC/JWKS HTTPS issuer, audience, RS256/ES256 access token with tenant_id and pipemind_roles. No demo bypass. One trusted issuer. All API data denied without token.
- Data boundary: tenant in signature-verified token is never taken from request body or a header. Every SQLite read/write includes tenant filter. API binds all SQL values; observations append-only.
- No machine-control APIs or hardware credentials anywhere in PipeMind.
- Security headers; Content-Length guard; structured Pydantic schema; 1-worker SQLite deployment; audited append-only record with hash-chain verification.

## Material limitations before real customers
- SQLite is single-container pilot storage, not horizontally scalable. Use APEX PostgreSQL RLS or a dedicated tenant-isolated PostgreSQL service for industrial scale.
- In-memory local rate limits are not implemented; deploy at ingress with per-subject/IP quotas, timeouts, WAF and payload enforcement.
- ASGI Content-Length screening does not reject chunked bodies; configure proxy body-size caps and implement stream accounting.
- SQLite hash chaining detects modifications in place only when externally anchored; it is NOT tamper-proof storage.
- JWT JWKS fetching is environment-configured; pin approved IdP TLS and egress, monitor key rotation and revocation.
- No security audit, penetration test, backups/restore test or incident response exercise completed.
- No certification to IEC 62443, ISO 27001, COMAH, DSEAR, PSSR, ISO 21009-1 or any plant operating approval is claimed.
- Site sensors must enter via independently configured read-only DMZ/OT gateway; never direct PipeMind internet-to-PLC connectivity.

## Safe next gate
Independent cyber audit, OIDC integration tests with real issuer, separation of environments, backup/restore rehearsals, dependency and SBOM scanning, telemetry retention policy, customer contracts/data processing assessment, safety-engineer sign-off and monitored pilot.
