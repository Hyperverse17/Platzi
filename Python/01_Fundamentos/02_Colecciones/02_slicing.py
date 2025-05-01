
# Supongamos que tenemos la lista:

a = [1,2,3,4,5]
# si realizamos la siguiente acción, aparentemente se está creando una nueva lista a partir de la primera:
b = a

print(a)
print(b)
print()

# Sin embargo. en Python al hacer esta acción estamos indicando que se haga referencia a la misma ubicación en memoria. Como consecuencia, todas las acciones que se realicen en a, van a repercutir en b también
print("--- Modificaciones ---")
del a[1] # eliminación del segundo elemento
a.append(6) # Se agrega el 6 al final de la lista

print(a)
print(b)
print()

# Esto se ve más claramente con la función id que regresa la posición en memoria
print("--- id() ---")
print(id(a))
print(id(b))
print()

# una forma de crear una nueva lista  a partir de una lista dada es con el Slicing
print("--- Slicing... ---")
c = a[:] # Estamos declarando una nueva lista c con los elementos desde el inicio hasta el final de a
print(a)
print(c)
print()

# modificando a
del a[0] # eliminación del segundo elemento
a.insert(0,2)
a.append(7) # Se agrega el 6 al final de la lista
print(a)
print(c)
print()

# Se verifica que la función id regresa dos valores distintos para la ubicación en memoria
print(id(a))
print(id(c))
print()
