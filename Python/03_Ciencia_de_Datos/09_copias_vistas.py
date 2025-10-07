
import numpy as np
print()

arrayX = np.arange(10)
vista = arrayX[1:3]

print("1. Ejemplo de modificación involuntaria de una vista")
print(f"Se tiene el siguiente arreglo: {arrayX} y la siguiente vista: {vista}\n")
# Modificar la vista
arrayX[1:3] = [10, 11]
print("Modifiando arreglo original...")
print(f"Si se modifica el arreglo original: {arrayX}, se modifica la vista: {vista}")
print("La vista refleja los cambios realizados en x, ya que es una porción del array original, mostrando la gran interdependencia entre ambos.\n")

print("2. Creación de una copia para no alterar la vista")
print(f"Se tiene el siguiente arreglo: {arrayX} y la siguiente vista: {vista}\n")
# Crear una copia de la porción del array
print("Copiando vista con el método .copy() ...")
copia = arrayX[1:3].copy()
# Hacer cambios en el array original
print("Modifiando arreglo original...")
arrayX[1:3] = [12, 13]
print(f"Ahora se tiene el siguiente arreglo: {arrayX} y la copia: {copia} que no fue afectada\n")
