from kafka import KafkaConsumer
from datetime import datetime
#from shared.helpers import cursor_get, cursor_post, cursor_delete

topic_name = 'clientes'

consumer = KafkaConsumer(topic_name, bootstrap_servers=['3.87.156.55:9092'], group_id=None, auto_offset_reset='smallest')

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
        
        """ if message.value.decode('utf-8')["method"] == "POST":
            cursor_post(message.value.decode('utf-8')) """
        
consumer.close()

print('Fim')