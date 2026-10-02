# 2026-10-02 strategy refresh

Fully automatic weekly X strategy refresh. No questions sent to Charlie.

## Question

What should PipeMind’s X operating system be for the week of 6 Oct 2026, given the ranker defaults synced on 1 Oct 2026?

## Findings

Primary source: [xai-org/x-algorithm `home-mixer/params/param.rs`](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs), header `last sync 2026-10-01T16:00:46Z`. Weights multiply predicted probabilities, not raw counts. The file itself warns against reading weight ratios as count equivalences.

Verified defaults:

- ShareViaCopyLinkWeight 20.0
- ReplyWeight 5.0, BidirectionalFollowReplyWeightBoost 15.0
- ShareViaDmWeight 5.0, QuoteWeight 5.0
- FollowAuthorWeight 4.0, ShareWeight 2.0, RetweetWeight 1.0, FavoriteWeight 0.5
- ContClickDwellTimeWeight 0.4, ClickWeight 0.3, OpenLinkWeight 0.2, DwellWeight 0.05, VideoOpenWeight 0.07, PhotoExpandWeight 0.05, ProfileClickWeight 0.0
- ReportWeight −234.0, MuteAuthorWeight −58.8, NotInterestedWeight −47.52, BlockAuthorWeight −31.2
- ColdStartImpressionThreshold 200, ColdStartMaxPostAgeSecs 7200, ColdStartFollowerCap 50000

Secondary sources used only for interpretation, and corrected where they disagreed with the file:

- DunSocial, 25 Sep 2026, on copy-link vs like and the September small-account boost narrative: https://www.dunsocial.com/blog/x-algorithm-update-2026-shares-outweigh-likes
- ClimbX, 30 Aug 2026, on stage-based growth (profile, replies, series, proof): https://climbx.so/blog/how-to-grow-on-x
- Wiro, 24 Sep 2026, on the disputed link penalty (Musk 29 Jul 2026 vs independent under-distribution): https://wiro.ae/articles/x-algorithm-2026

X search for PipeMind / SCARLET / MgB₂ pipeline conversation this week did not surface a usable niche cluster. Latest keyword hits were unrelated (Scarlet Pimpernel, an MgB₂ thin-film paper with 25 views, UNLV football). Distribution still has to be earned inside hydrogen-network and TSO threads, not by waiting for the topic to trend.

## Decisions written into the snapshot

1. One original post per weekday. Diversity decay makes a second same-day post a poor trade.
2. Six to ten specific replies before the original post. Empty agreement is disallowed.
3. One forwardable asset on Friday (checklist), link only in the reply.
4. Success metric is specialist replies and company-named conversations, not impressions.
5. No automated replies and no publishing from this refresh.

## Files updated

- `X Strategy Snapshot.md` (created; none existed)
- `Learning Log.md` (appended; none existed)
- `.claude/agents/x-strategy.md`
- `.claude/agents/x-drafter.md`
- `.claude/agents/x-reply.md`

## Next refresh

2026-10-09. Re-read `param.rs` header. If Typefully analytics are connected, replace the early-stage assumption with measured profile visits and reply rate.
