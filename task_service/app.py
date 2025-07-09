from flask import Flask
from config import Config
from database.db import db
from view.routes import task_bp
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(task_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)
