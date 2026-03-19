import threading
import time


def desayunar():
    print("Iniciando tarea 1")
    time.sleep(4)
    print("Finalizando tarea 1")


def tomar_agua():
    print("Iniciando tarea 2")
    time.sleep(2)
    print("Finalizando tarea 2")


def estudiar():
    print("Iniciando tarea 3")
    time.sleep(5)
    print("Finalizando tarea 3")


inicio = time.perf_counter()

# -- Funciones
# desayunar()
# tomar_agua()
# estudiar()


# --- Hilos
hilo_desayunar = threading.Thread(target=desayunar, args=())
hilo_desayunar.start()

hilo_agua = threading.Thread(target=tomar_agua, args=())
hilo_agua.start()

hilo_estudiar = threading.Thread(target=estudiar, args=())
hilo_estudiar.start()

hilo_desayunar.join()
hilo_agua.join()
hilo_estudiar.join()

# print(threading.active_count())
# print(threading.enumerate())

fin = time.perf_counter()

tiempo = fin - inicio

print(tiempo)
