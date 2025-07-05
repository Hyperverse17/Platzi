import os
from tools.myFunctions import read_csv
from tools.data import *

try:
    print("1. Lectura de archivos csv:")
    fileName = input("Ingresa el nombre del archivo: ") # No olvides visitar: https://www.kaggle.com/

    if fileName == "":
        fileName = fileWp
    pointer = inPath + fileName

    data = read_csv(pointer)
    print(data[0])

except(FileNotFoundError):
    os.system("cls")
    local = os.getcwd()
    print(f"Parece que algo anda mal con '{pointer}'")
    print(f"Directorio local: {local}")

finally:
    print()



