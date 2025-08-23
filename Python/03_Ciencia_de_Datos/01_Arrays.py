
import numpy as np # Import Numerical Python

# 1. Escalar
print("1. Escalar: ")
escalar = np.array(17)
print(escalar)
print(type(escalar)) # <class 'numpy.ndarray'>
print()

# 2. Vector
print("2. Vector: ")
vector = np.array([30, 29, 42, 35, 33, 36, 42])
print(vector) # Nótese la ausencia de comas!
# La ausencia de comas en la impresión de arrays de NumPy es solo estética, no cambia cómo funciona el array ni cómo se manejan los datos internamente.
print()

# 3. Matriz
print("3. Matriz: ")
# Una matriz, como la del ejemplo, puede facilitar la representación de píxeles de una imagen o productos vendidos mes a mes en un conjunto de datos de ventas.
matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) # Una matriz es basicamente una lista de listas
print(matriz)
print()

# 4. Tensor
print("4. Tensor: ")
# Un tensor es una extensión de matrices a más dimensiones, utilizado para representar estructuras de datos más complejas, como imágenes en 3D en las que se trabaja con los canales RGB:
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # Un buen hack para contar dimensiones es contando el numero de corchetes. Nótese que este array tiene "...]]]", s decir 3 dimensiones
# Un tensor de tres dimensiones como este puede manejar cantidades impresionantes de datos, ideal para proyectos avanzados de aprendizaje automático.
print(tensor)
print()
