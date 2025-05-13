
# reduce() es una función que toma una lista (u otro iterable) y la reduce a un solo valor, aplicando una función de dos argumentos de manera acumulativa.

# reduce() no está directamente en el núcleo de Python, así que debes importarla desde el módulo functools

from functools import reduce

# Sintaxis básica: reduce(función, iterable[, valor_inicial]), donde:
# función: toma dos argumentos (el acumulador y el siguiente elemento).
# iterable: lista o tupla que quieres reducir.
# valor_inicial (opcional): valor desde el cual empieza la acumulación.
print()
print("1. Ejemplo básico de suma de los números de una lista:")
numbers = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
print(numbers)
result = reduce(lambda accum, x: accum + x, numbers)
print(result)  # Resultado: 15
print()

print("2. Ejemplo con multiplicación")
print(numbers)
result = reduce(lambda accum, x: accum * x, numbers)
print(result)  # Resultado: 15
print()


print("2. Ejemplo básico de suma de los números de una lista comenzando desde un valor específico:")
numbers = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
result = reduce(lambda accum, x: accum + x, numbers, 5) # Ojo, es el valor inicial del contador, no el valor inicial del iterable
print(result)
print()
