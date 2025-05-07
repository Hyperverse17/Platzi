
# Todo sobre funciones!!

import random
from typing import Union

def message():
  """Función simple sin return y sin parámetros"""
  print("Ejecutando alguna acción...")
  
def greet(name:str) -> str: # De esta forma se define el tipo de entrada y de salida
  """Función simple sin return y que recibe parámetros"""
  print(f"Hola, {name}!") # No regresa resultado, sólo realiza alguna acción

def sum_with_range(min:int, max:int) -> int:
  """Función con Return"""
  print(f"Máximo: {min}, Mínimo: {max}")
  sum = 0
  for x in range(min, max):
    sum += x
  return sum # Devuelve un resultado

def volume(lenght:int=0, width:int=0 ,depht:int=0) -> int:
  """Función con valores por default"""
  volume = lenght*width*depht
  return volume

def multiple(name:str, lenght:int, width:int, depht:int) -> Union[str,int]:
  greet = f"Hola, {name}!"
  volume = lenght * width * depht
  return greet, volume
  

print()
print("1. Función simple:")
message()
print()

print("2. Función simple con parámetro 'Mayeya':")
greet("Mayeya")
print()

print("3. Función con return")
result = sum_with_range(1, 10) # El return debe cacharse en una variable
print(f"Suma: {result}")
print()

print("4. Función con valores por default")
lenght1 = random.randint(1,10)
width1 = random.randint(1,10)
depht1 = random.randint(1,10)
volume1 = volume(lenght=lenght1, width=width1, depht=depht1)
print(f"El volumen de un sólido de {lenght1}x{width1}x{depht1} es: {volume1} U3")
print(f"Por defecto (sin argumentos): {volume()}")
print(f"Por defecto (con argumentos imcompletos): {volume(width=10)}") # Igual es cero por la naturaleza del cálculo
print()


print("5. Función con retorno múltiple en tupla")
result = multiple("Otelo", lenght1, width1, depht1)
print(result) # Retorna una tupla con los elementos
print()

print("6. Función con retorno múltiple separado")
greet, volume = multiple("Mayeya", lenght1, width1, depht1) # Se cachan los valores en el mismo orden que se retornan
print(f"Primer retorno: {greet}")
print(f"Segundo retorno: {volume}")
print()
