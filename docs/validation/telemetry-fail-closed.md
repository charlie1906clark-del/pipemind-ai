# Offline telemetry and forecast v0.3 — fail-closed rules

## Validated ingestion sources
Only `simulated` and authenticated `operator-import` string tags are permitted. These are **labels**, not cryptographic source authenticity. The previous `signed-gateway` label was incorrectly accepted without any verified signature; it has been disabled pending a gateway-specific mutual-authentication protocol and OT/IT security review.

## Data-quality gates
Check fixed SI units, numeric validity, asset ID, UTC timestamps, future/skewed data and 31-day historical import window. Duplicate identity is (tenant, asset, metric, UTC timestamp, source): repeated network deliveries are ignored rather than silently overwriting values. Changed same-timestamp values need explicit versioned correction.

## Replay forecasting
- Requires >=12 samples of one metric/unit/source with strictly increasing timestamps and consistent cadence (within 10% or 1 second).
- Trend model is compared against persistence on rolling holdouts; descriptive historical error band is **not** a calibrated uncertainty guarantee.
- Irregular or mixed-source input produces abstention, not a confident forecast.
- Forecast is explicitly marked REPLAY/RESEARCH ONLY; no live operating alert, equipment setpoint or safety claim.
- Result snapshots include source and last historical timestamp.

## Before production telemetry
Use source-signed transport, gateway isolation, OT/IT one-way network architecture where feasible, certificate rotation, replay and sequence handling, calibration register, asset ownership, retention and evidence of independent security review. Reference NIST SP 800-82 Rev. 3 and IEC 62443 series; neither is certification.
