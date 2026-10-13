# Specialist agent system — advisory by construction

The repository's historical agent skill list (`docs/skills.md`) describes intended roles; those skills were not implemented as executable domain agents on `main`. The existing `.claude/agents/x-*.md` specialise in social media and are **not** hydrogen engineering agents.

## Operational architecture
- Domain agents read specific source folders and produce reviewable draft artifacts.
- A non-LLM deterministic physics service produces all engineering numeric results.
- The research-verifier agent produces source/evidence status and disputes.
- The cryogenic engineer defines models/test cases; independent specialist verification is required for industrial use.
- The safety reviewer flags missing requirements; a qualified engineer approves engineering safety work.
- The digital-twin agent designs sensor ingestion and tests; it does not control valves or cooling systems.
- The optimisation analyst cannot rank any action that violates hard constraints or lacks a validated model.
- The superconducting researcher prepares cable-interface research without claiming operational maturity.
- Existing X agents remain isolated in the marketing subsystem.

## Agent evaluation gates
1. Grounding: sources and excerpt support technical claims; missing sources -> `unverified`.
2. Math: units, equations, reproduction from code and parameter provenance.
3. Failure behaviour: uncertain or out-of-domain input produces abstention and an escalation path.
4. Security: no secrets/data exfiltration; tenant permissions, redaction and source trust.
5. Audit: versioned prompts, model/solver versions, reviewer, result IDs.
6. Human review on any safety, operating or customer-facing technical document.

There is **no autonomous running daemon**, no RAG index, no fine-tuned model and no permissions to operate industrial systems in this branch. These markdown files are development specifications that need separate runtime implementation and evaluation.
