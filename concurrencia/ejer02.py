# Objetivo: Visualizar concurrencia.

# Ennciado:
# Crear dos hilos:
# * uno imprime "A" 5 veces
# * otro imprime "B" 5 veces

import threading
import time

def imprimir_a():
    for _ in range(5):
        print("A")
        time.sleep(0.5)

def imprimir_b():
    for _ in range(5):
        print("B")
        time.sleep(0.5)

# Crear los hilos
hilo1 = threading.Thread(target=imprimir_a)
hilo2 = threading.Thread(target=imprimir_b)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()