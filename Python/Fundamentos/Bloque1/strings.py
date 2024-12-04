

name = "Otelo"

# La función type regresa el tipo de variable

print(type(name)) # retornas str

# Existen 3 formas de ingresar strings

str1 = "Comillas dobles"  # Clásico y elegante
str2 = 'Comillas simples' # Común y no tan elegante 
str3 = '''Comillas triples
...que además son sensibles al salto de linea!!!''' # wow!
# Una buena práctica es usar siempre el mismo tipo de comillas...

print(str1)
print(str2)
print(str3)

# Indexación

str4 = "Python es genial!"

# De esta forma se acceden a los elementos de un string
print(str4[0])  # En Python se comienza a contar desde la posición cero
print(str4[1])
print(str4[2])
print(str4[3])
print(str4[4])
print(str4[5])

# Para acceder de atrás hacia adelante se utilizan números negativos empezando por el -1

print(str4[-7])
print(str4[-6])
print(str4[-5])
print(str4[-4])
print(str4[-3])
print(str4[-2])
print(str4[-1])


# La concatenación se hace uniendo strings con +

lastname = "Galicia"

print(name + " " + lastname)

# Replicación: Se realiza usando el *

string5 = "ja, "
print(string5 * 7)

# La función Len devuelve la longitud de la cadena:

print(len(str4))



