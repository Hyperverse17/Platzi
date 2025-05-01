
import random
from typing import Union 
# Validaciones de tipo en funciones y métodos
# El método isinstance evalua si una variable es de determinado tipo y regresa un booleano 

class Calculator:
    """Calculadora Básica"""
    def addition(x: int, y: int) -> Union[int,None]:
        """Suma de dos números enteros"""
        if (isinstance(x,int) and (isinstance(y,int))):
            result: int = x + y
        else:
            result = None
            
        return result

    def substract(x: int, y: int) -> Union[int,None]:
        """Resta de dos números enteros"""
        if (isinstance(x,int) and (isinstance(y,int))):
            result: int = x - y
        else:
            result = None
            
        return result

    def multiply(x: int, y: int) -> Union[int,None]:
        """Producto de dos números enteros"""
        if (isinstance(x,int) and (isinstance(y,int))):
            result: int = x * y
        else:
            result = None
            
        return result

    def divide(x: int, y: int) -> Union[int, float, None]:
        """División de dos números enteros"""
        if (isinstance(x,int) and (isinstance(y,int)) and (y != 0)):
            result = x / y
        else:
            result = None
            
        return result 


# Instanciando calculadora
calculator = Calculator

# Definiendo dos números aleatorios
x: int = random.randint(0,9)
y: int = random.randint(0,9)
print()

print(f"El resultado de {x} + {y} es {calculator.addition(x,y)}")
print(f"El resultado de {x} - {y} es {calculator.substract(x,y)}")
print(f"El resultado de {x} * {y} es {calculator.multiply(x,y)}")
print(f"El resultado de {x} / {y} es {round(calculator.divide(x,y),2)}")
print()
