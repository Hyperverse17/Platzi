
import random
from typing import Optional # Esta librería es útil cuando no se espera que una función retorne algo específico siempre
from typing import Union # Esta librería es útil cuando no se espera que una función retorne algo específico siempre

# Anotaciones de tipo: Es una buena práctica especificar cada tipo de cada variable creada o retornada
# Re realiza especificando variable, tipo y valor > var : type [= value]

# Ejemplo 1: Anotaciones de tipo en funciones simples

def addition(x: int, y: int) -> int:
    """Función que realiza una suma de dos enteros"""
    z : int = x + y 
    return z

def substraction(x: int, y: int) -> int:
    """Función que realiza una resta de dos enteros"""
    z : int = x - y 
    return z

def multiply(x: int, y: int) -> int:
    """Función que multiplica dos números enteros"""
    z: int = x * y
    return z

# def divide(x: int, y: int) -> Optional[float]: Cuando no se está seguro si se retornará el tipo que está entre corchetes
# El uso de Union es más práctivo en estos casos
def divide(x: int, y: int) -> Union[int, float, None]: # En este caso no siempre se espera que se devuelva un entero o flotante porque si y es cero, la operación no se podrá realizar
    """Función que divide dos números enteros x/y si y es distinto de cero"""
    if y != 0:
        z = (x / y)
    else:
        z = None

    return z

print()
# Se obtienen dos numeros enteros aleatorios
x: int = random.randint(0,9)
y: int = random.randint(0,9) 

print(f"El resultado de {x} + {y} es: {addition(x,y)}")
print(f"El resultado de {x} - {y} es: {substraction(x,y)}")
print(f"El resultado de {x} X {y} es: {multiply(x,y)}")
print(f"El resultado de {x} / {y} es: {divide(x,y)}")
print()

# Ejemplo 2: Anotaciones de tipo en clases
class Person:
    def __init__(self, name: str, age: int):
        """Constructor de esta clase"""
        self.name = name.capitalize()
        self.age = age

    def greet(self, name: str) -> str:
        """Método para saludar"""
        name = name.capitalize()
        message = f"Hola, {name}. Mi nombre es {self.name} y tengo {self.age} años."
        return message
    
person1 = Person("otelo",33)
print(person1.greet("valeria"))






