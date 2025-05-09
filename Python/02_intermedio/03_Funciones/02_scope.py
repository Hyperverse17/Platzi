
x = 10  # Variable global

def mi_funcion():
    y = 5  # Variable local
    print("Dentro de la función:")
    print("x =", x)  # Se puede usar x porque es global
    print("y =", y)  # y existe solo dentro de esta función

print()
mi_funcion()

# Fuera de la función
print("Fuera de la función:")
print("x =", x)  # x sigue existiendo
# print("y =", y)  # Esto da error porque y solo existe dentro de la función
