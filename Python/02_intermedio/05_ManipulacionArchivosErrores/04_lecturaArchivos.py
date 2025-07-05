import os
from tools.data import *

try:
    print("1. Lectura de archivos:")
    fileName = input("Ingresa el nombre del archivo: ")
    
    if fileName == "":
        fileName = fileTxt
    pointer = inPath + fileName

    file1 = open(pointer)
    print(file1.read()) # Esta es la forma de leer todo el archivo de un ave
    file1.close()
    print()

    print("2. Lectura línea por linea:")
    fileName = input("Ingresa el nombre del archivo: ")
    
    if fileName == "":
        fileName = fileTxt
    pointer = inPath + fileName

    file2 = open(pointer)
    print(file2.readline()) # .readline() hace las veces de un iterador
    print(file2.readline())
    print(file2.readline())
    print(file2.readline())
    print(file2.readline())
    print(file2.readline())
    print(file2.readline())
    file2.close()
    print()

except(FileNotFoundError):
    os.system("cls")
    local = os.getcwd()
    print(f"Parece que algo anda mal con '{pointer}'")
    print(f"Directorio local: {local}")

finally:
    print()