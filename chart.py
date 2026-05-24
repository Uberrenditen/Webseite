import yfinance as yf

# ==============================================================================
# 1. LIVE-DATEN FÜR DEN TICKER & DIE HEATMAP HOLEN
# ==============================================================================
market_symbols = {
    'DAX': '^GDAXI', 'MDAX': '^MDAXI', 'TecDAX': '^TECDAX', 'SDAX': '^SDAXI', 'DivDAX': '^DIVDAX',
    'Eurostoxx': '^STOXX50E', 'DowJones': '^DJI', 'US Tech 100': '^NDX', 'S&P 500': '^GSPC', 'Nikkei': '^N225',
    'Gold': 'GC=F', 'Silber': 'SI=F', 'Öl Brent': 'BZ=F',
    'Bitcoin': 'BTC-USD', 'Ethereum': 'ETH-USD'
}

ticker_html_cards = ""
heatmap_html_tiles = ""

# Funktion, die basierend auf der Performance eine passende Hintergrundfarbe generiert
def get_heatmap_color(change):
    if change > 2.0: return "rgba(0, 255, 136, 0.35)"     # Tiefes Hellgrün
    elif change > 0.5: return "rgba(0, 255, 136, 0.18)"   # Leichtes Grün
    elif change >= -0.5: return "rgba(255, 255, 255, 0.05)" # Neutral (Grau)
    elif change >= -2.0: return "rgba(255, 51, 102, 0.18)"  # Leichtes Rot
    else: return "rgba(255, 51, 102, 0.35)"                # Tiefes Rot

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
            
            # 1. HTML für den Ticker generieren
            ticker_html_cards += f"""
            <div class="market-card">
                <span class="market-name">{name}</span>
                <span class="market-price">{price_str}</span>
                <span class="market-change {color_class}">{sign}{change_pct:.2f}%</span>
            </div>
            """
            
            # 2. HTML für die Heatmap-Kachel generieren
            bg_color = get_heatmap_color(change_pct)
            border_color = "#00ff88" if change_pct >= 0 else "#ff3366"
            
            heatmap_html_tiles += f"""
            <div class="heatmap-tile" style="background-color: {bg_color}; border-left: 4px solid {border_color};">
                <div class="tile-name">{name}</div>
                <div class="tile-price">{price_str}</div>
                <div class="tile-change {color_class}">{sign}{change_pct:.2f}%</div>
            </div>
            """
            
    except Exception as e:
        print(f"Fehler bei {name}: {e}")

# ==============================================================================
# 2. DAS HTML-LAYOUT (HEADER + TICKER + HEATMAP)
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
        
        /* HEATMAP SEKTION VIA CSS GRID */
        .heatmap-container {{
            max-width: 1600px;
            margin: 25px auto;
            padding: 0 20px;
        }}
        .heatmap-container h2 {{
            font-size: 16px;
            color: #8f9cae;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 15px;
        }}
        .heatmap-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 12px;
        }}
        .heatmap-tile {{
            border: 1px solid #242c3d;
            border-radius: 4px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 70px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .heatmap-tile:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        .tile-name {{
            font-size: 12px;
            font-weight: bold;
            color: #8f9cae;
            text-transform: uppercase;
        }}
        .tile-price {{
            font-size: 15px;
            font-weight: bold;
            margin: 4px 0;
        }}
        .tile-change {{
            font-size: 13px;
            font-weight: bold;
            text-align: right;
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

    <div class="heatmap-container">
        <h2>Markt-Heatmap (24h Performance)</h2>
        <div class="heatmap-grid">
            {heatmap_html_tiles}
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

print("Perfekt! Die Heatmap wurde erfolgreich unter dem Ticker integriert!")