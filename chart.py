import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Wir erstellen ein paar künstliche Aktiendaten für den Test
data = {
    'Date': ['2026-05-20', '2026-05-21', '2026-05-22', '2026-05-23', '2026-05-24'],
    'Open': [150.20, 152.10, 151.00, 153.50, 156.00],
    'High': [153.00, 154.50, 152.80, 157.00, 160.20],
    'Low': [149.50, 150.20, 148.10, 152.00, 155.10],
    'Close': [152.10, 151.00, 153.50, 156.00, 159.50]
}
df = pd.DataFrame(data)

# Hier erstellen wir den Candlestick-Chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'], 
    high=df['High'], 
    low=df['Low'], 
    close=df['Close']
)])

# Styling: Layout anpassen und den nervigen Slider unten ausschalten
fig.update_layout(
    title='Mein erster Krypto/Aktien Chart',
    yaxis_title='Kurs in €',
    xaxis_rangeslider_visible=False,
    template='plotly_dark' # Dunkler Modus, sieht cooler aus!
)

# Das Wichtigste: Wir speichern das Ganze als fertige HTML-Datei ab
fig.write_html("index.html")
print("Der Chart wurde erfolgreich als 'index.html' gespeichert!")