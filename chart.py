import yfinance as yf

# ==============================================================================
# 1. LIVE-DATEN FÜR DEN TICKER HOLEN
# ==============================================================================
market_symbols = {
    'DAX': '^GDAXI', 'MDAX': '^MDAXI', 'TecDAX': '^TECDAX', 'SDAX': '^SDAXI', 'DivDAX': '^DIVDAX',
    'Eurostoxx': '^STOXX50E', 'DowJones': '^DJI', 'US Tech 100': '^NDX', 'S&P 500': '^GSPC', 'Nikkei': '^N225',
    'Gold': 'GC=F', 'Silber': 'SI=F', 'Öl Brent': 'BZ=F',
    'Bitcoin': 'BTC-USD', 'Ethereum': 'ETH-USD'
}

ticker_html_cards = ""

for name, sym in market_symbols.items():
    try:
        t_data = yf.Ticker(sym).history(period='2d')
        if not t_data.empty and len(t_data) >= 1:
            current_price = t_data['Close'].iloc[-1]
            change_pct = ((current_price - t_data['Close'].iloc[-2]) / t_data['Close'].iloc[-2]) * 100 if len(t_data) >= 2 else 0.0

            # Passendes Währungssuffix anhängen
            if any(k in name for k in ['Gold', 'Silber', 'Öl', 'Bitcoin', 'Ethereum', 'Tech', 'S&P']):
                suffix = " USD"
            else:
                suffix = ""
            
            price_str = f"{current_price:,.2f}{suffix}".replace(",", "X").replace(".", ",").replace("X", ".")
            color_class = "pos" if change_pct >= 0 else "neg"
            sign = "+" if change_pct >= 0 else ""
            
            # HTML für den Ticker generieren
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
# 2. DAS HTML-LAYOUT (HEADER + TICKER)
# ==============================================================================
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Überrenditen.de</title>
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
            padding: 12px 20px;
            border-bottom: 1px solid #1f2633;
            display: flex;
            align-items: center;
        }}
        header h1 {{ margin: 0; color: #00ff88; font-size: 20px; letter-spacing: 1px; }}
        
        /* UNENDLICHER TICKER STRIP */
        .ticker-wrapper {{
            background-color: #0e121a;
            border-bottom: 1px solid #1f2633;
            overflow: hidden;
            display: flex;
            padding: 8px 0;
            position: relative;
        }}
        .ticker-track {{
            display: flex;
            width: max-content;
            animation: scroll-left 35s linear infinite;
        }}
        .ticker-wrapper:hover .ticker-track {{
            animation-play-state: paused;
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
            white-space: nowrap;
        }}
        .market-name {{ font-weight: bold; color: #8f9cae; margin-right: 8px; }}
        .market-price {{ font-weight: bold; margin-right: 8px; }}
        .market-change {{ font-weight: bold; }}
        
        @keyframes scroll-left {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}
        
        /* Globale Farbklassen */
        .pos {{ color: #00ff88; }}
        .neg {{ color: #ff3366; }}
    </style>
</head>
<body>

    <header>
        <h1>ÜBERRENDITEN.DE</h1>
    </header>

    <div class="ticker-wrapper">
        <div class="ticker-track">
            {ticker_html_cards}
            {ticker_html_cards}
        </div>
    </div>

</body>
</html>
"""

# ==============================================================================
# 3. DATEI SPEICHERN
# ==============================================================================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Erfolgreich! Die Heatmap wurde vollständig entfernt.")