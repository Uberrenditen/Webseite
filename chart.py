import plotly.graph_objects as go
import yfinance as yf

# 1. Echte Aktiendaten abrufen
ticker_symbol = 'AAPL' 
ticker_data = yf.Ticker(ticker_symbol)

# Wir holen die historischen Daten der letzten 6 Monate
df = ticker_data.history(period='6mo', interval='1d')
df = df.reset_index()

# 2. Den interaktiven Candlestick-Chart erstellen
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'], 
    high=df['High'], 
    low=df['Low'], 
    close=df['Close']
)])

# 3. Styling anpassen
fig.update_layout(
    title=f'Echter Live-Chart: {ticker_symbol} (Letzte 6 Monate)',
    yaxis_title='Kurs in USD',
    xaxis_rangeslider_visible=False,
    template='plotly_dark'
)

# 4. Als index.html für deine Webseite speichern
fig.write_html("index.html")
print(f"Der echte Chart für {ticker_symbol} wurde erfolgreich als 'index.html' gespeichert!")