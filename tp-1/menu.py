import os
from pathlib import Path

print("Bonjour le monde!")

def menu_1():
    nom = input("Entrez un nom de fichier avec extension : ")
    
    while not os.path.exists(nom):
        print(f"Le fichier {nom} n'existe pas.")
        action_fichier = int(input("Voulez-vous le créer (1) ou choisir un autre (2) ? Choix : "))
        
        if action_fichier == 1:
            with open(nom, "w+"):
                pass
            print(f"Le fichier est créé dans {Path.cwd()}")
        elif action_fichier == 2:
            nom = input("Choisir un autre nom de fichier : ")

    return nom

def menu_2(fichier_choisi):
    menu = "1. Choisir un autre nom de fichier\n2. Ajouter un texte\n3. Afficher le fichier complet\n4. Vider le fichier\n9. Quitter le programme\n"
    
    print(fichier_choisi)
    print(menu)

    choix = int(input("Choix : "))
    while choix not in [1, 2, 3, 4, 9]:
        choix = int(input("Reessayez : "))

    if choix == 1:
        fichier_choisi = menu_1()
    elif choix == 2:
        text = str(input("Entrez un texte à ajouter dans le fichier : "))
        with open(fichier_choisi, "a") as fichier:
            fichier.write(text + '\n')
    elif choix == 3:
        with open(fichier_choisi, "r") as fichier:
            contenu = fichier.read()
            print(contenu)
    elif choix == 4:
        open(fichier_choisi, 'w').close()
        print("Le fichier a été vidé.")
    elif choix == 9:
        exit()

    return fichier_choisi

def main():
    fichier_choisi = ""
    menu_principal = "1. Choisir un nom de fichier\n2. Ajouter un texte\n3. Afficher le fichier complet\n4. Vider le fichier\n9. Quitter le programme\n"

    print(menu_principal)

    choix = int(input("Choix : "))
    while choix not in [1, 2, 3, 4, 9]:
        choix = int(input("Reessayez : "))

    if choix == 1:
        fichier_choisi = menu_1()
        print(menu_principal)
        choix = int(input("Choix : "))

    while True:
        if choix == 9:
            exit()
        else:
            fichier_choisi = menu_2(fichier_choisi)
            print(menu_principal)
            choix = int(input("Choix : "))

if __name__ == "__main__":
    main()
