# Module 2 – Cooling & Cryogenics Optimiser
## Complete Research Synthesis

### Purpose
Calculate temperature rise, pressure drop and optimal cooling-station spacing for liquid-hydrogen cooled superconducting cables so that hydrogen remains liquid with adequate safety margin along the entire route.

### Core Physics
Liquid hydrogen at approximately 20 K cools the superconductor and simultaneously transports chemical energy. Continuous heat ingress from ambient, residual electrical losses and friction raise the fluid temperature and drop its pressure. The design must keep the fluid inside the liquid domain until the next recooling station.

### Key Published Values
- Heat leak: typically 1–2 W/m for high-quality multi-layer insulation (examples: 1.56 W/m for 60 mm class, ~2 W/m for larger cryostats)
- Current-lead heat load: often taken as ~50 W/kA per terminal (four terminals for bipolar)
- Station spacing: 5–10 km conservative; 20–50 km common in studies; up to 75 km claimed in highly optimised rigid-pipe GW-class designs
- Maximum pressure often limited by cryostat mechanical design (10–15 bar range in many concepts)

### Modelling Hierarchy
1. Fast 1-D steady-state thermo-hydraulic equations (primary for the module)
2. Higher-fidelity multi-physics / CFD for critical sections or validation
3. Indirect cooling variants (helium-filled protective pipe around the cable) exist for material compatibility and safety

### Required Inputs
- Inner diameter and insulation quality
- Mass-flow rate of LH₂
- Inlet temperature and pressure
- Cable current and estimated residual loss
- Route length and elevation profile (from Module 1)

### Outputs
- Axial temperature and pressure profiles
- Maximum allowable station spacing
- Required cooling power at each station
- Automatic station placement that minimises total capital + energy cost
- Sensitivity to insulation degradation, mass-flow change and ambient temperature

### Key Sources
Nature Communications Sustainability hybrid-pipeline tables, 75 km GW-class design paper, University of Bologna / Politecnico thermo-hydraulic work, KIT indirect-cooling experiments, SCARLET public parameters, Chinese composite pipeline studies.
