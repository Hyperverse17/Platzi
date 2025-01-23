
class Mamifero:
    def __init__(self):
        pass
    
    def features(self):
        print('Tiene pelaje y glandulas mamarias')

class Perro(Mamifero):
    def __init__(self):
        pass
    
    def bark(self):
        print('Woof!!')
    
    def walking(self):
        print('Paseando alegre')
        
    def eat(self):
        print('Comiendo contento')

class Cachorro(Perro):
    def __init__(self):
        pass
    
    def play(self):
        print('Jugando y mordiendo zapatos')

print()

print("Instanciando Cachorro")       
cachorro1 = Cachorro()
print()

print("--- Acciones propias de Perro ---")
cachorro1.bark() #Propiedades de clase Perro
print()

print("--- Acciones propias de Cachorro ---")
cachorro1.play() # Propiedades de clase Cachorro
print()

print("--- Propiedades de Mamifero ---")
cachorro1.features() # Propiedades de Mamifero
print()
