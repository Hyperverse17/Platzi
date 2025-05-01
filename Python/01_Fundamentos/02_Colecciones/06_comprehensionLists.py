
# Son formas de crear listas de una forma rápida expresiva y eficiente en una sola línea con ayuda de un for y condicionales!

# La sintaxis es: list = [función(<nombrevariable>) for <nombreVariable> in range(inicio,fin [,step]) [<condici+on>] ]

# Son como un espresso: Breve, rápida y potente

# Ejemplo 1: Obtener los cuadrados consecutivos de los primeros n números

n = 10

print("--- Comprehension Lists ---")

squares = [(x**2) for x in range(0,n+1)]
print(squares)

# Ejemplo 2: conversión de grados celsius a Kelvin y de celsius a farenheit

kelvin = [(c + 273.15) for c in range(0,n+1,2)] # range(inicio, fin [, step])
print(kelvin)

fahrenheit = [((c*9/5)+32) for c in range(0,n+1,2)]
print(fahrenheit)
print()

# Uso de condiciones
print("--- Uso de if ---")

# Ejemplo 3: Obtención de números pares y nones

evens = [x for x in range(0,n+1) if x%2==0]
odds = [x for x in range(0,n+1) if x%2!=0]
print(evens)
print(odds)
print()

# Uso en matrices:
print("--- Transpuesta de una matriz ---")

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] # Para obtener el numero de columnas de una matriz, basta con sacar la longitud de su fila 0

print(matrix)
print(transposed)
