
# La función Lambda es una función anónima, es decir, sin un nombre definido y se define en una sola línea usando la palabra clave lambda. 
# # Estas funciones son útiles para operaciones simples y cortas que se pueden definir rápidamente sin la necesidad de una función formal.
# Sintaxis: variable = lambda arg1, arg2, ..., argn : expresión. argumentos son los argumentos de entrada separados por comas, expresion hace las veces del return

print()
print("Función Lambda:")
print()

#Ejemplo 1: Suma básica
add = lambda a,b : a + b
print(add(6,7))

# Se puede devolver cualquier tipo de dato
boolean = lambda x : x%2 == 0
print(boolean(7)) # Devuelve False
print(boolean(18)) # Devuelve True
print()

# Ejemplo 2: Suma de los primeros n números naturales
sigma = lambda n : int((n*(n+1)/2))
n = int(input("Ingresa un límite: "))
print(sigma(n))
print()

#Ejemplo 3: Obtención de cuadrados aplicando una función a los elementos de usando un arreglo
limit = int(input("Ingresa un límite: "))
numbers = range(limit)
squares = list(map(lambda x : x*x, numbers)) # map(<function>, <array>) aplica <function> sobre los elementos del <array>
# list() Crea una nueva lista a partir de un objeto iterable.
# map() 
print(squares)
print()

# Ejemplo 4: Uso de condicionales para filtrar

limit = int(input("Ingresa un límite: "))
numbers = range(limit)
evenNumbers = list(filter(boolean,numbers)) # filter(), es similar a map(), sin embargo, sólo toma (filtra) los valores que son true 
print(evenNumbers)
print()
