# Module 1 – Smart Route Planner
## Complete Research Synthesis

### Purpose
Automatically find the best physical corridor for a hybrid liquid-hydrogen + superconducting energy pipeline. Strongly prefer existing major-road verges (motorways and A-roads) while balancing capital cost, environmental impact, safety, constructability and future expansion.

### Core Problem
A hybrid SCEP corridor is not a simple shortest-path problem. It must minimise disruption, avoid protected areas, respect slope and soil limits, count major crossings, and still stay close to the road network that the original concept targeted.

### Algorithms and Methods
- Least-Cost Path (LCP) on a multi-criteria cost surface
- Dijkstra or A* pathfinding
- Analytical Hierarchy Process (AHP) and weighted scoring for criteria
- Generation of multiple ranked alternatives (Best Cost, Best Environment/Safety, Shortest)
- Wide-corridor and multi-modal routing concepts from academic work
- Optional Simulated Annealing or genetic algorithms for joint geometry + hydraulic optimisation later

### Criteria Groups
1. Economy – length, number of crossings, slope severity
2. Engineering – soil type, geology, existing utility corridors, constructability
3. Environment – protected areas (Natura 2000, SSSIs), habitats, water bodies
4. Social – population density, settlements, visual impact
5. Hazard – seismic, landslide, flood risk

### Essential Data Layers
- Road centre-lines and carriageway (OpenStreetMap or national highways data) – motorways + A-roads preferred
- Existing pipeline, cable and utility rights-of-way
- Land cover / land use (CORINE or national)
- Protected areas
- Digital elevation model and derived slope
- Population density and building footprints
- Rivers, railways, major crossings
- Soil, geology, seismic and landslide susceptibility
- Client private layers (ownership, planning applications)

### Commercial and Open-Source Tools Referenced
- CostMAP PRO (Carbon Solutions) – specialised for hydrogen and energy pipelines
- Esri ArcGIS Network Analyst
- PowerLine-GIS open European friction layers and scripts
- QGIS + GRASS r.cost / r.walk
- Python stack: networkx, rasterio, geopandas, shapely

### Validation Targets
- Reproduce published routes within 5–10% length
- Generate usable ranked options in under 2 minutes for a 100 km corridor
- Client usefulness score ≥ 8/10

### Key Sources
Esri pipeline alignment papers, CostMAP PRO documentation, University of Calgary multi-modal corridor thesis, Vidarbha SMCA + LCP case study, Fuzzy MCDM subsea routing literature, open PowerLine-GIS datasets, Simulated Annealing sustainable pipeline papers.
