
import multiprocessing

def calcular_cuadrado(n):
    return n * n

# Está usando multiprocessing para calcular en paralelo el cuadrado de una lista de números ([1, 2, 3, 4, 5]), pero usando varios procesos, no sólo hilos.
# Procesos → cada uno corre en su propio espacio de memoria, separados completamente. (Más seguros para tareas pesadas de CPU).

if __name__ == "__main__": # Muy importante en Windows: garantiza que el código para crear procesos no se ejecute recursivamente (protección para que no explote todo). También buena práctica general en multiprocessing.
    numeros = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool: # multiprocessing.Pool() crea un grupo de procesos trabajadores (como un pequeño "ejército").
        resultados = pool.map(calcular_cuadrado, numeros) # reparte los números entre los procesos
        # Cada proceso recibe un número y le aplica calcular_cuadrado
    print(resultados)
