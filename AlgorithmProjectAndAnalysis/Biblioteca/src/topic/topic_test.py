from kafka.admin import KafkaAdminClient, NewTopic



admin_client = KafkaAdminClient({'bootstrap.servers': 'https://3.87.156.55:9092'})

topic_list = []
topic_list.append(NewTopic("clientes", 4, 1))
admin_client.create_topics(topic_list)