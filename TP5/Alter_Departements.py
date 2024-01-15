import csv
import sqlite3
import os

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute('''ALTER TABLE Departements ADD COLUMN NouvelleRegion INTEGER REFERENCES NouvellesRegions(Code_region)''')

path = "communes-2016.csv"
if(os.path.exists(path)):
    print("Le fichier demandé existe")
    with open(path,"r") as fichier:
        reader = csv.reader(fichier,delimiter=';')
        rows  = list(reader)
        for row in rows[1:]:
            cur.execute(f"UPDATE Departements SET NouvelleRegion = {row[3]} WHERE Code_Departement = '{row[2]}';")
           
        con.commit()
        #con.close()
else:
    print("Le fichier est introuvable")


cur.execute("Select * from Departements LIMIT 10")
rows = cur.fetchall()

for row in rows: 
    print(row)
con.close()