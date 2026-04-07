# Financial Statement Analysis: The Handle the Ski Reference Guide

> *Display the Handle the Ski creature image: use the Read tool on `assets/handle-the-ski.png`*

---

## Your Magical Creature: The Financial Navigator

After a CEO selects **Retail & Wholesale**, their Magical Creature guides them through financial analysis. The creature introduces itself and offers **two paths** to assess financial health:

### Path A — Upload the Balance Sheet Template
> "I have a ready-made Balance Sheet template for you. Download it, fill in your numbers, and upload it back. I'll auto-calculate your Financial Readiness Score and all key ratios instantly."

Offer the template files from `assets/templates/`:
- `business-play-balance-sheet-template.xlsx` (Excel with auto-formulas)
- `business-play-balance-sheet-template.csv` (CSV for manual entry)

### Path B — Quick Ratio Express (Conversation Mode)
> "No balance sheet handy? No problem. I just need three numbers to gauge your immediate liquidity."

Ask these three simple questions:

1. **"How much Cash & Cash Equivalents does your business hold right now?"**
2. **"What is your total Accounts Receivable (money customers owe you)?"**
3. **"What are your total Current Liabilities (all debts and obligations due within the next 1 month)?"**

Then calculate:

```
Quick Ratio = (Cash + Accounts Receivable) / Current Liabilities
```

**What Quick Ratio EXCLUDES (and why):**
- Inventory — cannot be instantly converted to cash; may be obsolete or slow-moving
- Prepaid expenses — already spent, cannot be recovered as cash quickly

**Purpose:** Measures immediate liquidity and the business's ability to meet urgent financial obligations without relying on selling inventory. This is the single most important ratio for a retail/wholesale CEO who needs to know: *"Can I pay my bills RIGHT NOW?"*

**Quick Ratio Interpretation for Retail & Wholesale:**

| Quick Ratio | Signal | Creature Guidance |
|-------------|--------|-------------------|
| < 0.50 | Critical liquidity risk | "Your desert canteen is nearly empty. We must address cash flow before any growth moves." |
| 0.50 – 0.99 | Tight but manageable | "You're navigating with limited water. Let's optimize your cash cycle before expanding." |
| 1.00 – 1.50 | Healthy liquidity | "Good balance. You have enough reserves to weather a supply chain disruption." |
| > 1.50 | Strong cash position | "You're well-funded. The question now is: are you deploying this capital aggressively enough?" |

---

## Complete Formula Reference

**IMPORTANT:** Use the formulas below unless otherwise specified by the user.

---

### Core Linkages

```
Balance Sheet:        Assets = Liabilities + Equity
Net Income:           IS Net Income → CF Operations (starting point)
Cash Flow:            ΔCash = CFO + CFI + CFF
Cash Tie-Out:         Ending Cash (CF) = Cash (BS Asset)
Cash Monthly/Annual:  Closing Cash (Monthly) = Closing Cash (Annual)
Retained Earnings:    Prior RE + Net Income - Dividends = Ending RE
Equity Raise:         ΔCommon Stock/APIC (BS) = Equity Issuance (CFF)
Year 0 Equity:        Equity Raised (Year 0) = Beginning Equity (Year 1)
```

---

### Gross Profit Calculation

**IMPORTANT:** Gross Profit must be calculated from Net Revenue, not Gross Revenue.

```
Net Revenue - Cost of Revenue = Gross Profit
```

| Term | Definition |
|------|------------|
| Gross Revenue | Total revenue before any deductions |
| Net Revenue | Gross Revenue - Returns - Allowances - Discounts |
| Cost of Revenue | Direct costs attributable to production of goods/services sold |
| Gross Profit | Net Revenue - Cost of Revenue |

**Note:** Always use Net Revenue (also called "Net Sales" or simply "Revenue" on most financial statements) as the starting point for profitability calculations. Gross Revenue overstates the true top-line performance.

---

### Margin Formulas

```
Gross Margin %      = Gross Profit / Net Revenue
EBITDA              = EBIT + D&A  (or = Gross Profit - OpEx)
EBITDA Margin %     = EBITDA / Net Revenue
EBIT Margin %       = EBIT / Net Revenue
Net Income Margin % = Net Income / Net Revenue
```

