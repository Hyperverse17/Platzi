
import random

countries = ["mx","col", "usa", "can", "bz", "per"]

# 1. Diccionario con condiciones
print("1. Diccionario con condiciones:")
dict1 = {country:random.randint(1,100) for country in countries} # Creación del diccionario
filtered = {country:population for (country, population) in dict1.items() if population >= 50} # nótese la forma de recorrer un diccionario usando for(key,value)
# la función .items() convierte algo a iterable
print(dict1)
print(filtered)
print()
