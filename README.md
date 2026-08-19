# Steam Top 100 – Economy Analyse Tool

Ein kleines Python/SQL-Projekt, das die aktuellen Top-100-Spiele auf Steam (nach Spielerzahl der letzten 2 Wochen) über die [SteamSpy API](https://steamspy.com/api.php) abruft, in einer SQLite-Datenbank speichert und mit SQL-Abfragen analysiert.

Entstanden als Lernprojekt in den Semesterferien, um praktische Erfahrung mit Python, SQL und dem Umgang mit einer echten API zu sammeln.

## Was das Projekt macht

1. Ruft die aktuellen Top-100-Spiele über die SteamSpy API ab (Name, Entwickler, Publisher, Preis, Bewertungen, Besitzerzahl)
2. Speichert die Daten in einer SQLite-Datenbank
3. Wertet die Daten mit SQL aus, u. a.:
   - Top 10 kostenlose Spiele nach Zustimmungsquote
   - Top 10 kostenpflichtige Spiele nach Zustimmungsquote
   - Durchschnittliche Zustimmungsquote je Preiskategorie (kostenlos / günstig / teuer)
   - Welche Publisher mehrere Spiele gleichzeitig in der Top 100 haben
4. Stellt die Publisher-Verteilung als Balkendiagramm dar

## Tech Stack

- Python 3
- SQLite (`sqlite3`, Standardbibliothek)
- [requests](https://pypi.org/project/requests/) – API-Anbindung
- [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/) – Visualisierung

## Projektstruktur

```
├── create_db.py       # Legt die SQLite-Datenbank und Tabelle an
├── fetch_data.py       # Ruft die SteamSpy-API ab und befüllt die Datenbank
├── analyse.py           # Führt die SQL-Analysen aus und erstellt das Diagramm
├── requirements.txt      # Benötigte Python-Bibliotheken
└── publisher_dominanz.png  # Beispiel-Output der Visualisierung
```

## Setup & Ausführen

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/DEIN-REPO-NAME.git
cd DEIN-REPO-NAME

# Abhängigkeiten installieren
pip install -r requirements.txt

# Datenbank anlegen
python create_db.py

# Aktuelle Steam-Daten abrufen und einfügen
python fetch_data.py

# Analysen ausführen
python analyse.py
```

## Was ich dabei gelernt habe

Ich komme aus dem Java-Umfeld und hatte SQL bisher nur aus der Theorie/Klausur gekannt, praktisch aber noch nie damit gearbeitet. In diesem Projekt habe ich mir selbstständig erarbeitet:

- Grundlegende und fortgeschrittenere SQL-Konzepte praktisch angewendet: `GROUP BY`, `HAVING`, `CASE WHEN`, Aggregatfunktionen
- Wie man mit Python (`sqlite3`) mit einer relationalen Datenbank interagiert
- Wie man eine externe REST-API anspricht (`requests`), JSON-Antworten verarbeitet und in eine Datenbank überführt
- Typische Python-Unterschiede zu Java (z. B. Dictionaries, List Comprehensions, Duck Typing)
