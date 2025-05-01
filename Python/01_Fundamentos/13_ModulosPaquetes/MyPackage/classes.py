
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self, someone):
        greet = f"Hola, {someone}, mi nombre es {self.name} y tengo {self.age} años"
        return greet
