
# En el fascinante mundo de la programación en Python, la eficiencia y la claridad son claves. Una herramienta que permite lograr estas cualidades en la creación de diccionarios es el Dictionary Comprehension. Esta técnica sintáctica no solo contribuye a un código más limpio, sino que también optimiza recursos al permitir crear diccionarios de manera concisa

# Sintaxis básica: dictionary = {key:value for var in iterable}

# 1. Creación de un diccionario  simple usando el método tradicional
print("1 Forma tradicional:")
dict1 = {} # Línea 1
for number in range(0,10): # Línea 2
    dict1[number] = (number * 5) # Línea 3

print(dict1)
print()

# 2. Creación de un diccionario simple usando comprehension dict
print("2. Comprehension dict:")
dict2 = {element : (element * 7) for element in range(0,10)}
print(dict2)
print()

# 3. Creación de un diccionario simple a partir de una lista
print("3. Diccionario a partir de una lista:")

keys = ["key1", "key2", "key3", "key4", "key5"]
values = ["value1", "value2", "value3", "value4", "value5"]

dict3 = {keys[counter]:values[counter] for counter in range(len(keys))}
print(dict3)
print()

