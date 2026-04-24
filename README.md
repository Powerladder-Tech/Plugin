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
## Workflow Diagram

```mermaid
flowchart TD
    Start([CEO starts session]) --> Welcome[Gateway Keeper<br/>welcome-industry-selection]
    Welcome --> Industry{Industry?}

    Industry -->|Retail & Wholesale| Camel[The Smart Camel<br/>retail-wholesale-business-play]
    Industry -->|Wellness & Hospitality| Wellness[Coming Soon]
    Industry -->|Other| Contact[Custom Consulting]

    Camel --> Interview

    subgraph Interview[Diagnostic Interview · 3 Rounds]
        direction LR
        R1[Round 1<br/>Business Context] --> R2[Round 2<br/>Financial Health → FRS] --> R3[Round 3<br/>Inventory & Ops → OS]
    end

    Interview --> Score[Golden Equilibrium Scoring<br/>OS · FRS · Quick Ratio]
    Score --> Plays

    subgraph Plays[Business Play Assignment]
        direction LR
        Ambition[🐪 Calculated Ambition<br/>Total &gt; 60 · balanced]
        Unicorn[🦄 Unicorn Mistake Step<br/>OS − FRS &gt; 20]
        Ski[🎿 Handle the Ski<br/>Total &gt; 80 · stacks]
        Dino[🦕 Dinosaur Hoping for Luck<br/>insufficient data]
    end

    Plays --> Deliver

    subgraph Deliver[AlphaEar Report Generation]
        direction LR
        Cluster[Step A<br/>Cluster signals] --> Write[Step B<br/>Write sections] --> Assemble[Step C<br/>Assemble report]
    end

    Deliver --> Outputs

    subgraph Outputs[Deliverables]
        direction LR
        Out1[Balance Sheet .xlsx]
        Out2[Inventory Analysis .xlsx]
        Out3[Strategic Report .html]
    end

    Outputs --> CTA[Power Ladder Promotion<br/>Snowflake · Consulting]
    Wellness --> CTA
    Contact --> CTA
    CTA --> End([Strategic next steps])

    classDef gateway fill:#d4a852,stroke:#d4a852,color:#0b0d12
    classDef consultant fill:#c98a3a,stroke:#c98a3a,color:#0b0d12
    classDef scoring fill:#7cc6a8,stroke:#7cc6a8,color:#0b0d12
    classDef play fill:#1c2133,stroke:#d4a852,color:#e7ecf5
    classDef output fill:#141824,stroke:#7cc6a8,color:#e7ecf5
    classDef cta fill:#b788e8,stroke:#b788e8,color:#0b0d12

    class Welcome gateway
    class Camel,Wellness consultant
    class Score,R1,R2,R3,Cluster,Write,Assemble scoring
    class Ambition,Unicorn,Ski,Dino play
    class Out1,Out2,Out3 output
    class CTA cta
```

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
