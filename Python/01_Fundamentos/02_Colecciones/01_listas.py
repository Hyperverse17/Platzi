
# Listas en Python:
# Una lista en Python es una colección ordenada de elementos que puede contener elementos de diferentes tipos (enteros, flotantes, cadenas, etc.). Las listas son mutables, lo que significa que sus elementos se pueden cambiar después de que se ha creado la lista.
# Es importante mencionar que las posiciones en las listas siempre se consideran a contar desde cero

# Ejemplo 1: Lista de actividades:
print()
print("--- Listas ---")
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
print()

# Ejemplo 2: Lista compuesta de enteros y strings
numbers = [1, 2, 3, 4, "cinco"] # <class 'list'>
print(type(numbers))
print()

# Ejemplo 3: Una lista puede contener cualquier tipo de elementos. Incluso más listas
mix = ["uno", 2, 3.14, True, [4,5,"seis"], False, "Otelo", 33]
print(mix)
print(len(mix)) # La lista definida contiene 5 elementos. Las listas dentro de otras listas se consideran elementos únicos e independientes
print()

# Indexación
# Es posible hacer referencia a algún elemento específico de las listas
print("--- Indexación ---")
print("Primer elemento", mix[0]) # El primer elemento de una lista está en la posición cero
print("Segundo elemento", mix[1]) # Consecutivamente, el segundo elemento de una lista es la posición cero
print("Último elemento:", mix[-1]) # El último elemento de una lista viene dado por la posición -1
print("Penúltimo elemento:", mix[-2]) # Consecutivamente, el penúltimo elemento de una lista viene dado por la posición -2
# Finalmente, es posible btener la posición dado el elemento de la lista usando el método .index(<arg>):
print(mix.index("Otelo"))
print()
# Slicing: es posible obtener sólo una porción definida de una lista
print("--- Slicing ---")
print(mix[2:-2]) # Regresará una nueva lista con elementos desde la segunda posición hasta uno antes de la penúltima posición.
# python considera sus elementos como cerrados a la izquierda pero abiertos a la derecha [)
print()
print("--- Métodos ---")

# Metodos útiles
mix.append(False) # Agrega une lemento al final de la lista
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"]) # A didferencia de .append(), .insert(<arg1>,<arg2>) agrega <arg2> en la posición <arg1> 
print(mix)
print()

# Funciones max y min
print("--- Max y Min ---")
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers)) # Devuelve el elemento mayor
print("Menor:",min(numbers)) # Devuelve el elemento menor
print()

# función del <lista>[<posición>]. Se usa para eliminar elementos de una lista dadas las posiciones
print("--- del ---")
del numbers[-1] # Elimina el último elemento
print(numbers)
del numbers[:2] # Elimina elementos desde la primera posición hasta la TERCERA (2) posición
print(numbers)
del numbers # Elimina por completo la lista
#print(numbers) # Esta línea regresa un error porque la lista ha dejado de existir
