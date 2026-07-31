# Module 2 – Cooling & Cryogenics Optimiser
## Super-Detailed Build Plan

### Goal
A calculator that takes pipeline geometry and operating conditions and returns temperature/pressure profiles plus optimal cooling station placement.

### Phase 1 – Core Solver
1. Implement hydrogen property lookups (density, Cp, viscosity) in the 15–30 K range
2. Write 1-D energy balance for temperature rise
3. Write momentum balance for pressure drop
4. Add heat-leak correlation (W/m or W/m²)
5. Enforce liquid-phase constraint with safety margin

### Phase 2 – Station Optimisation
6. Calculate maximum spacing for given conditions
7. Automatically place stations along a route
8. Compute total cooling power required
9. Simple cost proxy for number of stations

### Phase 3 – Usability
10. Clear input form (or API)
11. Profile plots (temperature and pressure vs distance)
12. Sensitivity sliders (insulation quality, mass flow, ambient)
13. Export results as tables and charts

### Phase 4 – Integration
14. Accept route length and elevation from Module 1
15. Pass heat load and station count to Module 4 (Cost)
16. Full documentation of equations and assumptions

### Definition of Done for v1
- Matches published example calculations within ~10%
- Engineer can complete a thermal design in under 15 minutes
- All assumptions are visible
