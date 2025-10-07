import numpy as np

print()
respuestas = np.array(['bueno', 'excelente', 'malo', 'bueno', 'bueno', 'bueno', 'malo', 'excelente', 'bueno', 'malo', 'malo', 'excelente', 'aceptable','Bueno'])
# Supongamos que tenemos la variable 'respuestas' con las opiniones de los clientes
print("1. Elementos Unicos")
print(f"Se tiene el siguiente arreglo de respuestas:\n {respuestas}\n")
elementos_unicos = np.unique(respuestas) #Nótese que distingue entre minúsculas y mayúsculas
print(f"Se Utiliza el método unique para encontrar los elementos únicos\n {elementos_unicos}\n\n")

print("2. Frecuencia")
elementos_unicos, frecuencia = np.unique(respuestas, return_counts=True)
print(f"Para contar la frecuencia de cada elemento se usa el parámetro 'return_counts = True'\n{elementos_unicos}\n{frecuencia}")
# Contar las frecuencias de los elementos únicos

