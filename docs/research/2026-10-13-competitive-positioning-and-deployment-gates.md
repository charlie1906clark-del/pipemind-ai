# Market and safety evidence refresh — 13 October 2026

## Market: compete where evidence can justify a purchase

IEA **Global Hydrogen Review 2026**: [executive summary](https://www.iea.org/reports/global-hydrogen-review-2026/executive-summary).
- 2025 hydrogen demand exceeded 100 Mt; largely incumbent industry and refining.
- Low-emissions hydrogen near 1 Mt in 2025; smaller than most vision-led market estimates imply.
- Announced low-emissions hydrogen production outlook to 2030 declined to 27 Mt; demand, offtake and late project decisions remain strong barriers.
- Consequently PipeMind should target **existing cryogenic H2 asset owners, OEMs, liquefaction facilities and qualified engineering integrators**, not rely entirely on speculative long-distance LH2 networks being constructed.

Competitor evidence: [AspenTech Hydrogen Solutions](https://www.aspentech.com/en/solutions/accelerate-innovation-for-the-hydrogen-economy) offers process design and digital-twin/optimisation tools across hydrogen. PipeMind has **competitors**; no credible 'only system in market' claim is possible without thorough feature and customer benchmarking. Potential differentiator to prove: explicit LH2 EOS and boil-off provenance, simulation-to-asset replay, uncertainty/abstention, economics and optional coupled superconducting cable analysis in one governed package.

## Security basis
[NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) gives OT cybersecurity guidance, including reliability and safety considerations. Revision 4 initial draft exists as of September 2026; no claim of compliance or certification follows merely from following the guide. Prefer OT -> secure export gateway / DMZ -> read-only data broker -> tenant-isolated PipeMind. No AI-originated commands to PLC/SIS. Formal IEC 62443 architecture assessment remains a separate site-specific gate.

## Cryogenic scientific basis
[NIST Leachman et al. 2009](https://www.nist.gov/publications/fundamental-equations-state-parahydrogen-normal-hydrogen-and-orthohydrogen) and [CoolProp ParaHydrogen](https://coolprop.github.io/devdocs/fluid_properties/fluids/ParaHydrogen.html) establish EOS provenance only, **not** that the current ideal rigid tank and Darcy line screening models are validated against full-scale experiments. Independent measured benchmarks, stratification and heat flux validation are required.

## Commercial adoption hypotheses (not forecasts)

**Beachhead:** fixed liquid-hydrogen storage and reliquefaction operators with known data access and costly unavoidable parasitic heat ingress; sell a *validation study and research/pilot monitoring*, then only a recurring advisory product if independently measured benefits exceed implementation/operation expense.

**Value metric:** measured electrical input (kWh), actual unrecovered H2 mass (kg), operator workload/incident-prevention proxies with uncertainty. Avoid double counting recovered gas as lost product. Control for ambient temperature, fill level, production rate, equipment cycling and grid pricing.

**Differentiation gates:**
1. Physical model explains a measured scenario with stated error and interval.
2. AI-based forecast outperforms persistence and physics baseline out of sample.
3. Economic recommended change is feasible after refrigeration electrical consumption and actual recovery costs.
4. Tenant isolation and hardware-control boundary independently verified.
5. Operator can replay every forecast to exact versioned data and evidence.
6. Price/contract aligned to measured value and procurement constraints.

## Site pilot scope
Synthetic/offline replay first; real facility read-only connection only after a signed data-rights agreement, competent safety/cyber assessment and site-authorised data gateway. Simulation cannot replace relief design, SIS, operating manuals or human engineering sign-off.
