

# Cuando hablamos de metaprogramación en Python con clases, entramos en terreno de metaclases y métodos especiales como __new__ y __call__. Vamos a ver cómo se relacionan.

# 1. El método especial __new__ se ejecuta antes de __init__ y es responsable de crear la instancia de la clase.
# Aquí, __new__ permite modificar o controlar la creación de instancias antes de que __init__ las inicialice.
class MiClase:
    def __new__(cls, *args, **kwargs):
        print("Creando una nueva instancia de", cls.__name__)
        instancia = super().__new__(cls)  # Crea la instancia real
        return instancia

    def __init__(self, valor):
        print("Inicializando la instancia con valor:", valor)
        self.valor = valor
print()
print("--- new ---")
obj = MiClase(42)

# 2. El método __call__ permite que una instancia de clase se comporte como una función.

class Llamable:
    def __call__(self, x):
        print(f"La instancia fue llamada con {x}")

print()
print("--- call ---")
obj = Llamable()
obj(17)  # Parece que estamos llamando a una función
obj(7)  # Parece que estamos llamando a una función
obj(91)  # Parece que estamos llamando a una función
print()

print("---Ejemplo con new y call ---")
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creando la clase {name}")
        dct["nuevo_atributo"] = "Agregado dinámicamente"
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print(f"Instanciando un objeto de {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MiClase(metaclass=Meta):
    pass

obj = MiClase()
print(obj.nuevo_atributo)  # La clase tiene un atributo nuevo

# Aquí, la metaclase Meta:

# Modifica la creación de MiClase con __new__.
# Controla la instanciación con __call__.