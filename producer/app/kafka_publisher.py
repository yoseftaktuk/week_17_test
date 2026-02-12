from confluent_kafka import Producer
import json
import time

producer_config = {
    "bootstrap.servers": "kafka:9092"
}
producer = Producer(producer_config)
def delivery_report(err, msg):
    pass
    # if err:
    #     # print(f"❌ Delivery failed: {err}")
    # else:
    #     # print(f"✅ Delivered {msg.value().decode('utf-8')}")
    #     # print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")



def send_30(data: list):
    producer = Producer(producer_config)
    data = json.dumps(data).encode("utf-8") 
    producer.produce(
        topic='suspicious',
        value=data,
        callback=delivery_report

    )   
    producer.poll(1.0)
    producer.flush()
    time.sleep(0.5)