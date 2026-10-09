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

## 2026-10-09 — W41 Friday analytics

Context: 7-day review. Typefully still has no API key, so `analytics:posts:list` with metrics did not run and the scheduled queue was not readable. PostHog `x_organic` is not connected. X search for 2–9 Oct returned no PipeMind posts. No engagement numbers were filled in.

Ranker: `param.rs` header is now `last sync 2026-10-08T16:00:35Z`. Copy-link 20.0, reply 5.0, bidirectional reply boost 15.0, profile click 0.0, cold-start impression threshold 200. No weight change versus 1 Oct that would alter the operating system.

Grades: Mon–Fri planned slots all F (not shipped). H1–H9 all untested. Nothing marked A. Kill rule (two posts, zero specialist replies) did not fire because the sample is zero posts, not two failures. Execution failure is still a kill of the unshipped W41 pack: do not let those five themes auto-publish next week.

Decision applied:

- Wrote `research/weekly/2026-W41-analytics.md` and `reviews/x/2026-W41 Review.md`.
- FULL KILL not executed. Blocked on Typefully auth. Losing themes listed for deletion on the next authenticated pass.
- Next week only: three unscheduled variants (H1 number, H2 correction, H3 build log) for 13–15 Oct. No W43 pack. No IG/TikTok. Friday 16 Oct stays empty unless one variant earns a specialist reply.
- Stage assumption unchanged: early / specialist. Do not treat silence as product-market rejection.

Open for 2026-10-16:

- Connect Typefully and rerun `analytics:posts:list` with metrics before grading anything A.
- Delete scheduled drafts matching the W41 losing themes.
- If PostHog `x_organic` appears, log sessions beside profile visits. Do not substitute it for replies.

## 2026-10-09 — Weekly strategy refresh

Context: same day as the W41 analytics note. This pass re-read the ranker and wrote the operating system. It did not grade posts and did not delete drafts.

Correction to the analytics note above: commit `e62790c` (6 Oct 2026) has `home-mixer/params/param.rs` header `last sync 2026-10-05T16:00:50Z`. The 8 Oct stamp was not in that file. Weights match the analytics note. Do not treat the 8 Oct stamp as verified.

What this pass confirmed in-file:

- Author diversity enabled, decay 0.5, floor 0.25. OON factor 0.75. Topic OON factor 0.5.
- `EnablePhoenixOonReplies` false. Replies are an in-thread channel only.
- Cold start: threshold 200, max age 7200s, follower cap 50,000, slot 15–16.
- `NewUserOonWeightFactor` 0.00001. DPP on, theta 0.65.

Decision applied: snapshot week of 12 Oct is the three variants from the W41 review, not a new five-post pack. Agent files updated. Copy-link checklist deferred.
