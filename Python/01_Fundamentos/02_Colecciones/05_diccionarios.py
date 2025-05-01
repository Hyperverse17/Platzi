

# Los diccionarios en Python son una estructura que almacenan dos datos, la clave y el valor. Un ejemplo cotidiano es un diccionario físico donde buscamos el significado de una palabra y encontramos la palabra (clave) y su definición (valor). Veamos cómo se utilizan en código.

print("--- Diccionarios ---")
# Se crean usando llaves {}. Dentro del diccionario se colocan pares llave - valor separado por comas
numbers = {1: "one", 2: "two", 3: "three", 4:"four", 5:"five"}
print(numbers)
print()

# Las llaves pueden ser asimismo, strings:
dictionary = {"value1":"info1", "value2":"info2", "value3":"info3"}
print(dictionary)
print()

# El acceso a los datos se hace mediante la indexación:
print(numbers[3])
print(dictionary["value2"])
print()

# Eliminación de valores: La eliminación se hace con la función del usando la llave y la indexación
del numbers[3]
print(numbers)
print()

# Métodos útiles para diccionarios
print("--- Métodos ---")
# items(): Regresa una lista con tuplas <llave : valor> de un diccionario dado
pairs = numbers.items()
print(pairs)
# .keys(): Regresa una lista con todas las llaves de un diccionario dado
keys = numbers.keys()
print(keys)
# .values(): De forma análoga a keys, regresa una lista con todas los valores de un diccionario dado
values = numbers.values()
print(values)
print()

print("--- Diccionarios Complejos ---")
# Los diccionarios pueden contener más diccionarios dentro. Esto es especialmente útil al hacer agendas de contactos, por ejemplo:

contactos = {
    "Carla": {"apellido": "Florida", "telefono": "5578995482", "edad": 30},
    "Diego": {"apellido": "Antesana", "telefono": "5578995483", "edad": 32},
    "Otelo":{"apellido": "Galicia", "telefono": "5578995484", "edad": 33}
}
print(contactos["Otelo"]["telefono"])

# Creación de una biblioteca:

book1 = {
    "title":"La Chica Gris",
    "author":"Antonio Runa",
    "year":"2022",
    "publisher":"Minotauro",
    "country":"Spain",
    "languaje":"Spanish",
    "ISBN":{
        "phisical":"9788445014752",
        "digital":"[???]"
    },
    "chapters":{
        0:{
            "title":"Capítulo 0",
            "page":14,
            "abstract":"Saul y Maxi..."
        },
        1:{
            "title":"Vuelta al ruedo",
            "page":23,
            "abstract":"Isaac Zarco..."
        },
        2:{
            "title":"La promesa",
            "page":87,
            "abstract":"En 1995..."
        },
        3:{
            "title":"Mentes abiertas",
            "page":119,
            "abstract":""
        }
    }
}

def getChapter(chapter,dataString):
    chapterN = book1.get("chapters")[chapter]
    chapterValue = chapterN[dataString]
    return chapterValue

def getChapterLenght(chapterA,chapterB):
    pageA = book1.get("chapters")[chapterA]["page"]
    pageB = book1.get("chapters")[chapterB]["page"]
    difference = abs(pageB-pageA)

    return difference

data = getChapter(1,"abstract")
print(data)

lenght = getChapterLenght(2,3)
print(lenght)

# Bonus

# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json
json_data = json.dumps(libro)
print("Datos en JSON:", json_data)
#Configuración de una Aplicación:
#Se crea un diccionario para almacenar configuraciones de una aplicación.
#Contador de Palabras:
#Se utiliza un diccionario para contar la frecuencia de palabras en una lista.
#Mapeo de Usuarios a Datos:
#Se crea un diccionario para mapear identificadores de usuarios a sus datos personales.
#Almacenamiento de Datos Estructurados:
#Se almacena información de un libro en un diccionario
#Formato JSON:
#Se convierte un diccionario a una cadena JSON utilizando el módulo json.
