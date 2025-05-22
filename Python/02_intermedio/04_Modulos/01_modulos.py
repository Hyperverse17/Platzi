
import random
import sys # Esta es la orma de importar módulos
from apps import utils1, utils2

print()
print("1. Es posible saber la ruta de un módulo con el método .path")
print(sys.path)
print()
# print(random.path) aunque no funciona con todos

print("2. importar de otra ruta")
a = random.randint(0,9)
b = random.randint(0,9)
c = utils1.suma(a,b)
print(f"La suma de {a} y {b} es: {c}")
d = utils2.resta(a,b)
print(f"La reata de {a} y {b} es: {d}")
print()
