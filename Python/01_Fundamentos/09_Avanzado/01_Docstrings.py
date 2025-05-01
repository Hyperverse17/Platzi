
# Docstrings
import random

# Ejemplo 1: Docstrings
def function():
    """Esto es un Doctring, se coloca entre triple comillas dobles y es una buena práctica."""
    pass

function() # Este es un comentario para recordarte colocar el cursor sobre el nombre de la función para ver el Docstring!

# Ejemplo 2: Aplicación
print()
def average(numbers: list): # Nótese el uso de anotaciones de tipo variable : tipo
    """Función que calcula el promedio de una lista de números dada. El resultado se redondea a dos decimales."""
    average = round(float(sum(numbers)/len(numbers)),2)
    return average

numbers = [random.randint(1,100) for _ in range(0,9)] # Comprehension list para generar 10 numeros enteros entre 1 y 100
numAverage = average(numbers) # Coloca el cursor sobre el nombre de la función!
print(f"Dada la lista: {numbers}")
print(f"El promedio de los numeros que contiene es: {numAverage}")

