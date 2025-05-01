
# En ocasiones es necesario detonar nosotros mismos errores con la función raise:

def verificarEdad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        raise Exception("La persona es menor de edad")
    else:
        return "Verificación Exitosa!"
    
try:
    print()
    edad = int(input("Ingresa tu edad: "))
    verification = verificarEdad(edad)

except ValueError as error:
    print()
    print("Error: ",error)

except Exception as ex:
    print()
    print("Hey! ",ex)

else:
    print()
    print(verification)

finally:
    print()
    print("Fin del programa")
    print()
