
import numpy as np
print()

print("1. arrange: ")
rango = np.arange(10) # np.arrange(n) crea un vector de 0 a n-1
print(rango)
print()

print("2. Matriz Identidad: ")
identidad = np.eye(5) # np.eye(n) crea una matriz identidad de nxn
print(identidad)
print()

print("3. Matriz Diagonal: ")
diagonal = np.diag([1, 2, 3, 4])
print(diagonal)
print()

print("4. Matriz Aleatoria: ")
aleatoria = np.random.rand(3, 5) # np.random.rand(n,m) Crea una matriz de nxm con valores aleatorios entre 0 y 1 
print(aleatoria)
print()

print("5. Matriz Aleatoria Pro: ")
import numpy as np

# Crear una matriz de 3 filas x 4 columnas con enteros aleatorios entre 5 y 30
matriz = np.random.randint(5, 30, (3, 4))
print(matriz)
