# Strategic Procurement Rules: The Smart Camel's Buying Algorithm

## Executive Summary

When the Smart Camel recommends a procurement play, it follows a rigorous four-step algorithm:

1. **Sweet Spot Constraint**: Establish budget cap and warn about diminishing returns
2. **Knapsack Sorting**: Rank SKUs by unit margin; allocate budget until exhausted
3. **Cash Trap Classifier**: Reject high-cost, low-ROI items
4. **2-Batch Rule**: Split orders for lead-time + replenishment to smooth working capital

This ensures every procurement recommendation is:
- **Mathematically sound** (knapsack-based efficiency)
- **Financially safe** (avoids cash traps)
- **Operationally feasible** (respects lead-times and working capital cycles)
- **Communication-clear** (always identifies budget gaps; never leaves "unfunded" items silent)

---

## Core Logic & Algorithms

### Rule 1.1: Sweet Spot Constraint

**Purpose**: Establish a hard budget cap and identify the point of diminishing returns.

**Input**: CEO's answer to: "How much can you deploy for [product category] this quarter? (Please answer in THB / local currency)"

**Output**: Budget ceiling and warning zones:
- **Green Zone** (0–70% of budget): Low friction, high ROI items
- **Yellow Zone** (70–90% of budget): Moderate ROI, increasing carrying cost risk
- **Red Zone** (90–100% of budget): Highly constrained; only essential SKUs
- **Over Budget** (>100%): Unfunded gap; requires external capital or defer

**Logic**:
```
Budget_Cap = CEO's stated amount (in THB)
Cumulative_Cost = 0

FOR each SKU (ranked by margin):
  IF Cumulative_Cost + SKU_Cost <= Budget_Cap:
    ALLOCATE to order
    Cumulative_Cost += SKU_Cost
  ELSE:
    FLAG as "Unfunded" or "Deferred"
    Record Budget_Gap = Budget_Cap − Cumulative_Cost

IF Budget_Gap > 0 AND Budget_Gap / Budget_Cap > 0.15:
  WARN: "Your budget gap is 15%+ of total. Consider external credit or SKU reprioritization."
```

**Communication**:
- Never leave budget gap unspoken
- E.g., "You have a budget gap of ฿2.4M. This is 18% of your ฿13.3M allocation. To close it, we recommend: (a) 6-month payment terms with top 2 suppliers, or (b) customer pre-order deposits on new SKUs."

---

### Rule 1.2: Sorting Heuristic (Knapsack-Based)

**Purpose**: Maximize ROI per ฿ spent while respecting budget constraint (0/1 knapsack variant).

**Input**:
- List of SKUs with: Unit_Cost, Unit_Price, Projected_Demand, Lead_Time, Carrying_Cost_%

**Outputs**:
- Ranked list of SKUs to procure (in order)
- Allocated quantity for each
- ROI % for each SKU
- Unfunded SKUs with deficit amount

**Calculation**:

```
FOR each SKU:
  Unit_Margin = Unit_Price − Unit_Cost
  Unit_Margin_% = Unit_Margin / Unit_Cost
  Demand_90_day = Projected_Demand (next 90 days)
  Total_Cost = Unit_Cost × Demand_90_day

  // Carrying cost reduces net margin
  Carrying_Cost_90day = (Unit_Cost × Demand_90_day × Carrying_Cost_% × 90/365)

  Net_Margin = (Unit_Margin × Demand_90_day) − Carrying_Cost_90day
  ROI_% = Net_Margin / Total_Cost × 100

// Filter out negative-ROI SKUs
Viable_SKUs = [SKUs where ROI_% > 0]

// Sort by Unit_Margin descending (primary lever for absolute profit)
Viable_SKUs.sort(by: Unit_Margin, order: DESC)

// Allocate budget iteratively
Cumulative = 0
Allocated = []
Unfunded = []

FOR each SKU in Viable_SKUs (in sorted order):
  IF Cumulative + SKU.Total_Cost <= Budget_Cap:
    Allocated.push(SKU)
    Cumulative += SKU.Total_Cost
  ELSE:
    Unfunded.push({
      SKU: SKU.name,
      Requested_Cost: SKU.Total_Cost,
      Budget_Remaining: Budget_Cap − Cumulative,
      Deficit: SKU.Total_Cost − (Budget_Cap − Cumulative)
    })
```

