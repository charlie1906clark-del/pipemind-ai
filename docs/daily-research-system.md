# PipeMind AI – Daily Research & Training System

This document explains how the research agents continuously improve the expert agents and keep Obsidian current.

## Overview

Every day a focused research cycle runs for one module. The cycle produces three things:

1. **Research Note** → goes into GitHub `docs/research/` and into Obsidian
2. **Knowledge Upgrade Block** → trains the corresponding expert skill
3. **Obsidian-ready note** → paste directly into the vault

This creates a closed loop:

Research Agent → New Knowledge → Expert Agent gets smarter → Better advice & code → Stronger product

## Daily Rotation

| Day | Module | Research Skill |
|-----|--------|----------------|
| Monday | 1 – Route | pipemind-research-route |
| Tuesday | 2 – Cooling | pipemind-research-cooling |
| Wednesday | 3 – Safety | pipemind-research-safety |
| Thursday | 4 – Cost | pipemind-research-cost |
| Friday | 5 – Twin | pipemind-research-twin |
| Saturday | 6 – Reports | pipemind-research-reports |
| Sunday | Domain / catch-up | pipemind-research-domain |

## How to run it

Simply say:

> run daily research

or

> run daily research for safety

The orchestrator (`pipemind-daily-research`) will:
- Choose the correct module
- Perform deep research
- Produce the three outputs
- Show you exactly what to paste into Obsidian
- Show the Knowledge Upgrade that trains the expert agent

## Obsidian Update Rule

After every research cycle, paste the provided note into:

```
02-Modules/Module-X/Research-Log.md
```

and also into that day’s Daily Note.

This keeps your personal brain perfectly in sync with the research the agents are doing.

## Training the Expert Agents

Each expert skill (pipemind-route, pipemind-safety, etc.) now contains a Knowledge Upgrade Protocol. When a Knowledge Upgrade Block is generated, the expert agent treats every bullet as permanent new knowledge and uses it in all future reasoning.

Over weeks this compounds: the agents become noticeably more accurate and up-to-date.

## Recommended Habit

- Run the daily research every morning (or the night before).
- Spend 5 minutes pasting the Obsidian note.
- Once a week, review the accumulated Knowledge Upgrades and decide if any build-plan changes are needed.
