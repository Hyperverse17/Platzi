
# El dominio de los métodos estáticos y de clase en Python es crucial para aprovechar al máximo las funciones de la programación orientada a objetos. Estos métodos ofrecen una solución eficiente para acceder y modificar las propiedades de las clases sin necesidad de crear instancias. 
# Un método estático en Python es un tipo de función definida dentro de una clase que no requiere acceso al estado de la instancia. Puede ser llamado directamente a través de la clase, eliminando la necesidad de instanciarla, lo que ahorra recursos y simplifica el código.


class Calculadora:

    @staticmethod
    def descuento(amount, rate):
        nuevoPrecio = round(amount - ((amount*rate)/100),2)
        return nuevoPrecio

print()
amount = float(input("Ingresa el monto: "))
rate   = float(input("Ingresa el descuento: "))
precio = Calculadora.descuento(amount,rate) # Es posible ejecutar el método sin instanciar la clase

print()
print(f"El precio con descuento es: ${precio}")

# A diferencia de los métodos estáticos, los class methods son capaces de modificar el estado de la clase. Se definen utilizando el decorador @classmethod y siempre reciben el parámetro cls, que representa la propia clase. Este enfoque es útil para afectar atributos de clase o para definir constructores alternativos.
# El primer parámetro de la función es cls, que es simplemente una convención (como self en los métodos normales).
# cls hace referencia a la propia clase, no a una instancia de la clase.
# Con cls, puedes crear o modificar cosas a nivel de clase, no a nivel de objeto.

class Pedido:
    descuento_global = 10

    @classmethod
    def actualizar_descuento(cls, nuevo_descuento):
        cls.descuento_global = nuevo_descuento

print("----------------------")
print(Pedido.descuento_global)  # Salida: 15
# Uso del class method
Pedido.actualizar_descuento(15)
print(Pedido.descuento_global)  # Salida: 15






