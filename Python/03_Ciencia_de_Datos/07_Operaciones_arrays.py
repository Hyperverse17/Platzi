
import numpy as np
print()
print("Operaciones lógicas en arrays con Numpy\n")
print("1. Uso del método numpy.all y numpy.any")
array1 = np.random.randint(1,10,10)
result1 = np.all(array1 > 0)
result2 = np.all(array1 > 5)
result3 = np.any(array1 > 7)
print(f"Sea el siguiente array: {array1}")
print(f"Son TODOS sus elementos mayores a cero?  : {result1}")
print(f"Son TODOS sus elementos mayores a cinco? : {result2}")
print(f"ALGUNO de sus elementos es mayor a siete? : {result3}")
print()

print("2. Concatenación ")
arrayA = np.random.randint(1,5,3)
arrayB = np.random.randint(5,9,3)
concat = np.concatenate((arrayA,arrayB))
print(f"Sean los arreglos: {arrayA} y {arrayB}\nLa concatenacion de ambos es: {concat}")
print()

print("3. Stacking Vertical")
arrayC = np.random.randint(3,7,3)
stackV = np.vstack((arrayA, arrayB, arrayC)) # v por vertical
print(f"Sean los arreglos: {arrayA}, {arrayB} y {arrayC}\nEl apilamiento vertical es la matriz:\n {stackV}")
print()

print("4. Stacking Horizontal")
stackH = np.hstack((arrayA, arrayB, arrayC)) # h por horizontal
print(f"Sean los arreglos: {arrayA}, {arrayB} y {arrayC}\nEl apilamiento horizontal es el vector:\n {stackH}")
print()

print("5. Split")
arrayD = np.arange(1,10)
print(f"Sea el siguiente array: {arrayD}")
splitted = np.split(arrayD,3) # al usar numpy.split(array,n) El array que se pasa como argumento debe ser perfectamente divisible entre n
print(splitted)
print()
