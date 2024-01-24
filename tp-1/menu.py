import os

import os

def choisir_fichier():
    try:
        nom = input("Entrez un nom de fichier avec extension : ")
        assert nom.endswith('.txt'), "Le fichier doit avoir une extension .txt"
        return nom
    except AssertionError as e:
        print(f"Erreur lors du choix du fichier : {e}")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None


def creer_fichier(nom):
    try:
        with open(nom, 'w+'):
            print(f"Le fichier {nom} a été créé dans {os.getcwd()}")
            return nom
    except Exception as e:
        print(f"Erreur lors de la création du fichier : {e}")
        return None
    else:
        print("Création du fichier réussie.")
    finally:
        print("Fin du processus de création du fichier.")

def ajouter_texte(nom):
    try:
        texte = input("Entrez un texte à ajouter dans le fichier : ")
        with open(nom, 'a') as fichier:
            fichier.write(texte + '\n')
        print("Le texte a été ajouté au fichier.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de texte au fichier : {e}")
    else:
        print("Ajout de texte réussi.")
    finally:
        print("Fin du processus d'ajout de texte.")

def afficher_contenu(nom):
    try:
        with open(nom, 'r') as fichier:
            contenu = fichier.read()
            print(contenu)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    else:
        print("Lecture du fichier réussie.")
    finally:
        print("Fin du processus de lecture du fichier.")

def vider_fichier(nom):
    try:
        open(nom, 'w').close()
        print("Le fichier a été vidé.")
    except Exception as e:
        print(f"Erreur lors de la suppression du contenu du fichier : {e}")
    else:
        print("Vidage du fichier réussi.")
    finally:
        print("Fin du processus de vidage du fichier.")

def main():
    fichier_choisi = ""

    while True:
        print("1. Choisir un nom de fichier")
        print("2. Ajouter un texte")
        print("3. Afficher le fichier complet")
        print("4. Vider le fichier")
        print("9. Quitter le programme")

        choix = input("Choix : ")

        if choix == "1":
            fichier_choisi = choisir_fichier()
            if fichier_choisi and not os.path.exists(fichier_choisi):
                fichier_choisi = creer_fichier(fichier_choisi)

            print(f"Fichier choisi : {fichier_choisi}")

        elif choix == "2":
            if not fichier_choisi:
                print("Veuillez d'abord choisir un fichier.")
            else:
                ajouter_texte(fichier_choisi)

        elif choix == "3":
            if not fichier_choisi:
                print("Veuillez d'abord choisir un fichier.")
            else:
                afficher_contenu(fichier_choisi)

        elif choix == "4":
            if not fichier_choisi:
                print("Veuillez d'abord choisir un fichier.")
            else:
                vider_fichier(fichier_choisi)

        elif choix == "9":
            break

        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
