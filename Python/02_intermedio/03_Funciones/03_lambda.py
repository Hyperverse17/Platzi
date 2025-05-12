
# Una lambda function en Python es una forma rápida y compacta de escribir funciones pequeñas. También se llaman funciones anónimas porque no necesitan un nombre (aunque puedes asignarles uno si quieres).

# Sintaxis básica:
# lambda argumentos: expresión
# Son muy útiles cuando necesitas una función pequeña, por ejemplo, cuando trabajas con funciones como map(), filter() o sorted():

def square(x:int) -> int:
    """Función tradicional que eleva la entrada al cuadrado"""
    return x * x

print()
print("0. Función tradicional:")
print(square(7))  # Resultado: 49
print()

print("1. Uso de Lambda con map():")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Usando map con una función lambda para elevar al cuadrado
# map(función, iterable)

# función: lo que quieres aplicar a cada elemento.
# iterable: una lista, tupla, etc.

# Nota:
# map no devuelve una lista directamente, sino un objeto especial tipo map, por eso usamos list() para ver los resultados.

squaresTrad = list(map(square, numbers))
print(squaresTrad, "- Forma tradicional")
squaresLambda = list(map(lambda x: x * x, numbers)) # en este caso el argumento "función de map es precisamente Lambda"
print(squaresLambda, "- Con uso de Lambda")  # Resultado: [1, 4, 9, 16, 25]
print()

print("2. Uso de Lambda con filter():")
# filter() sirve para filtrar elementos de una lista que cumplan cierta condición.
# Ejemplo Filtrar solo los pares
pairs = filter(lambda x: x % 2 == 0, numbers) #filter(condición, iterable)

print(list(pairs))
print()

print("3. Uso de Lambda con sorted():")
# sorted() sirve para ordenar listas. Puedes usar lambda para decirle cómo ordenar.
persons = [("Mayeya", 29), ("Otelo", 33), ("Heidi", 12), ("Lola", 10)] # una lista de tuplas

# Ordenar por edad (segundo valor)
ageOrdered = sorted(persons, key=lambda x: x[1])

# Recordemos que cada elemento es una tupla con dos partes:
# x[0]: el nombre ("Ana", "Luis", etc.)
# x[1]: la edad (25, 20, etc.)

# La función sorted() necesita saber por qué criterio ordenar.
# key= le dice a sorted() qué parte de cada elemento usar para comparar.
# lambda x: x[1] es una función anónima que toma cada tupla x y devuelve su edad (x[1]), es decir, el segundo elemento.
# En resumen se ordena la lista de personas usando la edad (x[1]) como criterio

print(ageOrdered)
print()


