
# En el mundo de la programación, especialmente cuando trabajamos con funciones, nos encontramos con situaciones donde la cantidad de argumentos que vamos a recibir es incierta. Aquí es donde los args y kwargs se convierten en aliados indispensables. Estos mecanismos permiten manejar un número variable de argumentos o parámetros, otorgando flexibilidad y dinamismo a las funciones que creamos.

print()
print("--- Uso de *args (argumentos posicionales variables) ---")
print("1. Suma Gaussiana fija")

def suma(*args):
    return sum(args)

print(f"a. Suma de los primeros 2 enteros: {suma(1,2)}")
print(f"b. Suma de los primeros 10 enteros: {suma(1,2,3,4,5,6,7,8,9,10)}")
print()

print("2. Suma Gaussiana dinámica: ")
numbers = []
limit = int(input("Ingresa un limite: "))

for counter in range(1,limit+1):
    numbers.append(counter)

print(f"La suma de los primeros {limit} enteros es: {suma(*numbers)}") # Notese el uso de * para "desempaquetar" la lista
print()

print()
print("--- Uso de *kwargs (argumentos con nombres variables) ---")

# Permite pasar una cantidad variable de argumentos con nombre (como un diccionario).
# Útil cuando queremos pasar opciones adicionales sin definirlas de antemano.

def showInfo(**kwargs):
    for key, value in kwargs.items(): # items devuelve un objeto iterable que contiene tuplas (clave, valor).
        print(f"{key}: {value}")

showInfo(nombre="Otelo", edad=33, ciudad="CDMX")
print()
showInfo(producto="Switch", modelo="ABC-123", marca="Nintendo", precio= 5000)
print()

