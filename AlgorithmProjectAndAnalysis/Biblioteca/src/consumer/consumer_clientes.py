from os import environ
from kafka import KafkaConsumer
from datetime import datetime
from shared.helpers import cursor_post, cursor_delete
from dotenv import load_dotenv
load_dotenv('/.env')

TOPIC_NAME = 'clientes'
DATABASE = 'db-livro.db'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[environ['URL'] + ':' + environ['PORT']], group_id=None, auto_offset_reset='smallest', consumer_timeout_ms = 5000)

print('Consumindo mensagens do tópico: ')

for message in consumer:
    if message is not None:
        print('Topico....: ' + str(message.topic))
        print('Particao..: ' + str(message.partition))
        print('Offset....: ' + str(message.offset))
        print('Timestamp.: ' + str(message.timestamp))
        print('Data/Hora.: ' + str(datetime.fromtimestamp(message.timestamp / 1000.0)))
        print('Chave.....: ' + str(message.key))         
        print('Valor.....: ' + message.value.decode('utf-8'))
        print('')
        
        if message.topic == TOPIC_NAME:
            if message.value.decode('utf-8')["method"] == "POST":
                sql = f'''
                INSERT INTO {TOPIC_NAME} (id,
                                    email, 
                                    nome, 
                                    cpf, 
                                    telefone, 
                                    sexo, 
                                    data_nascimento, 
                                    cep, 
                                    endereco, 
                                    numero, 
                                    bairro) 
                        VALUES ({message.value.decode('utf-8')["id"]},
                                {message.value.decode('utf-8')['email']}, 
                                {message.value.decode('utf-8')['nome']}, 
                                {message.value.decode('utf-8')['cpf']}, 
                                {message.value.decode('utf-8')['telefone']}, 
                                {message.value.decode('utf-8')['sexo']}, 
                                {message.value.decode('utf-8')['data_nascimento']}, 
                                {message.value.decode('utf-8')['cep']}, 
                                {message.value.decode('utf-8')['endereco']}, 
                                {message.value.decode('utf-8')['numero']}, 
                                {message.value.decode('utf-8')['bairro']})'''
                cursor_post(sql, DATABASE)
            elif message.value.decode('utf-8')["method"] == "DELETE":
                sql = f'''DELETE FROM {TOPIC_NAME} WHERE id = {message.value.decode('utf-8')['id']}'''
                cursor_delete(sql, DATABASE)
        
consumer.close()

print('Fim')