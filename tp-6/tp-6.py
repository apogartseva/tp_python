import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PIL import Image, ImageFilter, ImageOps

import os

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

# q1
# tableau avec shape (4, 3, 2) avec les nombres aléatoires
array = np.random.rand(4, 3, 2)

# array attributes
print("Array:")
print(array)

print("\nAttributes:")
print("ndim:", array.ndim)
print("shape:", array.shape)
print("size:", array.size)
print("dtype:", array.dtype)
print("itemsize:", array.itemsize)
print("data:", array.data)


#q2

matrix1 = np.arange(9).reshape(3,3)
matrix2 = np.arange(2, 11).reshape(3,3)

print("Matrice 1:")
print(matrix1)
print("\nMatrice 2:")
print(matrix2)

product = matrix1 * matrix2
print("\nProduit élément par élément:")
print(product)

dot_product = np.dot(matrix1, matrix2)
print("\nProduit scalaire:")
print(dot_product)

transposed_matrix = matrix1.T
print("\nMatrice transposée:")
print(transposed_matrix)

#q3

det = np.linalg.det(matrix1)
print("\nDéterminant de la matrice 1:", det)  # le déterminant vaut 0 et la matrice n'est pas inversible


# on créé une nouvelle matrice qui serait inversible 

matrix_inv = np.array([[1, 1, 2], [1, 2, 1], [2, 1, 1]])
print("\nDétérminant de la matrice inversible: ", np.linalg.det(matrix_inv))
inverse_matrix = np.linalg.inv(matrix_inv)
print("\nInverse de la matrice: \n", inverse_matrix)

# il existe une solution unique si la matrice est inversible 
constants = np.array([1, 2, 3])
lineq = np.linalg.solve(matrix_inv, constants)
print("\nSolution d'un système d'équations linéaires: ", lineq)



# valeurs propres de la matrice 
eigenvalues, eigenvectors = np.linalg.eig(matrix1)


print("\nValeurs propres de la matrice:")
print(eigenvalues)

print("\nVecteurs propres de la matrice:")
print(eigenvectors)
# q4


x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([3, 5.12, 17, 27, 34])

# nous avons mis les points croissants, on imagine que c'est ajustable par une droite linéaire
def func(x, a, b):
    return a * x + b

# on ajuste la fonction aux données
params, covariance = curve_fit(func, x_data, y_data)

print("Paramètres ajustés par curve_fit:", params)
print("Matrice de covariance:", covariance)

plt.scatter(x_data, y_data, label='Données')
plt.plot(x_data, func(x_data, *params), label='Ajustement)')
plt.legend()
plt.show()


#q5 

image_path = "tp-6/duck.jpg"
image = Image.open(image_path)


#image originale
image.show()

#10% de la taille originale
width, height = image.size
new_width = int(width * 0.1)
new_height = int(height * 0.1)
small_image = image.resize((new_width, new_height))
small_image.show()


#q6 


grayscale_image = image.convert("L")
inverted_image = ImageOps.invert(grayscale_image)

pencil_sketch = inverted_image.filter(ImageFilter.BLUR)

final_sketch = ImageOps.invert(pencil_sketch)
final_sketch.save('tp-6/duck_pencil_sketch.jpg')







