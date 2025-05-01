
# uso de if

# if <condición principal>:
#   <código a ejecutar>
# [elif <condición secundaria>:]
#   [<código a ejecutar>]    
#[else:]
#   [código a ejecutar]

# Ejemplo 1
x = 5
if x > 5:
    print("X es mayor que 5") # Parte a ejecutar si la condición se cumole
elif x == 5:
    print("X es igual que 5") # parte a jeecutar si se cumple la segunda condición diferente a la primera
else:
    print("X es menor que 5") # Parte a ejecutar si no se cumple ninguna condición
print("afuera")

# Ejemplo 2: uso de or, and y not

x = 15
y = 20

if x>10 and y>25:
    print("X es mayor que 10 y Y es mayor que 15")

if x>10 or y>25:
    print("X es mayor que 10 O Y es Mayor que 25")

if not x>10:
    print("X no es mayor que 10")

# Ejemplo 3

is_member = True
age = 11

if is_member:
    if age>=15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")
