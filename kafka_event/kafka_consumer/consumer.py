import sys
import os
import json
from datetime import datetime
from kafka import KafkaConsumer

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from logger_service.utils.event_buffer import event_log
from logger_service.model.event_model import db, EventLog  # ✅ Shared db instance


def consume_events():
    consumer = KafkaConsumer(
        'task-events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='logger-group',
        enable_auto_commit=True
    )

    for message in consumer:
        try:
            raw_data = message.value.decode()
            print(f"📥 Kafka message: {raw_data}")
            event_data = json.loads(raw_data)

            # Store to DB
            db_event = EventLog(
                topic=message.topic,
                event_type=event_data["event"],
                data=json.dumps(event_data["data"]),
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            db.session.add(db_event)
            db.session.commit()

            # Store to in-memory buffer for live view
            event_log.append({
                "topic": message.topic,
                "event_type": event_data["event"],
                "data": json.dumps(event_data["data"]),
                "timestamp": db_event.timestamp
            })

            print("✅ Event stored in DB and memory")

        except Exception as e:
            db.session.rollback()
            print("❌ Kafka Consumer Error:", e)
