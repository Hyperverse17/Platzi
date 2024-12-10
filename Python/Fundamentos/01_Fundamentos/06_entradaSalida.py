
# Es posible ingresar datos de manera interactiva con el usuario usando la función input()
print("--- Uso de la función input() ---")
name = input("Ingrese su nombre: ") # Interacción de entrada con el usuario
print(name.capitalize()) # capitalize() cambia la primera letra a mayúscula 
print(type(name))
age = input("Ingrese su edad: ")
print(age)
print(type(age)) # Nótese que a pesar de que se le está pasando un dato entero para la edad, el tipo de dato termina siendo str igual que el nombre
print()

# Es posible cambiar el tipo de dato dependiendo de nuestras necesidades
print("--- Casting --- ")
ageCast = int(input("Ingrese su edad: ")) # Hacer castimg a int, float, etc...
print(ageCast)
print(type(ageCast))
print()
