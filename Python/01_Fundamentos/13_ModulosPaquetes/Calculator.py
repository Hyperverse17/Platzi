
from typing import Union

def suma(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    c = a + b
    return c

def resta(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    c = a - b
    return c

def multiplicacion(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    c = a * b
    return c

def division(a:Union[int, float], b:Union[int, float]) -> Union[int, float, str]:
    if b != 0:
        c = round((a / b),2)
    else:
        c = "Not defined"
    return c
