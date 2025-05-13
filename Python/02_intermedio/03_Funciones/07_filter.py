
import random

# La función filter() en Python sirve para filtrar elementos de una lista (o cualquier iterable) según la condición definida.
# Solo se quedan los elementos que cumplen esa condición.
# Sintaxis: filter(función, iterable)
# función: una función que devuelve True o False para cada elemento.
# iterable: la lista (o tupla, etc.) que se desea filtrar.
# El resultado es un objeto tipo filter, por eso normalmente se convierte a lista con list().

numbers = list(range(2,101)) 

print("1. Uso de Lambda con filter():")
print()
integer = random.randint(1,10)
multiples = list(filter(lambda x: x % integer == 0, numbers)) # filter(condición, iterable)

print(f"Lista de múltiplos de {integer} del 1 al 100:")
print(list(multiples))
print()

print(f"2. Ejemplo con el uso de diccionarios: ")
print()

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Canada',
    'away_team': 'USA',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Colombia',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 4,
    'home_team_result': 'Win'
  }
]

# Cómo filtrar por ejemplo sólo los equipos locales que ganaron?

newList = list(filter(lambda item : item["home_team_result"] == "Win", matches))
print(newList)


