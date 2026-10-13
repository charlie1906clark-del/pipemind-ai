# Cable extension — bounded research programme
Status: RESEARCH PROPOSAL ONLY, 2026-10-11

## Product thesis
A liquid-hydrogen storage/cooling twin and a hybrid superconducting transmission-line twin share temperature, mass, energy, equipment efficiency, sensor and economic accounting. Reuse these **interfaces**, not the same fluid model assumptions. A long cable is a spatially distributed, flowing, electrically loaded system, not a stationary boil-off tank.

## Evidence and competitor context
Prior art includes research on MgB2 cables cooled by LH2, the SCARLET programme and KIT/other laboratory concepts, documented in this repository's research. Verify current status directly with project publications before claiming originality or commercial readiness.

## Minimum physics before any claim
- Geometry: outer cryostat, coolant channel, insulation, cable type, joints, terminations, cooling stations and station siting.
- Thermal: axial heat ingress [W/m], AC/DC electrical losses, joint losses, current lead loss, reversible power if used, transient load cases and insulation-vacuum degradation.
- Hydraulic: hydrogen phase composition and accurate T/P-dependent properties, mass flow [kg/s], Darcy/validated correlations, elevation and local pressure loss; pressure/phase limits.
- Electrical: measured manufacturer-specific MgB2 critical current vs field and temperature with derating, electrical insulation and quench-protection design (separate specialist safety workflow).
- Economics: cold-side refrigeration watts, electrical COP, hydrogen pumping energy, capital/maintenance, actual hydrogen throughput and conventional HVDC + LH2 comparator.
- Risk: qualified hydrogen/cryogenic/electrical safety engineering; do not use crude risk metrics for setbacks.

## Model interfaces
`CableSegmentInput`: length_m, elevation_m, inner_diameter_m, mass_flow_kg_s, inlet_temp_K, inlet_pressure_Pa, heat_ingress_w_per_m, electric_heat_w_per_m, source_hashes, operating_domain.

`CableSegmentOutput`: terminal temperature_K, terminal pressure_Pa, station_cold_load_W, electrical_loss_W, phase_margin, constraint_flags, numerical_tolerance, model_version, uncertainty and evidence IDs.

Reject out-of-domain conditions. Do not invent temperature profiles from the fixed latent-heat tank screening equation.

## Staged implementation
1. Verify relevant primary papers and minimum physical operating envelope.
2. Implement isolated unit and dimensional checks; validate property backend.
3. Benchmark 1-D steady profiles against published experiment and independently calculated test cases; quantify residual errors.
4. Parameter sweeps for inlet T/P, mass flow, insulation degradation, joint heat and cable load; distinguish credible vs hypothetical.
5. Fault simulations performed offline with separate validated specialist tools and independent reviewers.
6. Pilot only with OEM/university partner, certified equipment and proper permissions.

## Commercial hypothesis
The initial commercial differentiator is integrated cryogenic + cable total-cost optimisation, **not** an unproven frequency-based change of hydrogen's phase. Validate against independent infrastructure solutions and account for high liquefaction/refrigeration energy.
