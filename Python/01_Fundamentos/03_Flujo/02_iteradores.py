
# iteradores; Son elementos que permiten iterar sobre listas y strings sin necesidad de usar indexación

# Ejemplo 1: uso de iter() y next()
print("--- Iteración sobre listas ---")
numbers = [1,2,3,4,5] # Creación de la lista

iterNums = iter(numbers) # Con la función iter la lista se convierte en un <class 'list_iterator'>
# iter() toma un objeto iterable (como una lista, una tupla, una cadena, etc.) y devuelve un iterador, que es un objeto que se puede recorrer elemento por elemento usando funciones como next().

value = next(iterNums) # con la función next accedemoos consecutivamente a cada valor de la lista
print(value)
print(type(value)) # Se respeta el tipo de dato original, en este caso: <class 'int'>

print(next(iterNums)) # next se puede usar tantas veces como elementos tenga la lista y en cualquier parte del o los scripts relacionados al projecto
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
# print(next(iterNums)) si se excede el uso de next, devuelve el resultado: StopIteration
print()

# Ejemplo 2: Iteración sobre strings
print("--- Iteración sobre strings ---")
string = "Hola, mundo!"
iterstr = iter(string)

print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print(next(iterstr))
print()

# Ejemplo 3: Iteración usando for
print("--- Uso de for para iterar ---")
string2 = "I love Python!"
iterstr2 = iter(string2)

for char in iterstr2: # usando for no es necesario usar next() n veces para n elementos de la lista. for para automáticamente
    print(char)

print()

# Ejemplo 4: uso de range()
print("--- Filtro de numeros pares e impares usando range() ---")
print()
limit = int(input("Ingresa un limite: "))
iterNums = iter(range(0,limit+1))

for num in iterNums:
    mod = num%2
    if mod == 0:
        print(str(num) + " es par")
    else:
        print(str(num) + " es impar")