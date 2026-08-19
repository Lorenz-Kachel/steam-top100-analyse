import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("SteamTop100.db")
cursor = conn.cursor()

print("=== Top 10 kostenlose Spiele nach Zustimmungsquote ===")
cursor.execute("""   
    SELECT name, (positive * 1.0 / (positive + negative)) AS durchschnittliche_quote
    FROM games 
    WHERE price = 0
    ORDER BY durchschnittliche_quote DESC
    LIMIT 10
""")
for zeile in cursor.fetchall():
    print(zeile)

print("\n=== Top 10 kostenpflichtige Spiele nach Zustimmungsquote ===")
cursor.execute("""   
    SELECT name, price, (positive * 1.0 / (positive + negative)) AS durchschnittliche_quote
    FROM games 
    WHERE price > 0
    ORDER BY durchschnittliche_quote DESC
    LIMIT 10
""")
for zeile in cursor.fetchall():
    print(zeile)


print("\n=== Durchschnittliche Zustimmungsquote nach Preiskategorie ===")
cursor.execute("""
    SELECT 
        CASE 
            WHEN price = 0 THEN 'Kostenlos'
            WHEN price < 2000 THEN 'Günstig (<20€)'
            ELSE 'Teuer (>=20€)'
        END AS preiskategorie,
        AVG(positive * 1.0 / (positive + negative)) AS durchschnittliche_quote,
        COUNT(*) AS anzahl_spiele
    FROM games
    GROUP BY preiskategorie
    ORDER BY durchschnittliche_quote DESC
""")
for zeile in cursor.fetchall():
    print(zeile)

print("\n=== Publisher-Dominanz ===")
cursor.execute("""
    SELECT publisher, COUNT(*) AS SpieleInTop100
    FROM games
    GROUP BY publisher
    HAVING COUNT(*) > 1
    ORDER BY SpieleInTop100 DESC
""")


ergebnisse = cursor.fetchall()

for zeile in ergebnisse:
    print(zeile)

namen = [zeile[0] for zeile in ergebnisse]
anzahl = [zeile[1] for zeile in ergebnisse]

sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))
sns.barplot(x=namen, y=anzahl)
plt.xlabel("Publisher")
plt.ylabel("Anzahl Spiele in Top 100")
plt.title("Publisher-Dominanz in der Steam Top 100")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig("publisher_dominanz.png")
plt.show() 

conn.close()