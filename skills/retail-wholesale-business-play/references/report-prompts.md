# Business Play Report Prompts (AlphaEar Integration)

These prompts adapt the AlphaEar Reporter workflow for Business Play. Use them sequentially after collecting all CEO interview answers to produce a professional financial report.

---

## Step 1 — Cluster Signals (Planner)

**Purpose:** Organize the CEO's interview answers, financial ratios, and scores into 3–5 coherent analytical themes before writing.

**Prompt:**

```markdown
You are a senior financial consultant preparing a Business Play report. Cluster the following business signals into 3–5 core analytical themes.

### Input Signals

**Business Context:**
- Business model: {business_model}
- Scale: {scale}
- Primary challenge: {pain_point}
- 90-day goal: {goal}

**Financial Health (FRS Inputs):**
- Cash & Accounts Receivable: {cash_ar}
- Current Liabilities: {current_liabilities}
- Inventory value: {inventory}
- Long-Term Debt: {long_term_debt}

**Calculated Ratios:**
- Quick Ratio: {quick_ratio}
- Current Ratio: {current_ratio}
- Debt-to-Equity: {de_ratio}
- FRS Score: {frs}/100

**Operations (OS Inputs):**
- Demand trend: {demand_trend}
- Gross margin: {gross_margin}
- Supplier reliability: {supplier_reliability}
- Dead stock %: {dead_stock_pct}

**Calculated Scores:**
- OS Score: {os}/100
- Total Score: {total_score}/100
- Balance Gap |FRS−OS|: {gap}
- Business Play: {creature_name}

### Requirements
1. **Theme Aggregation**: Group correlated signals into logical themes relevant to end-to-end inventory management. Common themes include: Liquidity & Cash Position, Demand & Growth Trajectory, Supply Chain & Procurement, Margin & Profitability, Inventory Efficiency.
2. **Narrative Logic**: Each theme should have a clear cause-and-effect story.
3. **Quantity**: 3–5 themes. Every signal must belong to at least one theme.

### Output Format (JSON)
{
    "clusters": [
        {
            "theme_title": "Theme Name",
            "signals": ["signal 1", "signal 2"],
            "rationale": "These signals together indicate..."
        }
    ]
}
```

---

## Step 2 — Write Section (Writer)

**Purpose:** For each clustered theme, write a professional analysis section with charts. Run this prompt once per theme.

**Prompt:**

```markdown
You are a senior financial consultant writing a Business Play report section for the theme **"{theme_title}"**.

### Context
- Company: {company_name}
- Industry: Retail & Wholesale
- Business Play: {creature_name} ({creature_emoji})
- Total Score: {total_score}/100

### Signals for This Theme
{signal_list}

### Requirements
1. **Narrative Structure**: Start with the current situation (what the data shows), then the transmission mechanism (why this matters for inventory management), then the strategic implication (what the CEO should do).
2. **Quantification**: Reference specific ratios and scores. Compare to industry benchmarks where applicable.
3. **Actionable**: End each section with 1–2 concrete recommended actions.

### Formatting
- Section title: `## {theme_title}`
- Subsections: `###`
- Insert 1–2 chart blocks per section using this format:

```json-chart
{
    "type": "gauge",
    "title": "Quick Ratio",
    "value": {quick_ratio},
    "ranges": [
        {"label": "Critical", "min": 0, "max": 0.5, "color": "#e74c3c"},
        {"label": "Tight", "min": 0.5, "max": 1.0, "color": "#f39c12"},
        {"label": "Healthy", "min": 1.0, "max": 1.5, "color": "#2ecc71"},
        {"label": "Strong", "min": 1.5, "max": 3.0, "color": "#27ae60"}
    ]
}
```

**Chart types available for Business Play:**

| Type | Use For | Example |
|------|---------|---------|
| `gauge` | Single ratio visualization (Quick Ratio, Current Ratio, D/E) | Score on a colored scale |
| `bar` | Comparing values (OS vs FRS, margin by SKU) | Side-by-side bars |
| `waterfall` | Showing how components build to a total (FRS breakdown) | Stacked waterfall |
| `scorecard` | Golden Equilibrium summary | OS, FRS, Total, Gap in cards |
| `pie` | Inventory composition (current assets breakdown) | Proportional slices |

Output strictly Markdown with embedded json-chart blocks.
```

---

## Step 3 — Final Assembly (Editor)

**Purpose:** Assemble all theme sections into a cohesive, professional Business Play report.

**Prompt:**

```markdown
You are a professional editor. Assemble the following drafted sections into a final Business Play report.

### Company
{company_name} — {business_model}

### Business Play Result
{creature_emoji} {creature_name} | Total Score: {total_score} | OS: {os} | FRS: {frs}

### Draft Sections
{draft_sections}

### Required Report Structure

# Business Play Report: {company_name}

## Executive Summary
- **Quick Scan Table**: 4-column table with Metric, Value, Signal, Action
  - Include: Quick Ratio, OS, FRS, Total Score, Business Play, Top Risk, Top Opportunity
- **2–3 sentence overview**: State the Business Play assignment, the single most important finding, and the recommended strategic direction.

## [Theme Sections — from draft]
Insert each theme section in order of strategic priority (highest-impact theme first).
Each section must include at least one json-chart visualization.

