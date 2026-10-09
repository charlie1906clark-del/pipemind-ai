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

## 2026-10-09 — Weekly strategy refresh

Context: W41 originals were not observed. `reviews/x/2026-W41 Review.md` already graded the five planned slots F and blocked a queue wipe on missing Typefully auth. This refresh did not invent engagement. Public keyword search still does not show a PipeMind cluster; niche hits are Oman LH2 export links and unrelated Scarlet posts.

Ranker, re-read at commit `e62790c` (6 Oct 2026):

- Header on `home-mixer/params/param.rs` is `last sync 2026-10-05T16:00:50Z`, not 8 Oct. A same-day analytics note that cited 8 Oct is not confirmed against this commit.
- Weights that drive the operating system are unchanged: copy-link 20.0, reply 5.0, bidirectional reply boost 15.0, quote 5.0, DM share 5.0, follow-author 4.0, like 0.5, not-interested −47.52, profile click 0.0.
- Newly confirmed in-file, previously only “commonly cited”: author diversity decay 0.5 / floor 0.25 and enabled; OON factor 0.75; topic OON factor 0.5; cold-start threshold 200, max age 7200s, follower cap 50,000, slot 15–16.
- `EnablePhoenixOonReplies` is false. Replies are not an out-of-network For You channel.
- `NewUserOonWeightFactor` is 0.00001. Empty accounts will not be found by new viewers in For You.
- DPP is on (theta 0.65). Duplicate claims are a distribution tax.
- Playbook tables that still say click-dwell 0.0 or not-interested −43.2 are stale.

Decision applied:

- Did not restore the five-post W41 pack. Week of 12 Oct is three originals (Tue number, Wed correction, Thu build log), Monday replies only, Friday empty unless a specialist replies.
- Copy-link checklist deferred. No point shipping a forwardable asset before one post has a reader.
- Agent files updated: stamp path, OON-reply fact, three-variant cap, no invented heat-leak number.

Open for 2026-10-16:

- Typefully key still missing. Do not grade posts until `analytics:posts:list` can run.
- Record whether V1–V3 were armed, and whether any specialist reply arrived.
- Re-read the home-mixer header. If it is still 5 Oct, flag the snapshot stale rather than copying blog weights.
