# PipeMind AI — Cryogenic Hydrogen Intelligence

> **Current status: TESTED RESEARCH PILOT CANDIDATE — NOT INDUSTRIAL CONTROL SOFTWARE.**
> Main branch holds the original research; current integrated code is in
> [`integration/pipemind-platform-2026-10-13`](https://github.com/charlie1906clark-del/pipemind-ai/tree/integration/pipemind-platform-2026-10-13).
> Subsequent changes are proposed under [the telemetry/deployment hardening PR](https://github.com/charlie1906clark-del/pipemind-ai/pull/13).
> No public production deployment, site validation or connection to plant control equipment is claimed.

PipeMind combines source-traceable hydrogen thermodynamics, offline digital-twin replay,
conservative prediction and transparent cost comparisons. Long-term research includes
liquid-hydrogen-cooled superconducting transmission cables.

## Product principles

- **Physics calculation separate from language models.** CoolProp thermophysical models
  implement literature EOS; PipeMind's tank and cable solvers are provisional and must
  be benchmarked against independent measured experiments before relying on results.
- **Advisory, not autonomous plant control.** There are no valve, compressor, refrigeration,
  SCADA, PLC or safety-interlock control endpoints.
- **Source and unit traceability.** Calculation boundaries, measurement quality and source
  status are visible; claims in historical notes are not automatically accepted as facts.
- **Human review and strict tenant boundaries.** OIDC/JWKS roles in production; read-only
  import and analysis, never direct OT access.

## Current modules

| Area | Current implementation | Industrial readiness |
|---|---|---|
| LH2 tank model | CoolProp-backed rigid, well-mixed two-phase equilibrium screening | Unvalidated for plant operation |
| Cryogenic cable model | Steady single-phase 1-D pressure/enthalpy screening | No quench or electrical rating |
| Measurements | Offline import, source/unit/freshness gates, idempotent tenant history | No certified instrument or gateway |
| Forecasts | Historical trend and persistence benchmark; abstention for irregular data | No site-calibrated model or safety alarm |
| Optimisation | Screening economics, abstention when equipment costs missing | No proven commercial savings |
| Route planner | Synthetic graph-cost demonstration with exclusions | No licensed UK GIS or routing sign-off |
| Research and reports | Searchable original Markdown, checked links, audit-linked report drafts | No regulatory certificates |
| Specialist agents | Six roles and deterministic review workflow | No deployed multi-agent autonomous runtime |
| Soteria/Wong APEX | Separate consent-controlled evidence bridge, draft ontology and adapter | Not live-connected |

## Local research installation

Requires Python 3.12+ recommended, CoolProp-compatible platform and pip:

```bash
git checkout integration/pipemind-platform-2026-10-13
python -m venv .venv
# Activate .venv using your platform's standard activation command
python -m pip install -e ".[test]"
```

Set these environment variables in your shell (use your own strong token, do **not**
commit it):

```bash
export PIPEMIND_ENV=development
export PIPEMIND_DEV_TOKEN="<generate-at-least-24-random-characters>"
export PIPEMIND_DB_PATH="./data/pipemind-local.sqlite"
uvicorn pipemind.api.app:app --host 127.0.0.1 --port 8080
```

Open `http://127.0.0.1:8080` and enter the same bearer token in the access screen.
The token stays in browser memory, not local storage. Never expose this dev-token mode
to a public network. The UI is a locally served research interface, not an operating
plant dashboard. The current hardening branch is not on `main`; use its Git branch
explicitly for the most recent features until reviewed.

Run the gates:

```bash
PYTHONPATH=src:tools python -m unittest discover -s tests -v
python tools/brain_search.py "hydrogen cooling" --limit 3
node --check web/assets/app.js
```

## Production container preconditions

`Dockerfile` and `deploy/docker-compose.yml` describe a single-node **read-only
research pilot**. It refuses to start in production without an HTTPS OIDC/JWKS identity
provider, audience and persistent database path. Production cannot set a dev token.

In addition to correct OIDC claims (`sub`, `tenant_id`, `pipemind_roles`, `exp`,
`iat`, `iss`, `aud`), supply a TLS-terminating reverse proxy/ingress that enforces
body limits, per-principal rate limits and authorised network access. The SQLite
pilot store is **not** appropriate for horizontal multi-tenant industrial deployment:
migrate to RLS-protected PostgreSQL and a real historian before commercial scaling.

```bash
cp deploy/.env.example deploy/.env
# Configure a real IdP and review its tenant/role claim mapping.
docker compose --env-file deploy/.env -f deploy/docker-compose.yml up --build
```

The sample compose file binds to loopback only. Do not expose it externally without
completed security, privacy, backups/restore, availability, architecture and equipment
review. In particular **never** connect PipeMind to an OT network with a general-purpose
write-capable API account.

## Current research scope and physics limitations

- EOS basis: J. W. Leachman et al., [NIST hydrogen equations of state](https://www.nist.gov/publications/fundamental-equations-state-parahydrogen-normal-hydrogen-and-orthohydrogen), DOI 10.1063/1.3160306; CoolProp version reported with results.
- The tank calculation treats rigid, closed, two-phase equilibrium hydrogen with fixed heat ingress, no liquid withdrawal, fill cycle, vent/relief behaviour, stratification, wall thermal inertia or ortho-para conversion heat.
- The cable calculation includes approximate Darcy friction and distributed thermal load, **not** MgB2 critical current, voltage rating, joint losses, AC losses or validated quench analysis.
- The simpler fixed-latent-heat *economic* scenarios do not imply measured plant boil-off or an automatic operating recommendation.
- Forecast values are historical research estimates, not real-time safety alarms.
- Supplier claims and market forecasts require original source/date review.

## Repo layout

```
src/pipemind/physics/        Hydrogen EOS, tank, cable research models
src/pipemind/twin/           Quality gates and historical forecasting
src/pipemind/api/            Tenant-scoped, authenticated API and app
src/pipemind/agents/         Deterministic specialist review (not LLM execution)
src/pipemind/integrations/   Curated separate APEX public-evidence contract
web/                        Local dashboard; SVG engineering schematics
docs/                       Original six-module engineering research and build plans
docs/research/               Dated source review and business positioning
data/evidence/              Curated bibliographic evidence manifest
tests/                      Regression, EOS, tenancy, audit and CI gates
```

## Critical gates still open

1. Independently benchmark the physics against measured LH2 tank and cable cases; obtain cryogenic engineering review.
2. Establish licensed/signed, one-way read-only plant data integration, calibration records and data-rights agreements.
3. Benchmark predictive accuracy and system net energy savings out of sample against physics/persistence, including cost of cooling, recovery and liquefaction.
4. Replace single-node SQLite with a hardened industrial historian/RLS data plane, threat-model API and credentials, run penetration tests and backups/recovery rehearsals.
5. Verify APEX deployment on a separately governed environment and run cross-tenant/PII leakage tests; the Wong branch and PipeMind branch are *not* automatically synced.
6. Commission site-specific industrial safety and applicable regulatory assessments, including independent process-safety and high-voltage specialists.

This is an AI-assisted engineering tool, not a substitute for competent design verification,
pressure protection, OT security controls or legally required safety assessment.
