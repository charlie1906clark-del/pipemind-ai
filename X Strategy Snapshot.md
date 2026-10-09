# X Strategy Snapshot

Updated: 2026-10-09 (weekly refresh, automatic)
Account stage: early / specialist founder (PipeMind AI). Unchanged. No Typefully metrics this run.
Primary goal: qualified conversations with TSOs, hydrogen developers, cryogenics and superconducting-cable people — not vanity followers.
Voice: specific, numerical, builder. No hype, no engagement bait.

## Ranking facts that drive this week

Primary source: `xai-org/x-algorithm` commit `e62790c` (6 Oct 2026).

- Action weights and the probability caveat: `home-mixer/params/param.rs`, header `last sync 2026-10-05T16:00:50Z`.
- Same weights also declared in `vm-ranker/params.rs` at that commit (no header stamp). Use the home-mixer header as the freshness stamp.

Weights multiply *predicted* action probability, not raw counts. The file itself says ratio readings such as “one share equals 40 likes” are wrong.

Positive weights in production defaults (unchanged versus the 1 Oct stamp):

| Predicted action | Weight |
| --- | ---: |
| Share via copy link | 20.0 |
| Reply | 5.0 (plus 15.0 boost on original posts between mutual follows) |
| Share via DM | 5.0 |
| Quote | 5.0 |
| Follow the author | 4.0 |
| Share (button) | 2.0 |
| Repost | 1.0 |
| Favourite | 0.5 |
| Continuous click-dwell | 0.4 |
| Click | 0.3 |
| Open link | 0.2 |
| Continuous dwell time | 0.004 |
| Dwell | 0.05 |
| Video open | 0.07 |
| Photo expand | 0.05 |
| Post unexplored (in-network only) | 0.02 |
| Profile click | 0.0 |
| Profile-visit seconds | 0.0 |
| Video continuation | 0.0 |

Negative weights: report −234, mute author −58.8, not interested −47.52, block author −31.2, not dwelled −0.02.

Distribution constraints now read from the file, not from blogs:

- `EnableAuthorDiversity` true, decay 0.5, floor 0.25. A second post in the same ranked set is multiplied down. One original per day remains the cap.
- `OonWeightFactor` 0.75. `TopicOonWeightFactor` 0.5. Non-followers see a discounted score.
- `EnablePhoenixOonReplies` false. A reply does not enter For You for people who do not follow you. Discovery is in-thread, under a post those people already opened.
- Cold start, confirmed in `home-mixer/params/param.rs`: impression threshold 200, max post age 7200 seconds, follower cap 50,000, slot 15–16, viewer cold-start enabled, Thompson sampling enabled. The probe is two hours, not 48 hours.
- `NewUserOonWeightFactor` 0.00001 in `vm-ranker/params.rs`. Brand-new viewers almost do not see out-of-network posts. Do not plan on For You discovery from empty accounts.
- DPP rerank is on (`DppEnabled` true, theta 0.65, max selected rank 150). Near-duplicate claims get spread apart. Do not post two wordings of the same constraint on the same day.
- No explicit link-penalty constant. Body links stay in the first reply until this account has a follow graph.
- Secondary blogs are stale: the playbook still lists click-dwell at 0.0 and not-interested at −43.2. Ignore those tables.

## Operating system (this week)

W41 (6–10 Oct) did not ship. Public search found no PipeMind originals. Typefully analytics were unreachable (no API key). Kill rule did not fire: the sample is zero posts, not two failed posts. Do not republish the unshipped five-post pack.

Cadence, early-stage, restricted by the W41 review:

- At most one original on Tue 13, Wed 14, and Thu 15. Monday is replies only. Friday 16 stays empty unless one of those three has a specialist reply by Thursday night.
- Never two originals inside 3 hours. Never a second wording of the same claim.
- 6–10 specific replies per weekday, before any original. Target hydrogen networks, TSOs, superconductivity, cryogenics, grid planning. Add a number, a constraint, or a correction. No “great point.”
- Reply to every reply on our posts within the hour when online. The +15 mutual boost applies only on original posts between mutual follows.
- No Friday checklist this week. The copy-link asset waits until one post earns a specialist reply.
- 0 engagement-bait questions. External URLs in the first reply only.
- No automated replies. No follow/unfollow. No duplicate posts. No IG or TikTok.

Post shapes, in the only order allowed this week:

1. Forwardable number (Tue). Heat leak sets cooling-station spacing. Do not invent the 1 W/m figure; source it in the scratchpad before the draft is armed.
2. Correction (Wed). Superconducting cable in LH2 is not free cooling. Constraint is heat into the product stream, including quench.
3. Build log (Thu). Four scores before a line is drawn: heat leak, setback, road bias, consent friction. State what the route module cannot price yet.

Avoid: the unshipped W41 pack, generic AI threads, “the future of energy,” quote-tweeting news with no added calculation, link dumps, reply-guy volume on mega accounts.

## Weekly content plan (12–16 Oct 2026, Europe/London)

| Day | Original | Reply cluster |
| --- | --- | --- |
| Mon 12 | None. Replies only. | European H2 backbone, Gasunie, SCARLET, MgB2 paper accounts |
| Tue 13 | V1 number: station spacing is heat leak divided by recondenser or vent budget. No link in body. | Cryogenics and LH2 safety |
| Wed 14 | V2 correction: LH2 around an MgB2 cable is not free cooling. | Cable OEMs, superconductivity |
| Thu 15 | V3 build log: four scores before a corridor line. Name the two scores still missing. | TSO planning |
| Fri 16 | Empty unless Tue–Thu earned a specialist reply. | Only people who replied to V1–V3 |

Pinned post (set once, do not rotate weekly): one sentence on what PipeMind does, who it is for, and the single proof point currently true. No “coming soon.”

## Metrics to log next refresh

Track only: profile visits from posts, follows from posts, replies received, replies we answered, copy-link or quote events if visible, and conversations that named a company or a corridor. Ignore impressions as a success metric.

Kill rule: any format with two posts and zero specialist replies gets retired for two weeks. Unshipped drafts are not a test.
