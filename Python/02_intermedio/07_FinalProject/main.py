import os
from tools.functions import getCountryData
from tools.charts import *
from tools.data import *

default = 131

try:
    print()
    fileName = input("Ingresa el nombre del archivo csv: ") # No olvides visitar: https://www.kaggle.com/
    os.system("cls")
    if fileName == "":
        fileName = fileWp
    pointer = inPath + fileName

    countryData, countryPopulation = getCountryData(pointer)

    countryLabels = countryData[default].keys()
    countryValues = countryData[default].values()

    print(len(countryData))
    print(len(countryPopulation))
    print(countryValues)

    populationLabels = countryPopulation[default].keys()
    populationValues = countryPopulation[default].values()

    print("Mostrando gráfico")
    #barChart(populationLabels, populationValues)
    print("Gráfico finaliado")


except(FileNotFoundError, FileExistsError):
    os.system("cls")
    local = os.getcwd()
    print()
    print(f"Parece que algo anda mal con '{pointer}'")
    print(f"Directorio local: {local}")

except(ValueError) as e:
    os.system("cls")
    print()
    print("Parece que algo anda mal con los valores:")
    print(f"{e}")


finally:
    print()
    print("Fin del programa")
    print()
