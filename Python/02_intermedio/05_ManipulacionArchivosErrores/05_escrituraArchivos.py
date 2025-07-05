import os
from tools.data import *

try:
    print("1. Escritura en archivos:")
    fileName = input("Ingresa el nombre del archivo: ")
    
    if fileName == "":
        fileName = fileTxt
    pointer = inPath + fileName

    file = open(pointer)
    print(file.read())
    
    with open(pointer,"a") as file2: #a se usa para agregar al final, w para sobreescribir y r sólo para lectura
        file2.write("Nueva linea!\n")
        file2.close()
        print()

    file = open(pointer)
    print(file.read())
    
except(FileNotFoundError):
    os.system("cls")
    local = os.getcwd()
    print(f"Parece que algo anda mal con '{pointer}'")
    print(f"Directorio local: {local}")

finally:
    print()
