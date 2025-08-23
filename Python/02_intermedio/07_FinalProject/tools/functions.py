import csv
import re

criteria1 = r"country|capital|continent|A3"
criteria2 = r"population"
criteria3 = r"world|percentage"

def read_csv(pointer:str) -> list:
  """Lee un archivo CSV (valores separados por comas) y devuelve una lista de diccionarios, donde cada diccionario representa una fila, y las llaves son los encabezados (columnas)."""
  with open(pointer, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # csv.reader convierte el contenido en una secuencia de filas, donde cada fila es una lista
    header = next(reader) # Toma la primera fila que normalmente es un header
    data = []
    for row in reader:
      iterable = zip(header, row) # zip() en Python produce tuplas combinando elementos de dos (o más) iterables ítem por ítem.
      country_dict = {key: value for key, value in iterable} # Dict comprehension*
      data.append(country_dict)

    return data
  
def getCountryData(pointer:str) -> list:
  """Lee un archivo CSV (valores separados por comas) y devuelve una lista de diccionarios con informacion filtrada"""
  with open(pointer, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # csv.reader convierte el contenido en una secuencia de filas, donde cada fila es una lista
    header = next(reader) # Toma la primera fila que normalmente es un header
    
    countryData       = []
    CountryPopulation = []
    COUNTER = 0
    for row in reader:
      COUNTER += 1
      iterable = zip(header, row) # zip() en Python produce tuplas combinando elementos de dos (o más) iterables ítem por ítem.
      countryData_dict       = {}
      countryPopulation_dict = {}

      for key, value in iterable:
        
        if re.search(criteria1, key, re.IGNORECASE): # Super uso de research para buscar patrones en strings!
          countryData_dict[key] = value
          countryData.append(countryData_dict)

        elif re.search(criteria2, key, re.IGNORECASE):
          if not (re.search(criteria3, key, re.IGNORECASE)):
            countryPopulation_dict[key] = int(value)
            CountryPopulation.append(countryPopulation_dict)

    print(COUNTER)
    return countryData, CountryPopulation
