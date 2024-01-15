import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

regions_query = '''
    SELECT dep.Code_region, SUM(com.Population_totale) 
    FROM Communes com
    JOIN Departements dep ON com.Code_departement = dep.Code_departement
    JOIN Regions reg ON dep.Code_region = reg.Code_region
    GROUP BY dep.Code_region
'''
cursor.execute(regions_query)
regions_results = cursor.fetchall()

with open('population_sum_regions.txt', 'w') as file_regions:
    for row in regions_results:
        code_region, population_sum = row
        population_sum = str(population_sum).replace(" ", "")
        file_regions.write(f"Code_region: {code_region}, Population_sum: {population_sum}\n")

conn.close()