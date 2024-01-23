import csv
import sqlite3
import os

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Departements ''')
cur.execute('''CREATE TABLE Departements (
                                     Code_departement TEXT PRIMARY KEY, 
                                     Nom_departement  TEXT, 
                                     Code_region TEXT)''')

path = "departements.csv"
if(os.path.exists(path)):
    print("Le fichier demandé existe")
    with open(path,"r") as fichier:
        reader = csv.reader(fichier,delimiter=';')
        rows  = list(reader)
        for row in rows[1:]:
            cur.execute('''
            INSERT OR REPLACE INTO Departements (Code_departement, Nom_departement, Code_region)
            Values (?,?,?)
            ''',(
                row[2],
                row[3],
                row[0]
            ))
        con.commit()
        #con.close()
else:
    print("Le fichier est introuvable")


cur.execute("Select * from Departements LIMIT 10")
rows = cur.fetchall()

for row in rows: 
    print(row)
con.close()