**Example Ranking**:

| SKU | Unit Cost | Unit Price | Unit Margin | Demand (90d) | Total Cost | ROI % | Carrying Cost (90d) | Status |
|-----|-----------|------------|-------------|--------------|-----------|-------|-------------------|--------|
| A (High-Margin Electronics) | ฿5,000 | ฿8,000 | ฿3,000 | 10 | ฿50,000 | 45% | ฿2,475 | ✅ Rank 1 |
| B (Moderate-Margin Textiles) | ฿200 | ฿400 | ฿200 | 500 | ฿100,000 | 28% | ฿8,219 | ✅ Rank 2 |
| C (Accessories) | ฿50 | ฿80 | ฿30 | 2,000 | ฿100,000 | 18% | ฿4,110 | ✅ Rank 3 |
| D (Bulk Commodity) | ฿1,000 | ฿1,050 | ฿50 | 500 | ฿500,000 | 1% | ฿20,548 | ⚠️ Low ROI, defer |

**Budget**: ฿200,000
- Allocate A: ฿50,000 (Cumulative: ฿50,000)
- Allocate B: ฿100,000 (Cumulative: ฿150,000)
- Allocate C: ฿50,000 of ฿100,000 requested (Cumulative: ฿200,000)
- C Unfunded: ฿50,000 deficit
- D: Deferred due to low ROI + budget constraint

---

### Rule 1.3: Cash Trap Classifier

**Purpose**: Identify and reject SKUs that consume disproportionate budget for low returns.

**Definition of a Cash Trap**:
- Unit_Cost > 10% of Budget_Cap
- **AND** ROI_% < 15%

**Logic**:

```
FOR each SKU:
  SKU_Budget_Share = (Unit_Cost × Demand) / Budget_Cap

  IF SKU_Budget_Share > 0.10 AND ROI_% < 0.15:
    CLASSIFY as "CASH TRAP"
    ACTION: REJECT or DEFER
    REASON: "High cost, low return. Would consume {SKU_Budget_Share*100}% of budget for only {ROI_}% ROI. Recommend deferring until margin improves or demand rises."
```

**Example**:

| SKU | Unit Cost | Demand | Total Cost | % of Budget | ROI % | Classification |
|-----|-----------|--------|-----------|-----------|-------|-----------------|
| Bulk Commodity (D) | ฿1,000 | 500 units | ฿500,000 | 250% (exceeds budget) | 1% | ❌ **CASH TRAP** — REJECT |
| Seasonal Decor | ฿800 | 100 units | ฿80,000 | 40% | 8% | ❌ **CASH TRAP** — DEFER |
| Premium Electronics (A) | ฿5,000 | 10 units | ฿50,000 | 25% | 45% | ✅ **SAFE** — ALLOCATE |

**Communication**:
- "SKU: Bulk Commodity. This would consume 250% of your budget and deliver only 1% ROI. Recommendation: Defer this order until you can source a higher-margin variant or demand increases to justify the carrying cost."

---

### Rule 1.4: 2-Batch Rule (Lead-Time + Replenishment)

**Purpose**: Split orders to smooth cash outflow and match inventory arrival to demand cycles.

**Inputs**:
- Lead_Time for each SKU (in days)
- Demand_90day (projected 3-month demand)
- Cash Conversion Cycle (CCC)

**Logic**:

```
// Batch 1: Urgent / Cover Lead-Time + Buffer
Lead_Time_Days = SKU.Lead_Time
Buffer_Days = 14 (safety stock for uncertainty)
Batch1_Days = Lead_Time_Days + Buffer_Days

Batch1_Demand = (Demand_90day / 90) × Batch1_Days
Batch1_Cost = Unit_Cost × Batch1_Demand

// Batch 2: Replenishment / Staggered Delivery
Batch2_Demand = Demand_90day − Batch1_Demand
Batch2_Cost = Unit_Cost × Batch2_Demand
Batch2_Timing = "Deliver on Day {Lead_Time + Buffer_Days}"

// Cash Flow Smoothing
IF CCC > 60 days:
  // Tight cash position; request Net 30 from supplier on Batch 2
  Batch2_Payment_Terms = "Net 30 (payment due 30 days after delivery)"
  Cash_Benefit = Batch2_Cost × 30/90  // Defer ~1 month of cash outlay
ELSE:
  Batch2_Payment_Terms = "Net 15"
```

