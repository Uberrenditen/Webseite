import yfinance as yf

# ==============================================================================
# 1. LIVE-DATEN FÜR DEN TICKER HOLEN
# ==============================================================================
market_symbols = {
    'DAX': '^GDAXI', 'MDAX': '^MDAXI', 'S&P 500': '^GSPC', 'US Tech 100': '^NDX',
    'Gold': 'GC=F', 'Bitcoin': 'BTC-USD'
}

ticker_html_cards = ""

for name, sym in market_symbols.items():
    try:
        t_data = yf.Ticker(sym).history(period='2d')
        if not t_data.empty and len(t_data) >= 1:
            current_price = t_data['Close'].iloc[-1]
            change_pct = ((current_price - t_data['Close'].iloc[-2]) / t_data['Close'].iloc[-2]) * 100 if len(t_data) >= 2 else 0.0

            if any(k in name for k in ['Gold', 'Bitcoin', 'Tech', 'S&P']):
                suffix = " USD"
            else:
                suffix = ""
            
            price_str = f"{current_price:,.2f}{suffix}".replace(",", "X").replace(".", ",").replace("X", ".")
            color_class = "pos" if change_pct >= 0 else "neg"
            sign = "+" if change_pct >= 0 else ""
            
            ticker_html_cards += f"""
            <div class="market-card">
                <span class="market-name">{name}</span>
                <span class="market-price">{price_str}</span>
                <span class="market-change {color_class}">{sign}{change_pct:.2f}%</span>
            </div>
            """
    except Exception as e:
        print(f"Fehler bei {name}: {e}")


# ==============================================================================
# 2. MOCK-DATEN FÜR SUPERINVESTOREN (DATAROMA-STYLE)
# ==============================================================================
# Diese Daten werden später idealerweise aus einer Datenbank oder einem SEC-Scraper geladen
investors = [
    {"name": "Warren Buffett", "company": "Berkshire Hathaway", "value": "$ 284.1 B", "holdings": 41, "top_stock": "Apple Inc. (AAPL)"},
    {"name": "Mohnish Pabrai", "company": "Pabrai Funds", "value": "$ 185.4 M", "holdings": 5, "top_stock": "Alpha Metallurgical (AMR)"},
    {"name": "Li Lu", "company": "Himalaya Capital", "value": "$ 2.1 B", "holdings": 6, "top_stock": "Bank of America (BAC)"},
    {"name": "Guy Spier", "company": "Aquamarine Capital", "value": "$ 142.3 M", "holdings": 12, "top_stock": "American Express (AXP)"},
    {"name": "Michael Burry", "company": "Scion Asset Mgmt.", "value": "$ 94.5 M", "holdings": 18, "top_stock": "Alibaba Group (BABA)"},
    {"name": "Bill Gates", "company": "Gates Foundation", "value": "$ 42.6 B", "holdings": 24, "top_stock": "Microsoft Corp (MSFT)"},
]

recent_activity = [
    {"investor": "Warren Buffett", "action": "Buy", "stock": "Chubb Ltd (CB)", "portfolio_pct": "1.4%", "type_class": "pos"},
    {"investor": "Michael Burry", "action": "Buy", "stock": "Baidu Inc (BIDU)", "portfolio_pct": "4.2%", "type_class": "pos"},
    {"investor": "Li Lu", "action": "Reduce", "stock": "Apple Inc (AAPL)", "portfolio_pct": "-2.1%", "type_class": "neg"},
    {"investor": "Guy Spier", "action": "Buy", "stock": "Ferrari N.V. (RACE)", "portfolio_pct": "0.8%", "type_class": "pos"},
    {"investor": "Mohnish Pabrai", "action": "Sell", "stock": "Valaris Ltd (VAL)", "portfolio_pct": "Kpl. Verkauf", "type_class": "neg"},
]

# HTML für Investoren-Grid generieren
investor_html_cards = ""
for inv in investors:
    investor_html_cards += f"""
    <div class="investor-card">
        <h3>{inv['name']}</h3>
        <p class="company">{inv['company']}</p>
        <div class="inv-details">
            <div><span>Portfolio-Wert:</span> <strong>{inv['value']}</strong></div>
            <div><span>Positionen:</span> <strong>{inv['holdings']}</strong></div>
            <div><span>Größte Position:</span> <strong style="color: #00ff88;">{inv['top_stock']}</strong></div>
        </div>
        <a href="#" class="view-btn">Portfolio ansehen</a>
    </div>
    """

# HTML für Aktivitäts-Tabelle generieren
activity_html_rows = ""
for act in recent_activity:
    action_label = "Kauf" if act['action'] == "Buy" else ("Verkauf" if act['action'] == "Sell" else "Reduziert")
    activity_html_rows += f"""
    <tr>
        <td><strong>{act['investor']}</strong></td>
        <td><span class="badge {act['type_class']}">{action_label}</span></td>
        <td>{act['stock']}</td>
        <td class="{act['type_class']}">{act['portfolio_pct']}</td>
    </tr>
    """

