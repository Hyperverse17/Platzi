
import numpy as np
matrix = np.random.randint(0, 10, (3, 3))
print()
print(f"1. Transpuesta de una matriz")
transposed_matrix = matrix.T # Método T
print(f"Sea la siguiente matriz:\n{matrix}\n\nSu transpuesta se obtiene con el método .T:\n{transposed_matrix}\n")

print(f"2. Reshape")
# Crea un array con los números del 1 al 12
array = np.random.randint(0, 10, 12) # Es un arreglo con 12 valores aleatorios entre [0, 10)
# Cambia la forma del array a una matriz de 3 filas y 4 columnas
reshaped_array3x4 = array.reshape(3, 4)
reshaped_array2x6 = array.reshape(2, 6)
reshaped_array4x3 = array.reshape(4, 3) 
print(f"Se tiene el siguiente array: {array}\nSu reestructura en 3x4, queda así:\n{reshaped_array3x4}\n\nSu reestructura en 2x6, queda así:\n{reshaped_array2x6}\n\nSu reestructura en 4x3, queda así:\n{reshaped_array4x3}\n")

print(f"3. Inversión de array")
# Crea un array con los números del 1 al 5
array = np.random.randint(0, 10, 5)  
# Invierte el array
reversed_array = array[::-1]  # array[::-1] Invierte el array utilizando slicing. 
print(f"Se tiene el siguiente array: {array}\nSu inverso es: {reversed_array}\n")

print(f"4. Flattening")
# Crea un array 2D
matrix = np.random.randint(0, 10, (3, 3))
# Aplana el array 2D a 1D
flattened_array = matrix.flatten()  
print(f"Se tiene la siguiente matriz:\n {matrix}\n\nSu versión plana es: {flattened_array}\n\n")