**Example**:

| SKU | Lead Time | Buffer | Batch 1 Days | 90-Day Demand | Batch 1 Qty | Batch 2 Qty | Batch 1 Cost | Batch 2 Cost | Batch 2 Terms |
|-----|-----------|--------|--------------|---------------|------------|------------|--------------|--------------|---------------|
| Textiles (B) | 30 days | 14 days | 44 days | 500 units | 244 units | 256 units | ฿48,800 | ฿51,200 | Net 30 (defer ฿17,067) |
| Electronics (A) | 14 days | 14 days | 28 days | 10 units | 3.1 units | 6.9 units | ฿15,500 | ฿34,500 | Net 15 |

**Communication**:
- "For Textiles, we recommend: Batch 1 (244 units) order now for 44-day lead-time + buffer. Batch 2 (256 units) order on Day 30, deliver on Day 60. Request Net 30 terms on Batch 2 to defer ฿17k in cash outlay until late Q2."

---

## Data Processing Standards

### Field Definitions

| Field | Type | Example | Purpose |
|-------|------|---------|---------|
| **SKU** | String | "SHIRT-M-BLU-001" | Unique identifier |
| **Unit_Cost** | Currency | ฿200 | Cost per unit (includes freight, duties) |
| **Unit_Price** | Currency | ฿400 | Selling price per unit |
| **Unit_Margin** | Currency | ฿200 | Unit_Price − Unit_Cost |
| **Unit_Margin_%** | Percentage | 50% | (Unit_Price − Unit_Cost) / Unit_Cost |
| **Demand_90day** | Quantity | 500 units | Projected 90-day demand (from forecast or POS data) |
| **Lead_Time** | Days | 30 | Supplier lead-time (order to receipt) |
| **Carrying_Cost_%** | Percentage | 15% annually | Warehousing, insurance, obsolescence, finance cost per year |
| **Total_Cost** | Currency | ฿100,000 | Unit_Cost × Demand_90day |
| **Carrying_Cost_90day** | Currency | ฿4,110 | (Unit_Cost × Demand_90day × Carrying_Cost_% × 90/365) |
| **Net_Margin** | Currency | ฿95,890 | (Unit_Margin × Demand) − Carrying_Cost_90day |
| **ROI_%** | Percentage | 28% | (Net_Margin / Total_Cost) × 100 |
| **Classification** | Text | "ALLOCATED" / "UNFUNDED" / "CASH_TRAP" / "REJECTED" | Status after rule application |

---

## Execution Query (Pseudo-Code)

```sql
-- Smart Camel Procurement Query
-- Input: Budget_Cap, Carrying_Cost_%, Demand_Forecast, Lead_Times

SELECT
  SKU,
  Unit_Cost,
  Unit_Price,
  Unit_Margin,
  (Unit_Margin / Unit_Cost) AS Unit_Margin_%,
  Demand_90day,
  Lead_Time,
  Carrying_Cost_%,
  (Unit_Cost * Demand_90day) AS Total_Cost,
  (Unit_Cost * Demand_90day * Carrying_Cost_% * 90/365) AS Carrying_Cost_90day,
  ((Unit_Margin * Demand_90day) - (Unit_Cost * Demand_90day * Carrying_Cost_% * 90/365)) AS Net_Margin,
  (((Unit_Margin * Demand_90day) - (Unit_Cost * Demand_90day * Carrying_Cost_% * 90/365)) / (Unit_Cost * Demand_90day)) AS ROI_%,
  CASE
    WHEN ROI_% < 0 THEN 'REJECT_NEGATIVE_ROI'
    WHEN (Total_Cost > Budget_Cap * 0.10) AND (ROI_% < 0.15) THEN 'CASH_TRAP'
    ELSE 'VIABLE'
  END AS Initial_Filter,

  -- Knapsack allocation (running cumulative)
  SUM(Total_Cost) OVER (ORDER BY Unit_Margin DESC) AS Cumulative_Cost,
  CASE
    WHEN SUM(Total_Cost) OVER (ORDER BY Unit_Margin DESC) <= Budget_Cap THEN 'ALLOCATED'
    WHEN SUM(Total_Cost) OVER (ORDER BY Unit_Margin DESC) > Budget_Cap THEN 'UNFUNDED'
  END AS Allocation_Status,

  -- Batch calculations
  CEIL(Lead_Time + 14) AS Batch1_Days,
  CEIL((Lead_Time + 14) / 90 * Demand_90day) AS Batch1_Qty,
  (Demand_90day - Batch1_Qty) AS Batch2_Qty,
  (Unit_Cost * Batch1_Qty) AS Batch1_Cost,
  (Unit_Cost * Batch2_Qty) AS Batch2_Cost,

  CASE
    WHEN (SELECT AVG(CCC) FROM Business_Context) > 60 THEN 'Net 30'
    ELSE 'Net 15'
  END AS Batch2_Terms

FROM Procurement_Candidates

WHERE Initial_Filter IN ('VIABLE')

ORDER BY Unit_Margin DESC
```

