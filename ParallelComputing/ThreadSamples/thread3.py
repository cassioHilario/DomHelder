from threading import Thread
from time import perf_counter
import os


def substituir(filename, substr, new_substr):
    diretorio = os.path.abspath(os.getcwd())
    print(f'Processando o arquivo : {filename}')
    # Lendo conteudo do arquivo
    with open(diretorio + '/' + filename, 'r') as f:
        conteudo = f.read()

    # Substituindo a string por uma nova
    conteudo = conteudo.replace(substr, new_substr)

    # Gravando dados no arquivo
    with open(diretorio + '/' + filename, 'w') as f:
        f.write(conteudo)




if __name__ == "__main__":
    start_time = perf_counter()


    arquivos = [
        'teste1.txt',
        'teste2.txt',
        'teste3.txt',
        'teste4.txt',
        'teste5.txt',
        'teste6.txt',
        'teste7.txt',
        'teste8.txt',
        'teste9.txt',
        'teste10.txt',
    ]

    # Criando uma thread para cada arquivo
    threads = [Thread(target=substituir, args=(filename, 'Senpre', 'Sempre')) for filename in arquivos]

    # Inicializando threads
    for thread in threads:
        thread.start()

    # Aguardando as threads finalizarem para o codigo continuar a execucao
    for thread in threads:
        thread.join()


    end_time = perf_counter()
    print(f'As tarefas levaram {end_time- start_time: 0.2f} segundo(s) para executar.')
