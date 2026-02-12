import mysql_connection
import os
from confluent_kafka import Consumer
import json


uri = os.getenv('KAFKA_URI')
consumer_config = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "register-grop",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["suspicious"])


print("🟢 Consumer is running and subscribed to suspicious topic")
def get_data(connection):
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue

            value = msg.value().decode("utf-8")
            data = json.loads(value)
            for item in data:
                if item['type'] == 'customer':
                    connection.insert_to_customer(item)
                    continue
                connection.insert_to_order(item)
                print(f"📦 Received order: {item}")

    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")

    finally:
        consumer.close()