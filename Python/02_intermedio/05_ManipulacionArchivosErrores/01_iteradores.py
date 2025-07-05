
# En Python, next() es una función que se utiliza para obtener el siguiente elemento de un iterador. Cuando tienes un objeto iterable (como una lista, una tupla, un archivo, etc.), primero necesitas convertirlo en un iterador usando iter(), y después puedes obtener sus elementos uno por uno usando next().

print("")

print("Ejemplo 1.")
print()

myList = [1,2,3,4,5,6,7]

myList=iter(myList)

print(next(myList))
print(next(myList))
print(next(myList))
next(myList)
next(myList)
print(next(myList))
print()

print("Ejemplo 2. Excepcion generada")
print()

myList2 = iter(range(0,3))
print(next(myList2)) # 0
print(next(myList2)) # 1
print(next(myList2)) # 2
print(next(myList2)) # !? StopIteration
