
import random
# La función map() es muy útil también con el manejo de diccionarios

# Creación de una lista compleja: una lista de diccionarios
print()
clothes = [
    {"product":"pants",
     "price":100},

     {"product":"shirt",
     "price":60},

     {"product":"jacket",
     "price":250},

     {"product":"tie",
     "price":90},

     {"product":"shoes",
     "price":350},

     {"product":"socks",
     "price":20}
]

print("1. Obtención de una lista con precios usando map ()")
prices = list(map(lambda item : item["price"], clothes))
maxPrice = max(prices)
print(prices)
print(f"Precio Máximo: {maxPrice}")
print()

print("2. Adición de una nueva llave en un diccionario usando map()")
print()
# Supongamos que ahora se desea agregar un nuevo valor en el diccionario: La cantidad de artículos de cada tipo
# Es una función un poco más compleja para usar lambda, por lo que la función se define de manera tradicional:

def addQuantity(item):
    item["quantity"] = random.randint(1,10) # Nótese que se hace referencia a una llave inexistente
    return item

print(clothes)
print()
list(map(addQuantity,clothes)) # Nótese que el arreglo original se modifica! REFERENCIA EN MEMORIA!
print(clothes)
print()

# Para lograr que la lista original no se modifique, lo más natural es copiar
print("3. Adición de una nueva llave sin modificar la lista original")
print()
# Imaginemos ahora que se desea agregar la marca

def addBrand(item):
    newItem = item.copy()
    newItem["brand"] = f"brand {random.randint(1,5)}"
    return newItem

print(clothes)
print()
newClothes = list(map(addBrand,clothes))
print(clothes)
print(newClothes)
print()

