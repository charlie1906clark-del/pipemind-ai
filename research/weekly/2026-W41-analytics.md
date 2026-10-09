# 2026-W41 analytics

Window: 2026-10-02 00:00 UTC through 2026-10-09 15:01 BST (7d).
Account: PipeMind X (identity not resolved in Typefully; no public posts matched).
Run: Friday analytics. No questions sent.

## Sources

| Source | Result |
| --- | --- |
| Typefully `analytics:posts:list` with metrics | Not run. CLI returned API key not found. `includeMetrics` unavailable. |
| Typefully queue / scheduled drafts | Not run. Same auth block. Full kill not executed. |
| PostHog `x_organic` | Not available. PostHog is not a connected service on this run. |
| X keyword + semantic search, 2–9 Oct 2026 | No PipeMind, hybrid LH2+HTS, or SCARLET corridor posts from this account. Hits were unrelated (game Scarlet, fiction, trading links). |
| Ranker file | `xai-org/x-algorithm` `home-mixer/params/param.rs`, header `last sync 2026-10-08T16:00:35Z`. |

Impressions, profile visits, follows, replies, bookmarks, and copy-link events are unmeasured. None are estimated.

## Account totals (7d)

| Metric | Value |
| --- | --- |
| Originals found | 0 |
| Replies found | 0 |
| Impressions | unmeasured |
| Engagements | unmeasured |
| Profile visits | unmeasured |
| Follows from posts | unmeasured |
| Specialist replies | 0 observed |
| PostHog x_organic sessions | unavailable |

## Post grades

Grade rule used: A = specialist reply or copy-link/quote with a named company or corridor. B = profile visit or follow with no specialist reply. C = impressions only. F = shipped and zero specialist signal, or planned and not shipped. Unmeasured is not promoted.

| Planned slot (6–10 Oct) | Theme | Grade | Why |
| --- | --- | --- | --- |
| Mon 6 build log | Corridor planner must score heat leak, setback, road bias, consent | F | Not found shipped. |
| Tue 7 forwardable number | Cooling-station spacing is a heat-leak problem | F | Not found shipped. |
| Wed 8 correction | LH2 is not free cooling for HTS; quench / heat load | F | Not found shipped. |
| Thu 9 cost frame | CAPEX/km is the wrong headline vs HVAC/HVDC + H2 logistics | F | Not found shipped. Today is Thu 9; slot still unshipped at review time. |
| Fri 10 checklist | 7 checks before a hybrid corridor leaves the whiteboard | F | Not shipped. Do not pre-schedule a pack around it. |

No post is A, B, or C.

## Hypothesis grades (H1–H9)

These are the only hypotheses allowed for next-week variants. None earned A.

| ID | Hypothesis | Grade | Decision |
| --- | --- | --- | --- |
| H1 | Forwardable number, one claim, one source, one implication | untested | Hold. Eligible for a single next-week variant. Not A. |
| H2 | Correction of a repeated HTS/LH2 claim with the constraint | untested | Hold. Eligible. Not A. |
| H3 | Build log of what a module can and cannot do | untested | Hold. Eligible. Not A. |
| H4 | Real design question a TSO engineer can answer with a number | untested | Hold. Not scheduled this week. |
| H5 | External URL only in the first reply | untested | Policy stands. No body-link test. |
| H6 | One original per weekday; no second post inside 3 hours | untested | Policy stands. No multi-week pack. |
| H7 | Friday checklist of at most 7 checks, pasteable | untested | Not shipped 10 Oct. Do not recycle as a series. |
| H8 | 6–10 specific replies before the original | untested | Still the discovery path. No volume replies. |
| H9 | No engagement bait, no hashtags, no IG/TikTok cross-post | policy | Kept. IG and TikTok not touched. |

Losing themes for queue kill: all five W41 planned originals, plus any scheduled draft whose scratchpad or text matches build-log-without-proof, free-cooling, CAPEX-per-km headline, generic hydrogen-is-growing, or a multi-day content pack. Kill not executed (Typefully auth).

## Ranker check

Stamp moved from `2026-10-01T16:00:46Z` to `2026-10-08T16:00:35Z`. Weights re-read and unchanged: ShareViaCopyLink 20.0, Reply 5.0, bidirectional reply boost 15.0, ShareViaDm 5.0, Quote 5.0, FollowAuthor 4.0, Share 2.0, Favorite 0.5, Click 0.3, OpenLink 0.2, ProfileClick 0.0, ColdStartImpressionThreshold 200.

## Next week only

2–3 variants, W42 only (13–17 Oct 2026), unscheduled. See `reviews/x/2026-W41 Review.md`. No W43+ pack.
