from time import sleep, perf_counter
from threading import Thread
from random import randint


def tarefa(id):
    print(f'\n Inicializando a tarefa {id}...')
    tempo = randint(1, 5)
    print(f' >> Vai esperar {tempo} segundo(s)')
    sleep(tempo)
    print(f' >> A tarefa {id} foi completada')


start_time = perf_counter()

# Criando e inicializando 5 threads
threads = []
for n in range(1, 6):
    t = Thread(target=tarefa, args=(n,))
    threads.append(t)
    t.start()

# Aguardando as threads finalizarem para o codigo continuar a execucao
for t in threads:
    t.join()

end_time = perf_counter()

print(f'As tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')