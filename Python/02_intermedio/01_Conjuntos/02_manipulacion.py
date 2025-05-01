
#Funciones de set:
# add(): Añade un elemento.
# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
# discard(): Elimina un elemento y si ya existe no lanza ningún error.
# remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
# pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
# clear(): Elimina todo el contenido del conjunto.

set_bands = {"Archspire", "Beyond Creation", "Gorod", "Benighted", "The Zenith Passage", "Allegaeon", "Kardashev"}

print()
print(set_bands)

# 1. Longitud de un conjunto
size = len(set_bands)
print(f"El conjunto tiene: {size} elementos")
print()

# 2. Saber si un elemento es parte de un conjunto"
band1 = "Gorod"
band2 = "Warbringer"
response = (band1 in set_bands)
print(f"{band1} está en el conjunto?: {response}")
response = (band2 in set_bands)
print(f"{band2} está en el conjunto?: {response}")
print()

# 3. Agregar elementos uno por uno .add()
print(set_bands)
set_bands.add("Havok")
print(set_bands)
print()

# 4. Agregar elementos .update() permite agregar elementos más complejos como una lista u otros conjuntos
set_2 = {"Warbringer", "Municipal Waste", "Power Trip", "Ouroboros", "Motley Crue"}
print(set_bands)
set_bands.update(set_2)
print(set_bands)
print()

# 5. Eliminar elementos existentes .remove() Si el elemento no existe, manda error
print(set_bands)
set_bands.remove("Motley Crue")
print(set_bands)
#set_bands.remove("Mortuary Drape") # KeyError: 'Mortuary Drape'
print()

# 6. Eliminar elementos, si no existen no marca error
set_bands.discard("Motley Crue")

# 7. Tomar un elemento y eliminarlo del conjunto: .pop()
# A diferencia de las listas, los conjuntos no están ordenados, así que no puedes controlar cuál elemento se eliminará.
print(set_bands)
band = set_bands.pop()
print(band)
print(set_bands)
print()

# 8. ELiminar todo el conjunto
print(set_bands)
set_bands.clear()
print(set_bands)
print()
