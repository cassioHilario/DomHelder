from time import perf_counter
from random import randint

def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


if __name__ == '__main__':
    lista = []

    for i in range(1000):
        lista.append(randint(1, 1000))

    start_time = perf_counter()

    print('Lista original : ' + str(lista))

    bubblesort(lista)

    print('Lista ordenada : ' + str(lista))

    end_time = perf_counter()

    print(f'\nA ordenacao levou {end_time - start_time: 0.4f} segundo(s).')
