from threading import Thread, Lock
from time import sleep
from random import randint
from datetime import datetime

contador = 0

def incrementar(valor, id, lock):
    global contador

    lock.acquire()

    local_contador = contador
    local_contador += valor

    sleep(randint(1, 5))

    contador = local_contador

    print(f'\n Thread {id} - contador = {contador} [{datetime.now()}]')

    lock.release()


if __name__ == "__main__":
    lock = Lock()

    t1 = Thread(target=incrementar, args=(5,1, lock))
    t2 = Thread(target=incrementar, args=(10,2, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'\n Contador final = {contador}')