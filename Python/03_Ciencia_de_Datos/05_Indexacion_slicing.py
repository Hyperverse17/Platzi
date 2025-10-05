
import numpy as np

print()
array = np.random.randint(0, 20, 10) # Genera un arreglo con 10 numeros aleatorios entre 0 y 19 

print()

print("1.Indexación en Arreglos: ")
print()
print(f"Sea el siguiente array: {array}")

# Es la forma de acceder a los elementos de un array por medio de su índice.
# Los indices empiezan a partir del 0 que representa el primer elemento del array.

print("Elemento en la posición 5           : ", array[5])
print("Elemento en la primer posición      : ", array[0])
print("Elemento en la última posición      : ", array[-1])
print("Elemento en la ante última posición : ", array[-2])
print()

print("2. Indexación Booleana")
# Es una forma de obtener datos a partir de una condición. Todos los elementos de un array que cumplan con la condición serán “devueltos”.
print()
print(f"Sea el siguiente array   : {array}")
bool_index = array > 5 # Guarda en la variable bool_index todos los elementos mayores a 5 
print("Array booleano  (>5)     :", bool_index)
print("Elementos mayortes a 5   :", array[bool_index])
print("Elementos entre (5,7]    :", array[(array > 5 ) & (array <= 7)])
print()

print("3. Indexación por listas")
print()
print(f"Sea el siguiente array                  : {array}")
# Permite obtener multiples elementos de un array con una lista de indices. 
# Al mandarle indices “desordenados” el array resultante obtiene los elementos en el orden en que se pasó el índice centro de la lista.
positions_list = [3,8,5,0]
print("Elementos en las posiciones 3,8,5 y 0   :",array[positions_list])
print("Elementos en las posiciones -1, 2,3 y 5 :",array[[-1,2,3, 5]])
print()

print("4. Indexación de arrays multidimensionales")
print()
# Para acceder a un elemento de un array bidimensional, le indicamos 2 indices.
# [indice_fila, indice_columna]

matrix = np.random.randint(0, 10, (5,5))
print("Sea la siguiente matriz 5x5: ")
print(matrix)
print()
print("Elemento de la fila 2, columna 2                        :", matrix[2,2]) # Elemento especifio
print("Elementos de las fila 1 y 2, columna 2                  :", matrix[[1,2],2]) # Indexaciónb por lista (1)
print("Elementos en la fila 1 , columna 2, y fila 3, columna 2 :", matrix[[1,2,3],2]) # Indexaciónb por lista (2)
print("Elementos mayores a 7                                   :", matrix[matrix > 7]) # Indexación booleana
print()

# Slicing
# Selección de sub-arrays, donde le indicamos el índice inicial e índice final del conjunto original.
# También se se pueden agregar “saltos”
print("5. Sicing")
print()
print(f"Sea el siguiente array                             : {array}")
print("Elementos desde el incio hasta la posición 2       :", array[:3])
print("Elementos desde la posición 5 hasta el final       :", array[5:])
print("Elementos desde la posición 5 hasta la posición 10 :", array[5:9])
print("Elementos desde la posición hasta la penultima posición dando 2 saltos:", array[3:-2:2])
print()

print("Sea la siguiente matriz 5x5: ")
print(matrix)
print()
print("Elementos a partir de la fila uno, y columnas a partir de la fila 2:\n", matrix[1:, 2:])
print()
print("Elementos hasta la fila 3, y hasta la columna 2:\n", matrix[:3, :2])
print()
print("Elementos a partir de la fila 1 dando 2 saltos, hasta la columna 1 dando 2 saltos\n",matrix[1::2, :1:2])
print()
