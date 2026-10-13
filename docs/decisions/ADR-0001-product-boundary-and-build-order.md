# ADR-0001: Product boundary and build order
Date: 2026-10-11
Status: proposed for review

## Context
PipeMind's six modules cover hybrid LH2/superconducting transmission. The main branch contains research and build plans but no executable source, test harness, or live industrial integrations. The most commercially testable first wedge is **decision support for liquid-hydrogen thermal management**, later extended to cryogenic cable analysis.

## Decision
1. Keep every original research note intact on `main`. Treat research statements as claims requiring independent verification, **not** trusted numerical constants or compliance approval.
2. Deliver a traceable **screening calculation** first: heat ingress -> potential vaporisation -> cost, including candidate cold-side cooling and captured vapour. This is not a pressure, thermo-hydraulic, safety, or actual plant-control model.
3. Then implement a validated LH2 thermophysical property provider with source, valid temperature/pressure domain, uncertainty and boundary handling; add mass/energy balances and sensor quality checks.
4. Introduce data-driven forecasting only after holdout validation against a physics-only baseline. Optimisation must be subject to physical and safety constraints and remain operator advisory.
5. Extend shared thermal models to MgB2 cable segments after validation and competent engineering review.
6. Retain route planning, safety, finance and reports as separate domain packages that consume versioned physics outputs.

## Separation of responsibilities
- Physics engine: deterministic, unit tested, versioned parameters, defined validity ranges.
- Digital twin: observation/state estimation; sensor provenance and uncertainty.
- Forecast/optimiser: ranked options, expected cost, confidence and constraints.
- LLM agents: research, explain and draft; **never** change operating setpoints or certify designs.
- Instrumentation and safety: independent plant PLC/SIS, mechanical protection and engineering sign-off.

## Non-goals of first delivery
No claims of safer design, certified compliance, pressure prediction, quench protection, gas dispersion, operational savings, 'zero boil-off' or autonomous control. No assumptions about physics improvements through frequency/light.

## Rejected alternatives
- Building all six modules in parallel before a verified solver.
- Using an LLM to infer hydrogen property tables or calculate safety standoffs.
- Deploying direct actuation of valves, refrigeration or electrical equipment.

## Decision gates
G0 unit and dimensional tests; G1 benchmark against authoritative published data; G2 independent specialist review; G3 closed-loop simulation and fault injection; G4 site-specific, authorised read-only pilot. Actuation requires a **separate** formal engineering and regulatory programme.