# ==============================================================================
# 3. DAS HTML-LAYOUT (FINALES DASHBOARD)
# ==============================================================================
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Überrenditen.de - Superinvestor Tracker</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #0b0e14;
            color: #ffffff;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}
        header {{
            background-color: #151a24;
            padding: 15px 20px;
            border-bottom: 1px solid #1f2633;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        header h1 {{ margin: 0; color: #00ff88; font-size: 22px; letter-spacing: 1px; }}
        header nav a {{ color: #8f9cae; text-decoration: none; margin-left: 20px; font-size: 14px; }}
        header nav a:hover {{ color: #00ff88; }}
        
        /* UNENDLICHER TICKER STRIP */
        .ticker-wrapper {{
            background-color: #0e121a;
            border-bottom: 1px solid #1f2633;
            overflow: hidden;
            display: flex;
            padding: 8px 0;
        }}
        .ticker-track {{
            display: flex;
            width: max-content;
            animation: scroll-left 35s linear infinite;
        }}
        .market-card {{
            display: flex;
            align-items: center;
            background-color: #151a24;
            border: 1px solid #242c3d;
            border-radius: 4px;
            padding: 6px 12px;
            margin-right: 12px;
            font-size: 13px;
        }}
        .market-name {{ font-weight: bold; color: #8f9cae; margin-right: 8px; }}
        .market-price {{ font-weight: bold; margin-right: 8px; }}
        .market-change {{ font-weight: bold; }}
        
        @keyframes scroll-left {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}

        /* MAIN CONTENT LAYOUT */
        .main-container {{
            max-width: 1400px;
            margin: 30px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }}

        @media (max-width: 900px) {{
            .main-container {{ grid-template-columns: 1fr; }}
        }}

        h2 {{
            font-size: 18px;
            color: #8f9cae;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 20px;
            border-bottom: 1px solid #1f2633;
            padding-bottom: 8px;
        }}

        /* INVESTOREN GRID */
        .investor-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }}
        .investor-card {{
            background-color: #151a24;
            border: 1px solid #242c3d;
            border-radius: 6px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .investor-card h3 {{ margin: 0 0 5px 0; font-size: 18px; color: #ffffff; }}
        .investor-card .company {{ margin: 0 0 15px 0; color: #8f9cae; font-size: 13px; }}
        .inv-details {{ font-size: 14px; margin-bottom: 20px; }}
        .inv-details div {{ margin-bottom: 8px; display: flex; justify-content: space-between; }}
        .inv-details span {{ color: #8f9cae; }}
        .view-btn {{
            background-color: #242c3d;
            color: #ffffff;
            text-align: center;
            padding: 8px;
            border-radius: 4px;
            text-decoration: none;
            font-size: 13px;
            font-weight: bold;
            transition: background 0.2s;
        }}
        .view-btn:hover {{ background-color: #00ff88; color: #0b0e14; }}

        /* AKTIVITÄTS TABELLE */
        .activity-panel {{
            background-color: #151a24;
            border: 1px solid #242c3d;
            border-radius: 6px;
            padding: 20px;
            height: fit-content;
        }}
        .activity-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        .activity-table th {{ text-align: left; color: #8f9cae; padding: 10px 5px; border-bottom: 1px solid #1f2633; }}
        .activity-table td {{ padding: 12px 5px; border-bottom: 1px solid #1f2633; }}
        
        .badge {{
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 11px;
            font-weight: bold;
        }}
        .badge.pos {{ background-color: rgba(0, 255, 136, 0.15); color: #00ff88; }}
        .badge.neg {{ background-color: rgba(255, 51, 102, 0.15); color: #ff3366; }}

        /* Globale Farbklassen */
        .pos {{ color: #00ff88; }}
        .neg {{ color: #ff3366; }}
    </style>
</head>
<body>

    <header>
        <h1>ÜBERRENDITEN.DE</h1>
        <nav>
            <a href="#">Superinvestoren</a>
            <a href="#">Top Käufe</a>
            <a href="#">13F-Filings</a>
        </nav>
    </header>

    <div class="ticker-wrapper">
        <div class="ticker-track">
            {ticker_html_cards}
            {ticker_html_cards}
        </div>
    </div>

    <div class="main-container">
        <div>
            <h2>Value- & Superinvestoren</h2>
            <div class="investor-grid">
                {investor_html_cards}
            </div>
        </div>

        <div class="activity-panel">
            <h2>Letzte Aktivitäten (13F)</h2>
            <table class="activity-table">
                <thead>
                    <tr>
                        <th>Investor</th>
                        <th>Aktion</th>
                        <th>Aktie</th>
                        <th>% Portf.</th>
                    </tr>
                </thead>
                <tbody>
                    {activity_html_rows}
                </tbody>
            </table>
        </div>
    </div>

</body>
</html>
"""

# ==============================================================================
# 4. DATEI SPEICHERN
# ==============================================================================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Erfolgreich! Das Dataroma-Dashboard wurde generiert.")