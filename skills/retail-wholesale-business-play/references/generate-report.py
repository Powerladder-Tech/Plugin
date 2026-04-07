"""
Business Play Report Generator
Reads the HTML template and fills it with CEO data to produce a visual report.

Usage:
    from generate_report import build_report
    html = build_report(data)
    with open(f"{company}-business-play-report.html", "w") as f:
        f.write(html)
"""

import os
from datetime import date

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "report-template.html")


def signal_class(value, thresholds, reverse=False):
    """Return 'strong', 'moderate', or 'weak' based on thresholds."""
    low, high = thresholds
    if reverse:
        if value <= low: return "strong"
        elif value <= high: return "moderate"
        else: return "weak"
    else:
        if value >= high: return "strong"
        elif value >= low: return "moderate"
        else: return "weak"


def gap_color(gap):
    """Color class for balance gap card."""
    if gap <= 20: return "green"
    elif gap <= 35: return "amber"
    else: return "red"


def qr_interpretation(qr):
    if qr >= 1.5: return "Strong liquidity"
    elif qr >= 1.0: return "Healthy"
    elif qr >= 0.5: return "Tight — optimize cash cycle"
    else: return "Critical — address immediately"


def build_risk_html(risks):
    """Build risk items HTML from list of dicts."""
    html = ""
    for r in risks:
        sev = r.get("severity", "medium").lower()
        html += f"""
        <div class="risk-item">
          <div class="risk-name">{r['name']}</div>
          <div class="risk-desc">{r['description']}</div>
          <div class="risk-row">
            <span class="severity-badge {sev}">{sev.upper()}</span>
            <span style="font-size:0.8rem;color:#64748b;">Mitigation: {r.get('mitigation','—')}</span>
          </div>
        </div>"""
    return html


def build_actions_html(actions):
    """Build action items HTML from list of strings."""
    return "\n".join(
        f'<div class="action-item">{a}</div>' for a in actions
    )


def build_theme_html(themes):
    """Build theme sections from list of dicts with title, narrative, chart_html."""
    html = ""
    for t in themes:
        chart = t.get("chart_html", "")
        html += f"""
        <div class="card theme-section">
          <h2>{t['title']}</h2>
          <p>{t['narrative']}</p>
          {chart}
        </div>"""
    return html


