import plotly.graph_objects as go
import yfinance as yf
import pandas as pd

# 1. DATEN HOLEN (Mehrere Werte für den Ticker + Haupt-Aktie)
ticker_symbol = 'AAPL'
aktie = yf.Ticker(ticker_symbol)
df = aktie.history(period='6mo', interval='1d').reset_index()

# Aktuellen Kurs und Änderung berechnen
aktueller_kurs = round(df['Close'].iloc[-1], 2)
letzter_kurs = df['Close'].iloc[-2]
prozent_aenderung = round(((aktueller_kurs - letzter_kurs) / letzter_kurs) * 100, 2)
farbe_aenderung = "#00ff88" if prozent_aenderung >= 0 else "#ff3366"

# 2. CHART ERSTELLEN
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
)])
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_rangeslider_visible=False,
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)', # Transparent für nahtloses Design
    plot_bgcolor='rgba(0,0,0,0)'
)
# Chart in HTML-Code umwandeln (ohne die ganze Seite zu blockieren)
chart_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

# 3. DAS GESAMTE WEBSEITEN-LAYOUT (HTML/CSS) BAUEN
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Überrenditen.de - Das Finanzportal</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0b0e14;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #151a24;
            padding: 20px;
            border-bottom: 2px solid #1f2633;
            text-align: center;
        }}
        h1 {{ margin: 0; color: #00ff88; font-size: 28px; letter-spacing: 1px; }}
        .ticker {{
            background-color: #1f2633;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}
        .container {{
            display: flex;
            max-width: 1400px;
            margin: 20px auto;
            padding: 0 20px;
            gap: 20px;
        }}
        .main-content {{ flex: 3; background-color: #151a24; padding: 20px; border-radius: 8px; }}
        .sidebar {{ flex: 1; background-color: #151a24; padding: 20px; border-radius: 8px; }}
        .kurs-info {{ font-size: 24px; font-weight: bold; margin-bottom: 15px; }}
        .news-card {{
            background-color: #1f2633;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 15px;
            border-left: 4px solid #00ff88;
        }}
        .news-card h3 {{ margin: 0 0 10px 0; font-size: 16px; }}
        .news-card p {{ margin: 0; font-size: 14px; color: #b5c2d5; }}
    </style>
</head>
<body>

    <header>
        <h1>ÜBERRENDITEN.DE</h1>
    </header>

    <div class="ticker">
        🔥 Top-Fokus heute: {ticker_symbol}: {aktueller_kurs} USD (<span style="color: {farbe_aenderung}">{prozent_aenderung}%</span>)
    </div>

    <div class="container">
        <div class="main-content">
            <h2>Markt-Chart: {ticker_symbol}</h2>
            <div class="kurs-info">
                {aktueller_kurs} USD <span style="color: {farbe_aenderung}; font-size: 18px;">{prozent_aenderung}%</span>
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
                <p>Die Notenbanken signalisieren eine Pause. Was das jetzt für dein Krypto-Portfolio bedeutet.</p>
            </div>
            
            <div class="news-card">
                <h3>Überrenditen-Strategie</h3>
                <p>Erfahre mehr über unseren regelbasierten Ansatz zur Outperformance des breiten Marktes.</p>
            </div>
        </div>
    </div>

</body>
</html>
"""

# 4. SPEICHERN
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Das neue Magazin-Layout wurde erfolgreich generiert!")