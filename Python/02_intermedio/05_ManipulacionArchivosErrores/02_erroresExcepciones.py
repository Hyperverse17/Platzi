
print()
print("1. Uso de try, except y finally")
print()
div = lambda x,y : x/y

try:
    x = int(input("Ingresa un entero: "))
    y = int(input("Ingresa un entero: "))
    print(f"El resultado de {x} / {y} es {div(x,y)} 😎")

except(ZeroDivisionError):
    print("No se puede dividir por cero 😏")

except(ValueError) as e:
    print(f"{e} ...Qué? 👀")

finally:
    print()

