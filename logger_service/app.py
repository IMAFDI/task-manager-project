import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from config import Config
from logger_service.model.event_model import db
from routes.routes import routes_bp
from kafka_event.kafka_consumer.consumer import consume_events
import threading

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # ✅ MUST do this here

# Register routes
app.register_blueprint(routes_bp)

# Start Kafka Consumer thread inside app context
def start_consumer():
    with app.app_context():
        print("✅ Kafka Consumer started inside app context.")
        consume_events()

threading.Thread(target=start_consumer, daemon=True).start()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5002, debug=True)
