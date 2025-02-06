
import random

# 1. Generar un número aleatorio
print()
randomNumber = random.randint(0,9)
print(randomNumber)

# 2. Elegir un elemento aleatorio de una lista
bands = ["SepticFlesh","Mortuary Drape", "Evile", "Dimmu Borgir", "Moonlight Sorcery"]
todaysBand = random.choice(bands)
print(todaysBand)

# 3. Revolver elementos de una lista.
cards = ["Ace", "King", "Queen", "Joker", "10", "7"]
random.shuffle(cards)
print(cards)

