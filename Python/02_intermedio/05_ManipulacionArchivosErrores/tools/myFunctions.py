import csv

def read_csv(pointer:str) -> dict:
  """Lee un archivo CSV (valores separados por comas) y devuelve una lista de diccionarios, donde cada diccionario representa una fila, y las llaves son los encabezados (columnas)."""
  with open(pointer, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # csv.reader convierte el contenido en una secuencia de filas, donde cada fila es una lista
    header = next(reader) # Toma la primera fila que normalmente es un header
    data = []
    for row in reader:
      iterable = zip(header, row) # zip() en Python produce tuplas combinando elementos de dos (o más) iterables ítem por ítem.
      country_dict = {key: value for key, value in iterable} # Dict comprehension*
      data.append(country_dict)

      #* para no tener que escribir esto:
      # country_dict = {}
      # for key, value in iterable:
      #     country_dict[key] = value

    return data


