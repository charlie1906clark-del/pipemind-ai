---
name: x-strategy
description: Weekly and daily X operating system for PipeMind. Load before any X drafting, scheduling, or analytics review.
---

# X strategy agent

Read `X Strategy Snapshot.md` and the latest `research/daily/*-strategy-refresh.md` before recommending a post. If `reviews/x/` has a newer review than the snapshot, the review’s kill list wins.

## Rules

- Optimise for copy-link shares, specialist replies, and follows. Do not optimise for likes.
- One original post per weekday at most. Do not propose a second original inside three hours. Do not propose a second wording of the same claim (DPP theta 0.65).
- Week of 12 Oct 2026 is capped at three originals (13, 14, 15). Do not restore the unshipped 6–10 Oct pack.
- No link in the post body. Put sources in the first reply.
- No engagement bait, no “thoughts?”, no generic AI energy takes.
- Never publish or auto-reply. Draft only unless Charlie explicitly says publish.
- Freshness: `home-mixer/params/param.rs` header at commit `e62790c` is `last sync 2026-10-05T16:00:50Z`. Weights are duplicated in `vm-ranker/params.rs`. If that header is older than 14 days relative to today, flag the snapshot stale instead of inventing weights.
- Do not quote weight ratios as “one share equals N likes.” Weights apply to predicted probabilities.
- `EnablePhoenixOonReplies` is false. Do not plan reply-guy volume as For You distribution.

## Weekly job

When asked for a strategy refresh: re-read the open-source ranker defaults, update the snapshot, append the learning log, write `research/daily/YYYY-MM-DD-strategy-refresh.md`, and adjust these agent files only when a rule is contradicted by the primary source.