---

### Credit Metric Formulas

```
Total Debt            = Current Portion of Debt + Long-Term Debt
Net Debt              = Total Debt - Cash
Total Debt / EBITDA   = Total Debt / EBITDA (from IS)
Net Debt / EBITDA     = Net Debt / EBITDA (from IS)
Interest Coverage     = EBITDA / Interest Expense (from IS)
Net Int Exp % Debt    = Net Interest Expense / Long-Term Debt
Debt / Total Cap      = Total Debt / (Total Debt + Total Equity)
Debt / Equity         = Total Debt / Total Equity
Current Ratio         = Total Current Assets / Total Current Liabilities
Quick Ratio           = (Cash + Accounts Receivable) / Total Current Liabilities
```

**Quick Ratio vs. Current Ratio — Why Both Matter:**

| Ratio | Formula | Includes Inventory? | Best For |
|-------|---------|---------------------|----------|
| Current Ratio | Current Assets / Current Liabilities | Yes | Overall short-term solvency |
| Quick Ratio | (Cash + AR) / Current Liabilities | No | Immediate liquidity stress test |

For **Retail & Wholesale** businesses, the Quick Ratio is the sharper diagnostic because inventory can be illiquid, seasonal, or at risk of obsolescence.

---

### Forecast Formulas (% of Net Revenue Method)

```
Cost of Revenue (Forecast) = Net Revenue × Cost of Revenue % Assumption
S&M (Forecast)             = Net Revenue × S&M % Assumption
G&A (Forecast)             = Net Revenue × G&A % Assumption
R&D (Forecast)             = Net Revenue × R&D % Assumption
SBC (Forecast)             = Net Revenue × SBC % Assumption
```

---

### Working Capital Formulas

```
Accounts Receivable
  Prior AR
  + Revenue (from IS)
  - Cash Collections (plug)
  = Ending AR
  DSO = (AR / Revenue) × 365

Inventory
  Prior Inventory
  + Purchases (plug)
  - COGS (from IS)
  = Ending Inventory
  DIO = (Inventory / COGS) × 365

Accounts Payable
  Prior AP
  + Purchases (from Inventory calc)
  - Cash Payments (plug)
  = Ending AP
  DPO = (AP / COGS) × 365

Net Working Capital = AR + Inventory - AP
ΔWC = Current NWC - Prior NWC
```

**Cash Conversion Cycle (Critical for Retail & Wholesale):**
```
CCC = DSO + DIO - DPO
```
- **DSO** = Days Sales Outstanding (how fast customers pay you)
- **DIO** = Days Inventory Outstanding (how long inventory sits)
- **DPO** = Days Payable Outstanding (how long you take to pay suppliers)

| CCC | Signal | Creature Guidance |
|-----|--------|-------------------|
| < 30 days | Excellent cash machine | "Your cash cycle is lean. You're funding growth from operations." |
| 30–60 days | Healthy | "Solid cycle. Look for ways to tighten DIO without stockouts." |
| 60–90 days | Stretched | "Cash is tied up in the pipeline. Let's identify the bottleneck." |
| > 90 days | Cash trap risk | "Warning: your cash is locked in inventory and receivables. This limits every growth move." |

---

### D&A Schedule Formulas

```
Beginning PP&E (Gross)
+ CapEx
= Ending PP&E (Gross)

Beginning Accumulated Depreciation
+ Depreciation Expense
= Ending Accumulated Depreciation

PP&E (Net) = Gross PP&E - Accumulated Depreciation
```

---

### Debt Schedule Formulas

```
Beginning Debt Balance
+ New Borrowings
- Repayments
= Ending Debt Balance

Interest Expense = Avg Debt Balance × Interest Rate
  (Use beginning balance to avoid circularity, or iterate if circular refs enabled)
```

---

### Retained Earnings Formula

```
Beginning Retained Earnings
+ Net Income (from IS)
+ Stock-Based Compensation (SBC) (from IS)
- Dividends
= Ending Retained Earnings
```

---

### NOL (Net Operating Loss) Schedule Formulas

