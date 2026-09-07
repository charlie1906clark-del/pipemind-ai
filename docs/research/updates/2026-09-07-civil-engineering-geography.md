# Civil Engineering & Geography Research for PipeMind – 2026-09-07

This note is the living reference for how geography and civil engineering actually constrain a hybrid LH2 + superconducting energy pipeline along UK (and European) main-road and existing-infrastructure corridors.

## 1. How real UK hydrogen pipelines are built (civil methods)

Current UK hydrogen pipeline projects (HyNet North West, H2East / Humber, H2Teesside) use a consistent construction logic:

- **Default method:** open-cut / open-trench.
- **Trenchless only where required:** major roads, motorways, railways, large watercourses, designated environmental sites.
- **Trenchless toolkit:** Horizontal Directional Drilling (HDD), micro-tunnelling / micro-bored tunnelling (MBT), auger boring.
- After construction the pipeline is buried. Only HAGIs (hydrogen above-ground installations) and block-valve installations remain visible.

Typical construction corridor width for buried pipelines: **10–25 m**, depending on diameter and location.

Typical trenchless depths on UK NSIPs:
- Sensitive watercourses / designated sites: often 10 m minimum; Tees crossing examples 25–60 m (design range).
- Motorway / rail crossings: trenchless as standard (M56, M62, M6, Durham Coast Line, etc.).

Minimum clearance when crossing existing gas assets (NGN practice): **600 mm**, increased for ground conditions, reamer size, accuracy and consequence of damage.

**Implication for PipeMind Route module:** every generated corridor must output a **crossing inventory** (roads, rail, water, existing pipelines, designated sites) and a default construction method per crossing. A route that looks short on a map but requires many HDD/MBT crossings can lose to a slightly longer open-cut route.

## 2. Geography layers that actually decide the route

Best-practice local-scale hydrogen GIS (Sauerland 2025/26 and UK Humber least-regret work) uses these layers, in roughly this priority:

1. **Conservation / designated land** – highest weight in local AHP studies (~0.42). Includes SSSI, SAC, SPA, Ramsar, National Parks, ancient woodland, scheduled monuments.
2. **Flood risk** – Flood Zones 2/3 and climate-adjusted flood / erosion layers.
3. **Settlements / population density** – avoid dense urban fabric; increase cost, not always a hard no-go.
4. **Existing linear infrastructure** – roads, railways, existing gas/oil/chemical corridors. Bundling is a *positive* cost-surface factor in both industry practice and recent GIS papers.
5. **Slope / topography** – important for construction cost and HDD feasibility, but often lower weight than conservation/flood at local scale (~0.08 in Sauerland AHP).
6. **Soil corrosivity, peat, shrink-swell, running sand** – BGS corrosivity map and GeoSure are the UK sources.
7. **Erosivity / scour** – especially river crossings and embankments.

UK Humber least-regret study explicitly treated as obstacles or high-cost: densely populated areas, peaty soils, conservation areas, national parks, rivers, scheduled monuments, ancient woodlands.

**Implication:** PipeMind must not treat “along the main road” as automatically cheap. Road corridors help with access and bundling, but they also concentrate utilities, Special Engineering Difficulty designations, and highway-authority constraints.

## 3. UK data sources the Route module should ingest

| Layer | Source | Use in PipeMind |
|---|---|---|
| Strategic / primary road network | OS Open Roads; OS MasterMap Highways Network; National Highways SRN | Preferred bundling alignment |
| Rail | OS / Network Rail | Trenchless trigger |
| Flood Zones 2/3 + climate | Environment Agency | High-cost / avoid working areas |
| Designated sites | MAGIC / Natural England / NRW / NatureScot | Highest-weight avoid |
| Geology, peat, shrink-swell, landslides | BGS Geology, GeoSure, GeoScour | Construction risk + burial design |
| Soil corrosivity | BGS Corrosivity Map (CIPA/DIPRA scoring) | Outer pipe / coating / cathodic protection |
| Land use / urban | OS / Corine / UKCEH | Population and amenity cost |
| Existing pipelines | UKOPA / operator records / LSBUD | Clearance, protective provisions, bundling opportunity |
| Street works / SED | NSG / TRSG / RAMI Special Engineering Difficulty | Highway working constraints |

