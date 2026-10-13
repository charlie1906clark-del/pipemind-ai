# NASA K-Site and MHTB experiments as future benchmark anchors

The paper **S. Fernandes et al., A CFD comparison of interfacial phase change models for boil-off, self-pressurisation and thermal stratification in liquid hydrogen storage tanks** (International Journal of Heat and Mass Transfer 256, March 2026, article 128067; DOI 10.1016/j.ijheatmasstransfer.2025.128067) compares Schrage, modified energy jump and Lee interfacial phase-change models against **five NASA experiments**.

Original source: https://www.sciencedirect.com/science/article/pii/S0017931025014024

The project now holds a machine-readable manifest at `src/pipemind/validation/nasa_cases.json` recording five published cases and identified tank volume, fill, net heat, initial pressure and duration. **This file does not include measured time-series values**, sensor calibrations or full model boundaries. Nothing in this registry establishes PipeMind's current simplified tank model accurately reproduces the published experiment.

Important physical finding: NASA K-Site initial temperatures were vertically stratified; MHTB input temperatures were treated as approximately isothermal in the 2026 CFD paper. PipeMind's closed homogeneous equilibrium approximation ignores these gradients, tank wall conduction, interface kinetics, liquid withdrawal and pressure relief. Consequently a correct first-order EOS solver can diverge substantially from the transient behaviour.

## Next research step
1. Obtain the original K-Site and MHTB **numerical experimental traces** with data redistribution rights. If only graphs are available, record digitisation uncertainty explicitly and obtain human review.
2. Confirm para/ortho composition, initial stratification, wall-specific heat, heat-flux distribution, geometry, vessel mass, material, vent history and sensor precision.
3. Run PipeMind's current approximation with only traceable inputs; report error metrics against blind withheld pressure and temperature observations. Do not calibrate and score on the same trace.
4. Implement and compare a stratified finite-volume two-zone model before moving to high-cost CFD.
5. Document thermodynamic domain and uncertainty; obtain qualified cryogenics-engineer review.

Reference design for the hybrid cable: [Cryogenic Tests of 30 m Flexible Hybrid Energy Transfer Line with Liquid Hydrogen and Superconducting MgB₂ Cable](https://www.sciencedirect.com/science/article/pii/S1875389215004149) documents experimentally tested temperature (20–26 K), mass flow (100–450 g/s) and line pressure (0.25–0.5 MPa) in a 30-m prototype. Its reported cable current of approximately 3500 A near 21 K is an experimental critical current, **not a general installed cable's operating rating**. Thermo-hydraulic results for various insulation modes should not be applied to a different geometry without validation.

NASA's [Ground Operations Demonstration Unit](https://ntrs.nasa.gov/citations/20180006814) involved a 125,000-L tank with integrated refrigeration. These experiments provide particularly useful case studies for future refrigeration-control research, but access to full test curves is still a prerequisite for claiming quantitative validation.
