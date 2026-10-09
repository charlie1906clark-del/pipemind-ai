# 2026-10-09 strategy refresh

Fully automatic weekly X strategy refresh. No questions sent to Charlie.

## Question

What should PipeMind’s X operating system be for 12–16 Oct 2026, given the ranker at commit `e62790c` and a W41 week that did not ship?

## Findings

Primary source: [xai-org/x-algorithm `home-mixer/params/param.rs` at e62790c](https://github.com/xai-org/x-algorithm/blob/e62790c99484b51424c2eccc488ed4e7517e8778/home-mixer/params/param.rs), header `last sync 2026-10-05T16:00:50Z`. Weights also sit in [`vm-ranker/params.rs`](https://github.com/xai-org/x-algorithm/blob/e62790c99484b51424c2eccc488ed4e7517e8778/vm-ranker/params.rs) at the same commit. Weights multiply predicted probabilities. The file warns against count-equivalence readings.

Verified defaults, unchanged on the levers we use:

- ShareViaCopyLinkWeight 20.0
- ReplyWeight 5.0, BidirectionalFollowReplyWeightBoost 15.0, BidirectionalFollowDwellWeightBoost 0.0
- ShareViaDmWeight 5.0, QuoteWeight 5.0
- FollowAuthorWeight 4.0, ShareWeight 2.0, RetweetWeight 1.0, FavoriteWeight 0.5
- ContClickDwellTimeWeight 0.4, ClickWeight 0.3, OpenLinkWeight 0.2, ContDwellTimeWeight 0.004, DwellWeight 0.05, VideoOpenWeight 0.07, PhotoExpandWeight 0.05, PostUnexploredWeight 0.02
- ProfileClickWeight 0.0, ProfileVisitSecsWeight 0.0, VideoContinuationWeight 0.0
- ReportWeight −234.0, MuteAuthorWeight −58.8, NotInterestedWeight −47.52, BlockAuthorWeight −31.2, NotDwelledWeight −0.02
- EnableAuthorDiversity true, AuthorDiversityDecay 0.5, AuthorDiversityFloor 0.25
- OonWeightFactor 0.75, TopicOonWeightFactor 0.5, NewUserOonWeightFactor 0.00001
- EnablePhoenixOonReplies false
- ColdStartImpressionThreshold 200, ColdStartMaxPostAgeSecs 7200, ColdStartFollowerCap 50000, ColdStartSlotMin 15, ColdStartSlotMax 16, EnableViewerColdStart true
- DppEnabled true, DppTheta 0.65, DppMaxSelectedRank 150

Secondary sources, used only where they disagreed with the file:

- HowSociable, 8 Oct 2026, repeats the published weights and the small-account probe: https://howsociable.com/guides/how-to-grow-followers-on-x
- LinkIntel, 6 Oct 2026, points at `vm-ranker/params.rs` commit e62790c and still describes ratios as “40 x a like,” which the source file forbids: https://www.getlinkintel.com/x-algorithm
- tang-vu playbook still lists ContClickDwellTimeWeight 0.0 and NotInterestedWeight −43.2. Both are wrong against e62790c.

Account evidence: Typefully was not called. Prior same-day review already recorded API key missing. X keyword search did not return PipeMind posts. No performance claim added.

## Decisions written into the snapshot

1. Do not republish the unshipped 6–10 Oct pack.
2. Three originals only: Tue 13 number, Wed 14 correction, Thu 15 build log. Monday replies only. Friday empty unless a specialist reply lands.
3. Replies stay the discovery channel because Phoenix OON replies are off and new-user OON weight is ~0.
4. No invented heat-leak number. Source the 1 W/m line before anyone arms V1.
5. No publishing and no automated replies from this refresh.

## Files updated

- `X Strategy Snapshot.md` and `docs/x-strategy/X Strategy Snapshot.md`
- `Learning Log.md` and `docs/x-strategy/Learning Log.md` (appended; docs copy keeps the earlier W41 analytics entry)
- `.claude/agents/x-strategy.md`
- `.claude/agents/x-drafter.md`
- `.claude/agents/x-reply.md`

## Next refresh

2026-10-16. Re-read the home-mixer header. If Typefully is authenticated, log profile visits and specialist replies before writing another pack.
