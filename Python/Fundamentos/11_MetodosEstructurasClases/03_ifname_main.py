
import random
from typing import Union

def suma(a:int, b:int) -> int:
    """Devuelve la suma de dos enteros dados"""
    c:int = a + b
    return c

def resta(a:int, b:int) -> int:
    """Devuelve la resta de dos enteros dados"""
    c:int = a - b
    return c

def multiply(a:int, b:int) -> int:
    """Devuelve el producto de dos enteros dados"""
    c:int = a * b
    return c

def division(a:int, b:int) -> Union[int,float, None]:
    """Devuelve el cociente de dos enteros dados"""
    if b != 0:
        c:Union[int, float] = round((a / b),2)
    else:
        c = None

    return c

if __name__ == "__main__": # Es útil para ejecutar scripts directamente
    a = random.randint(0,9)
    b = random.randint(0,9)
    print()
    print(f" 1. El resultado de {a} + {b} es {suma(a,b)}")
    print(f" 2. El resultado de {a} - {b} es {resta(a,b)}")
    print(f" 3. El resultado de {a} * {b} es {multiply(a,b)}")
    print(f" 4. El resultado de {a} / {b} es {division(a,b)}")
    print()