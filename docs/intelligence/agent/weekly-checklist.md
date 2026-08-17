# Automated Agent Weekly Checklist
**Powered by the Obsidian / GitHub brain**

This checklist is written for an automated agent. The agent must read the living knowledge base in `docs/intelligence/` and `docs/research/updates/` before acting.

---

## Pre-Flight (Always do first)
1. Read the latest file in `docs/research/updates/` (most recent training dump).
2. Read all files in `docs/intelligence/company-profiles/`.
3. Confirm the current date and the period covered by this weekly cycle.

---

## Phase 1 – Signal Intake (Monday–Tuesday logic)
1. Search for new high-signal items only:
   - New corridor or interconnect agreements
   - Capacity reservation or oversubscription announcements
   - First fills, operational milestones, or commissioning events
   - Technology validations (especially cooling / cryostat / insulation)
   - Material cost or threshold claims that affect the 610 / 1430 €/km/MW reference
   - Regulatory or safety basis changes
2. Discard low-signal noise (generic “hydrogen is growing” statements).
3. Tag each retained signal with the modules it affects (Route, Cooling, Safety, Cost, Twin, Reports) and the company profiles it touches.

---

## Phase 2 – Profile Update (Wednesday logic)
1. For every company profile that is affected:
   - Update the “Current Intelligence Snapshot” section with the new facts.
   - Update “Last updated” date.
   - Add any new rival or project if required.
2. Do not rewrite the entire profile — only append or amend the living snapshot and notes.
3. If a completely new relevant company appears, create a new profile from the template in `docs/intelligence/templates/`.

---

## Phase 3 – Implication Generation (Core Intelligence Step)
1. For each active company profile, run the following internal queries using the specialist knowledge:
   - What does this week’s signal mean for this company’s strategic priorities?
   - How does it change their position relative to the rivals listed in their profile?
   - What should this company be paying attention to right now?
2. Produce short, sharp implication statements (3–6 bullets maximum per company).
3. Prefer competitive and decision-relevant language over descriptive language.

---

## Phase 4 – Brief Generation (Thursday logic)
1. Generate one **Master Brief** containing:
   - Executive Snapshot (what actually moved)
   - Cost & Competitiveness Watch (threshold status)
   - Technology / Safety / Regulatory Signals
2. Generate **Company-Specific Overlays** for every active profile using the implications from Phase 3.
3. Structure each company overlay as:
   - What this means for you
   - Competitive angle
   - Recommended attention
4. Save all briefs into `docs/intelligence/briefs/` with clear naming:
   - `YYYY-MM-DD-master-brief.md`
   - `YYYY-MM-DD-brief-gasunie-hynetwork.md`
   - `YYYY-MM-DD-brief-oge-thyssengas.md`
   - etc.

---

## Phase 5 – Storage & Learning (Friday logic)
1. Commit all new and updated files to the repository.
2. Ensure the new briefs and profile updates are available for the next cycle.
3. If any signal is especially important, create a short note in `docs/research/updates/` so future training cycles retain it.

---

## Quality Rules for the Agent
- Never produce generic news summaries.
- Always translate facts into implications for the specific company.
- Keep language direct, strategic, and decision-oriented.
- When in doubt, prefer fewer high-value points over many low-value points.
- The goal is a product that a senior decision-maker will actually read and act on.

---

## Success Criteria for a Good Weekly Run
- All affected company profiles have been updated.
- At least one Master Brief and two Company-Specific Overlays have been generated.
- The implications are clearly different between rival companies.
- Everything is stored cleanly in the GitHub / Obsidian brain for the next cycle.
