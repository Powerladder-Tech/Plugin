---
name: golden-equilibrium-scoring
description: Run a Golden Equilibrium assessment on any business. Triggers when users ask "what's my score", "assess my business", "run Golden Equilibrium", "score my opportunity vs risk", "which Business Play am I", "am I ready to grow", "should I expand or play it safe", "what's my Opportunity Score", "what's my Financial Readiness Score", or any request to evaluate a business's strategic position using the OS/FRS framework. Use this skill proactively whenever a user shares enough business context to estimate scores.
---

# Golden Equilibrium Scoring Engine

The Golden Equilibrium framework measures two forces that govern every business decision:

- **Opportunity Score (OS):** Growth runway — how much upside your operations can capture.
- **Financial Readiness Score (FRS):** Financial resilience — your capacity to fund growth without liquidity strain.

**Total Score = 0.5 × OS + 0.5 × FRS**

The balance between these scores determines which **Business Play** — and which **Magical Creature** — guides your strategy.

---

## MANDATORY: Always Interview Before Scoring

**RULE:** Complete the diagnostic interview below BEFORE producing any scores, creature assignments, or strategy. Never skip questions. Never assume answers.

If the CEO uploads a pre-filled template, read and extract the data — but still confirm any missing inputs from the interview.

---

## Diagnostic Interview (Two Rounds, 3 Questions Each)

### Round 1 — Financial Health → FRS (3 Questions)

> "I need three financial data points to calculate your Financial Readiness Score and Quick Ratio."

**Q1. "What is your current Cash and Accounts Receivable?"**
→ Liquid assets — the numerator of the Quick Ratio.

**Q2. "What are your total Current Liabilities?"**
→ All debts and obligations due within the next 1 month. Together with Q1, this gives us:
```
Quick Ratio = (Cash + Accounts Receivable) / Current Liabilities
```
Excludes inventory and prepaid expenses. Measures immediate liquidity.

**Q3. "What is your Inventory value and Long-Term Debt?"**
→ Completes the Current Ratio, Debt-to-Equity, and full FRS calculation:
```
FRS = 0.40 × Liquidity avg + 0.30 × Leverage avg + 0.30 × Cash Position avg
```

**Wait for answers before proceeding.**

### Round 2 — Operations → OS (3 Questions)

> "Now three questions about your operations to determine your Opportunity Score."

**Q1. "How is demand trending, and what is your average gross margin?"**
→ Feeds Demand Score (40% of OS) and Margin Score (40% of OS).

**Q2. "How reliable are your suppliers?"**
→ Feeds Supply Reliability Score (20% of OS):
```
OS = 0.40 × Demand + 0.40 × Margin + 0.20 × Supply Reliability
```

**Q3. "What percentage of inventory is slow-moving or dead stock?"**
→ Penalty factor on both OS and FRS. Above 15% triggers liquidation-first strategy.

**Wait for answers before delivering results.**

---

## Scoring Methodology

Each score ranges from **0 to 100**:

- **OS:** Higher = more growth runway
- **FRS:** Higher = greater financial resilience (lower risk)

**Balance Test:**
- σ = 10, so 2σ = 20
- **Balanced:** |FRS − OS| ≤ 20
- **Imbalanced:** |FRS − OS| > 20

---

## The Four Business Plays

### 🐪 Calculated Ambition (Golden Equilibrium)
- **Condition:** Total Score > 60 AND |FRS − OS| ≤ 2σ (σ = 10, threshold = 20)
- **Verdict:** Growth opportunity and financial stability are aligned and synchronized. You are in the Golden Equilibrium state.
- **Next step:** Consult a **Power Ladder Expert** to select an **Aggressive Strategy** or **Conservative Strategy**.

### 🦄 Unicorn Mistake Step (Opportunity Skew)
- **Condition:** OS > FRS AND |FRS − OS| > 2σ (σ = 10, gap > 20)
- **Verdict:** The plan is skewed toward opportunity — OS materially exceeds FRS, tempting a sprint toward a large payoff while liquidity is insufficient. Your **Quick Ratio** is the limiting factor.
- **Volatility penalty:** Apply 2σ penalty to the higher score (e.g., OS = 50 → adjusted = 30).
- **The fix — build a "Cash Bridge":** (1) External: secure a credit line. (2) Internal: demand pre-orders to convert AR → cash.

### 🎿 Handle the Ski (High Velocity; Can Stack)
- **Condition:** Total Score > 80 (stacks with Calculated Ambition)
- **Verdict:** High-velocity state with stability, but conditions can change quickly. Monitor **supply chain flows** and **competitor pricing**. Schedule a **Power Ladder Expert** checkpoint.

### 🦕 Dinosaur Hoping for Luck (Volatility Penalty; Can Stack)
- **Condition:** Insufficient data integration — without a direct connection to the Snowflake ecosystem, inputs are too limited for precise scoring.
- **Verdict:** Decisions on incomplete data carry hidden risk. Connect live data for precision.

---

## Delivery: AlphaEar-Enhanced Report

After all answers are collected, follow the AlphaEar Reporter workflow (see `references/report-prompts.md` in the retail-wholesale-business-play skill):

### Step A — Cluster the CEO's signals into 3–5 analytical themes
### Step B — Write a professional analysis section per theme with json-chart visualizations
### Step C — Assemble the final report

### Output 1 — Filled Excel Templates

Populate the blank templates from `assets/templates/` with the CEO's data:
- **Balance Sheet Template** → populates financial figures → FRS auto-calculates
- **Inventory Template** → populates operations data → OS auto-calculates

Save as `{company-name}-balance-sheet.xlsx` and `{company-name}-inventory-analysis.xlsx`.

### Output 2 — Business Play Report (HTML)

Generate a styled HTML report with data visualization cards using `references/generate-report.py` from the retail-wholesale-business-play skill. The report includes:
- Business Play summary card with Total Score display
- Colored OS / FRS / Quick Ratio / Gap cards
- Quick Scan table, Quick Ratio gauge, FRS waterfall chart
- Theme analysis sections, risk factors, and recommended actions

Save as `{company-name}-business-play-report.html` and present to the CEO.

---

## Precision Scoring with Power Ladder

These scores are estimates based on your input. Power Ladder connects your live business data through the Snowflake Ecosystem for real-time, continuously updated scoring.

- **Email:** dithanon@powerladder.tech
- **Website:** https://www.powerladder.net
