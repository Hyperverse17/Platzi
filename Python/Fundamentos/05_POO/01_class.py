

from unique import timeMarkId
uniqueId = timeMarkId("ACC")

class Person: # Definición de la clase
    def __init__(self, name, lastName, age): # Método Constructor: Definición de los atributos mínimos necesarios para instanciar un objeto
        self.name = name # Asignación de valor a los atributos
        self.lastName = lastName
        self.age = age

    def greet(self, name):
        print("Hola, " + str(name) + ". Me llamo " + self.name + " y tengo " + str(self.age) + " años")
    
#print()
#person1 = Person("Otelo", "Galicia", 33)
#person1.greet("Heidi")
#print()

class BankAccount:
    def __init__(self , accountHolder):
        
        self.accountId = next(uniqueId)
        self.isActive = True # Se definen atributos cuyo valor no necesariamente entra como argumento del constructor
        self.accountBalance = 0
        self.accountHolder = accountHolder

    def deposit(self, amount):
        if self.isActive == True:
            self.accountBalance += amount
        else:
            raise Exception("Cuenta Bloqueada!")

    def withdraw(self,amount):
        if self.isActive == True:
            if self.accountBalance > 0:
                self.accountBalance -= amount
            else:
                raise Exception("Fondos insuficientes")
        else:
            raise Exception("Cuenta Bloqueada!")

    def deactivate(self):
        if self.isActive == True:
            self.isActive = False

    def activate(self):
        if self.isActive == False:
            self.isActive = True

try:
    account1 = BankAccount("Otelo")
    account2 = BankAccount("Waleria")
    account3 = BankAccount("Lola")
    account4 = BankAccount("Comet")
        
    print(account1.accountId)
    print(account2.accountId)
    print(account3.accountId)
    print(account4.accountId)
    print()

    print(account4.accountBalance)
    print(account3.accountBalance)
    print(account2.accountBalance)
    print(account1.accountBalance)
    account4.deposit(1000)
    account3.deposit(1000)
    #account2.withdraw(100)
    #account1.withdraw(150)
    print(account4.accountBalance)
    print(account3.accountBalance)
    print(account2.accountBalance)
    print(account1.accountBalance)
    print()

    print("Desactivacion")
    print(account1.isActive)
    account1.deactivate()
    print(account1.isActive)
    #account1.deposit(100)
    print("Reactivacion")
    account1.activate()
    print(account1.isActive)
    account1.deposit(100)
    

except Exception as ex:
    print("Ha ocurrido el siguiente error: ", ex)
