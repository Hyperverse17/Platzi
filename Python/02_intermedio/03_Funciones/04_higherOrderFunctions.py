
print()
print("Ejemplo 1. Recepción de una función como argumento")
def functionApply(func, value):
    """Función de orden superior"""
    return func(value)

def square(x):
    return x * x

result = functionApply(square, 5)
print(result)  # Salida: 25
print()

print("Ejemplo 2: Obtención de una función como salida")
# Es un caso donde una función devuelve otra función, algo muy poderoso en Python.
def multiplyer(factor):
    """Función que toma un argumento, llamado factor."""
    def multiply(x):
        """Función multiplica su argumento x por factor, que es una variable externa para ella, pero accesible porque Python permite el closure (cierre)"""
        return x * factor
    
    return multiply # devuelve la función multiply, no el resultado de ejecutarla, sino la función en sí.

twice = multiplyer(2) # Crea una función que multiplique por 2 y guárdala en la variable twice"
print(twice(10))  # Salida:
print(twice(17))  # Salida:
print(twice(0))  # Salida: 
print()

# Uso de lambda
# es muy común en Python, sobre todo cuando necesitas lógica rápida y no quieres escribir una función con def.
print("Ejemplo 3: Uso de lambda")

def multiplyerLambda(factor):
    return lambda x: x * factor # Es una función anónima (sin nombre) que recibe un parámetro x y retorna x * factor. Al momento de ejecutar multiplicador(2), Python devuelve esta función lambda, ya con factor = 2 capturado internamente.

sevenfold = multiplyerLambda(7)
print (sevenfold(1))
print (sevenfold(0))
print (sevenfold(7))
