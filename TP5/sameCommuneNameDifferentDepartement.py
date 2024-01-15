import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

query = '''
    SELECT c1.Nom_commune, GROUP_CONCAT(DISTINCT c1.Code_departement) AS Departements
    FROM Communes c1
    JOIN Communes c2 ON c1.Nom_commune = c2.Nom_commune AND c1.Code_departement <> c2.Code_departement
    GROUP BY c1.Nom_commune
    HAVING COUNT(DISTINCT c1.Code_departement) > 1
'''

cursor.execute(query)
results = cursor.fetchall()

with open('sameCommuneNameDifferentDepartement.txt','w') as file_Com_Dep:
    for row in results:
        nom_commune, departements = row
        file_Com_Dep.write(f"Nom de la commune: {nom_commune}, N° de départements: {departements}\n")

conn.close()
