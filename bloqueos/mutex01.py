import threading
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(10000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(2)]

for h in hilos:
    h.start()
    h.join()

print(contador)