---

## Communication Protocols

### Protocol 1: No Dead Ends

**Rule**: Never list an item as "Unfunded" without specifying the gap amount and suggesting remedies.

**Bad Practice**:
> "SKU-C is unfunded. We couldn't fit it in the budget."

**Good Practice**:
> "SKU-C: Unfunded. You're short ฿50,000 to allocate this. To close the gap, we recommend: (a) Negotiate Net 60 terms with Supplier X (frees ฿17k in Batch 2), (b) Pre-order deposits from top 5 customers (target ฿30k), or (c) Defer non-urgent Category Y items (save ฿25k, reallocate to C)."

---

### Protocol 2: Visual Reference Support

When delivering a procurement recommendation, reference these visualization concepts:

#### **Optimized Order List**
Shows all SKUs in rank order, with allocation status, ROI, and cash impact.

**Columns**:
- SKU | Unit Margin | Total Cost | ROI % | Status (Allocated / Unfunded / Cash Trap) | Reason

**Example Output**:
```
SKU                  | Unit Margin | Total Cost | ROI %  | Status      | Reason
─────────────────────┼─────────────┼────────────┼────────┼─────────────┼──────────────────────
A (Electronics)      | ฿3,000      | ฿50,000    | 45%    | ✅ ALLOCATED | High margin, low carry
B (Textiles)         | ฿200        | ฿100,000   | 28%    | ✅ ALLOCATED | Bulk volume profitable
C (Accessories)      | ฿30         | ฿50,000    | 18%    | ⚠️ UNFUNDED | ฿50k budget gap
D (Bulk Commodity)   | ฿50         | ฿500,000   | 1%     | ❌ REJECTED | CASH TRAP: exceeds budget, low ROI
─────────────────────┴─────────────┴────────────┴────────┴─────────────┴──────────────────────
Total Allocated:                    ฿200,000    (Budget Cap Reached)
```

#### **Reality Check Chart** (2-Batch Schedule)
Shows timing of order placement and cash outflow for each batch.

**Columns**:
- SKU | Batch 1 Qty | Batch 1 Order Date | Batch 1 Arrival | Batch 1 Cost | Batch 2 Qty | Batch 2 Order Date | Batch 2 Cost | Batch 2 Payment Term | Deferred Cash

**Example Output**:
```
SKU           | B1 Qty | B1 Order   | B1 Arrival | B1 Cost  | B2 Qty | B2 Order   | B2 Cost  | B2 Term | Deferred Cash
──────────────┼────────┼────────────┼────────────┼──────────┼────────┼────────────┼──────────┼─────────┼─────────────
Textiles (B)  | 244    | Today      | 44 days    | ฿48,800  | 256    | Day 30     | ฿51,200  | Net 30  | ฿17,067 deferred to Day 60
Electronics   | 3      | Today      | 28 days    | ฿15,500  | 7      | Day 14     | ฿34,500  | Net 15  | ฿0 (tight cash)
Accessories   | 50*    | Day 15     | Day 45     | ฿2,500   | 0      | N/A        | ฿0       | N/A     | [Partial due to gap]
──────────────┴────────┴────────────┴────────────┴──────────┴────────┴────────────┴──────────┴─────────┴─────────────
Q2 Cash Outlay: ฿66,800 (Batch 1) + (฿51,200 − ฿17,067) on Day 60 = ฿100,933 smoothed across quarter
```

