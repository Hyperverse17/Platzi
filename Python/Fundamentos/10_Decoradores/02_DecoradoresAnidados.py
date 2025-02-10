
# Un decorador anidado o múltiples decoradores ocurren cuando aplicamos varios decoradores a una misma función. Python permite anidar decoradores simplemente colocándolos en capas, con @decorador1, @decorador2, etc.

def decorador1(func):
    def envoltura(*args, **kwargs):
        print("🚀 Ejecución del decorador 1")
        resultado = func(*args, **kwargs)
        print("🚀 Fin del decorador 1")
        return resultado
    return envoltura

def decorador2(func):
    def envoltura(*args, **kwargs):
        print("⭐ Ejecución del decorador 2")
        resultado = func(*args, **kwargs)
        print("⭐ Fin del decorador 2")
        return resultado
    return envoltura

@decorador1
@decorador2
def saludo(nombre):
    print(f"👋 ¡Hola, {nombre}!")

print()
print("-------------")
saludo("Otelo")
print()

