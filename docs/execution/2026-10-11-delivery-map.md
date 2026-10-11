# Delivery map — PipeMind AI (2026-10-11)

## Repo inventory and status
- Default branch `main` at `4c291bd2b5674a8edd9ec96eeae7ec57448a9ce1` when inventoried.
- 66 entries including directories; 6 module research notes + 6 build plans, historical updates, 2 company profiles, X-agent markdown and recent marketing notes.
- Obsidian Brain is **a proposed vault structure** in `docs/02-obsidian-brain.md`, not a standalone database, trained model, running knowledge graph or continuously retrained system.
- No application code, tests, live sensor integration or model weights were present on `main` at inventory.

## Strategic Git branches
| Branch | Scope | Milestone |
| --- | --- | --- |
| `plan/knowledge-architecture` | Decision records, evidence governance, milestones | Common architecture and traceability |
| `feat/cryogenic-screening-engine` | First physics calculation, typed data, tests, CI | Transparent screening model |
| `feat/agent-governance` | Specialist AI role contracts, orchestration and escalation | Auditable advisory agents |
| `research/superconducting-cable` | Future segment physics and interface contracts | Research backlog, no invented validation |

All branches are based on the original `main` and are independent drafts. Do not merge without checking conflicts, tests and domain expert review.

## Build loops and exit criteria
### Loop 0 — Preserve the brain
1. Inventory notes and dependencies; preserve originals.
2. Make an evidence ledger tagging claims: verified primary source, secondary source, assumption, stale, disputed.
3. Align source and formula ownership to each module.
**Exit:** every modelled constant is linked to provenance and validity domain.

### Loop 1 — Screening model (first vertical slice)
1. Implement heat-ingress -> latent-heat evaporation equivalent with limits and consistent units.
2. Compare cooling/vent recovery scenarios; price assumptions explicit.
3. Negative/NaN/oversupply guards and mass/energy balance tests; CI.
**Exit:** code executes; no unsupported pressure or safety claims.

### Loop 2 — Research-grade LH2 properties and transients
1. Introduce validated property backend with versioned source data covering operating domain; distinguish ortho/para composition.
2. Add control-volume mass-energy balance and phase-equilibrium regime classification.
3. Benchmark against published test cases and report uncertainty.
**Exit:** quantitative accuracy pre-agreed with cryogenics reviewer over stated validity range.

### Loop 3 — Digital twin + AI
1. Versioned immutable sensor snapshots (UTC time, units, calibration, missing data).
2. Physics baseline and forecasting on holdout data; drift/out-of-distribution tests.
3. Constraint-based recommendation ranking; deterministic gates; explainability and approval logs.
**Exit:** forecasts exceed baseline with documented metrics and failure-mode tests.

### Loop 4 — Cable extension
1. Segment-level steady 1-D heat ingress and coolant flow interfaces, independent cryogenic boundary assumptions.
2. MgB2 critical-current curves from manufacturer/test evidence; conservative thermal margin; quench escalation to external specialist tools.
3. Compare whole-system LH2 + cable cost against independent HVDC + LH2 options.
**Exit:** independently reviewed published/design-case benchmark, not an operational safety rating.

### Loop 5 — Customer evidence
Identify an LH2 operator/OEM/research group; negotiate **read-only and anonymised** datasets and objectives. Validate measured rather than projected savings. Regulatory and cyber assessment before any field deployment.

## Dependencies and governance
- Route costs feed finance but **not** safety certification.
- Cooling feeds twin and cable thermal boundary conditions.
- Safety module is a research/requirements interface until validated specialist solvers are approved.
- Reports must reproduce numeric outputs and claim status without generating unverified certifications.
- Marketing agents remain isolated from engineering agents.

## First pilot acceptance criteria
Reproducible reference dataset; versioned assumptions; baseline-vs-model error summary; offline recommendation audit; human sign-off; confirmed data rights; documented security and resilience controls. No equipment control.
