import threading

buffer = []
cond = threading.Condition()

def productor():
    global buffer
    for i in range(5):
        with cond:
            buffer.append(i)
            print(f"Producido: {i}")
            cond.notify()

def consumidor():
    global buffer
    for _ in range(5):
        with cond:
            while not buffer:
                cond.wait()
            item = buffer.pop(0)
            print(f"Consumido: {item}")

t1 = threading.Thread(target=productor)
t2 = threading.Thread(target=consumidor)

t1.start()
t2.start()

t1.join()
t2.join()
