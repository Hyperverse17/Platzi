
# 

class Person:
    def __init__(self, name: str, lastName: str, age: int):
        """Constructor"""
        self.name = name.capitalize()
        self.lastName = lastName.capitalize()
        self.age = age

    def __str__(self) -> str: # Método mágico 1
        """Devuelve una representación amigable para el usuario"""
        return f"{self.name} {self.lastName}, {self.age} años"
    
    def __repr__(self) -> str: # Método mágico 2
        """Devuelve una representación detallada del objeto para depuración"""
        return f"Person(name='{self.name}', lastName='{self.lastName}', age={self.age})"
    
    def __eq__(self, anotherInstance) -> bool: # Método Mágico 3
        """Compara si dos instancias de la misma clase son iguales"""
        return (self.name == anotherInstance.name) and (self.lastName == anotherInstance.lastName) and (self.age == anotherInstance.age)
    
    def __lt__(self, anotherInstance) -> bool: # Método Mágico 4
        # Compara si un valor de una instancia es "menor" al mismo valor de otra instancia
        return self.age < anotherInstance.age
    
    def __add__(self, anotherInstance):
        # Sobrecarga el operador + para sumar las edades de dos personas
        return self.age + anotherInstance.age
    

print("Instanciando ...")
persona1 = Person("valeria", "Domínguez", 28) # Instanciando objeto
persona2 = Person("otelo", "galicia", 33) # Instanciando objeto


# Ejemplo 1: Uso de __str__
print(persona1)
print()

# Ejemplo 2: Uso de __repr__
print(repr(persona2))
print()

# Ejemplo 3: Uso de __eq__
print(persona1 == persona2)
print()

# Ejemplo 4: Uso de __lt__
print(persona1 < persona2)
print()

# Ejemplo 5: Uso de __add__
print(persona1 + persona2)
print()
