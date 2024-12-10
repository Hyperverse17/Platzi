

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
print("-------------------------------------------")
#Otras funciones interesantes...
str5 = "I like my coffee just like my metal: Black!"
str6 = "this message begins with a lowercase letter and the rest of the words do too."
str7 = "- this message begins and ends with midline -"
str8 = "aaaaaaaaaaaaa?aaeiiiiiiiiiiiiiiiiiioooo?oooooooouuuuuuuuuuuu"

# .upper convierte todo a mayúsculas
print(str5.upper())

# .lower convierte todo a minúsculas
print(str5.lower())

# .count(<arg>) Devuelve el número de apariciones de un caracter (distingue mayúsculas y minúsculas)
print(str5.count("e"))  
# igual funciona con substrings
print(str5.count("coffee")) 

# .capitalize() Regresa el string cambiando la primer letra por mayúscula
print(str6.capitalize()) 

# .title() devuelve el string cambiando todas sus palabras comenzando con mayúscula
print(str6.title()) 

# .swapcase() devuelve el string invirtiendo mayúsculas por minúsculas y vice versa
print(str5.swapcase()) 

# .replace(<arg1>,<arg2>) reemplaza el argumento 1 por el argumento 2 en el string donde se aplica
print(str5.replace("e","o"))

# .split() separa los elementos de un string en una lista, toma por default el espacio
newList = str5.split()
print(newList)

# .strip() elimina al principio y al final el caracter argumentado
print(str7.strip("-"))

# .lstrip elimina al principio el caracter argumentado 
print(str7.lstrip("-"))

# .rstrip elimina al final el caracter argumentado 
print(str7.rstrip("-"))

# .find() devuelve el index de la primera ocurrencia del caracter o string especificado. Devuelve -1 si no se encuentra
print(str8.find("e"))
print(str8.find("z"))

# .index() devuelve el índice del caracter o string argumentado
print(str8.index("?"))

# eval(<expression>) ejecuta una expresión si es una expresión legal para Python
command = "print('Good bye')"
eval(command)

# exec(<expression>) similar a eval pero para comandos más complejos
program = 'a = 5\nb=10\nprint("Sum =", a+b)' # la diagonal invertida y n representan salto de linea
exec(program)
