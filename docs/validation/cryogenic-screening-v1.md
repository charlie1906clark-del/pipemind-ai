# Screening engine v1 — assumptions and validation limits

## Physics
A saturated-tank, fixed latent-heat **equivalent** calculation, not a phase-equilibrium or pressure solver.

- Heat input [J] = heat ingress [W] x seconds.
- Cold-side heat removed [J] = min(heat ingress, active cooling duty) x seconds.
- Vaporisation equivalent [kg] = max(0, net heat [J]) / assumed latent heat [J/kg].
- In-tank vaporised [kg] = min(initial LH2 inventory, equivalent). Any excess heat after total inventory vaporisation is outside the model domain.
- Recovered vapour is captured *outside* the tank; it does not remain in the tank inventory.
- Electrical refrigeration energy [kWh] = (cold-side thermal watts / COP) x hours / 1000.

`latent_heat_j_per_kg=445000` is **illustrative only**. It is not a validated property lookup and must not silently be used for engineering design. Inputs assume heat only contributes to vaporisation at saturation: no temperature-dependent enthalpy, stratification or pressure evolution.

## Example
1 kW for 24 h -> 86.4 MJ -> 194.16 kg *equivalent*, before inventory limits. Without active cooling the corresponding equipment electricity in this model is zero; that does **not** imply no upstream liquefaction power or recovery equipment costs.

## Boundaries and known omissions
This does not calculate pressure, phase margins, line hydraulics, storage filling/withdrawals, warm-up, hydrogen liquefaction energy, leaks, vent sizing, oxygen deficiency, explosive atmosphere, safety standoffs, cable quench, ortho/para conversion, material compatibility or legal compliance.

If `boiloff_equivalent_kg` exceeds tank inventory, the reported mass is capped but the underlying thermodynamic evolution is **not** simulated. No result is approved for plant control.

## Independent validation roadmap
1. Cross-check zero input, pure heat, pure cooling, inventory cap, mass balance, cost balance (unittest).
2. Link authoritative NIST property data and document saturation temperature, pressure, ortho/para composition.
3. Add control volume and benchmark against published cryogenic tank datasets with reference errors.
4. Introduce sensor-noise, missing-data and adversarial tests.
5. Cryogenic engineer review before using in commercial recommendations.

## Usage
```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m pipemind.cli
```
