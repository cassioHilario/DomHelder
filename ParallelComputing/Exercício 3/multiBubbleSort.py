from asyncio import threads
from threading import Thread
from time import perf_counter
from random import randint

def paralelSort(lista, posicao=0):
    if(posicao < len(lista)):
        if lista[posicao] > lista[posicao+1]:
            oldNum = lista[posicao]
            lista[posicao] = lista[posicao+1]
            lista[posicao+1] = oldNum
            return paralelSort(lista, posicao+1)
        else:
            return paralelSort(lista, posicao+1)
    else: 
        return lista


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
        
    start_time = perf_counter()
    
    
    for numero in range(lista):
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
    
    for list in listas:
        t = Thread(target=paralelSort, args=(list))
        threads.append(t)
        t.start()
        lista += list
        
    for t in threads:
        t.join()
        
    
    
    print ('Lista Original: ', str(lista))
    
    print('Lista ordenada: ', str(lista))
    
    end_time = perf_counter()
    
    print(f'\nA ordenação levou {end_time - start_time: 0.2f} segundo(s).')