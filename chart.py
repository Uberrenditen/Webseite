import plotly.graph_objects as go
import yfinance as yf
import pandas as pd

# ==============================================================================
# 1. ALLE 18 SYMBOLE AUS DEINEN SCREENSHOTS NACH KATEGORIEN SORTIERT
# ==============================================================================
categories = {
    "Deutsche Indizes": {
        'DAX': '^GDAXI', 'MDAX': '^MDAXI', 'TecDAX': '^TECDAX', 'SDAX': '^SDAXI', 'DivDAX': '^DIVDAX'
    },
    "Internationale Märkte": {
        'Eurostoxx': '^STOXX50E', 'DowJones': '^DJI', 'US Tech 100': '^NDX', 'S&P 500': '^GSPC', 'Nikkei': '^N225'
    },
    "Rohstoffe": {
        'Gold': 'GC=F', 'Silber': 'SI=F', 'Öl Brent': 'BZ=F'
    },
    "Kryptowährungen": {
        'Bitcoin': 'BTC-USD', 'Ethereum': 'ETH-USD', 'Solana': 'SOL-USD', 'XRP': 'XRP-USD', 'Dogecoin': 'DOGE-USD'
    }
}

total_ticker_html = ""

# Wir gehen jede Kategorie durch und bauen die Boxen
for cat_name, symbols in categories.items():
    total_ticker_html += f'<div class="category-section"><h3>{cat_name}</h3><div class="ticker-grid">'
    
    for name, sym in symbols.items():
        try:
            # Daten für die letzten 2 Tage holen, um die Änderung zu berechnen
            t_data = yf.Ticker(sym).history(period='2d')
            if not t_data.empty and len(t_data) >= 1:
                current_price = t_data['Close'].iloc[-1]
                
                # Falls der Markt geschlossen hat oder nur 1 Tag liefert, künstliche Änderung abfangen
                if len(t_data) >= 2:
                    prev_price = t_data['Close'].iloc[-2]
                    change_pct = ((current_price - prev_price) / prev_price) * 100
                else:
                    change_pct = 0.0

                # Währungs-Suffix und Nachkommastellen festlegen
                if cat_name in ["Rohstoffe", "Kryptowährungen"] or "Tech" in name or "S&P" in name:
                    suffix = " USD"
                else:
                    suffix = ""
                
                # Spezielle Formatierung für super günstige Kryptos wie Dogecoin oder XRP
                if current_price < 2:
                    price_str = f"{current_price:.4f}{suffix}"
                else:
                    price_str = f"{current_price:,.2f}{suffix}"
                
                # Deutsche Formatierung (Komma statt Punkt)
                price_str = price_str.replace(",", "X").replace(".", ",").replace("X", ".")
                
                # Farbe und Vorzeichen bestimmen
                if change_pct >= 0:
                    color_class = "pos"
                    sign = "+"
                else:
                    color_class = "neg"
                    sign = ""
                
                # HTML für die einzelne Karte hinzufügen
                total_ticker_html += f"""
                <div class="market-card">
                    <div class="market-name">{name}</div>
                    <div class="market-details">
                        <span class="market-price">{price_str}</span>
                        <span class="market-change {color_class}">{sign}{change_pct:.2f}%</span>
                    </div>
                </div>
                """
        except Exception as e:
            print(f"Fehler bei {name}: {e}")
            
    total_ticker_html += "</div></div>" # Grids und Sektionen schließen

# ==============================================================================
# 2. HAUPT-CHART GENERIEREN (Apple)
# ==============================================================================
ticker_symbol = 'AAPL'
aktie = yf.Ticker(ticker_symbol)
df = aktie.history(period='6mo', interval='1d').reset_index()

aktueller_kurs = round(df['Close'].iloc[-1], 2)
letzter_kurs = df['Close'].iloc[-2]
prozent_aenderung = round(((aktueller_kurs - letzter_kurs) / letzter_kurs) * 100, 2)
farbe_aenderung = "#00ff88" if prozent_aenderung >= 0 else "#ff3366"

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
)])
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_rangeslider_visible=False,
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
chart_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

# ==============================================================================
# 3. DAS GESTYLTE MAGAZIN-LAYOUT (HTML & CSS)
# ==============================================================================
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Überrenditen.de - Das Finanzportal</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #0b0e14;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #151a24;
            padding: 20px;
            border-bottom: 1px solid #1f2633;
            text-align: center;
        }}
        header h1 {{ margin: 0; color: #00ff88; font-size: 28px; letter-spacing: 1px; }}
        
        /* Das große Ticker-System für alle Kategorien */
        .master-ticker {{
            background-color: #0e121a;
            padding: 15px 20px;
            border-bottom: 1px solid #1f2633;
        }}
        .category-section {{
            margin-bottom: 15px;
        }}
        .category-section h3 {{
            margin: 0 0 8px 0;
            font-size: 13px;
            color: #00ff88;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ticker-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 10px;
        }}
        .market-card {{
            background-color: #151a24;
            border: 1px solid #242c3d;
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .market-name {{
            font-size: 12px;
            font-weight: bold;
            color: #8f9cae;
            margin-bottom: 4px;
        }}
        .market-details {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .market-price {{
            font-size: 14px;
            font-weight: bold;
        }}
        .market-change {{
            font-size: 13px;
            font-weight: bold;
        }}
        .pos {{ color: #00ff88; }}
        .neg {{ color: #ff3366; }}
        
        /* Haupt-Inhalt */
        .container {{
            display: flex;
            max-width: 1600px;
            margin: 20px auto;
            padding: 0 20px;
            gap: 20px;
        }}
        .main-content {{ flex: 3; background-color: #151a24; padding: 20px; border-radius: 8px; border: 1px solid #1f2633; }}
        .sidebar {{ flex: 1; background-color: #151a24; padding: 20px; border-radius: 8px; border: 1px solid #1f2633; }}
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

    <div class="master-ticker">
        {total_ticker_html}
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

print("Perfekt! Alle 18 Markt-Karten wurden geladen und im Layout verbaut!")