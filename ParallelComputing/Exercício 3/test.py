from random import randint


def sort(lista, posicao=0):
    if(posicao < len(lista)):
        if(lista[posicao] > sort(lista,len(lista)-posicao-1)):
            old = lista[posicao]
            lista[posicao] = lista[posicao+1]
            lista[posicao+1] = old
            return sort(lista,posicao+1)
        else:
            return sort(lista, posicao+1)
    else:
        return lista
    
if __name__ == '__main__':
    lista = []
    for i in range (5):
        lista.append(randint(1, 5))
    print(sort(lista))