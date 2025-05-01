
# En Python una matriz se define como una "lista de listas". Las filas y columnas se comienzan a contar desde la posición cero
# Las matrices al ser listas de más dimensiones, conservan su propiedad de mutabilidad 

#columnas  0 1 2    Filas
matrix = [[1,2,3], # 0
          [4,5,6], # 1
          [7,8,9]] # 2

print(matrix)
print(matrix[2]) # al especificar una sola posición se hace referencia a la fila, en este caso la última
print(matrix[2][0]) # al especificar dos pocisiones 

# Ejemplo más complejo

matrix2 = [[["a", "b"],["c", "d"]],
           [["e", "f"],["g", "h"]]]

print(matrix2)

print(matrix2[1])
print(matrix2[1][0])
print(matrix2[1][0][1])
print()

# Es posible usar métodos de listas en matrices
print("--- Métodos ---")
matrix.append([10,11,12])
matrix.insert(0,["a","b","c"])
print(matrix)

# Tuplas: las tuplas son los homólogos INMUTABLES de las listas. Ls sintaxis es tupla = (a,b,c...) o simplemente con comas
print("--- Tupplas ---")
tupla1 = (1,2,3,4,5)
tupla2 = 5,7,8,9,10 # Python en automático coloca los paréntesis
print(tupla1)
print(type(tupla1))
print(tupla2)
print(type(tupla2))
print()

# Inmutabilidad: los métodos .append() y .insert() No están disponibles
# tupla1[3] = 3 # Regresa el error: TypeError: 'tuple' object does not support item assignment




