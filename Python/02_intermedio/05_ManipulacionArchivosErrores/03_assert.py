
print()

print("1. Uso de assert")
print()
suma = lambda x,y : x+y
mult = lambda x,y : x*y

try:
    x = int(input("Ingresa un entero: "))
    y = int(input("Ingresa un entero: "))

    assert suma(x,y) == mult(x,y) # Si esta condición se cumple, el programa sigue su flujo de manera normal. Si no, manda un AssertionError 

    print("Todo ok por aqui 😎")
    
except AssertionError:
    print("Algo no salió bien... 🙃")

finally:
    print()