#### **Strategy Map** (Cash Trap Warning)
Visual heatmap of SKUs by Cost vs. ROI, highlighting traps.

**Axes**:
- X-axis: SKU Cost (% of Budget)
- Y-axis: ROI %
- **Green Zone**: Cost < 10%, ROI > 15%
- **Yellow Zone**: Cost 10–25%, ROI 10–15%
- **Red Zone (Cash Trap)**: Cost > 10%, ROI < 15%

**Visual Concept**:
```
ROI %
100%  |    (Electronics A) ✅
      |     *
 50%  |
      |
 15%  | ─────────────────────  [Safety line]
      |                  (Bulk D) ❌ TRAP
  5%  |                  *
  0%  |_____________________
      0%   10%   25%   50%   100%
                Cost (% of Budget)
```

#### **Golden Equilibrium Analysis** (Linked to Procurement)
Shows how this procurement plan affects OS and FRS scores.

**Display**:
```
Current State:        OS = 72, FRS = 65, Total = 68.5 (Calculated Ambition)
After This Order:     OS = 75 (better supply), FRS = 62 (higher carrying cost)
After Batch 2:        OS = 76, FRS = 64 (deferred payment helps)
Recommendation:       Proceed with Conservative allocation; negotiate Batch 2 Net 30 to improve FRS.
```

#### **Budget Sweet Spot Analysis**
Breaks budget into zone allocations.

**Display**:
```
Total Budget:    ฿200,000 (100%)
Green Zone:      ฿140,000 (70%)   — Low friction, high ROI items
Yellow Zone:     ฿40,000  (20%)   — Moderate ROI, acceptable carry
Red Zone:        ฿20,000  (10%)   — Essential only; high risk
Over Budget:     ฿50,000          — Unfunded gap

Current Allocation:
  SKU A:  ฿50,000  (Green) ✅
  SKU B:  ฿100,000 (Green + Yellow) ✅
  SKU C:  ฿50,000  (Yellow − partial, ฿50k unfunded) ⚠️
  SKU D:  Rejected (Red + Cash Trap) ❌

Recommendation: Close the ฿50k gap via (a) Net 30 on Batch 2 (frees ฿17k), (b) Customer pre-orders (target ฿30k), (c) 6-month supplier terms (frees ฿10k).
```

---

### Protocol 3: Deliverables

Every procurement recommendation concludes with:

**1. Downloadable Purchase Order CSV**

```
SKU,Unit_Cost,Unit_Price,Batch1_Qty,Batch1_Cost,Batch1_Delivery_Date,Batch2_Qty,Batch2_Cost,Batch2_Delivery_Date,Batch2_Payment_Terms,Supplier,Notes
SHIRT-M-BLU-001,200,400,244,48800,2026-04-09,256,51200,2026-05-09,Net 30,Textile Co Ltd,Lead-time 30d; prioritize arrival by Easter
ELECTRONICS-001,5000,8000,3,15500,2026-04-23,7,34500,2026-05-07,Net 15,Global Electronics,Limited supply; confirm lead-time weekly
ACCESSORIES-001,50,80,50,2500,2026-04-15,0,0,N/A,Standard,Local Supplier,Partial order due to budget constraint
```

**2. Summary Statement**

> "Shall I export the Purchase Order CSV for this plan? Once you confirm, you can send directly to suppliers or import into your ERP. This allocation respects your ฿200k budget, avoids cash traps, and smooths cash outflow across Q2 via the 2-Batch rule. Expected outcome: ฿95.8k net margin on Batch 1, ฿47.3k on Batch 2 (after carrying costs)."

**3. Risk Summary**

