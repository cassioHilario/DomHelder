from threading import Thread
from threading import Lock
from time import sleep


def tarefa1(lock1, lock2):
    print('>>TAREFA 1')

    r = lock1.acquire(timeout=10)
    if r:
        print('Tarefa 1 - Lock 1 : Ok')

        sleep(3)

        # Tentativa de obter o bloqueio 2
        r = lock2.acquire(timeout=10)
        if r:
            print('Tarefa 1 - Lock 2 : Ok')
            lock2.release()

        lock1.release()

    print('>>TAREFA 1 FINALIZADA')


def tarefa2(lock1, lock2):
    print('>>TAREFA 2')

    r = lock2.acquire(timeout=10)
    if r:
        print('Tarefa 2 - Lock 2 : Ok')

        sleep(3)

        # Tentativa de obter o bloqueio 1
        r = lock1.acquire(timeout=10)
        if r:
            print('Tarefa 2 - Lock 1 : Ok')
            lock1.release()

        lock2.release()

    print('>>TAREFA 2 FINALIZADA')


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=tarefa1, args=(lock1, lock2))
    t2 = Thread(target=tarefa2, args=(lock2, lock2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()