
# Operaciones matemáticas con Python

# Dados a y b...
a = 15
b = 4

# Operaciones básicas
print("--- Operaciones Básicas ---")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print()

# Operaciones no tan básicas
print("--- Operaciones no tan Básicas ---")
print("Parte entera de la división:", a // b)
print("Módulo:", a % b) # Devuelve el residuo de realizar alguna división
print()

print("--- Shortcuts ---")
# Shortcuts es posible modificar una variable dada:
c = 17
# Por ejemplo sumar cualquier cantidad a c
# c = c + 3 -> c += 3 (shortcut)
c += 3
print(c)

# Este shortcut se puede extender al resto de las operaciones
c -= 5
print(c)

c *= 3
print(c)

c /= 9
print(c) 

c **= 2 # Incluso con operadores más complejos
print(c)
print()

# Criterio PEMDAS. Es un criterio de orden para operar: Paréntesis, Exponenciación, Multiplicación, División, Adición y Sustracción 
print("--- PEMDAS ---")
operation_1  = 2 + 3 * 4 # De acuerdo con PEMDAS, se realiza primero la multiplicación
operation_2  = (2 + 3) * 4 # Este resultado será distindo al anterior porque de acuerdo con PEMDAS, las operaciones entre paréntesis se realizan primero
print(operation_1)
print(operation_2)

operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_3)
print()