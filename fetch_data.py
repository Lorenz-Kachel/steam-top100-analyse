import requests
import sqlite3

conn = sqlite3.connect("SteamTop100.db")
cursor = conn.cursor()

response = requests.get("https://steamspy.com/api.php?request=top100in2weeks")
data = response.json()

for app_id, spiel in data.items():
    cursor.execute(
    "INSERT OR REPLACE INTO games (app_id, name, developer, publisher, price, positive, negative, owners) VALUES (?,?,?,?,?,?,?,?)",
    (app_id, spiel["name"], spiel["developer"], spiel["publisher"], spiel["price"], spiel["positive"], spiel["negative"], spiel["owners"]) 
    )

conn.commit()
conn.close()