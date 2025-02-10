
import random

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

x1: int = random.randint(0,9)
y1: int = random.randint(0,9)

x2: int = random.randint(0,9)
y2: int = random.randint(0,9)

v1 = Vektor(x1, y1)
v2 = Vektor(x2, y2)

v3 = v1 + v2  # Sobrecarga de "+"

print()
print(repr(v1))
print(repr(v2))
print(repr(v3))
print()
