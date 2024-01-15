import csv
import sqlite3
import os

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Regions ''')
cur.execute('''CREATE TABLE Regions (
                                     Code_region TEXT PRIMARY KEY, 
                                     Nom_region  TEXT)''')

path = "regions.csv"
if(os.path.exists(path)):
    print("Le fichier demandé existe")
    with open(path,"r") as fichier:
        reader = csv.reader(fichier,delimiter=';')
        rows = list(reader)
        for row in rows[1:]:
            cur.execute('''
            INSERT OR REPLACE INTO Regions (Code_region, Nom_region)
            Values (?,?)
            ''',(
                row[0],
                row[1]
            ))
        con.commit()
        #con.close()
else:
    print("Le fichier est introuvable")


cur.execute("Select * from Regions LIMIT 10")
rows = cur.fetchall()

for row in rows: 
    print(row)
con.close()