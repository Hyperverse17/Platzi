
import numpy as np

print()
print("1. Broacasting: ")
print()
# El Broadcasting es una funcionalidad poderosa en NumPy que permite realizar operaciones aritméticas en arrays de diferentes tamaños y formas de manera eficiente. 
# En lugar de iterar sobre cada elemento de los arrays para realizar las operaciones, NumPy extiende automáticamente los arrays más pequeños para que coincidan con las dimensiones de los más grandes, sin duplicar datos. Esto no solo optimiza el uso de la memoria, sino que también acelera significativamente las operaciones.
# El broadcasting permite que las operaciones entre arrays de diferentes dimensiones se realicen como si todos los arrays tuvieran la misma forma. 
# NumPy extiende los arrays más pequeños a la forma del más grande de manera implícita, facilitando las operaciones sin necesidad de copiar los datos.

prices = np.array([100, 200, 300]) # Lista de precios
tax1 = np.array([1.16]) # Aplicación del IVA
taxedPrices = prices * tax1
print(f"Sea la siguiente lista de precios: {prices} \nSe le aplicará un iva del 16%: {taxedPrices}")
print()

print("2. Operaciones con Arrays Multidimensionales")
# Podemos realizar operaciones elementales entre arrays de diferentes dimensiones.
print()

matrixA = np.array([[0.0, 0.0, 0.0],
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])

arrayB = np.array([1.0, 2.0, 3.0])
result = matrixA + arrayB

print(f"Sea la siguiente matriz:\n {matrixA}\n\ny el siguiente arreglo: {arrayB}")
print(f"El resultado de sumerlos es:\n {result}")
print()

print("3. Compatibilidad: ")
print("Compatibilidad array 1D y Escalar 0D")
array1  = np.array([1, 2, 3])
scalar1 = 2
result = array1 * scalar1
print(f"Sea el array: {array1} y el escalar: {scalar1}")
print(f"El resultado de multiplicarlos es: {result}")  # Output: [2 4 6]
print()

matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #3x3
arrayB = np.array([1, 0, 2]) # 1x3
result = matrixA * arrayB
print("Compatibilidad array 1D y matriz 2D")
print(f"Sea la matriz:\n{matrixA}\n\ny el arreglo: {arrayB}\n")
print(f"El resultado de multiplicarlos es:\n{result}")
# Output:
# [[1 0 3]
#  [4 0 6]
#  [7 0 9]]

