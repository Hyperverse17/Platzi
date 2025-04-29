
# Un paquete es una carpeta que contiene uno o más módulos (archivos .py) y un archivo especial llamado __init__.py (puede estar vacío).

from MyPackage.classes import Person # de esta forma se importan paquetes

print("")
persona1 = Person("Otelo",33,"Male")
print(persona1.greet("Heidi"))
print("")
