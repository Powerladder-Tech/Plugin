# Template Fill Guide: How to Populate Excel Templates from CEO Answers

This reference tells you EXACTLY which cells to fill when populating the Business Play templates with a CEO's interview answers.

---

## Balance Sheet Template (`business-play-balance-sheet-template.xlsx`)

### Sheet: "Balance Sheet" — Cell Map

All input cells are in **column C** with **blue text** (hardcoded inputs). Only fill cells where the CEO provided data. Leave unknown cells blank — the formulas handle zeros gracefully.

| Row | Cell | Field | Interview Question |
|-----|------|-------|--------------------|
| 6 | C6 | Cash & Cash Equivalents | "How much Cash does your business hold right now?" |
| 7 | C7 | Accounts Receivable (Net) | "What is your total Accounts Receivable?" |
| 8 | C8 | Inventory (Net) | "What is your total Inventory value?" |
| 9 | C9 | Prepaid Expenses & Other Current Assets | Optional — ask if CEO mentions prepaid items |
| 13 | C13 | Property, Plant & Equipment (Net) | Optional — ask if CEO mentions fixed assets |
| 14 | C14 | Intangible Assets & Goodwill | Optional — rarely needed for Quick Ratio |
| 15 | C15 | Other Non-Current Assets | Optional |
| 21 | C21 | Accounts Payable | Optional — ask if CEO mentions supplier payments |
| 22 | C22 | Short-Term Debt & Current LTD | Part of "Current Liabilities" answer — split if CEO gives detail |
| 23 | C23 | Accrued Expenses & Other Current | Part of "Current Liabilities" answer — split if CEO gives detail |
| 27 | C27 | Long-Term Debt | "Any Long-Term Debt? Approximately how much?" |
| 28 | C28 | Deferred Tax Liabilities | Optional — rarely needed |
| 29 | C29 | Other Non-Current Liabilities | Optional |
| 35 | C35 | Paid-In Capital / Share Capital | Part of "Total Equity" answer |
| 36 | C36 | Retained Earnings | Part of "Total Equity" — split if CEO gives detail |
| 37 | C37 | Other Equity Components | Optional |

### Auto-Calculated Cells (DO NOT OVERWRITE)

| Cell | Formula | Description |
|------|---------|-------------|
| C10 | =SUM(C6:C9) | Total Current Assets |
| C16 | =SUM(C13:C15) | Total Non-Current Assets |
| C18 | =C10+C16 | TOTAL ASSETS |
| C24 | =SUM(C21:C23) | Total Current Liabilities |
| C30 | =SUM(C27:C29) | Total Non-Current Liabilities |
| C32 | =C24+C30 | TOTAL LIABILITIES |
| C38 | =SUM(C35:C37) | TOTAL EQUITY |
| C40 | =C18-C32-C38 | Balance Check (should = 0) |

### Sheet: "FRS Score" — Auto-Calculated

All cells on this sheet are formulas that pull from the Balance Sheet tab. **Do not edit this sheet.** Once you populate the Balance Sheet tab and run recalc, the FRS Score appears automatically in cell **D16**.

**Key output cells:**

| Cell | What It Shows |
|------|---------------|
| C5 | Current Ratio |
| C6 | Quick Ratio |
| C9 | Debt-to-Equity Ratio |
| C10 | Working Capital % of Total Assets |
| C13 | Cash % of Total Assets |
| C14 | Inventory % of Current Assets |
| **D16** | **YOUR FRS SCORE (0–100)** |

---

## Inventory Template (`business-play-inventory-template.xlsx`)

### Sheet: "Inventory Data" — Cell Map

The template has **5 pre-filled sample rows** (rows 4–8) and **15 blank rows** (rows 9–23) for CEO data. Each row represents one SKU or product category.

| Column | Field | Source |
|--------|-------|--------|
| A | SKU / Product Name | "What are your top 3–5 products or categories?" |
| B | Category | CEO's product category grouping |
| C | Units in Stock | "How many units of each?" (or estimate) |
| D | Unit Cost | "What does each unit cost you?" |
| E | Total Inventory Cost | =C×D (auto-formula) |
| F | Unit Selling Price | "What do you sell each for?" |
| G | Total Revenue Potential | =C×F (auto-formula) |
| H | Unit Margin | =F−D (auto-formula) |
| I | Margin % | =H/F (auto-formula) |
| J | Monthly Demand (units) | "How many units sell per month?" |
| K | Lead Time (days) | "How long from order to delivery?" |
| L | ROI % | =H/D (auto-formula) |
| M | Cash Trap Status | =IF(E/budget<0.15,"OK","CASH TRAP") (auto) |

**Minimum data needed per SKU:** Name (A), Unit Cost (D), Selling Price (F), Monthly Demand (J)

### Sheet: "OS Score" — Requires Manual Input

Unlike the FRS tab, the OS Score sheet needs the creature to input **scored values** based on conversation, not raw financial data.

