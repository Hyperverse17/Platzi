
# La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.

# Sintaxis.
# map(function, iterables)
# Para estos fines es posible usar lambda en vez de una función prefefinida

import random

numbers1 = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
numbers2 = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]

print("1. Uso de lambda para elevar al cuadrado")
result1 = list(map(lambda x: x**2,numbers1))
print(numbers1, "- Original")
print(result1, "- al cuadrado")
print()

print("2. Ejemplo de uso de map() con dos listas")
result2 = list(map(lambda x, y: x + y, numbers1, numbers2))
print(numbers1, "- Lista 1")
print(numbers2, "- Lista 2")
print(result2, "- Suma")
print()

# En caso de que la cardinalidad de las listas sea diferente, map() no regresa error, más bien actúa sobre el total de elementos menor
