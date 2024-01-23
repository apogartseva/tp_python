import sqlite3
import xml.etree.ElementTree as ET

def enregistrer_xml(database,xml):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Communes")
    rows = cursor.fetchall()

    # Structure du xml
    root = ET.Element("database")
    # Pour chaque ligne, on crée les éléments du XML et on y attribue la valeur dans la ligne
    for row in rows:
        commune_el = ET.SubElement(root,"commune")
        code_departement_el = ET.SubElement(commune_el, "code_departement")
        code_departement_el.text = str(row[0])
        code_commune_el = ET.SubElement(commune_el, "code_commune")
        code_commune_el.text = row[1]
        nom_commune_el = ET.SubElement(commune_el, "nom_commune")
        nom_commune_el.text = row[2]
        population_el = ET.SubElement(commune_el, "population")
        population_el.text = str(row[3])

    
    tree = ET.ElementTree(root)
    tree.write(xml, encoding="utf-8", xml_declaration=True)

    conn.close()

def charger_xml(xml, database):
    tree = ET.parse(xml)
    root = tree.getroot()

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS Communes''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Communes (
                        Code_departement TEXT,
                        Code_commune TEXT,
                        Nom_commune TEXT,
                        Population_totale INTEGER
                    )''')
    
    for commune_element in root.findall(".//commune"):
        cursor.execute('''
            INSERT OR REPLACE INTO Communes (Code_departement, Code_commune, Nom_commune, Population_totale)
            VALUES (?, ?, ?, ?)
        ''', (commune_element.find("code_departement").text, commune_element.find("code_commune").text, commune_element.find("nom_commune").text,  int(commune_element.find("population").text)))

    conn.commit()
    conn.close()


enregistrer_xml("database.db","database.xml")
charger_xml("database.xml","database_bis.db")