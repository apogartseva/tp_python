from enum import Enum
import random

SEUIL_LUMINANCE = 40

def generate_random_color():
    # Générer des valeurs aléatoires pour les composantes RGB
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Retourner la couleur au format RGB
    return (red, green, blue)

def generer_probabilites():
    # Générer trois nombres aléatoires entre 0 et 1
    Pd = random.random()
    Pg = random.random()
    Pt = random.random()
    
    # Normaliser les probabilités pour que leur somme soit égale à 1
    somme_probabilites = Pd + Pg + Pt
    Pd /= somme_probabilites
    Pg /= somme_probabilites
    Pt /= somme_probabilites
    
    # Retourner les probabilités normalisées
    return Pd, Pg, Pt

# Créer une liste de 10 couleurs aléatoires
liste_couleurs = [generate_random_color() for _ in range(10)]



class Direction(Enum):
    HAUT = "Haut"
    BAS = "Bas"
    GAUCHE = "Gauche"
    DROITE = "Droite"
    
class Fourmi:
    def __init__(self, taille_toile):
        # on donne une position aléatoire à la fourmi sur la toile
        self.position = (random.randint(0,taille_toile), random.randint(0,taille_toile))
        self.couleur = random.choice(liste_couleurs)
        self.couleur_suivie = random.choice(liste_couleurs)
        self.probabilite = generer_probabilites()                #vecteur probabilité d'aller tout à gauche, droite ou tout droit     
        self.taille_diffusion = random.uniform(0, 1)
        self.direction = random.choice(Direction.HAUT,Direction.BAS,Direction.DROITE,Direction.GAUCHE)
        self.taille_toile = taille_toile # taille de la toile qui est un carré

    def deplacer(self):
            # fonction qui calcule les proba
            rand = random.random()
            if rand < self.probabilite[0]:
                self.avancer_tout_droit()
            elif rand < self.probabilite[0] + self.probabilite[1]:
                self.tourner_droite()
            else:
                self.tourner_gauche()

    def tourner_gauche(self):
        if self.direction == Direction.HAUT:
            self.direction = Direction.GAUCHE
        elif self.direction == Direction.GAUCHE:
            self.direction = Direction.BAS
        elif self.direction == Direction.DROITE:
            self.direction = Direction.HAUT
        else:
            self.direction = Direction.DROITE

    def tourner_droite(self):
        if self.direction == Direction.HAUT:
            self.direction = Direction.DROITE
        elif self.direction == Direction.GAUCHE:
            self.direction = Direction.HAUT
        elif self.direction == Direction.DROITE:
            self.direction = Direction.BAS
        else:
            self.direction = Direction.GAUCHE

    def move(self, couleurs_environnantes):
        # appelle fonction pour savoir si on peut suivre une couleur
        if(any(couleur != (255, 255, 255) for couleur in couleurs_environnantes)):
            # appelle la fonction pour tourner si besoin (vers couleur suivie)
            pass
        else : 
        # appelle la fonction pour avancer d'un pas
            self.avancer_tout_droit()
        pass

    def avancer_tout_droit(self):
        x, y = int(self.position[0]), int(self.position[1])
        if self.direction == Direction.HAUT:
            self.position = (x, self.taille_toile if y == 0 else y - 1)
        elif self.direction == Direction.GAUCHE:
            self.position = (self.taille_toile if x == 0 else x - 1, y)
        elif self.direction == Direction.DROITE:
            self.position = (0 if x==self.taille_toile else x + 1, y)
        else:
            self.position = (x,0 if y==self.taille_toile else y + 1,)

    def suivre_odeur(self, toile):
        # Implémentez la logique pour suivre l'odeur sur la toile
        pass


    def calcul_luminance(codeCouleur):
        return (0,2426 * codeCouleur.red + 0,7152 * codeCouleur.green + 0,0722 * codeCouleur.blue)
    
    def difference_luminance(self,codeCouleur):
        return abs(self.calcul_luminance(self.couleur) - self.calcul_luminance(codeCouleur))
    
 