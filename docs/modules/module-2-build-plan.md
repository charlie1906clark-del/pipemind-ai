# Module 2 – Cooling & Cryogenics Optimiser
## Super-Detailed Build Plan

### Goal of v1
A fast, transparent calculator that produces temperature/pressure profiles and optimal cooling-station placement for a hybrid LH₂ + superconducting pipeline.

### Phase 1 – Core Solver
1. Implement accurate hydrogen property tables (density, Cp, viscosity, thermal conductivity) covering 15–30 K and 0.5–15 bar
2. Code the 1-D energy balance for temperature rise
3. Code the momentum balance for pressure drop (including corrugated-pipe friction factors where relevant)
4. Implement heat-leak correlation (both W/m and W/m² forms)
5. Enforce liquid-phase constraint with configurable safety margin

### Phase 2 – Station Logic
6. Calculate maximum spacing for given conditions
7. Automatically place stations along a route length
8. Compute required cooling power per station
9. Simple capital-cost proxy for number of stations

### Phase 3 – Usability
10. Clear input interface (form or API)
11. Profile plots (T and P versus distance)
12. Sensitivity panel with live sliders
13. Export of tables, charts and assumption list

### Phase 4 – Integration & Audit
14. Accept route geometry and elevation from Module 1
15. Pass heat load and station count to Module 4 (Cost)
16. Full documentation of every equation and source

### Definition of Done
- Reproduces published example calculations within ~10%
- Engineer can complete a thermal design in under 15 minutes
- All assumptions visible and exportable
