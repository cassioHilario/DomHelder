from kafka import KafkaProducer
import json

def serializer(mensagem):
    return json.dumps(mensagem).encode('utf-8')

def send_message(mensagem):                         
    producer.send('messages', mensagem)
    producer.flush()


producer = KafkaProducer(bootstrap_servers=['3.83.120.31:9092'],
                         value_serializer=serializer)
mensagem = json.dumps('3:{["name":"flaviano", "idade": "21"]}')

if __name__ == '__main__':
    send_message(mensagem)
    print('deu certo')