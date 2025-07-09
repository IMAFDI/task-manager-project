# 🧩 Task Manager Microservices with Kafka Integration

A Python-based microservices project built with Flask that demonstrates asynchronous event-driven communication using Apache Kafka. It consists of two independent services:

- **Task Manager Service** (Producer): A RESTful API that allows users to manage tasks and publish task-related events.
- **Logger Service** (Consumer): A service that listens to Kafka events and logs them in both memory and a persistent SQLite database.

---

## 🔧 Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Messaging**: Apache Kafka
- **UI**: Bootstrap (Jinja2 Templates)
- **Containerization**: Docker (Kafka + Zookeeper)
- **Others**: threading, kafka-python

---

## 🧱 Architecture

```
+--------------------+            +------------------------+
| Flask App          |            | Flask Logger Service   |
| (Producer)         |            | (Consumer)             |
| task_service       |            | logger_service         |
| Port 5001          |            | Port 5002              |
+--------------------+            +------------------------+
           \                            /
            \                          /
             ------->  localhost:9092 <---------
                      (Docker: Kafka + Zookeeper)
```

---

## 🚀 Features

### ✅ Task Manager (Producer) — `localhost:5001`

- Create, update, and delete tasks
- Publishes events to Kafka topic: `task-events`

### 📄 Logger Service (Consumer) — `localhost:5002`

- Consumes task events from Kafka
- Stores all events in SQLite (`stored-events` view)
- Displays real-time, in-memory events (`kafka-events` view)
- Supports clearing real-time events manually

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/task-manager-kafka.git
cd task-manager-kafka
```

### 2️⃣ Start Kafka with Docker

Ensure Docker is installed, then run:

```bash
docker-compose -f docker-compose-kafka.yml up -d
```

Kafka should now be available at `localhost:9092`.

### 3️⃣ Install Python Dependencies

Create virtual environments and install requirements separately for both services.

#### Task Manager Service (Producer)

```bash
cd task_service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### Logger Service (Consumer)

```bash
cd logger_service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 📬 API Endpoints

### Task Manager API (`localhost:5001`)

| Method | Endpoint      | Description             |
|--------|---------------|-------------------------|
| GET    | `/tasks`      | List all tasks          |
| POST   | `/tasks`      | Create a new task       |
| PUT    | `/tasks/<id>` | Update an existing task |
| DELETE | `/tasks/<id>` | Delete a task           |

---

## 🌐 Logger UI (`localhost:5002`)

- `http://localhost:5002/kafka-events` — View live Kafka events (in-memory)
- `http://localhost:5002/stored-events` — View stored Kafka events (from DB)
- `http://localhost:5002/clear-events` — Clear live Kafka events manually

---

## 🖼️ Sample Screenshots

> Add UI screenshots in the `/screenshots/` directory.

| Task Manager UI                     | Logger Service UI                       |
|------------------------------------|-----------------------------------------|
| ![task-ui](screenshots/task-ui.png) | ![logger-ui](screenshots/logger-ui.png) |

---

## 🐳 Docker Support (Optional)

To add full Docker support:

### 1. Add Dockerfiles

Create a `Dockerfile` in both `task_service/` and `logger_service/`.

### 2. Create a `docker-compose.yml` for All Services

```yaml
version: '3.8'
services:
  kafka:
    image: bitnami/kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_LISTENERS: PLAINTEXT://:9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

  zookeeper:
    image: bitnami/zookeeper:latest
    ports:
      - "2181:2181"

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

Then run:

```bash
docker-compose up --build
```

---

## 📌 Future Improvements

- ✅ Add user authentication
- ✅ Swagger/OpenAPI documentation
- ✅ Add pagination and filtering to event views
- ✅ Dockerize both services
- ✅ Deploy using Kubernetes
- ✅ Upgrade to PostgreSQL or MySQL in production
- ✅ Real-time frontend updates (WebSockets)
- ✅ Add unit and integration tests

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

**Abadullah Faridi**  
📧 [abadullahfaridi40@gmail.com](mailto:abadullahfaridi40@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/abadullahfaridi)
