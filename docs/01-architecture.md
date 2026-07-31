# PipeMind AI – Architecture & Scaling Rules

## Repository Design Principles (Never break these)

1. **One clear hierarchy** – Everything lives under `docs/`, `src/`, or `data/`
2. **Markdown first** – All knowledge is in Markdown so it works with Obsidian, GitHub, and future tools
3. **Module isolation** – Each module has its own research file and build-plan file
4. **No dumping** – Never put random notes in the root
5. **Future code stays clean** – When code arrives, it goes in `src/module-name/`

## Recommended long-term structure

```
pipemind-ai/
├── docs/                     # All human knowledge
│   ├── 00-overview.md
│   ├── 01-architecture.md
│   ├── 02-obsidian-brain.md
│   ├── research/             # Deep research (one file per module)
│   ├── modules/              # Detailed build plans (one file per module)
│   ├── execution/            # Plans, roadmaps, decisions
│   └── decisions/            # Architecture Decision Records (ADRs)
├── src/                      # Actual software code
│   ├── route_planner/
│   ├── cooling/
│   ├── safety/
│   ├── cost/
│   ├── digital_twin/
│   └── reports/
├── data/                     # Sample corridors, test cases, reference data
├── notebooks/                # Exploratory Jupyter notebooks (optional)
└── tests/
```

## Rules for keeping it clean forever

- Every new piece of knowledge must live in the correct folder
- Use consistent naming: `module-X-short-name.md`
- Prefer many small focused files over one giant file
- When a decision is made, write a short ADR in `docs/decisions/`
- Never commit large binary files (PDFs, heavy images) – keep Markdown versions
- Update the README only when the high-level structure changes
