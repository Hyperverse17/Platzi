
import statistics
import csv

mainFile = "./07_Bibliotecas/monthlySales.csv"
monthlySales = {}
with open(mainFile, mode = 'r') as analysisFile:
    reader = csv.DictReader(analysisFile)
    for row in reader:
        month = row['month'] # Nombre de la columna
        totalSales = float(row['sales'])
        monthlySales[month] = totalSales # Creación del diccionario mes:ventas <nombreDiccionario>[<llave>]:<valor>

# Creación de una lista con solo los valores der las ventas
salesList = list(monthlySales.values())
print(salesList)

# Haciendo la magia
print()
print("... Datos estadísticos ...")
print()
salesMean = round(statistics.mean(salesList),2)
salesMedian = round(statistics.median(salesList),2)
salesMode = round(statistics.mode(salesList),2)
salesStDev = round(statistics.stdev(salesList),2)
salesVariance = round(statistics.variance(salesList),2)

print(f"Media: {salesMean}")
print(f"Mediana: {salesMedian}")
print(f"Moda: {salesMode}")
print(f"Desviación Estándar: {salesStDev}")
print(f"Varianza: {salesVariance}")
print()

maxValue = max(salesList)
minValue = min(salesList)
print(f"El valor Mínimo es {minValue} y el Máximo es {maxValue}")
print(f"Finalmente, el rango es: {maxValue-minValue}")
print()



