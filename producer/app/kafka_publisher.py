from confluent_kafka import Producer
import json


producer_config = {
    "bootstrap.servers": "kafka:9092"
}
producer = Producer(producer_config)
def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

def send(data):
    data = data.model_dump()
    data['user_id'] = str(data['user_id'])
    data = json.dumps(data).encode("utf-8")
    producer.produce(
    topic="registration",
    value=data,
    callback=delivery_report
)
    producer.flush() 

def send_10(data: list):
    producer = Producer(producer_config)
    data = json.dumps(data).encode("utf-8") 
    producer.produce(
        topic='registration',
        value=data,
        callback=delivery_report
 
    )   
    producer.poll(1.0)