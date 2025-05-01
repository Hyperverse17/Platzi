
import random
import math
# los decoradores @staticmethod, @classmethod y @property están predefinidos en Python y se usan en clases para modificar el comportamiento de los métodos.

print()
x: int = random.randint(0,9)
y: int = random.randint(0,9)
r: int = random.randint(0,9)

#Ejemplo 1. @staticmethod – Método estático
# Se usa para definir métodos que no dependen de la instancia (self) ni de la clase (cls). Son como funciones normales dentro de la clase, pero se agrupan dentro de ella por organización.

class Maths:
    @staticmethod
    def addition(a: int, b: int) -> int: # No usa self ni cls
        result: int = a + b
        return result

print(f"1. El resultado de {x} + {y} es {Maths.addition(x, y)}")# Permite llamar a un método sin instanciar la clase
print() 

#Ejemplo 2. @classmethod – Método de clase
# Se usa cuando el método necesita acceder a la clase en sí misma (cls) en lugar de a una instancia específica.

class Person:
    species = "Human"

    @classmethod
    def getSpecies(cls): # Usa cls para acceder a atributos de la clase
        return cls.species

print(f"2. Obtener Espcie: {Person.getSpecies()}") # Se puede llamar sin instanciar la clase
print()

#Ejemplo 3. 3. @property – Definir atributos como propiedades
# Convierte un método en una propiedad de solo lectura. Se usa para encapsular atributos sin que parezcan métodos al acceder a ellos.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Convención: "_" indica atributo "privado"

    @property
    def getRadius(self) -> int:
        return self._radius

    @property
    def area(self) -> float:
        area = round(math.pi * (self._radius**2),2)
        return area  # Permite acceder como si fuera un atributo
    
#   Si queremos permitir la modificación del atributo, agregamos un "setter":
    @getRadius.setter 
    def newRadius(self, newRadius):
        if newRadius > 0:
            self._radius = newRadius
        else:
            raise ValueError("El radio debe ser positivo")


circle = Circle(r) # Instancia del objeto

print(f"3. El área de un círculo de radio {circle.getRadius} es: {circle.area}") # Permite acceder a métodos como si fueran atributos, sin uso de ()
print()

# Modificando el valor encapsulado
circle.newRadius = 17 # Modifica el radio


