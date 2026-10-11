# Cable engineering validation matrix

| Feature / claim | Available baseline | Current status | Evidence required |
| --- | --- | --- | --- |
| LH2 storage thermal screening | Fixed-latent-heat calculation on dedicated code branch | Prototype | Tank property validation |
| LH2 temperature vs distance | Research notes only | NOT IMPLEMENTED | Coupled flow/enthalpy benchmark |
| Hydrogen phase and pressure margins | Research notes only | NOT IMPLEMENTED | Verified property dataset, measurement |
| MgB2 electrical load capacity | Literature discussion | NOT IMPLEMENTED | Device-specific Ic(T,B), derating |
| Cooling station optimisation | Literature discussion | NOT IMPLEMENTED | Validated thermal/hydraulic solver and cost model |
| Cable quench response | Hazard note only | NOT IMPLEMENTED | Qualified specialist dynamic model and tests |
| GIS route safety and civil constructability | Historical research | NOT IMPLEMENTED | Geospatial data licence, competent review |
| Cost advantage over alternatives | Research assumptions | UNPROVEN | Matched lifecycle comparison |
| Light/frequency stabilising LH2 | No validated pathway | SPECULATIVE | Reproducible calorimetry and net-energy test |

## Research question register
- Which liquid-hydrogen properties, ortho/para composition models and critical-current datasets match the planned operating envelopes?
- How does heat leak vary with actual cryostat geometry, vacuum state and joint construction?
- What fraction of refrigeration demand is unavoidable and what can forecasting optimise?
- What would be a fair commercial counterfactual: separate power HVDC plus LH2, or H2 gas pipeline plus power?
- What are the measured potential energy benefits vs sensor/control implementation and maintenance costs?

**Gate:** no downstream engineering recommendation from a research-only quantity. Numeric assumptions are illustrative until proven and versioned.
