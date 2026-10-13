# Module dependency map and data contracts

```mermaid
flowchart TD
  R[Module 1: Route and civil geometry] --> C[Module 2: Cryogenic solver]
  R --> F[Module 4: Finance]
  C --> T[Module 5: Twin and forecasts]
  C --> S[Module 3: Safety scenarios - specialist validation]
  C --> F
  T --> F
  T --> A[AI advisory agents]
  R --> X[Module 6: Reports]
  C --> X
  S --> X
  F --> X
  T --> X
```

## Shared contracts (future)
`RunContext`: run ID, timestamp UTC, revision hashes, parameter references, unit registry, model version, quality flags.

`Asset`: site/tank/cable-segment ID, equipment revision, data rights, location sensitivity, calibration metadata.

`Measurement`: asset ID, variable, SI unit, time UTC, value, quality, origin, bounds.

`PhysicsResult`: output SI units, scenario, model limitations, input hashes, claim/evidence IDs, validation status.

`Recommendation`: options ranked by forecasted cost or risk, hard constraints, confidence, supporting PhysicsResults, human approver; never directly maps to an actuator command.

## Agent boundary
Agents can annotate research/interpret checked solver outputs and prepare draft reports. They must not manufacture pressure, safety, regulation or cost results. The physics and permissions service is the system of record.
