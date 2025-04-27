
import threading
import time

def procesar_solicitud(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completada")

print("---------")
hilos = [] # Se crea una lista vacía que almacenará todos los objetos hilo (Thread) que vas a lanzar.
for i in range(3): # Se hace un ciclo para crear tres hilos (i = 0, 1, 2).
    hilo = threading.Thread(target=procesar_solicitud, args=(i,))
    # target=procesar_solicitud indica que cuando el hilo inicie, va a ejecutar la función procesar_solicitud.
    # args=(i,) significa que le pasa como argumento i a esa función (procesar_solicitud(i)).
    # Nota: (i,) es una tupla de un solo elemento, por eso lleva la coma.
    
    hilos.append(hilo) # Se guarda el hilo en la lista hilos.
    hilo.start() # el hilo comienza a ejecutar procesar_solicitud(i) en paralelo al flujo principal del programa.

print("---------")
for hilo in hilos:
    hilo.join() # detiene el flujo principal hasta que cada hilo termine.

print("Todas las solicitudes completadas")


