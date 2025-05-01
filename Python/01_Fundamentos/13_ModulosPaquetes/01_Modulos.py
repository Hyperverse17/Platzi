
# Un módulo es simplemente un archivo .py que contiene definiciones de funciones, clases o variables que puedes importar.

import random
from Calculator import suma, resta # De esta forma se importan elementos de un módulo

print("")
a = random.randint(0,9)
b = random.randint(0,9)
print(f"1. El resultado de {a} + {b} es: {suma(a,b)}")
print(f"2. El resultado de {a} - {b} es: {resta(a,b)}")  
# print(f"3. El resultado de {a} * {b} es: {multiplicacion(a,b)}") # Marca error porque no se ha importado esta funcion
print("---")

from Calculator import * # De esta forma se importan todos los elementos de un módulo
print("")
print(f"1. El resultado de {a} + {b} es: {suma(a,b)}")
print(f"2. El resultado de {a} - {b} es: {resta(a,b)}")
print(f"3. El resultado de {a} * {b} es: {multiplicacion(a,b)}")
print(f"4. El resultado de {a} / {b} es: {division(a,b)}")
print("")
