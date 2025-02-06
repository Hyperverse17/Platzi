
# Java Script Object Notation

import json

# 1. Apertura y Lectura 
# Lectura del archivo
with open("products.json", mode="r") as jsonFileR:
    productsList = json.load(jsonFileR)

# Mostrar el contenido
for product in productsList:
    # print(product) # Se imprime TODO en formato de diccionario

    priceFmt = f"${product['price']:,.2f}"
    print(f"Producto: {product['name']} {product['brand']} por tan solo {priceFmt}") # Imprime sólo propiedades definidas


#2. Escritura en archivos json

newProduct = {
    "name":"Coffee Warmer",
    "price":30.99,
    "quantity":50,
    "brand":"Death Wish Coffee",
    "category":"Accesories",
    "entryDate":"2025-02-05"
}

with open("products.json", mode="r") as jsonFileR: # Primero se abre en modo lectura
    productsList = json.load(jsonFileR)

productsList.append(newProduct) # Después se agrega el nuevo producto a la lista previamente definida

with open("products.json", mode="w") as jsonFileW: # Y Finalmente se abre en modo lectura
    json.dump(productsList, jsonFileW, indent = 4) # Para agregar la lista actualizada, el objeto de archivo abierto y una identación con fines de visualización




