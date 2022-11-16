import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['3.87.156.55:9092'], value_serializer=serializer)

if __name__ == '__main__':
    producer.send('clientes', value={'method': 'POST', 'name': 'nome', 'address': 'endereco', 'contact': 'contato', 'mail': 'email'})
    time.sleep(1)