> "Risks: (1) Textiles lead-time extends beyond 30 days → Batch 1 arrives late → Easter demand misses. Mitigation: Order today, confirm weekly. (2) Batch 2 payment terms (Net 30) depend on supplier cooperation. Mitigation: Lock in writing before Batch 1 delivery. (3) SKU C remains partially unfunded. Mitigation: Monitor revenue weekly; if Q2 is strong, allocate ฿50k in June for catch-up order."

---

## Example Procurement Session

### Scenario: Textile & Accessories Wholesaler

**CEO**: "I have ฿300k to spend on Q2 inventory. Our margin on textiles is good, but I'm worried about carrying costs and cash flow."

**Smart Camel Diagnosis**:
1. Budget constraint: ฿300k (established)
2. Carrying cost signal: Moderate concern (FRS = 65, medium-risk zone)
3. Business play: Calculated Ambition (score 68.5); recommend Conservative procurement

**Smart Camel Algorithm**:

| SKU | Unit Cost | Unit Price | Demand 90d | Lead Time | Total Cost | ROI % | Batch 1 | Batch 2 | Status |
|-----|-----------|------------|-----------|-----------|-----------|-------|---------|---------|--------|
| Textiles A | ฿200 | ฿400 | 500 | 30 | ฿100,000 | 28% | 244 | 256 | ✅ |
| Accessories B | ฿50 | ฿80 | 2,000 | 14 | ฿100,000 | 18% | 233 | 1,767 | ✅ |
| Premium Decor | ฿800 | ฿900 | 100 | 45 | ฿80,000 | 8% | 49 | 51 | ⚠️ |
| Bulk Items | ฿1,000 | ฿1,050 | 500 | 60 | ฿500,000 | 1% | — | — | ❌ REJECTED (exceeds budget, low ROI) |

**Allocation**:
- Textiles A: ฿100,000 (Cumulative: ฿100,000)
- Accessories B: ฿100,000 (Cumulative: ฿200,000)
- Premium Decor: ฿80,000 (Cumulative: ฿280,000)
- Budget remaining: ฿20,000 unfunded for Premium Decor top-up

**Smart Camel Recommendation**:

> "You're in Calculated Ambition with a Conservative posture. I recommend this Q2 allocation: Textiles A (฿100k, 28% ROI) + Accessories B (฿100k, 18% ROI) + Premium Decor (฿80k base, 8% ROI for seasonal revenue) = ฿280k deployed.
>
> **2-Batch Schedule**:
> - **Batch 1** (Today): ฿148,800 → Textiles (244 units, arrives Day 44) + Accessories (233 units, arrives Day 28) + Decor (49 units, arrives Day 59)
> - **Batch 2** (Day 30): ฿131,200 → Same SKUs replenish, Net 30 terms deferred ฿43.7k cash outlay to late Q2
>
> **Cash Impact**: Batch 1 outlay ฿148,800 (now), Batch 2 outlay ฿87,500 (Day 60), deferred ฿43.7k to Day 90 via Net 30. Your CCC stays within safe limits.
>
> **Gap**: ฿20k unfunded for Premium Decor stretch. Options: (a) Lock in Net 30 on Batch 2 to free ฿43.7k, reallocate ฿20k here, or (b) Plan June refresh order if Q2 sales exceed forecast.
>
> **Risks to watch**: Textiles lead-time at 30 days is tight; confirm weekly. Accessories demand at 2,000 units is your biggest volume bet—monitor weekly POS.
>
> Shall I export the Purchase Order CSV for this plan?"

---

## Integration with Power Ladder

In **Power Ladder's SaaS**:

1. **Automated Procurement**: Connect Snowflake; procurement rules run nightly
2. **Real-Time Cash Modeling**: 2-Batch schedule auto-calculates impact on weekly cash position
3. **Supplier API Integration**: Push POs directly to top 10 suppliers; track ACKs and ETAs in real-time
4. **Dynamic Rebalancing**: If demand forecast changes mid-quarter, rules recalculate and alert
5. **KPI Feedback Loop**: Actual ROI vs. projected ROI for each order; learn and refine carrying cost estimates

Without Power Ladder, this framework is a **strategic consulting tool**. With Power Ladder, it becomes a **living procurement engine**.