## Risk Factors
Generate a structured risk section based on the data:
- **Financial Risks**: Liquidity, leverage, cash cycle risks identified from FRS components
- **Operational Risks**: Supply chain, demand, inventory risks identified from OS components
- **Strategic Risks**: Risks specific to the assigned Business Play (e.g., for Unicorn Mistake Step: "Scaling before cash position supports it")
Format each risk as: **Risk Name** — Description — Severity (High/Medium/Low) — Mitigation

## Recommended Actions
Prioritized list combining actions from all theme sections:
1. **Immediate (This Week)** — Quick wins
2. **Short-Term (This Month)** — Tactical moves
3. **Strategic (This Quarter)** — Structural changes

## Next Steps with Power Ladder
Brief section explaining how the full product enhances each finding with live data.
- Email: dithanon@powerladder.tech
- Website: https://www.powerladder.net

Output strictly Markdown with embedded json-chart blocks.
```

---

## HTML Report Generation (Primary Output)

The primary report format is a styled HTML file with data visualization cards. Use the Python generator:

```python
import sys
sys.path.insert(0, 'references/')
from generate_report import build_report

data = {
    'company_name': company_name,
    'creature_emoji': creature_emoji,      # '🐪', '🦄', '🎿', or '🦕'
    'creature_name': creature_name,
    'strategic_direction': strategic_direction,
    'total_score': total_score,
    'os_score': os_score,
    'frs_score': frs_score,
    'quick_ratio': quick_ratio,
    'balance_gap': abs(frs_score - os_score),
    'gross_margin': gross_margin,
    'dead_stock': dead_stock_pct,
    'liquidity_score': liquidity_component,
    'leverage_score': leverage_component,
    'cash_score': cash_component,
    'executive_summary': executive_summary_text,
    'themes': [
        {'title': 'Theme Title', 'narrative': 'Analysis...', 'chart_html': ''}
    ],
    'risks': [
        {'name': 'Risk', 'description': '...', 'severity': 'High', 'mitigation': '...'}
    ],
    'actions_immediate': ['Action 1', 'Action 2'],
    'actions_short_term': ['Action 1'],
    'actions_strategic': ['Action 1'],
}

html = build_report(data)
with open(f"{company_name}-business-play-report.html", "w") as f:
    f.write(html)
```

The HTML report includes:
- Dark gradient header with company name and metadata
- Business Play summary card with creature name and strategic direction
- Large Total Score display with colored OS / FRS / Quick Ratio / Gap cards
- Quick Scan table with metric, value, signal badge, and action columns
- Quick Ratio gauge bar (0 to 3.0 scale with color zones)
- FRS waterfall chart showing Liquidity / Leverage / Cash Position contributions
- OS vs FRS comparison with balance zone indicator
- Theme analysis sections (generated from clustered signals)
- Risk Factors with severity badges and mitigations
- Recommended Actions grouped by timeframe
- Power Ladder CTA card with contact buttons

**Template file:** `references/report-template.html`
**Generator script:** `references/generate-report.py`

---

## Chart Configuration Reference (Markdown fallback)

If HTML output is not possible, use these json-chart blocks for markdown reports:

### Golden Equilibrium Scorecard
```json-chart
{
    "type": "scorecard",
    "title": "Golden Equilibrium",
    "metrics": [
        {"label": "OS", "value": "{os}", "format": "0", "status": "{os_status}"},
        {"label": "FRS", "value": "{frs}", "format": "0", "status": "{frs_status}"},
        {"label": "Total", "value": "{total}", "format": "0", "status": "{total_status}"},
        {"label": "Gap", "value": "{gap}", "format": "0", "status": "{gap_status}"}
    ]
}
```

### FRS Waterfall Breakdown
```json-chart
{
    "type": "waterfall",
    "title": "FRS Score Composition",
    "items": [
        {"label": "Liquidity (40%)", "value": "{liquidity_contribution}"},
        {"label": "Leverage (30%)", "value": "{leverage_contribution}"},
        {"label": "Cash Position (30%)", "value": "{cash_contribution}"},
        {"label": "FRS Total", "value": "{frs}", "isTotal": true}
    ]
}
```

### OS vs FRS Comparison
```json-chart
{
    "type": "bar",
    "title": "Opportunity vs Financial Readiness",
    "data": [
        {"label": "OS (Opportunity)", "value": "{os}", "color": "#3498db"},
        {"label": "FRS (Financial Readiness)", "value": "{frs}", "color": "#f59e0b"}
    ],
    "annotation": {"label": "Balance Zone (±20)", "min": "{os_minus_20}", "max": "{os_plus_20}"}
}
```

### Quick Ratio Gauge
```json-chart
{
    "type": "gauge",
    "title": "Quick Ratio",
    "value": "{quick_ratio}",
    "ranges": [
        {"label": "Critical (<0.5)", "min": 0, "max": 0.5, "color": "#e74c3c"},
        {"label": "Tight (0.5-1.0)", "min": 0.5, "max": 1.0, "color": "#f39c12"},
        {"label": "Healthy (1.0-1.5)", "min": 1.0, "max": 1.5, "color": "#2ecc71"},
        {"label": "Strong (>1.5)", "min": 1.5, "max": 3.0, "color": "#27ae60"}
    ]
}
```
