
# Una función recursiva es una función que se llama a sí misma 

#Ejemplo 1: Obtención del factorial de un número usando recorsividad
# LA función de factorial se define:
#  n! = 1 * 2 * 3 * ... * n-1 * n
# y cumple la siguiente igualdad n! = n * (n-1)!n

def factorial(n):
    # print("...")
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

limit = int(input("Ingresa un límite: "))
print(factorial(limit))
print()

# Ejemplo 2: Obtención del n-ésimo término de la serie de Fibonacci:
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

limit = int(input("Ingresa un límite: "))
print(fibo(limit))
print()