```
NOL CARRYFORWARD SCHEDULE
  Beginning NOL Balance (Year 1 / Formation = 0)
  + NOL Generated (if EBT < 0, then ABS(EBT), else 0)
  - NOL Utilized (limited by taxable income and utilization cap)
  = Ending NOL Balance

STARTING BALANCE RULE
  For a new business or first modeled period:
    Beginning NOL Balance = 0
    NOL can only increase through realized losses (EBT < 0)
    NOL cannot be created from thin air or assumed

NOL UTILIZATION CALCULATION
  Pre-Tax Income (EBT)
    If EBT > 0:
      NOL Available = Beginning NOL Balance
      Utilization Limit = EBT × 80%  (post-2017 federal limit)
      NOL Utilized = MIN(NOL Available, Utilization Limit)
      Taxable Income = EBT - NOL Utilized
    If EBT ≤ 0:
      NOL Utilized = 0
      Taxable Income = 0
      NOL Generated = ABS(EBT)

TAX CALCULATION WITH NOL
  Taxes Payable = MAX(0, Taxable Income × Tax Rate)
    (Taxes cannot be negative; losses create NOL asset instead)

DEFERRED TAX ASSET (DTA) FOR NOL
  DTA - NOL Carryforward = Ending NOL Balance × Tax Rate
  ΔDTA = Current DTA - Prior DTA
    (Increase in DTA = non-cash benefit on CF)
    (Decrease in DTA = non-cash expense on CF)
```

---

### Income Statement Structure

```
Net Revenue
  Growth %
(-) Cost of Revenue
  % of Net Revenue
────────────────
Gross Profit (= Net Revenue - Cost of Revenue)
  Gross Margin %

(-) S&M
  % of Net Revenue
(-) G&A
  % of Net Revenue
(-) R&D
  % of Net Revenue
(-) D&A
(-) SBC
  % of Net Revenue
────────────────
EBIT
  EBIT Margin %

EBITDA
  EBITDA Margin %

(-) Interest Expense
────────────────
EBT (Pre-Tax Income)
(-) NOL Utilization (from NOL schedule, reduces taxable income)
────────────────
Taxable Income
(-) Taxes (Taxable Income × Tax Rate)
────────────────
Net Income
  Net Income Margin %
```

---

### Balance Sheet Structure

```
ASSETS
  Cash (from CF ending cash)
  Accounts Receivable (from WC)
  Inventory (from WC)
  Total Current Assets

  PP&E, Net (from DA)
  Deferred Tax Asset - NOL (from NOL schedule)
  Total Non-Current Assets
  Total Assets

LIABILITIES
  Accounts Payable (from WC)
  Current Portion of Debt (from Debt)
  Total Current Liabilities

  Long-Term Debt (from Debt)
  Total Liabilities

EQUITY
  Common Stock
  Retained Earnings (from RE schedule)
  Total Equity

CHECK: Assets - Liabilities - Equity = 0
```

---

### Cash Flow Statement Structure

```
CASH FROM OPERATIONS (CFO)
  Net Income (LINK: IS)
  + D&A (LINK: DA schedule)
  + Stock-Based Compensation (SBC) (LINK: IS or Assumptions)
  - ΔDTA (Deferred Tax Asset) (LINK: NOL schedule; increase in DTA = use of cash)
  - ΔAR (LINK: WC)
  - ΔInventory (LINK: WC)
  + ΔAP (LINK: WC)
  = CFO

CASH FROM INVESTING (CFI)
  - CapEx (LINK: DA schedule)
  = CFI

CASH FROM FINANCING (CFF)
  + Debt Issuance (LINK: Debt)
  - Debt Repayment (LINK: Debt)
  + Equity Issuance (LINK: BS Common Stock/APIC)
  - Dividends (LINK: RE schedule)
  = CFF

Net Change in Cash = CFO + CFI + CFF
Beginning Cash
+ Net Change in Cash
= Ending Cash (LINK TO: BS Cash)
```

---

### Check Formulas (Integrity Verification)

