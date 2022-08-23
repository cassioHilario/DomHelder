from threading import Thread
from threading import Lock
from time import sleep


def tarefa1(lock1, lock2):
    print('>>TAREFA 1')

    lock1.acquire()

    print('Tarefa 1 - Lock 1 : Ok')

    sleep(3)

    # Tentativa de obter o bloqueio 2
    lock2.acquire()

    # Só irá liberar os bloqueios se os dois forem adquiridos
    lock1.release()
    lock2.release()


def tarefa2(lock1, lock2):
    print('>>TAREFA 2')

    lock2.acquire()

    print('Tarefa 2 - Lock 2 : Ok')

    sleep(3)

    # Tentativa de obter o bloqueio 1
    lock1.acquire()

    # Só irá liberar os bloqueios se os dois forem adquiridos
    lock1.release()
    lock2.release()


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=tarefa1, args=(lock1, lock2))
    t2 = Thread(target=tarefa2, args=(lock2, lock2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()