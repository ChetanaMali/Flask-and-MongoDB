# 🐳 Multi-Service Docker Deployment — Frontend, Backend & MongoDB

A multi-service application with a Python frontend, Python backend, and MongoDB database — all containerized using Docker and orchestrated with Docker Compose.

---

## 📁 Project Structure

```
project/
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
└── docker-compose.yaml
```

---

## 🔧 Services

| Service | Technology | Port |
|---------|-----------|------|
| **Frontend** | Python | `8000` |
| **Backend** | Python | `5000` |
| **Database** | MongoDB | `27017` |

---

## 🐍 Backend — Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build & Run Backend Manually

```bash
# Build image
docker build -t backend .

# Run container
docker run -d -p 5000:5000 backend

# Test
curl http://localhost:5000
```

---

## 🐍 Frontend — Dockerfile

```dockerfile
FROM python:3.14-slim

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

### Build & Run Frontend Manually

```bash
# Build image
docker build -t frontend .

# Run container
docker run -d -p 8000:8000 frontend

# Test
curl http://localhost:8000
```

---

## 🐙 Docker Compose

Instead of running each container separately, Docker Compose starts all three services together with a single command.

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    container_name: frontend
    ports:
      - "8000:8000"
    env_file:
      - ./frontend/.env
    environment:
      - BACKEND_URL=http://backend:5000
    depends_on:
      - backend
    networks:
      - docker-network

  backend:
    build: ./backend
    container_name: backend
    ports:
      - "5000:5000"
    env_file:
      - ./backend/.env
    environment:
      - MONGO_URL=mongodb://mongo:27017/
    networks:
      - docker-network

  mongo:
    image: mongo
    ports:
      - "27017:27017"
    networks:
      - docker-network

networks:
  docker-network:
```

### Start All Services

```bash
docker compose up
```

### Start in Detached Mode (background)

```bash
docker compose up -d
```

### Stop All Services

```bash
docker compose down
```

---

## 🌐 Service Communication

```
Browser
  ↓
Frontend (port 8000)
  ↓  BACKEND_URL=http://backend:5000
Backend (port 5000)
  ↓  MONGO_URL=mongodb://mongo:27017
MongoDB (port 27017)
```

> All services communicate internally via `docker-network` — no need to use `localhost` between containers.

---

## ✅ Testing

| Service | URL |
|---------|-----|
| Frontend | http://localhost:8000 |
| Backend | http://localhost:5000 |
| MongoDB | mongodb://localhost:27017 |

---

## 🔑 Environment Variables

### `frontend/.env`
```env
BACKEND_URL=http://backend:5000
```

### `backend/.env`
```env
MONGO_URL=mongodb://mongo:27017/
```

---

## 📋 Useful Docker Commands

```bash
# View running containers
docker ps

# View logs of a service
docker compose logs frontend
docker compose logs backend

# Rebuild images after code changes
docker compose up --build

# Remove containers, networks and volumes
docker compose down -v
```
