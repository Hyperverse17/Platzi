
# Un decorador en Python es una función que modifica el comportamiento de otra función sin cambiar su código. Se usa para agregar funcionalidades de manera elegante y reutilizable.
# Los decoradores se definen con @nombre_del_decorador antes de la función que queremos modificar.

import random
from typing import Union

# Ejemplo 1: Decorador para escribir log

def writeLog(func): # Nombre del decorador, recibe como parámetro una función (func no es palabra reservada)
    def wrapper(): # Función de envoltura, debe definirse siempre (wrapper es solo un nombre de ejemplo)
        print("Inicializando log...") # Acciones a ejecutar antes de la función
        func() # Función que se decorará
        print("Finalizando log... ...") # Acciones después de la función
    return wrapper

# Definición y ejecución de la función sin decorador
def paymentProcess():
    print("Mostrat total")
    print("Acerca tu tarjeta")
    print("Procesando pago")
    print("Pago finalizado!")

print()

print("--- Cobro Automático ---")
paymentProcess()
print()

# Definicipon y ejecución de la función con decorador
@writeLog # Asignación del decorador
def paymentProcess():
    print("Mostrat total")
    print("Acerca tu tarjeta")
    print("Procesando pago")
    print("Pago finalizado!")

print("--- Cobro Automático Pro---")
paymentProcess()
print()


# Ejemplo 2: Decorador en función con parámetros

def writeLog2(func): # Nombre del decorador, recibe como parámetro una función (func no es palabra reservada)
    def wrapper(*args, **kwargs): # Función de envoltura, debe definirse siempre. Para este ejemploc omo la función original recibe parámetros, se usa *args y **kwargs
        print("Inicializando log...") # Acciones a ejecutar antes de la función
        result = func(*args,**kwargs) # Función que se decorará. Su return se cacha en una variable
        print("Finalizando log... ...") # Acciones después de la función
        return result # Se devuelve el resultado de la función original
    return wrapper

@writeLog2 # Asignación del decorador
def divide(x: int, y: int) -> Union[int, float, None]: # En este caso no siempre se espera que se devuelva un entero o flotante porque si y es cero, la operación no se podrá realizar
    """Función que divide dos números enteros x/y si y es distinto de cero"""
    if y != 0:
        print(f"Dividiendo {x} entre {y}")
        z = round((x / y),2)
    else:
        print("Algo salió mal")
        z = None

    return z

print()

x: int = random.randint(0,9)
y: int = random.randint(0,9) 

z: int = divide(x,y)

print(f"El resultado de {x} / {y} es: {z}")
print()