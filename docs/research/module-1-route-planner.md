# Module 1 Research – Smart Route Planner

## Purpose
Find the best physical corridor for a hybrid LH₂ + superconducting pipeline, strongly preferring major road verges and existing utility rights-of-way while balancing cost, environment, safety and constructability.

## Key Methods
- Least-Cost Path (LCP) on a multi-criteria cost surface
- Analytical Hierarchy Process (AHP) or weighted scoring for criteria
- Generation of multiple ranked alternatives (not just one “best” route)
- Preference for motorways and A-roads as default bias

## Important Criteria Groups
- Economy (length, crossings, slope)
- Engineering (soil, geology, existing corridors)
- Environment (protected areas, habitats)
- Social (population density, visual impact)
- Hazard (seismic, landslide, flood)

## Data Layers Required
- Road network (motorways + A-roads preferred)
- Existing utility corridors
- Land cover / protected areas
- Elevation and slope
- Population and settlements
- Rivers, railways, major crossings

## Tools & References
- Esri Network Analyst / CostMAP Pro style approaches
- Open-source: networkx + rasterio + geopandas
- PowerLine-GIS open European friction layers
- Academic multi-criteria corridor papers (Vidarbha, Greek seismic, etc.)

## Success Metrics
- Produce 3 ranked routes in under 2 minutes for a 100 km corridor
- Routes should be explainable and auditable
