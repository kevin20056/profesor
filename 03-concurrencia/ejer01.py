# Objetivo
# Aprender a crear varios hilos dinámicamente utilizando un ciclo y entender su ejecución concurrente.

# Enunciado
# Crear un programa en Python que:
# genere 5 hilos utilizando un ciclo
# cada hilo debe imprimir su identificador
# Salida esperada (el orden puede variar):

import threading


def tarea(numero):
    print(f"Hilo numero {numero}")


hilos = []


for i in range(1, 10):
    hilo = threading.Thread(target=tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
