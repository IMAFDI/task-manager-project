import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Blueprint, render_template, redirect, url_for
from logger_service.model.event_model import db, EventLog
from logger_service.utils.event_buffer import event_log  

routes_bp = Blueprint("routes_bp", __name__)

@routes_bp.route("/")
def home():
    return redirect(url_for("routes_bp.kafka_events"))

@routes_bp.route("/kafka-events")
def kafka_events():
    return render_template("events.html", events=event_log)

@routes_bp.route("/stored-events")
def stored_events():
    events = EventLog.query.order_by(EventLog.timestamp.desc()).all()
    return render_template("stored_events.html", events=events)

@routes_bp.route("/delete-event/<int:event_id>")
def delete_event(event_id):
    event = EventLog.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for("routes_bp.stored_events"))

@routes_bp.route("/delete-all-events")
def delete_all_events():
    db.session.query(EventLog).delete()
    db.session.commit()
    return redirect(url_for("routes_bp.stored_events"))

@routes_bp.route("/clear-memory-events", methods=["POST"])
def clear_memory_events():
    event_log.clear()
    print("🧹 Cleared live events from memory.")
    return redirect(url_for("routes_bp.kafka_events"))
