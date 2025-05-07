
#Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.

#Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:

#countries - Países del continente en general.
#northAmerica - Países del norte de América.
#centralAmerica - Países del centro de América.
#southAmerica - Países del sur de América.
#En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇

new_set = new_set.union(countries)
new_set = new_set.union(northAm)
new_set = new_set.union(centralAm)
new_set = new_set.union(southAm)

print(new_set)

