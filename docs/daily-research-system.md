# PipeMind AI – Daily Research & Knowledge Upgrade System

## Goal
Every day a focused research cycle runs on one module. The findings are used to:
1. Update the research documents in this repository
2. Train / upgrade the corresponding expert skill
3. Keep the user’s Obsidian vault current

## How it works

### 1. Daily Research Orchestrator
Skill name: `pipemind-daily-research`

Trigger phrases:
- “Run daily research”
- “Start the research cycle”
- “Update knowledge for Module X”
- “Train the agents”

### 2. Rotation Schedule
| Day | Module | Research Skill |
|-----|--------|----------------|
| Monday | 1 – Route | pipemind-research-route |
| Tuesday | 2 – Cooling | pipemind-research-cooling |
| Wednesday | 3 – Safety | pipemind-research-safety |
| Thursday | 4 – Cost | pipemind-research-cost |
| Friday | 5 – Twin | pipemind-research-twin |
| Saturday | 6 – Reports | pipemind-research-reports |
| Sunday | Domain / Catch-up | pipemind-research-domain |

You can override the schedule by naming a specific module.

### 3. What happens in one cycle
1. Choose a sharp research question for that module
2. Deep research with live web tools
3. Produce a structured research note
4. Update the GitHub research file
5. Generate a short “Knowledge Upgrade” for the expert skill
6. Generate an Obsidian-ready note the user pastes into their vault

### 4. Obsidian Integration
After every cycle you will receive a clean Markdown block. Paste it into:

```
02-Modules/
  Module-X-Name/
    Research-Log.md   ← append the new entry
    Notes.md          ← if important permanent knowledge
```

Also drop a short entry into your Daily Notes.

### 5. Feedback Loop
The expert skills (pipemind-route, pipemind-cooling, etc.) are designed to absorb the new findings when you next work on that module. Over time the research skills keep the expert skills sharp.

## How to run it
Simply say:

> Run today’s daily research

or

> Run daily research for the Safety module

The orchestrator will execute the full cycle.