OS Open Roads is the right *open* starting dataset. For construction-grade routing, OS MasterMap Highways + RAMI (restrictions, Special Engineering Difficulty, pipelines and specialist cables designations) is required.

## 4. Civil-engineering facts a hybrid LH2 + superconducting line must add

A hybrid energy pipeline is not a standard gas pipe. Extra civil constraints:

- **Larger buried envelope.** A concentric cryostat + vacuum jacket + outer pipe is physically larger than a typical 6–24 inch hydrogen gas line. Construction corridor and trench width scale with that envelope, not just the inner conductor.
- **Thermal contraction, not expansion.** Cryogenic inner pipe operates near 20 K. Design must accommodate contraction and settlement, not hot-oil expansion buckling. Pipe-in-pipe systems with a near-ambient outer pipe are the civil-friendly architecture (outer pipe sees soil loads; inner pipe sees cryogen).
- **Burial depth is a live-load and thermal problem.** Conventional buried hydrogen/gas practice is typically ~0.9–1.2 m cover in open country, deeper under roads. Vehicle-traffic cover rules in hydrogen piping codes can be as little as 18 inches of compacted backfill plus pavement in some jurisdictions — UK practice for transmission lines is usually deeper. PipeMind should treat cover as a design variable, not a constant.
- **Joints and cooling stations are the above-ground problem.** Long buried runs are feasible; the civil-visible objects are cooling stations, terminations, block valves and HAGIs. Station spacing from the Cooling module therefore becomes a geography problem (land take, access, flood level, setbacks).
- **Ground investigation is not optional.** Gasunie’s DRC West work (Fugro + Sweco) is the template: CPTs, boreholes, contamination, archaeology, UXO, ecology and cultural heritage *before* the corridor is frozen.
- **Protective provisions dominate urban/industrial routing.** Crossing existing high-pressure gas, chemical or fuel lines typically requires 600 mm+ clearance, exposure of the existing asset, hand-dig near the asset, non-percussive piling within defined distances, and operator approval. These rules change the true cost of “shortest path through an industrial cluster”.

## 5. What “along the UK main road system” really means

The original PipeMind idea (follow the UK main-road network) is directionally right for three reasons:

1. Access for construction plant and later maintenance.
2. Existing linear disturbance already accepted in planning terms.
3. Bundling with other energy corridors (gas, power, CO2) is now explicit TSO practice.

It is *not* automatically the cheapest or fastest path because:

- Motorways and trunk roads trigger trenchless crossings and National Highways / DMRB constraints.
- Highway verges are already crowded with utilities.
- Special Engineering Difficulty designations can make open-cut illegal or extremely expensive.
- Conservation and flood layers still override road preference when they coincide with the corridor.

**Correct PipeMind rule:** prefer *parallelism* with the strategic road and existing pipeline network, not occupancy of the carriageway. Score “distance to SRN/PRN + existing energy corridor” as a benefit layer, and treat the carriageway itself, rail, major rivers and designated sites as trenchless or no-go.

## 6. Knowledge upgrades for the modules

### Route
- Always output a crossing inventory and method (open-cut vs HDD vs MBT vs auger).
- Conservation + flood remain highest-weight avoid layers.
- Score existing-infrastructure synergy and road-corridor *parallelism*, not road occupancy.
- Include BGS GeoSure / corrosivity / peat as cost-surface layers for the UK.

### Cooling
- Cooling-station land take, access and flood level are civil constraints, not just thermo-hydraulic ones.
- Outer-pipe / pipe-in-pipe architecture is the constructible buried form.

### Cost
- HDD/MBT crossings and protective-provision crossings are first-class CAPEX items. A short route with many trenchless crossings can lose to a longer open-cut route.
- Construction corridor width (10–25 m) drives land and reinstatement cost.

### Safety / Reports
- Protective provisions, easement widths and inspection access (typically excavation envelope around the buried asset) belong in the assumption register and compliance matrix.
