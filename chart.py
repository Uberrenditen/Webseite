import plotly.graph_objects as go
import yfinance as yf
import pandas as pd

# ==============================================================================
# 1. LIVE-DATEN FÜR DEN TICKER (Bereinigt)
# ==============================================================================
market_symbols = {
    # Deutsche Indizes
    'DAX': '^GDAXI', 'MDAX': '^MDAXI', 'TecDAX': '^TECDAX', 'SDAX': '^SDAXI', 'DivDAX': '^DIVDAX',
    # Internationale Märkte
    'Eurostoxx': '^STOXX50E', 'DowJones': '^DJI', 'US Tech 100': '^NDX', 'S&P 500': '^GSPC', 'Nikkei': '^N225',
    # Rohstoffe
    'Gold': 'GC=F', 'Silber': 'SI=F', 'Öl Brent': 'BZ=F',
    # Krypto
    'Bitcoin': 'BTC-USD', 'Ethereum': 'ETH-USD'
}

ticker_html_cards = ""

for name, sym in market_symbols.items():
    try:
        t_data = yf.Ticker(sym).history(period='2d')
        if not t_data.empty and len(t_data) >= 1:
            current_price = t_data['Close'].iloc[-1]
            change_pct = ((current_price - t_data['Close'].iloc[-2]) / t_data['Close'].iloc[-2]) * 100 if len(t_data) >= 2 else 0.0

            if any(k in name for k in ['Gold', 'Silber', 'Öl', 'Bitcoin', 'Ethereum', 'Tech', 'S&P']):
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
# 2. HAUPT-CHART GENERIEREN (Apple)
# ==============================================================================
ticker_symbol = 'AAPL'
df = yf.Ticker(ticker_symbol).history(period='6mo', interval='1d').reset_index()

aktueller_kurs = round(df['Close'].iloc[-1], 2)
letzter_kurs = df['Close'].iloc[-2]
prozent_aenderung = round(((aktueller_kurs - letzter_kurs) / letzter_kurs) * 100, 2)
farbe_aenderung = "#00ff88" if prozent_aenderung >= 0 else "#ff3366"

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
)])
fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_rangeslider_visible=False,
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
chart_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

# ==============================================================================
# 3. ANIMATED TICKER LAYOUT (HTML & CSS ANIMATION)
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
        
        /* TICKER CONTAINER SCHLANK & ANIMIERT */
        .ticker-wrapper {{
            background-color: #0e121a;
            border-bottom: 1px solid #1f2633;
            overflow: hidden; /* Versteckt alles, was aus dem Bildschirm ragt */
            display: flex;
            padding: 6px 0;
            position: relative;
        }}
        
        .ticker-track {{
            display: flex;
            width: max-content;
            animation: scroll-left 35s linear infinite; /* 35 Sekunden für einen Durchlauf */
        }}
        
        /* Pausiert die Animation, wenn man mit der Maus darüber fährt (wichtig zum Lesen!) */
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
        
        .pos {{ color: #00ff88; }}
        .neg {{ color: #ff3366; }}
        
        /* DIE MAGISCHE ANIMATION */
        @keyframes scroll-left {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }} /* Verschiebt exakt um die Länge der ersten Leiste */
        }}
        
        /* Haupt-Inhalt */
        .container {{
            display: flex;
            max-width: 1600px;
            margin: 15px auto;
            padding: 0 15px;
            gap: 15px;
        }}
        .main-content {{ flex: 3; background-color: #151a24; padding: 15px; border-radius: 6px; border: 1px solid #1f2633; }}
        .sidebar {{ flex: 1; background-color: #151a24; padding: 15px; border-radius: 6px; border: 1px solid #1f2633; }}
        h2 {{ margin-top: 0; font-size: 18px; color: #8f9cae; }}
        .kurs-info {{ font-size: 22px; font-weight: bold; margin-bottom: 10px; }}
        
        .news-card {{
            background-color: #1f2633;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 10px;
            border-left: 3px solid #00ff88;
        }}
        .news-card h3 {{ margin: 0 0 5px 0; font-size: 14px; }}
        .news-card p {{ margin: 0; font-size: 13px; color: #b5c2d5; }}
    </style>
</head>
<body>

    <header>
        <h1>ÜBERRENDITEN.DE</h1>
    </header>

    <div class="ticker-wrapper">
        <div class="ticker-track">
            {ticker_html_cards}
            {ticker_html_cards} </div>
    </div>

    <div class="container">
        <div class="main-content">
            <h2>Markt-Chart: {ticker_symbol}</h2>
            <div class="kurs-info">
                {aktueller_kurs} USD <span style="color: {farbe_aenderung}; font-size: 16px;">{prozent_aenderung}%</span>
            </div>
            {chart_div}
        </div>

        <div class="sidebar">
            <h2>Neueste Analysen</h2>
            <div class="news-card">
                <h3>Märkte im Aufwind</h3>
                <p>Anleger greifen bei Tech-Giganten wieder kräftig zu. Die charttechnische Situation hellt sich auf...</p>
            </div>
            <div class="news-card">
                <h3>Zinsentscheid im Fokus</h3>
                <p>Die Notenbanken signalisieren eine Pause. Was das jetzt bedeutet.</p>
            </div>
        </div>
    </div>

</body>
</html>
"""

# ==============================================================================
# 4. DATA SPEICHERN
# ==============================================================================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Perfekt! Der unendliche Live-Laufband-Ticker ist einsatzbereit!")