

# La librería collections en Python es un módulo estándar que extiende las capacidades de las estructuras de datos básicas, proporcionando tipos de datos especializados y optimizados para distintas necesidades.

from collections import * # Defalultdict se usa para valores por defecto

# Ejemplo 1: Counter
# Es una subclase de dict diseñada para contar elementos repetidos en una colección (listas, cadenas, tuplas, etc.).

print()
text = "Torment your soul with hell's rock n' roll"
counter = Counter(text)
print(counter)
print()

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8, 8, 9]
counter = Counter(numbers)
print(counter)

# Otros métodos útiles
# most_common(n): Devuelve los n elementos más comunes.
# elements(): Devuelve un iterador con los elementos contados.

print(counter.most_common(1))
print()

# Ejemplo 2: Default Dict
# Es similar a un diccionario normal (dict), pero si accedes a una clave inexistente, en lugar de lanzar un error, crea automáticamente un valor por defecto.

myDictionary = defaultdict(int)  # int() retorna 0 por defecto cuando no existe la llave de referencia
myDictionary["newKey"] += 1
print(myDictionary["newKey"])  # Salida: 1
print(myDictionary["inexistent"])  # Salida: 0 (no lanza error)
print(myDictionary)
print()

# Ejemplo 3: Default dict con list por defecto

myDictionary2 = defaultdict(list)
myDictionary2["colores"].append("azul")
print(myDictionary2["colores"])  # Salida: ['azul']

# Otras clases interesantes
# deque	Lista optimizada para agregar/quitar elementos de ambos extremos.
# namedtuple	Tupla con nombres en sus campos.
# OrderedDict	Diccionario que mantiene el orden de inserción (obsoleto en Python 3.7+).
# ChainMap	Agrupa múltiples diccionarios en uno solo.
# UserDict, UserList, UserString	Permiten extender diccionarios, listas y cadenas.
