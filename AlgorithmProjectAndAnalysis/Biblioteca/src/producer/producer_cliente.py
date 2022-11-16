import time
import json
from kafka import KafkaProducer
from dotenv import load_dotenv
from os import environ
load_dotenv('../.env')

def serializer(message):
        return json.dumps(message).encode('utf-8')
    
producer = KafkaProducer(bootstrap_servers=[environ['URL'] + ':' + environ['PORT']], value_serializer=serializer)

if __name__ == '__main__':
    
    def send_message(topic, message, method):
        producer.send(topic, value=message)
        time.sleep(1)