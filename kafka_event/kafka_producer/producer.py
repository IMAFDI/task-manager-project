from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(event_type, data):
    message = {
        "event": event_type,
        "data": data
    }
    producer.send("task-events", value=message)
    producer.flush()
