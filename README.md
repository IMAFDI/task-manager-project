Here’s your updated and **corrected** `README.md` with adjustments based on everything we've done so far:

---

```markdown
# 🧩 Task Manager Microservices with Kafka Integration

A Python-based microservices project built with Flask that demonstrates asynchronous event-driven communication using Apache Kafka. It consists of two independent services:

- **Task Manager Service** (Producer): A RESTful API that allows users to manage tasks and publish task-related events.
- **Logger Service** (Consumer): A service that listens to Kafka events and logs them both in-memory (for live view) and persistently in a SQLite database.

---

## 🔧 Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite (for logger service)
- **Messaging**: Apache Kafka (via Docker)
- **UI**: Bootstrap (with Jinja2 templates)
- **Containerization**: Docker (Kafka + Zookeeper)
- **Other**: kafka-python, threading, event buffers

---

## 🧱 Architecture

```

+--------------------+            +------------------------+
\| Flask App          |            | Flask Logger Service   |
\| (Producer)         |            | (Consumer)             |
\| task\_service       |            | logger\_service         |
\| Port 5001          |            | Port 5002              |
+--------------------+            +------------------------+
\                            /
\                          /
\------->  localhost:9092 <---------
(Docker: Kafka + Zookeeper)

````

---

## 🚀 Features

### ✅ Task Manager (Producer) — `localhost:5001`

- Create, update, and delete tasks
- Publishes JSON events to Kafka topic: `task-events`

### 📄 Logger Service (Consumer) — `localhost:5002`

- Consumes task events from Kafka in real-time
- Stores all events in SQLite (`stored-events`)
- Displays **live (in-memory)** Kafka events (`kafka-events`)
- Manual option to clear **live memory-only** events
- Stored events **remain preserved in DB**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/imafdi/task-manager-kafka.git
cd task-manager-kafka
````

### 2️⃣ Start Kafka with Docker

Make sure Docker is installed. Run Kafka and Zookeeper:

```bash
docker-compose -f docker-compose-kafka.yml up -d
```

Kafka should now be running on `localhost:9092`.

### 3️⃣ Install Python Dependencies

Create virtual environments and install dependencies for both services.

#### ➤ Task Manager Service

```bash
cd task_service
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

#### ➤ Logger Service

```bash
cd logger_service
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

---

## 📬 API Endpoints

### Task Manager API (`http://localhost:5001`)

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/tasks`      | List all tasks          |
| POST   | `/tasks`      | Create a new task       |
| PUT    | `/tasks/<id>` | Update an existing task |
| DELETE | `/tasks/<id>` | Delete a task           |

---

## 🌐 Logger UI (`http://localhost:5002`)

| Page                   | Description                                |
| ---------------------- | ------------------------------------------ |
| `/kafka-events`        | Shows live Kafka events (from memory only) |
| `/stored-events`       | Shows all persisted events from SQLite     |
| `/clear-memory-events` | Clears in-memory (live) events only        |

---

## 🖼️ Screenshots

> Store these in `/screenshots/` directory.

| Task Manager UI                     | Logger Service UI                       |
| ----------------------------------- | --------------------------------------- |
| ![task-ui](screenshots/task-ui.png) | ![logger-ui](screenshots/logger-ui.png) |

---

## 🐳 Docker Support (Optional)

To run all services using Docker:

### Sample `docker-compose.yml`

```yaml
version: '3.8'
services:
  zookeeper:
    image: bitnami/zookeeper:latest
    ports:
      - "2181:2181"

  kafka:
    image: bitnami/kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_LISTENERS: PLAINTEXT://:9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

  task_service:
    build: ./task_service
    ports:
      - "5001:5001"
    depends_on:
      - kafka

  logger_service:
    build: ./logger_service
    ports:
      - "5002:5002"
    depends_on:
      - kafka
```

Run everything:

```bash
docker-compose up --build
```

---

## 📌 Future Improvements

* Add Swagger/OpenAPI docs
* Dockerize both Flask apps fully
* Switch to PostgreSQL or MySQL for prod
* Add authentication for Task Manager
* Enable WebSocket for live updates
* Add unit + integration tests

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Abadullah Faridi**
📧 [abadullahfaridi40@gmail.com](mailto:abadullahfaridi40@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/abadullahfaridi)

```

---

Let me know if you'd like the README broken into actual files like `README.md`, `docker-compose.yml`, or if you want help creating `Dockerfile` templates too.
```
