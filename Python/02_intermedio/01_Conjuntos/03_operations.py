
set_a = {"Archspire", "Beyond Creation", "Gorod", "Tool"}
set_b = {"GNR", "AC/DC", "Led Zepellin", "Tool"}

# Union:
print("1. union()")
set_c = set_a.union(set_b) # En este caso, el método union se aplica sobre set_a para incluirle set_b
print(set_c)
print("Uso de |:")
print(set_a | set_b)
print()

print("2. Interseccion")
set_c = set_a.intersection(set_b)
print(set_c)
print("Uso de &:")
print(set_a & set_b)
print()

print("3. Diferencia")
set_c = set_a.difference(set_b)
print(set_c)
print("Uso de -:")
print(set_a - set_b)
print()

print("4. Diferencia simétrica") # Negación de la intersección
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print("Uso de ^:")
print(set_a ^ set_b)
