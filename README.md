# 🚀 Model Server Deployment on AWS EC2 using Docker

## 📌 Project Overview
This project demonstrates deployment of a machine learning model server using FastAPI + Docker on an AWS EC2 Ubuntu instance.  
The API exposes an OpenAI-compatible endpoint for chat completions.

---

## ⚙️ Tech Stack
- Python 3.10
- FastAPI
- Uvicorn
- Docker
- Transformers (Hugging Face)
- PyTorch
- AWS EC2 (Ubuntu)

---

## 🚀 API Endpoint

### Base URL
http://<EC2-PUBLIC-IP>:8000

### POST /v1/chat/completions

Example Request:
{
  "model": "local-model",
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}

Example Curl:
curl -X POST http://<EC2-PUBLIC-IP>:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "local-model",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'

---

## 🐳 Docker Setup

docker build -t model-server .
docker run -d -p 8000:8000 model-server

---

## ☁️ AWS EC2 Steps

1. Launch Ubuntu EC2
2. Install Docker
3. Clone repo
4. Build image
5. Run container

---

## 🧪 Test

curl http://localhost:8000/docs

---

## 📊 Status
Server Running ✔
API Working ✔
Docker Deployed ✔

