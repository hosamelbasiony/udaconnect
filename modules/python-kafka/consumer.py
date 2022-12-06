import json 
from kafka import KafkaConsumer
if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        # 'first_kafka_topic',
        'items',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        # msg = json.loads(message.value)
        # print(msg["foo"])
        print(json.loads(message.value))