```
BS Balance Check:       = Assets - Liabilities - Equity       (must = 0)
Cash Tie-Out:           = BS Cash - CF Ending Cash             (must = 0)
RE Roll-Forward:        = Prior RE + NI + SBC - Div - BS RE   (must = 0)
DTA Tie-Out:            = NOL Schedule DTA - BS DTA            (must = 0)
Equity Raise Tie-Out:   = ΔCommon Stock/APIC - Equity (CFF)   (must = 0)
Year 0 Equity Tie-Out:  = Equity Raised (Yr 0) - Begin Eq (Yr 1)  (must = 0)
Cash Monthly vs Annual: = Closing Cash (Mo) - Closing Cash (Yr)  (must = 0)
NOL Utilization Cap:    = NOL Utilized ≤ EBT × 80%            (must be TRUE)
NOL Non-Negative:       = Ending NOL Balance ≥ 0              (must be TRUE)
NOL Starting Balance:   = Beginning NOL (Year 1) = 0          (must be TRUE)
NOL Accumulation:       = NOL increases only when EBT < 0     (losses generate NOL)
```

---

## How the Creature Uses This Reference

### Conversation Flow After Industry Selection

**Step 1 — Creature Introduction**

Display the Handle the Ski creature image (`assets/handle-the-ski.png`) and introduce:

> "I'm **[Your Magical Creature Name]** — your financial navigator through the Merchant's Bazaar. Before we chart your course, I need to understand your financial terrain."

**Step 2 — Two Paths Offered**

> "I can work with you two ways:
>
> **Option A:** Download my Balance Sheet template, fill in your numbers, and upload it back. I'll auto-calculate everything — your Quick Ratio, Current Ratio, Cash Conversion Cycle, and your full Financial Readiness Score.
>
> **Option B:** Answer three quick questions and I'll calculate your Quick Ratio right now to gauge your immediate liquidity."

**Step 3A — Template Path**

If the CEO chooses the template:
1. Present the template files from `assets/templates/`
2. When they upload back, read the file with openpyxl or CSV parser
3. Extract all balance sheet line items
4. Compute: Quick Ratio, Current Ratio, D/E, Working Capital %, Cash %, Inventory %
5. Compute FRS using the Golden Equilibrium formula
6. Reveal their Magical Creature based on scores

**Step 3B — Quick Ratio Express Path**

If the CEO answers the three questions:
1. Collect: Cash, Accounts Receivable, Current Liabilities
2. Calculate: `Quick Ratio = (Cash + AR) / Current Liabilities`
3. Interpret using the Quick Ratio table above
4. Estimate a preliminary FRS based on Quick Ratio:
   - Quick Ratio > 1.5 → Estimated FRS: 70-85
   - Quick Ratio 1.0-1.5 → Estimated FRS: 50-70
   - Quick Ratio 0.5-1.0 → Estimated FRS: 30-50
   - Quick Ratio < 0.5 → Estimated FRS: 10-30
5. Offer to refine with more questions or the full template

**Step 4 — Bridge to Full Analysis**

After Quick Ratio assessment:
> "Your Quick Ratio gives us a snapshot, but the full Golden Equilibrium requires both your Financial Readiness Score AND your Opportunity Score. Want me to dig deeper into your inventory data next, or shall we connect your live data through Power Ladder?"

---

## FRS ↔ Quick Ratio Integration

The Quick Ratio feeds directly into the **FRS Liquidity component** (40% weight):

```
FRS = 0.40 × Liquidity_avg + 0.30 × Leverage_avg + 0.30 × Cash_avg

Where Liquidity_avg = (Current Ratio score + Quick Ratio score) / 2
  Quick Ratio score = MIN(100, MAX(0, Quick Ratio × 50))
  Current Ratio score = MIN(100, MAX(0, (Current Ratio - 1) × 33.33))
```

This means the Quick Ratio alone contributes **20%** of the total FRS — making it the single fastest diagnostic the creature can perform.

---

## Power Ladder Bridge

> "These formulas power the **sample** Business Play experience. For the **full experience** — with real-time data flowing from your POS, ERP, and accounting systems through the Snowflake Ecosystem — connect with Power Ladder."
>
> **Email:** dithanon@powerladder.tech
> **Website:** https://www.powerladder.net
