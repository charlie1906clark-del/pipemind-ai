# X Strategy Snapshot

Updated: 2026-10-02 (weekly refresh, automatic)
Account stage: early / specialist founder (PipeMind AI)
Primary goal: qualified conversations with TSOs, hydrogen developers, cryogenics and superconducting-cable people — not vanity followers.
Voice: specific, numerical, builder. No hype, no engagement bait.

## Ranking facts that drive this week

Source: `xai-org/x-algorithm` `home-mixer/params/param.rs`, header stamp `last sync 2026-10-01T16:00:46Z`. Weights multiply *predicted* action probability, not raw counts. Do not treat ratios as “one share equals 40 likes.”

Positive weights in production defaults:

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
| Dwell | 0.05 |
| Video open | 0.07 |
| Photo expand | 0.05 |
| Profile click | 0.0 |

Negative weights: report −234, mute author −58.8, not interested −47.52, block author −31.2, not dwelled −0.02.

Distribution constraints that matter more than likes:

- Author diversity decay floors later posts from the same author in one ranked set (commonly cited decay 0.5, floor 0.25 — second post ~0.625). Posting more does not linearly add reach.
- Out-of-network factor is commonly cited at 0.75. Non-followers see a discounted score, so replies inside the right conversations are the discovery channel.
- Candidate age for the main ranker is short (widely documented 48h cap). A post that does not earn a conversation in the first hour is mostly done.
- Cold-start impression threshold default is 200; cold-start max post age default is 7200 seconds; follower cap for that path is 50,000. Small accounts still get a probe, then die if the probe does not convert.
- Cross-request author diversity exists in the repo but defaults off (`EnableCrossRequestAuthorDiversity` false in open PRs). Do not plan around it.
- Link penalty is disputed. Musk said (29 Jul 2026) links have not been penalised for over a year; published scorer has no explicit link-penalty constant; independent analyses still show link posts under-distribute, especially without Premium. Treat body links as a reach tax until this account has a follow graph.

## Operating system (this week)

Cadence, early-stage:

- 1 original post per day, 5 days (Mon–Fri). Never two originals inside 3 hours.
- 6–10 specific replies per weekday, before the original post. Target accounts in hydrogen networks, TSOs, superconductivity, cryogenics, grid planning. Add a number, a constraint, or a correction. No “great point.”
- Reply to every reply on our posts within the hour when online. The mutual-follow reply boost (5 + 15) only helps once people follow back; the conversation itself is still the distribution event.
- 1 copy-link asset per week: a checklist, a worked number, or a one-page comparison someone can forward to a colleague.
- 0 engagement-bait questions (“thoughts?”). Questions only if a specialist can answer them from experience.
- External URLs go in the first reply, not the body, until profile visits are converting.
- No automated replies. No follow/unfollow. No duplicate posts across accounts.

Post shapes that match the weights:

1. Forwardable number. One claim, one source, one implication for a corridor or a cost model. Built to be copied into a team chat.
2. Correction. A widely repeated hydrogen or HTS claim that is wrong, with the constraint that makes it wrong.
3. Build log. What the route, cooling, safety, or cost module can and cannot do this week. Proof over vision.
4. Reply bait that is real. A design choice (MgB₂ vs REBCO cooling station spacing, road-following vs greenfield) framed so a TSO engineer can disagree with a number.

Avoid: generic AI threads, “the future of energy,” quote-tweeting news with no added calculation, link dumps, reply-guy volume on mega accounts (spam classifiers on large accounts were tightened in September 2026).

## Weekly content plan (6–10 Oct 2026, Europe/London)

| Day | Original | Reply cluster |
| --- | --- | --- |
| Mon 6 | Build log: what a hybrid LH2 + HTS corridor planner must score before it draws a line (heat leak, setback, road bias, consent). No link in body. | Gasunie / European H2 backbone, SCARLET, MgB₂ papers |
| Tue 7 | Forwardable number: cooling-station spacing is a heat-leak problem, not a map pin. One worked assumption, one sensitivity. | Cryogenics and LH2 safety accounts |
| Wed 8 | Correction: superconducting cable in LH2 is not “free cooling.” State the quench and heat-load constraint. | Superconductivity paper accounts, cable OEMs |
| Thu 9 | Cost frame: CAPEX per km is the wrong headline; competitiveness is vs new HVAC/HVDC plus separate H2 logistics. | TSO planning, grid commentators |
| Fri 10 | Copy-link asset: 7 checks before a hybrid corridor leaves the whiteboard. Link to the note only in reply. | Anyone who engaged Mon–Thu |

Pinned post (set once, do not rotate weekly): one sentence on what PipeMind does, who it is for, and the single proof point currently true. No “coming soon.”

## Metrics to log next refresh

Track only: profile visits from posts, follows from posts, replies received, replies we answered, copy-link or quote events if visible, and conversations that named a company or a corridor. Ignore impressions as a success metric.

Kill rule: any format with two posts and zero specialist replies gets retired for two weeks.
