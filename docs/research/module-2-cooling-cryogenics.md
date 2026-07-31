# Module 2 Research – Cooling & Cryogenics Optimiser

## Purpose
Calculate temperature rise, pressure drop and optimal cooling-station spacing for liquid-hydrogen cooled superconducting cables.

## Core Physics
- Heat leak into the cryostat (typically 1–2 W/m for good insulation)
- Frictional pressure drop
- Temperature rise determined by mass flow rate and specific heat of LH₂
- Constraint: hydrogen must stay liquid with safety margin

## Key Published Ranges
- Heat leak: ~1.5–2 W/m typical
- Station spacing: 5–10 km (conservative) up to 50–75 km in optimised designs
- Current-lead heat load often ~50 W/kA per terminal

## Modelling Approach
Start with fast 1-D steady-state thermo-hydraulic equations. Later optional CFD for critical sections.

## Inputs the module needs
- Pipe diameter and insulation quality
- Mass flow rate
- Inlet temperature and pressure
- Cable current and residual losses
- Route length and elevation profile (from Module 1)

## Outputs
- Axial temperature and pressure profiles
- Maximum allowable station spacing
- Required cooling power per station
- Sensitivity to insulation degradation
