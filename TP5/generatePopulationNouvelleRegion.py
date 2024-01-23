import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

regions_query = '''
    SELECT dep.NouvelleRegion, SUM(com.Population_totale) 
    FROM Communes com
    JOIN Departements dep ON com.Code_departement = dep.Code_departement
    GROUP BY dep.NouvelleRegion
'''
cursor.execute(regions_query)
regions_results = cursor.fetchall()

with open('population_sum_nouvellesregions.txt', 'w') as file_regions:
    for row in regions_results:
        code_region, population_sum = row
        population_sum = str(population_sum).replace(" ", "")
        file_regions.write(f"Code_region: {code_region}, Population_sum: {population_sum}\n")

conn.close()