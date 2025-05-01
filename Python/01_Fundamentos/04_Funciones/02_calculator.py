
def add(a,b):
    result = a + b
    return result

def substraction(a,b):
    result = a - b
    return result

def multiply(a,b):
    result = a * b
    return result

def divide(a,b):
    result = a / b
    return result

def calculator():
    
    while True:
        print()
        
        print("Calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        option = input("Elige una opción: ")
        print()
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingresa el primer valor: "))
            num2 = float(input("Ingresa el segundo valor: "))

        if option == "1":
            print("La suma es: ",add(num1,num2))

        elif option == "2":
            print("La resta es: ",substraction(num1,num2))

        elif option == "3":
            print("La multiplicación es: ",multiply(num1,num2))

        elif option == "3":
            print("La multiplicación es: ",multiply(num1,num2))

        elif option == "4":
            print("La división es: ",divide(num1,num2))

        elif option == "5":
            print("Hasta luego! ")
            break

        else:
            print("Opción no válida")

        print()

calculator()

         