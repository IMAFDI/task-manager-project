from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    event_type = db.Column(db.String(100))
    data = db.Column(db.Text)
    timestamp = db.Column(db.String(100))
