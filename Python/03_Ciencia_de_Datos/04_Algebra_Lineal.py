
import numpy as np

print()
print("Operaciones Básicas. Sean las:")
print()

A = np.array([[1, 2], [3, 4]]) # matriz 2x2
B = np.array([[5, 6], [7, 8]])

print(f"Matriz A:\n {A}")
print()
print(f"Matriz B:\n {B}")
print()

# La suma de matrices se realiza elemento por elemento. Por ejemplo, si tenemos dos matrices A y B:
suma = A + B
print("1. Suma de matrices\n",suma)
print()

# La multiplicación de matrices combina filas de una matriz con columnas de otra. Por ejemplo, si tenemos las mismas matrices A y B:
producto = np.dot(A, B)
print("2. Multiplicación de Matrices\n",producto)
print()

# El determinante de una matriz cuadrada es un valor único
determinante = np.linalg.det(A)
print("3. Determinante de A:", determinante)
print()

# La inversa de una matriz A es una matriz A' tal que A x A' = I (identidad)
inversaA = np.linalg.inv(A)
print("4. Inversa de A:\n", inversaA)
print()
result = np.dot(A,inversaA)
print("Resultado de A x A':\n", result)
print()

# Valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(A)
print("5. Valores propios de A:\n", valores_propios)
print()
print("6. Vectores propios de A:\n", vectores_propios)
print()

# Resolucion de sistemas de ecuaciones lineales del tipo AX=B donde A es la atriz de coeficientes, X el vector de incógnitas y B el vetor de resultados
C = np.array([
    [2, 1, -1], 
    [-3, -1, 2], 
    [-2, 1, 2]]) # matriz 3x3

D = np.array([1, -4, -2])
E = np.linalg.solve(C, D)

print("7. Solución del sistema AX = B:\n", E)
