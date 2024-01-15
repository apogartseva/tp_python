import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

query = "SELECT Code_departement, SUM(Population_totale) FROM Communes GROUP BY Code_departement"
cursor.execute(query)

results = cursor.fetchall()

with open('population_sum_departements.txt', 'w') as file:
    # Write the results to the file
    for row in results:
        code_departement, population_sum = row
        population_sum = str(population_sum).replace(" ", "")
        file.write(f"Code_departement: {code_departement}, Population_sum: {population_sum}\n")

conn.close()