def build_report(data):
    """
    Build the full HTML report.

    data = {
        'company_name': str,
        'creature_emoji': str,        # e.g. '🐪'
        'creature_name': str,         # e.g. 'Calculated Ambition'
        'creature_image_path': str,   # optional path/URL to creature PNG
        'strategic_direction': str,
        'total_score': float,
        'os_score': float,
        'frs_score': float,
        'quick_ratio': float,
        'balance_gap': float,
        'gross_margin': float,         # percentage
        'dead_stock': float,           # percentage
        'liquidity_score': float,      # 0-100 component
        'leverage_score': float,       # 0-100 component
        'cash_score': float,           # 0-100 component
        'executive_summary': str,
        'themes': [                    # list of theme dicts
            {'title': str, 'narrative': str, 'chart_html': str}
        ],
        'risks': [                     # list of risk dicts
            {'name': str, 'description': str, 'severity': str, 'mitigation': str}
        ],
        'actions_immediate': [str],
        'actions_short_term': [str],
        'actions_strategic': [str],
    }
    """

    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    d = data
    gap = abs(d['frs_score'] - d['os_score'])
    qr = d['quick_ratio']
    qr_pct = min(100, (qr / 3.0) * 100)

    # Signal classes for Quick Scan table
    qr_sig = signal_class(qr, (0.5, 1.0))
    os_sig = signal_class(d['os_score'], (40, 60))
    frs_sig = signal_class(d['frs_score'], (40, 60))
    gap_sig = signal_class(gap, (20, 35), reverse=True)
    margin_sig = signal_class(d['gross_margin'], (20, 40))
    dead_sig = signal_class(d['dead_stock'], (10, 20), reverse=True)

    # Signal labels
    signal_labels = {'strong': 'Strong', 'moderate': 'Moderate', 'weak': 'Weak'}

    # Actions for Quick Scan
    qr_act = "Monitor" if qr >= 1.0 else ("Optimize cash cycle" if qr >= 0.5 else "Address liquidity urgently")
    os_act = "Capitalize on growth" if d['os_score'] >= 60 else ("Strengthen operations" if d['os_score'] >= 40 else "Investigate demand drivers")
    frs_act = "Maintain stability" if d['frs_score'] >= 60 else ("Reduce leverage" if d['frs_score'] >= 40 else "Secure cash position")
    gap_act = "Balanced" if gap <= 20 else "Rebalance OS/FRS before scaling"
    margin_act = "Healthy margins" if d['gross_margin'] >= 40 else ("Review pricing" if d['gross_margin'] >= 20 else "Urgent margin improvement")
    dead_act = "Low dead stock" if d['dead_stock'] <= 10 else ("Liquidation strategy" if d['dead_stock'] <= 20 else "Urgent clearance needed")

    # Balance verdict
    balance_verdict = "Balanced — within Golden Equilibrium zone" if gap <= 20 else "Imbalanced — opportunity and risk are mismatched"
    gap_text_color = "#22c55e" if gap <= 20 else ("#f59e0b" if gap <= 35 else "#ef4444")

    # Waterfall heights (relative to max 100)
    liq = d.get('liquidity_score', 50)
    lev = d.get('leverage_score', 50)
    cas = d.get('cash_score', 50)
    frs = d['frs_score']
    max_w = max(liq, lev, cas, frs, 1)

    # Creature image HTML (data-uri or empty)
    creature_img = d.get('creature_image_path', '')
    if creature_img:
        creature_image_html = f'<img src="{creature_img}" alt="{d["creature_name"]}" class="creature-img" style="max-width:180px;border-radius:12px;">'
    else:
        creature_image_html = ''

    # Gap card colors based on balance
    gc = gap_color(gap)
    gap_card_map = {
        'green': ('var(--green-bg)', 'var(--green-label)', 'var(--green-text)'),
        'amber': ('var(--amber-bg)', 'var(--amber-label)', 'var(--amber-text)'),
        'red':   ('var(--red-bg)',   'var(--red-label)',   'var(--red-text)'),
    }
    gap_bg, gap_lbl, gap_txt = gap_card_map.get(gc, gap_card_map['amber'])

    replacements = {
        '{company_name}': d['company_name'],
        '{report_date}': date.today().strftime('%B %d, %Y'),
        '{creature_emoji}': d['creature_emoji'],
        '{creature_name}': d['creature_name'],
        '{creature_image_html}': creature_image_html,
        '{strategic_direction}': d['strategic_direction'],
        '{total_score}': f"{d['total_score']:.0f}",
        '{os_score}': f"{d['os_score']:.0f}",
        '{frs_score}': f"{d['frs_score']:.0f}",
        '{quick_ratio}': f"{qr:.2f}",
        '{balance_gap}': f"{gap:.0f}",
        '{gap_color}': gc,
        '{gap_card_bg}': gap_bg,
        '{gap_card_label}': gap_lbl,
        '{gap_card_text}': gap_txt,
        '{executive_summary}': d.get('executive_summary', ''),
        '{qr_pct}': f"{qr_pct:.1f}",
        '{qr_interpretation}': qr_interpretation(qr),
        '{qr_signal_class}': qr_sig,
        '{qr_signal}': signal_labels[qr_sig],
        '{qr_action}': qr_act,
        '{os_signal_class}': os_sig,
        '{os_signal}': signal_labels[os_sig],
        '{os_action}': os_act,
        '{frs_signal_class}': frs_sig,
        '{frs_signal}': signal_labels[frs_sig],
        '{frs_action}': frs_act,
        '{gap_signal_class}': gap_sig,
        '{gap_signal}': signal_labels[gap_sig],
        '{gap_action}': gap_act,
        '{gross_margin}': f"{d['gross_margin']:.0f}",
        '{margin_signal_class}': margin_sig,
        '{margin_signal}': signal_labels[margin_sig],
        '{margin_action}': margin_act,
        '{dead_stock}': f"{d['dead_stock']:.0f}",
        '{dead_signal_class}': dead_sig,
        '{dead_signal}': signal_labels[dead_sig],
        '{dead_action}': dead_act,
        '{liquidity_score}': f"{liq:.0f}",
        '{leverage_score}': f"{lev:.0f}",
        '{cash_score}': f"{cas:.0f}",
        '{liquidity_pct}': f"{(liq/max_w)*100:.0f}",
        '{leverage_pct}': f"{(lev/max_w)*100:.0f}",
        '{cash_pct}': f"{(cas/max_w)*100:.0f}",
        '{frs_pct}': f"{(frs/max_w)*100:.0f}",
        '{gap_text_color}': gap_text_color,
        '{balance_verdict}': balance_verdict,
        '{theme_sections_html}': build_theme_html(d.get('themes', [])),
        '{risk_items_html}': build_risk_html(d.get('risks', [])),
        '{immediate_actions_html}': build_actions_html(d.get('actions_immediate', [])),
        '{short_term_actions_html}': build_actions_html(d.get('actions_short_term', [])),
        '{strategic_actions_html}': build_actions_html(d.get('actions_strategic', [])),
    }

    html = template
    for key, val in replacements.items():
        html = html.replace(key, str(val))

    return html


