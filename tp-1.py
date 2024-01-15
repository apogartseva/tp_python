import os 

from pathlib import Path

print ("Bonjour le monde ! ")




def menu_1(): 
    nom = input("Entrez un nom de fichier avec extension: ")
    print("Fichier choisi : ", nom)


    while os.path.exists(nom) == False:
        print("Le fichier", nom, "n'existe pas. Voulez vous le créer (1) ou choisir un autre (2)")
        action_fichier = int(input("Choix : "))
        fichier.close()
        if action_fichier == 1:
            fichier = open(nom, "w+")
            print("Le fichier est créé dans ", Path.cwd())
            fichier.close()
        if action_fichier == 2:
            nom = input("Choisir un nom de fichier")
    return nom





def main():
    fichier_choisi = ""
    menu = "1. Choisir un nom de fichier\n2. Ajouter un texte\n3. Afficher le fichier complet\n4. Vider le fichier\n9. Quitter le programme\n"
    menu2 = "1. Choisir un autre nom de fichier\n2. Ajouter un texte\n3. Afficher le fichier complet\n4. Vider le fichier\n9. Quitter le programme\n"
    if (fichier_choisi == ""):
        print(menu)
    else:
        print(fichier_choisi)
        print(menu2)


    choix = int(input("Choix : "))
    while choix not in [1, 2, 3, 4, 9]:
        choix = int(input("Reessayez : "))

    if choix == 1 : 
        fichier_choisi = menu_1()
        print(menu2)
        choix = int(input("Choix : "))
    if choix == 2 : 
        text = str(input("Entrez un texte a ajouter dans le fichier : "))
        with open(fichier_choisi, "w") as fichier_choisi:
            fichier_choisi.write(text)
    if choix == 3 : 
        with open(fichier_choisi, "r"):
            fichier_choisi.read()
    if choix == 4 : 
        open(fichier_choisi, 'w').close()
    if choix == 9: 
        exit()

main()
    



### q3

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __eq__(self, date):
        self.day = date.day
        self.month = date.month
        self.year = date.year

    def __lt__(self, date): #returns True if date is lesser than self 
        if (date.year < self.year):
            return True
        if (date.year == self.year):
            if date.month < self.month : 
                return True
            if date.month == self.month :
                if date.day < self.day:
                    return True 
                else: 
                    return False
            else : 
                return False
        else : 
            return False



class Etudiant():
    def __init__(self, nom, prenom, date_de_naissance):
        self.nom = nom
        self.prenom = prenom 
        self.date_de_naissance = date_de_naissance
    def creer_mail(self):
        mail = self.prenom + "." + self.nom + "@etu.univ-tours.fr"
        return mail
    def age(self):
        # date_de_naissace ressemble a "01/01/1970"
        today = date.today()
            # Calculation
        
        years = current_date.year - birth_date.year
        months = current_date.month - birth_date.month
        days = current_date.day - birth_date.day

        # Adjust for negative differences
        if days < 0:
            months -= 1
            days += get_days_in_month(birth_date.month, birth_date.year)
        if months < 0:
            years -= 1
            months += 12