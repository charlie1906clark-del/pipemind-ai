# Learning Log — X strategy

Append-only. Newest at the bottom.

## 2026-10-02 — Weekly strategy refresh

Context: first snapshot written into the repo. No prior `X Strategy Snapshot.md` or learning log was in `charlie1906clark-del/pipemind-ai`. Account analytics were not available in this run, so no performance claims were invented.

What changed in the live ranker (verified against `home-mixer/params/param.rs`, sync stamp 2026-10-01):

- Copy-link share remains the largest positive weight at 20.0. Reply, quote, and DM share stay at 5.0. Follow-author is 4.0. Like is 0.5.
- Several secondary 2026 blog roundups are stale versus the 1 Oct file. Video open is 0.07 (not 0.05). Click is 0.3 (not 0.4). Dwell is 0.05. Continuous click-dwell is 0.4. Not-interested is −47.52. Profile click remains 0.0, so profile clicks are not a ranking reward even though they are the business metric we care about.
- Mutual-follow reply boost is +15.0 on original posts only. Worth earning follows, not worth faking mutuals.
- Cold-start probe is small (impression threshold 200, max age 7200s). The first hour still decides whether a post lives.
- Explicit link-penalty constant is absent. Empirical under-distribution of body links is still reported. Policy stays: link in the first reply.

Decision applied:

- Cadence capped at one original per weekday because author-diversity decay punishes bursts.
- Content mix shifted toward forwardable numbers and corrections, away from like-optimised hot takes.
- Reply quality rule tightened: add a number, a constraint, or a correction. Empty replies are now treated as a spam-classifier risk, not a growth tactic.
- Agent files under `.claude/agents/` updated so drafting and reply agents load this snapshot before writing.

Open for next Friday:

- Pull Typefully / X analytics if the account is connected and replace the stage assumption.
- Record which of the five post shapes earned a specialist reply.
- Re-check `param.rs` sync stamp; do not trust blog weight tables older than the file header.