| Cell | Field | How to Score | Source Question |
|------|-------|--------------|-----------------|
| C5 | Revenue Growth Rate % | Enter the CEO's stated growth rate | "How is demand trending?" |
| C6 | Market Share Trend | 30=Declining, 50=Stable, 70=Growing, 90=Surging | "How is demand trending?" |
| D5 | Demand Score 1 (0–100) | Auto-formula from C5 | |
| D6 | Demand Score 2 (0–100) | Auto-formula from C6 | |
| C9 | Avg Gross Margin % | Enter CEO's stated margin | "What is your average gross margin?" |
| C10 | High-Margin SKU % | Estimate from product mix discussion | |
| D9 | Margin Score 1 (0–100) | Auto-formula from C9 | |
| D10 | Margin Score 2 (0–100) | Auto-formula from C10 | |
| C13 | Supplier On-Time Rate % | Estimate: Excellent=95, Mixed=75, Unreliable=50 | "How reliable are your suppliers?" |
| C14 | Dead Stock % | CEO's stated dead stock percentage | "What % is slow-moving?" |
| D13 | Supply Score 1 (0–100) | Auto-formula from C13 | |
| D14 | Supply Score 2 (0–100) | Auto-formula from C14 | |
| **D16** | **YOUR OS SCORE (0–100)** | Auto-formula | |

### Sheet: "Procurement Plan" — Reference Only

This sheet provides the Knapsack optimization framework. After filling the Inventory Data tab, the creature can reference this sheet to discuss procurement strategy.

---

## Python Code: Complete Template Fill Workflow

```python
import openpyxl
import subprocess
import os

def fill_balance_sheet(template_path, output_path, answers):
    """
    Fill the Balance Sheet template with CEO's financial answers.

    answers = {
        'cash': 500000,
        'accounts_receivable': 300000,
        'inventory': 800000,
        'prepaid': 50000,           # optional
        'ppe': 1200000,             # optional
        'accounts_payable': 200000, # optional
        'short_term_debt': 150000,
        'accrued_expenses': 100000, # optional
        'long_term_debt': 500000,
        'equity_capital': 1000000,
        'retained_earnings': 400000, # optional
    }
    """
    wb = openpyxl.load_workbook(template_path)
    ws = wb['Balance Sheet']

    # Map answers to cells
    cell_map = {
        'cash': 'C6',
        'accounts_receivable': 'C7',
        'inventory': 'C8',
        'prepaid': 'C9',
        'ppe': 'C13',
        'intangibles': 'C14',
        'other_noncurrent': 'C15',
        'accounts_payable': 'C21',
        'short_term_debt': 'C22',
        'accrued_expenses': 'C23',
        'long_term_debt': 'C27',
        'deferred_tax': 'C28',
        'other_noncurrent_liab': 'C29',
        'equity_capital': 'C35',
        'retained_earnings': 'C36',
        'other_equity': 'C37',
    }

    for key, cell in cell_map.items():
        if key in answers and answers[key] is not None:
            ws[cell] = answers[key]

    wb.save(output_path)
    return output_path


def fill_inventory(template_path, output_path, skus, os_scores):
    """
    Fill the Inventory template with CEO's product data.

    skus = [
        {'name': 'Widget A', 'category': 'Widgets', 'units': 500,
         'unit_cost': 100, 'selling_price': 180, 'monthly_demand': 150,
         'lead_time': 14},
        ...
    ]

    os_scores = {
        'revenue_growth': 15,      # percentage
        'market_share_trend': 70,  # 30/50/70/90 scale
        'gross_margin': 45,        # percentage
        'high_margin_pct': 60,     # percentage
        'supplier_ontime': 85,     # percentage
        'dead_stock_pct': 12,      # percentage
    }
    """
    wb = openpyxl.load_workbook(template_path)

    # Fill Inventory Data tab (start at row 9 for blank rows)
    ws_inv = wb['Inventory Data']
    start_row = 9  # First blank row after samples
    for i, sku in enumerate(skus):
        row = start_row + i
        if row > 23:  # Max 15 blank rows
            break
        ws_inv[f'A{row}'] = sku.get('name', '')
        ws_inv[f'B{row}'] = sku.get('category', '')
        ws_inv[f'C{row}'] = sku.get('units', 0)
        ws_inv[f'D{row}'] = sku.get('unit_cost', 0)
        ws_inv[f'F{row}'] = sku.get('selling_price', 0)
        ws_inv[f'J{row}'] = sku.get('monthly_demand', 0)
        ws_inv[f'K{row}'] = sku.get('lead_time', 0)

    # Fill OS Score tab
    ws_os = wb['OS Score']
    ws_os['C5'] = os_scores.get('revenue_growth', 0) / 100
    ws_os['C6'] = os_scores.get('market_share_trend', 50)
    ws_os['C9'] = os_scores.get('gross_margin', 0) / 100
    ws_os['C10'] = os_scores.get('high_margin_pct', 0) / 100
    ws_os['C13'] = os_scores.get('supplier_ontime', 0) / 100
    ws_os['C14'] = os_scores.get('dead_stock_pct', 0) / 100

    wb.save(output_path)
    return output_path


def recalc_and_verify(filepath):
    """Run recalc script to compute formula values and verify zero errors."""
    result = subprocess.run(
        ['python', '/path/to/recalc.py', filepath, '60'],
        capture_output=True, text=True
    )
    print(result.stdout)
    return 'total_errors": 0' in result.stdout
```

---

## Quick Ratio: The First Diagnostic

The Quick Ratio is the **first number** the creature should calculate and share, even before the full FRS. It only needs 3 inputs (Cash, AR, Current Liabilities) and provides an immediate signal:

| Quick Ratio | Signal | Creature Response |
|-------------|--------|-------------------|
| < 0.50 | Critical | "Your canteen is nearly empty. We must address cash flow before growth." |
| 0.50–0.99 | Tight | "Limited water. Let's optimize your cash cycle before expanding." |
| 1.00–1.50 | Healthy | "Good reserves. You can weather a supply chain disruption." |
| > 1.50 | Strong | "Well-funded. Are you deploying capital aggressively enough?" |

**Full formula reference** → See `references/financial-statements.md`
