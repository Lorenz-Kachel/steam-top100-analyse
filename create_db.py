import sqlite3

conn = sqlite3.connect("SteamTop100.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
    app_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    developer VARCHAR(50),
    publisher VARCHAR(50),
    price REAL,
    positive INTEGER,
    negative INTEGER,
    owners VARCHAR(50)
    )
""")

conn.commit()
conn.close()