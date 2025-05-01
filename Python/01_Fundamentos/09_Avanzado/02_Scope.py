
# Scope de las variables

import random

# Ejemplo 1. Variable global y local
x = 100 # variable global se puede usare en todo el script

def getNumber():
    """Función que devuelve un número aleatorio"""
    number = random.randint(1,x) # number es una variable local, no se puede usar fuera de esta función
    return number

print("----------")
print(getNumber())
print()


# Ejemplo 2: Uso de global
y = random.randint(0,9)
print(f"Valor inicial de y: {y}")

def globalVar():
    """Función para ejemplificar el uso de la palabra reservada global"""
    global y
    y += random.randint(0,9)
    print("Modificando...")

globalVar() # Nótese que y no entra como parámetro ni de retorna
print(f"Valor final de y: {y}")
print()

#Ejemplo 3: Uso de nonlocal
# La palabra reservada nonlocal en Python se usa dentro de una función anidada para indicar que una variable pertenece al ámbito de una función externa (pero no global). Esto permite modificar su valor en la función interna sin que se cree una nueva variable local.

def outerFunction():
    x = "a"
    y = "b"
    def innerFunction():
        nonlocal x
        x = "c"
        y = "d"
        print(f"Los valores en inner son x = {x}, y = {y}")
    innerFunction()
    print(f"Los valores en outer son x = {x}, y = {y}")

outerFunction()

print(f"El valor de x es : {x}") # x toma el valor global definido desde el ejemplo 1, no el que se definió en inner/outer
