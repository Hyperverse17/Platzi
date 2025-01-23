

class Car:
    """Autos"""
    def __init__(self, brand, model,year,price):
        self.brand = brand
        self.model = model
        self.year  = year
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El coche {self.brand} {self.model} {self.year} ha sido vendido.")
        else:
            print(f"El coche {self.brand} {self.model} {self.year} no está disponible.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price


class Customer:
    """Clientes"""
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.cars_purchased = []

    def buy_car(self, car): # Nótese que el segundo parámetro es un objeto!
        if car.check_availability():
            car.sell() # Se llama a un método del objeto que se recibe como parámetro
            self.cars_purchased.append(car) # Se agrega el objeto al atributo "lista" propia de esta clase
        else:
            print(f"Lo siento, {car.brand} {car.model} {car.year} no está disponible.")

    def inquire_car(self, car):
        availability = "disponible" if car.check_availability() else "no disponible"
        print(f"El coche {car.brand} {car.model} {car.year} está {availability} y cuesta {car.get_price()}.")


class Dealership: # La concesionaria gestiona carros y clientes; sólo funciona existir si ya se tienen carros y clientes registrados 
    """Concesionaria de Autos"""
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} {car.year} ha sido añadido al inventario.")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} {customer.lastname} ha sido registrado en la concesionaria.")

    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} {car.year} por {car.get_price()}")

print()
print("------- Concesionaria de Autos El Papá de Matilda----------")
print()
print("Instancia de Autos...")
# Crear instancias de coches
car1 = Car("Dodge", "Attitude","2020", 200000)
car2 = Car("Mazda", "CX5","2019", 500000)
car3 = Car("Toyota", "Corolla","2021", 180000)
car4 = Car("Honda", "Civic", "2022",220000)
car5 = Car("Ford", "Mustang", "1960",350000)

print("Instancia de Clientes... ")
# Crear instancia de cliente
customer1 = Customer("Otelo","Galicia")
customer2 = Customer("Valeria","Dominguez")
customer3 = Customer("Heidi","Galicia")
customer4 = Customer("Lola","Dominguez")
print()

print("--- Registro de Autos: ---")
# Crear instancia de concesionaria y registrar coches y clientes
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.add_car(car4)
dealership.add_car(car5)
print()

print("--- Registro de Clientes: ---")
dealership.register_customer(customer1)
dealership.register_customer(customer2)
dealership.register_customer(customer3)
dealership.register_customer(customer4)
print()

# Mostrar coches disponibles
print("--- Inventario ---")
dealership.show_available_cars()
print()

# Cliente consulta un coche
print("Consulta...")
customer1.inquire_car(car1)
print()

# Cliente compra un coche
print("Compra...")
customer1.buy_car(car1)
print()

# Mostrar coches disponibles nuevamente
dealership.show_available_cars()

# Cliente intenta comprar un coche ya vendido
customer1.buy_car(car1)

