
# El manejo de excepciones en Python es una forma de controlar errores durante la ejecución de un programa, permitiendo anticiparlos y manejarlos adecuadamente mediante bloques como try, except, else, y finally, para evitar que el programa se detenga inesperadamente.

try:
    print()
    A = int(input("Ingresa A: "))
    B = int(input("Ingresa B: "))
    C = A/B
    
except ZeroDivisionError as error: # se pueden poner tantas excepciones como se deseen. En caso de dejar un solo except sin nada más, cualquier excepción entrará en ese caso
    print()
    print("Ha ocurrido el siguiente error: ", error)

except ValueError as valueError:
    print()
    print("Ha ocurrido el siguiente error: ", valueError)

else: # El bloque else se ejecuta después de try si no ocurren excepciones
    print()
    print("El resultado de A/B es: " + str(C))

finally: # El bloque finally se ejecuta siempre hayan ocurrido o no excepciones
    print()
    print("Fin del programa")
    print()