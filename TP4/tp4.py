import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


nb_aleatoire = [random.randint(0, 10) for _ in range(100)]

# Courbe d'une série aléatoire
plt.plot(nb_aleatoire)
plt.ylabel('Liste valeur 1')
plt.show()

# Création de trois séries de valeur
val_Axe = [i for i in range(10)]  # Ajustez selon le nombre d'éléments dans vos listes
val1 = [random.randint(0, 150) for _ in range(10)]
val2 = [random.randint(0, 150) for _ in range(10)]
val3 = [random.randint(0, 150) for _ in range(10)]

# label permet de donner un nom à la courbe pour la légende
# b-- change le style de la courbe (devient haché)
# linewidth est la largeur de la courbe
# val_Axe permet de configurer les valeurs de l'axe des abcisses
plt.plot(val_Axe, val1, "b--", label="Course 1")
plt.plot(val_Axe, val2, "g", linewidth=5, label="Course 2")
plt.plot(val_Axe, val3, "r", label="Course 3")

# configuration de la fléche descriptive :
# l'emplacement de la pointe de la flèche, l'emplacement du contenu, le design de la flèche (couleur et l'épaisseur de la point)
plt.annotate('Anomalie', xy=(4, 80), xytext=(5.5, 75), arrowprops={'facecolor': 'black', 'shrink': 0.01})
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.legend()
plt.show()


# Création d'un histogramme
histogramme_values = [random.randint(0, 100) for _ in range(1000)]
plt.hist(histogramme_values, bins=50, density=1, facecolor='g', alpha=0.5, edgecolor='black')

plt.xlabel('Numéros des tickets')
plt.ylabel(u'Probabiliter de tirer le ticket')
plt.title('Histogramme des probabilités de tirer le ticket')
plt.axis([0, 100, 0, 0.02])
plt.grid(True)
plt.show()

# Création d'un camembert
name = ['DI', 'DII', 'DAE','DMS']
data=['7','2','50','10']
plt.pie(data,labels=name,autopct='%1.1f%%',startangle=90)
plt.title('Répartition selon spés femmes promotion 2023-2024')
plt.axis('equal')
plt.show()

# Création de données
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Initialisation de la figure
fig = plt.figure()

# Création de l'axe 3D
ax = fig.add_subplot(111, projection='3d')

# Affichage de la surface 2D dans l'espace 3D
ax.plot_surface(x, y, z, cmap='viridis')

# Affichage
plt.show()