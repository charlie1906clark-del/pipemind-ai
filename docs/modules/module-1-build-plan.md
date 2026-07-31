# Module 1 – Smart Route Planner
## Super-Detailed Build Plan (Expert Level)

### Goal of v1
A working web tool where a user can set start and end points (or upload GeoJSON), adjust criterion weights with sliders, and receive three ranked route alternatives with statistics and exportable geometry.

### Development Phases and Exact Tasks

**Phase 1 – Core Engine**
1. Create package structure `src/route_planner/`
2. Implement cost-surface generation from weighted raster layers
3. Implement A* (or Dijkstra) pathfinding on the cost surface
4. Add ability to generate multiple alternatives by varying weights or using k-shortest path methods
5. Calculate basic statistics: total length, number and type of major crossings, percentage of route on major-road verge

**Phase 2 – Data Integration**
6. Load OpenStreetMap road network and apply strong preference to motorways and A-roads
7. Add protected-area avoidance layer
8. Add slope penalty derived from DEM
9. Support user-defined start/end coordinates and GeoJSON / KML upload
10. Handle basic barriers (large rivers, railways) as high-cost or forbidden cells

**Phase 3 – Interface**
11. Build interactive web map (Leaflet or Mapbox GL)
12. Add weight sliders for the five main criteria groups
13. Display the three ranked routes with clear colour coding
14. Show summary statistics panel
15. Export routes as GeoJSON, KML and a simple PDF map pack
16. Save each generated route version together with the exact weights used

**Phase 4 – Quality and Audit**
17. Validate against published case studies (Vidarbha, European open-data examples)
18. Document every modelling assumption in code and UI
19. Add performance testing for corridors up to 300 km
20. Error handling for missing data layers and invalid inputs

### Definition of Done for First Usable Version
- Three ranked routes generated and displayed
- Results fully explainable to an engineer
- Code is modular and ready for integration with other modules
- Can be demonstrated live in a customer conversation
