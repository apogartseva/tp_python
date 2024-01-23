import sqlite3
import os
import csv

# Connexion à la database SQLite
conn = sqlite3.connect('database.db')

# Creation d'un curseur permettant l'execution de requêtes sur la base
cursor = conn.cursor()

# Création de la table Communes selon les données contenues dans les fichiers .csv
cursor.execute('''DROP TABLE IF EXISTS Communes''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Communes (
                    Code_departement TEXT,
                    Code_commune TEXT,
                    Nom_commune TEXT,
                    Population_totale INTEGER
                )''')


path = "communes.csv"
if(os.path.exists(path)):
    print("Le fichier demandé existe")
    with open('communes.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        rows = list(csv_reader)
        for row in rows[1:]:
            cursor.execute('''INSERT INTO Communes (Code_departement, Code_commune, Nom_commune, Population_totale)
                            VALUES (?, ?, ?, ?)''', (row[2], row[5], row[6], row[9]))
        conn.commit()
else:
    print("Le fichier est introuvable")

# On enlève les espaces en trop dans les chiffres de la colonne population totale
cursor.execute("UPDATE Communes SET Population_totale = REPLACE(Population_totale, ' ', '')")

conn.commit()
conn.close()