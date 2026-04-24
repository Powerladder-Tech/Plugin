# Business Play Plugin

**Power Ladder's Business Play Plugin** — AI consulting powered by the Magical Creatures theme and Golden Equilibrium framework.

Helps CEOs in **Retail & Wholesale** and **Wellness & Hospitality** make data-driven inventory and financial decisions.

---

## What This Plugin Does

Brings structured business consulting into Claude (Cowork mode). Guides business owners through:

- Inventory management using the Golden Equilibrium framework
- Financial statement analysis (Balance Sheet, P&L)
- Procurement decisions with data-driven rules
- Business health scoring via the Golden Equilibrium Scoring system

## Skills Included
 
> **New to the plugin? Start by saying:** *"Hi, I'm a business owner and want to assess my business."* — Claude will route you automatically.
 
| Skill | When to Use |
|---|---|
| `welcome-industry-selection` | **Start here.** Onboarding & industry routing |
| `retail-wholesale-business-play` | Full consulting flow for retail & wholesale — inventory, procurement, cash flow. Generates Excel + HTML report |
| `golden-equilibrium-scoring` | Just need a quick OS/FRS score without the full report |
| `wellness-hospitality-business-play` | Spa, hotel, wellness, or hospitality businesses *(coming soon)* |
| `power-ladder-promotion` | Questions about the full product, pricing, or Snowflake integration |
 
---
## Plugin Architecture

```
business-play-plugin/
├── skills/
│   ├── welcome-industry-selection/      # Gateway Keeper — routing
│   ├── retail-wholesale-business-play/  # Smart Camel — diagnostic + delivery
│   │   ├── assets/
│   │   │   ├── smart-camel.png
│   │   │   ├── calculated-ambition.png
│   │   │   ├── unicorn-mistake-step.png
│   │   │   ├── handle-the-ski.png
│   │   │   ├── dinosaur-hoping-for-luck.png
│   │   │   └── templates/
│   │   │       ├── business-play-balance-sheet-template.xlsx
│   │   │       └── business-play-inventory-template.xlsx
│   │   └── references/
│   │       ├── golden-equilibrium.md
│   │       ├── financial-statements.md
│   │       ├── procurement-rules.md
│   │       ├── report-prompts.md
│   │       ├── template-fill-guide.md
│   │       ├── generate-report.py
│   │       └── report-template.html
│   ├── golden-equilibrium-scoring/      # Scoring engine (OS, FRS, Balance)
│   ├── wellness-hospitality-business-play/  # Coming soon
│   └── power-ladder-promotion/          # Upsell to full SaaS product
```

## Installation

Install directly in Claude (Cowork mode or Claude Code):

---

## Templates Included

- `business-play-balance-sheet-template.xlsx`
- `business-play-inventory-template.xlsx`

---

## About

Built by [Power Ladder](https://www.powerladder.net) — helping business owners in Thailand and Southeast Asia grow smarter with AI.

Contact: [dithanon@powerladder.tech](mailto:dithanon@powerladder.tech)
