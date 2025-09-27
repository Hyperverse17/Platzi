
import numpy as np

# NumPy proporciona diversas maneras de crear arrays, facilitando la realización de cálculos numéricos y análisis de datos de manera eficiente en Python.
print()
# 1. Creación de Arrays a partir de Listas: Es posible crar un array a partir de una lista o lista de listas:
print("1. Creación de Arrays a partir de listas: ")
# Array unidimensional
array_1d = np.array([1, 2, 3, 4])
print(array_1d)
print()
# Array bidimensional
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)
print()

print("2. Creación de Arrays con Funciones Predefinidas")
# NumPy proporciona funciones predefinidas para crear arrays de manera más rápida y conveniente:

# np.zeros(): Crea un array lleno de ceros.
zeros_array = np.zeros((3, 3))
print(zeros_array)
print()

# np.ones(): Crea un array lleno de unos.
ones_array = np.ones((2, 4))
print(ones_array)
print()

# np.arange(): Crea un array con una secuencia de números.
range_array = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
print(range_array)
print()

# np.linspace(): Crea un array con números igualmente espaciados.
linspace_array = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]
print(linspace_array)
print()
print()

print("Especificando Datatypes:")

# Array de enteros
int_array = np.array([1, 2, 3], dtype='int32')
print(int_array)

# Array de flotantes
float_array = np.array([1.0, 2.0, 3.0], dtype='float32')
print(float_array)

# Array de booleanos
bool_array = np.array([True, False, True], dtype='bool')
print(bool_array)

# Array de números complejos
complex_array = np.array([1 + 2j, 3 + 4j], dtype='complex64')
print(complex_array)

# Array de cadenas de texto
str_array = np.array(['a', 'b', 'c'], dtype='str')
print(str_array)

# Creando un array con dtype 'd' (equivalente a float64)
array_float64 = np.array([1, 2, 3], dtype='d')
print(array_float64)

# NaN (Not a Number)
# NaN es un valor especial utilizado para representar datos que no son números, especialmente en el contexto de operaciones matemáticas que no tienen un resultado definido. Por ejemplo, la división de cero por cero (0/0) o la raíz cuadrada de un número negativo.

nan_array = np.array([1, 2, np.nan, 4])
print(nan_array)

