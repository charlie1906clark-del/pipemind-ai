# Module 1 – Smart Route Planner
## Super-Detailed Build Plan

### Goal
A web-based tool where a user sets start and end points (or uploads a corridor), adjusts weights for different criteria, and receives 3 ranked route options with statistics and exportable geometry.

### Phase 1 – Core Engine (Week 1–2 of building)
1. Set up a clean Python package `src/route_planner/`
2. Create a cost-surface generator that accepts weighted raster layers
3. Implement A* or Dijkstra pathfinding on the cost surface
4. Add ability to generate multiple alternative routes (k-shortest or varied weights)
5. Calculate basic statistics: length, number of major crossings, % on road verge

### Phase 2 – Data & Constraints
6. Integrate OpenStreetMap road data (motorways + A-roads bias)
7. Add simple protected-area avoidance
8. Add slope penalty
9. Allow user-defined start/end coordinates or GeoJSON upload

### Phase 3 – Interface & Output
10. Simple web map (Leaflet or Mapbox) showing the routes
11. Weight sliders for the main criteria groups
12. Export as GeoJSON + summary table
13. Save route versions with their weight settings

### Phase 4 – Hardening
14. Validation against published case studies
15. Clear documentation of every assumption
16. Error handling and performance testing on 200+ km corridors

### Definition of Done for v1
- User can generate 3 ranked routes
- Results are fully explainable
- Code is clean and modular
- Ready to demonstrate to a real engineer
