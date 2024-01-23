import csv
import sqlite3
import os

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS NouvellesRegions ''')
cur.execute('''CREATE TABLE NouvellesRegions (
                                     Code_region TEXT PRIMARY KEY, 
                                     Nom_region  TEXT)''')

path = "zones-2016.csv"
if(os.path.exists(path)):
    print("Le fichier demandé existe")
    with open(path,"r") as fichier:
        reader = csv.reader(fichier,delimiter=';')
        rows = list(reader)
        for row in rows[1:]:
            cur.execute('''
            INSERT OR REPLACE INTO NouvellesRegions (Code_region, Nom_region)
            Values (?,?)
            ''',(
                row[1],
                row[2]
            ))
        con.commit()
        #con.close()
else:
    print("Le fichier est introuvable")


cur.execute("Select * from NouvellesRegions LIMIT 10")
rows = cur.fetchall()

for row in rows: 
    print(row)
con.close()