
# El List Comprehension es una técnica poderosa y eficiente en Python que permite generar listas de manera concisa. Su sintaxis más corta y directa mejora la legibilidad del código, uno de los principios fundamentales de Python. Con List Comprehension, puedes transformar números, aplicar funciones y establecer condiciones dentro de una lista, todo en una sola línea de código. 
# Sintaxis básica: list = [element for element in iterable] 

# 1. Creación de una lista simple usando el método tradicional
print("1 Forma tradicional:")
list1 = [] # Línea 1
for number in range(0,10): # Línea 2
    list1.append(number) # Línea 3

print(list1)
print()

# 2. Uso de Comprehension Lists
print("2. Comprehension List:")
list2 = [number for number in range(1,21)] # Creación en una sola línea!
print(list2)
print()

# 3. Operación de los elementos
print("3. Operación de los elementos:")
list3 = [((number*17)+3) for number in range(1,11)] # Creación en una sola línea!
print(list3)
print()


print("4. Uso de funciones:")

def kelvin(celsius):
    """Recibe grados celsius y la convierte a kelvin"""
    kelvin = celsius + 273
    return kelvin

def fahrenheit(celsius):
    """Recibe grados celsius y la convierte a fahrenheit"""
    fahrenheit = round((celsius * 9 / 5) + 32,2)
    return fahrenheit

cels    = [celsius for celsius in range(0,31)]
kelvins = [kelvin(celsius) for celsius in range(0,31)] # Creación en una sola línea!
fahrenheit = [fahrenheit(celsius) for celsius in range(0,31)] # Creación en una sola línea!
print(cels)
print(kelvins)
print(fahrenheit)
print()

# Comprehension Lists condicionales
# Sintaxis básica: list = [element for element in iterable if condition]

print("5. Creacion de un Comprehension List condicional con múltiplos de 5")
list3 = [element for element in range(1,101) if element % 5 == 0] # % operación módulo
print(list3)
print()
