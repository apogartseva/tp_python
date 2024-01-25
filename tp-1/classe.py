import csv
from datetime import date

class Date:
    def __init__(self, day, month, year):
        if year > date.today().year:
            raise ValueError("L'année de naissance ne peut pas être ultérieure à l'année actuelle.")
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)


class Etudiant:
    def __init__(self, prenom, nom, date_naissance):
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance

    def adresselec(self):
        return f"{self.prenom.lower()}.{self.nom.lower()}@etu.univ-tours.fr"

    def age(self, date_actuelle):
        delta = date_actuelle.year - self.date_naissance.year - ((date_actuelle.month, date_actuelle.day) < (self.date_naissance.month, self.date_naissance.day))
        return delta

def lire_fichier_csv(nom_fichier):
    liste_etudiants = []

    try:
        with open(nom_fichier, 'r') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            next(lecteur_csv)  # skip the first line

            for ligne in lecteur_csv:
                try:
                    prenom = ligne[0]
                    nom = ligne[1]
                    jour, mois, annee = map(int, ligne[2].split('/'))
                    date_naissance = Date(jour, mois, annee)

                    etudiant = Etudiant(prenom, nom, date_naissance)
                    liste_etudiants.append(etudiant)
                except (ValueError, IndexError) as e:
                    print(f"Erreur lors de la création d'un objet Etudiant : {e}")

    except FileNotFoundError:
        print(f"Fichier CSV non trouvé : {nom_fichier}")
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture du fichier CSV : {e}")
    else:
        print("Lecture du fichier CSV réussie.")
    finally:
        print("Fin du processus de lecture du fichier CSV.")

    return liste_etudiants

try:
    date_actuelle = date.today()
    liste_etudiants = lire_fichier_csv('fichetu.csv')

    for etudiant in liste_etudiants:
        print(f"{etudiant.prenom} {etudiant.nom}")
        print(f"Adresse électronique : {etudiant.adresselec()}")
        print(f"Âge : {etudiant.age(date_actuelle)} ans\n")

except ValueError as ve:
    print(f"Erreur : {ve}")
except Exception as e:
    print(f"Erreur inattendue lors de l'exécution du programme : {e}")