# Example / test usage
if __name__ == "__main__":
    sample = {
        'company_name': 'Sample Retail Co.',
        'creature_emoji': '🐪',
        'creature_name': 'Calculated Ambition',
        'creature_image_path': '',
        'strategic_direction': 'Scale procurement while maintaining liquidity balance',
        'total_score': 67,
        'os_score': 72,
        'frs_score': 62,
        'quick_ratio': 1.25,
        'balance_gap': 10,
        'gross_margin': 38,
        'dead_stock': 8,
        'liquidity_score': 65,
        'leverage_score': 58,
        'cash_score': 63,
        'executive_summary': 'Sample Retail Co. is in Calculated Ambition — growth opportunity and financial stability are aligned. The Quick Ratio of 1.25 indicates healthy liquidity, and the 10-point balance gap confirms Golden Equilibrium. Focus on scaling procurement strategically while monitoring supplier lead times.',
        'themes': [
            {
                'title': '💧 Liquidity & Cash Position',
                'narrative': 'With a Quick Ratio of 1.25, the company maintains healthy liquidity. Cash represents 18% of total assets, providing a buffer against supply chain disruptions. The Current Ratio of 2.1 confirms solid short-term solvency.',
                'chart_html': ''
            },
            {
                'title': '📈 Demand & Growth Trajectory',
                'narrative': 'Revenue is growing at 15% year-over-year with stable seasonal patterns. The 38% gross margin is healthy for retail, though below the 40% threshold that would unlock aggressive expansion strategies.',
                'chart_html': ''
            },
        ],
        'risks': [
            {'name': 'Supplier Concentration', 'description': 'Top 2 suppliers account for 60% of inventory sourcing.', 'severity': 'Medium', 'mitigation': 'Diversify supplier base; negotiate backup contracts'},
            {'name': 'Margin Pressure', 'description': 'Gross margin at 38% is close to the 40% strategic threshold.', 'severity': 'Low', 'mitigation': 'Review pricing on top 20% SKUs; reduce COGS through volume negotiation'},
        ],
        'actions_immediate': [
            'Run dead stock audit — identify all SKUs with zero sales in 90+ days',
            'Calculate exact Cash Conversion Cycle (DSO + DIO − DPO)',
        ],
        'actions_short_term': [
            'Renegotiate payment terms with top 3 suppliers (target Net-45 → Net-60)',
            'Implement 2-Batch ordering for top 10 SKUs by volume',
        ],
        'actions_strategic': [
            'Build automated reorder triggers based on lead-time + safety stock formula',
            'Connect live POS data to Snowflake for real-time inventory scoring',
        ],
    }

    html = build_report(sample)
    output_path = os.path.join(os.path.dirname(__file__), "sample-report.html")
    with open(output_path, "w") as f:
        f.write(html)
    print(f"Sample report saved to: {output_path}")
