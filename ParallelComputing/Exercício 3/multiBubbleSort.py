from asyncio import threads
from threading import Thread
from time import perf_counter
from random import randint

def paralelSort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


if __name__ == '__main__':
    lista = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    
    limite = 1000
    nThreads = 4
    controle = limite//nThreads
    
    for i in range (limite):
        lista.append(randint(1, limite))
        
    print ('Lista Original: ', str(lista))
    start_time = perf_counter()
    
    
    for numero in lista:
        if numero <= controle:
            lista1.append(numero)
        elif numero > controle and numero <= controle*2:
            lista2.append(numero)
        elif numero > controle*2 and numero <= controle*3:
            lista3.append(numero)
        else:
            lista4.append(numero)
            
    listas = [lista1, lista2, lista3, lista4]
    lista = []
    threads = []
    
    for l in listas:
        paralelSort(l)
        lista.append(l)
    
    for l in listas:
        t = Thread(target=paralelSort, args=(l))
        threads.append(t)
        t.start()
        lista.extend(l)
        
    for t in threads:
        t.join()
        
        
    
    print('Lista ordenada: ', lista)
    
    end_time = perf_counter()
    
    print(f'\nA ordenação levou {end_time - start_time: 0.2f} segundo(s).')