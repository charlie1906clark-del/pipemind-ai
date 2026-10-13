# Test protocol — LH2 tank model vs measured pressure (research only)

The first comparative validation slice uses an existing tank run `run_id` (which fixes the input model, EOS version and assumptions), a separately time-stamped offline instrument pressure series in SI Pascals, and an explicit operator-defined `model_start_utc`. We interpolate model pressure to observation times and calculate MAE, RMSE, mean signed bias and MAPE.

## Required before using measured facility data
- Dataset rights and confidentiality classification; independently authorised read-only export.
- Instrument calibration history, sampling period and source identity.
- Precisely known tank geometric volume, inventory/fill fraction, para/ortho composition, initial temperature/pressure, heat transfer, pressure limits and withdrawal/vent history.
- A full experimental setup description; never infer actual heat ingress or pressure directly from liquid fill alone.
- Pre-agreed benchmark error tolerance by a qualified domain reviewer, and holdout datasets that the solver was **not** calibrated on.
- Explicit record that current solver lacks stratification, wall inertia, withdrawals, venting and conversion heat.

A perfect match with generated synthetic data proves mathematical interpolation and data plumbing **only**. It does not demonstrate accuracy on industrial LH2 equipment.

Results must say RESEARCH_BENCHMARK_NOT_CERTIFICATION; zero observations, invalid units, timestamps or missing overlap must never be reported as passing validation.
