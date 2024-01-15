from enum import Enum
import random


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
    def __init__(self, largeur, hauteur, mouvement_droit, direction):
        # on donne une position aléatoire à la fourmi sur la toile
        self.position[0] = random.randint(0,hauteur)
        self.position[1] = random.randint(0,largeur)
        self.couleur = random.choice(liste_couleurs)
        self.couleur_suivie = random.choice(liste_couleurs)
        while self.couleur_suivie==self.couleur:
            self.couleur_suivie = random.choice(liste_couleurs)
        self.probabilite = generer_probabilites()                #vecteur probabilité d'aller tout à gauche, droite ou tout droitl
        self.mouvement_droit = mouvement_droit        #boolean pour savoir si on est en mouvement droit ou oblique
        self.taille_diffusion = random.uniform(0, 1)
        self.direction = direction

    def deplacer(self):
            rand = random.random()
            if rand < self.prob_gauche:
                self.tourner_gauche()
            elif rand < self.prob_gauche + self.prob_droite:
                self.tourner_droite()
            elif rand < self.prob_gauche + self.prob_droite + self.prob_tout_droit:
                self.avancer()

    def tourner_gauche(self):
        if self.mouvement_droit == "Droit":
            self.position.x, self.position.y = self.position.y, -self.position.x
        else:
            angle = random.uniform(0, rl.PI / 2)
            self.position = rl.Vector2(self.position.x + rl.cos(angle), self.position.y + rl.sin(angle))

    def tourner_droite(self):
        if self.mouvement_droit == "Droit":
            self.position.x, self.position.y = -self.position.y, self.position.x
        else:
            angle = random.uniform(0, rl.PI / 2)
            self.position = rl.Vector2(self.position.x - rl.cos(angle), self.position.y - rl.sin(angle))

    def avancer(self):
        if self.mouvement_droit == "Droit":
            self.position.x += 1
        else:
            angle = random.uniform(0, rl.PI / 2)
            self.position = rl.Vector2(self.position.x + rl.cos(angle), self.position.y + rl.sin(angle))

    def deposer_odeur(self, toile):
        # Utilisez la taille de diffusion pour déposer l'odeur sur la toile
        # La logique exacte dépendra de votre implémentation spécifique
        pass

    def suivre_odeur(self, toile):
        # Implémentez la logique pour suivre l'odeur sur la toile
        pass

    def calcul_luminance():
        