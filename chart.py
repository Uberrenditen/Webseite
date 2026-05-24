# ==============================================================================
# 1. DATEN FÜR DIE WIDGETS UND LINKS (WONDERLINK-STYLE)
# ==============================================================================

# 2 Horizontale Widgets
widgets = [
    {"title": "🚀 Zum Blog", "url": "https://dein-blog.de"},
    {"title": "📩 Newsletter", "url": "https://dein-newsletter.de"}
]

# 6 Vertikale Felder (basierend auf dem Screenshot)
links = [
    {
        "name": "InvestingPro", 
        "desc": "InvestingPRO | *15% Nachlass", 
        "url": "#", 
        "bg_top": "#1a1a1a", 
        "color_top": "#ff8c00"
    },
    {
        "name": "bitvavo", 
        "desc": "Hier handle ich Krypto! Sichere dir einen Bonus*", 
        "url": "#", 
        "bg_top": "#003cf0", 
        "color_top": "#ffffff"
    },
    {
        "name": "parqet", 
        "desc": "Mein Depot tracke ich mit Parqet<br>*sichere dir 15% Rabatt", 
        "url": "#", 
        "bg_top": "#00857a", 
        "color_top": "#ffffff"
    },
    {
        "name": "TRADE REPUBLIC", 
        "desc": "Mein Broker - sicherer dir einen<br>Willkommensbonus*", 
        "url": "#", 
        "bg_top": "#ffffff", 
        "color_top": "#000000"
    },
    {
        "name": "Bondora", 
        "desc": "Bondora Go&Grow<br>*sichere dir 5€ Startguthaben", 
        "url": "#", 
        "bg_top": "#ffffff", 
        "color_top": "#000000"
    },
    {
        "name": "Dein 6. Link", 
        "desc": "Hier kommt die Beschreibung für das sechste Feld rein*", 
        "url": "#", 
        "bg_top": "#333333", 
        "color_top": "#ffffff"
    }
]

# ==============================================================================
# 2. HTML-BAUSTEINE GENERIEREN
# ==============================================================================

# HTML für die horizontalen Widgets bauen
widgets_html = ""
for w in widgets:
    widgets_html += f"""
    <a href="{w['url']}" class="widget-card" target="_blank">
        {w['title']}
    </a>
    """

# HTML für die vertikalen Felder bauen
links_html = ""
for link in links:
    links_html += f"""
    <a href="{link['url']}" class="link-card" target="_blank">
        <div class="card-top" style="background-color: {link['bg_top']}; color: {link['color_top']};">
            <h2>{link['name']}</h2>
        </div>
        <div class="card-bottom">
            <p>{link['desc']}</p>
        </div>
    </a>
    """

# ==============================================================================
# 3. DAS HTML-LAYOUT (FINALE SEITE)
# ==============================================================================
html_content = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Links</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #62b9b6; /* Türkiser Hintergrund wie im Bild */
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }}
        .main-container {{
            max-width: 500px;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 25px;
        }}
        
        /* 2 Horizontale Widgets */
        .widget-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }}
        .widget-card {{
            background-color: #ffffff;
            color: #333333;
            text-decoration: none;
            text-align: center;
            padding: 15px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }}
        .widget-card:hover {{
            transform: translateY(-2px);
        }}

        /* 6 Vertikale Felder */
        .link-list {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .link-card {{
            display: flex;
            flex-direction: column;
            text-decoration: none;
            border-radius: 35px; /* Starke Rundung wie im Bild */
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }}
        .link-card:hover {{
            transform: translateY(-2px);
        }}
        .card-top {{
            padding: 25px 20px;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .card-top h2 {{
            margin: 0;
            font-size: 32px;
            letter-spacing: -0.5px;
        }}
        .card-bottom {{
            background-color: #c0e6e6; /* Hellblau/Türkiser unterer Bereich */
            color: #000000;
            padding: 20px 15px;
            text-align: center;
        }}
        .card-bottom p {{
            margin: 0;
            font-size: 13px;
            font-weight: 700;
            line-height: 1.4;
        }}

        /* Disclaimer Footer */
        .footer-disclaimer {{
            margin-top: 30px;
            font-size: 11px;
            color: #1c3b39;
            line-height: 1.5;
            text-align: justify;
        }}
        .footer-disclaimer p {{
            margin-bottom: 10px;
        }}
        .footer-disclaimer strong {{
            color: #0d1e1c;
        }}
    </style>
</head>
<body>

    <div class="main-container">
        
        <div class="widget-grid">
            {widgets_html}
        </div>

        <div class="link-list">
            {links_html}
        </div>

        <div class="footer-disclaimer">
            <p>* Bei den mit einem Sternchen (*) markierten Links handelt es sich um Affiliate-Links. Kommt darüber ein Kauf zustande, erhalte ich eine Provision vom Anbieter. Für dich entsteht dadurch kein Nachteil.</p>
            
            <p><strong>DISCLAIMER</strong><br>
            <strong>Achtung – Wichtiger Hinweis:</strong></p>
            
            <p>Alle meine Beiträge dienen ausschließlich allgemeinen Informations- und Unterhaltungszwecken. Die Beiträge stellen keine Anlageberatung, keine Kauf- oder Verkaufsempfehlung und keine individuelle Finanzberatung dar.</p>
            
            <p>Investitionen in Aktien, Kryptowährungen oder andere Finanzinstrumente sind mit erheblichen Risiken verbunden – bis hin zum Totalverlust des eingesetzten Kapitals.</p>
            
            <p>Treffen Sie eigene Entscheidungen und lassen Sie sich ggf. von einem zugelassenen Finanzberater beraten. Ich übernehme keine Haftung für etwaige Verluste oder Entscheidungen, die aufgrund meiner Beiträge getroffen werden.</p>
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

print("Erfolgreich! Die Link-Seite wurde als 'index.html' generierts.")