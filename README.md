# 🤖 Multi-Agent Hallucination Detection & Trust Score Engine

An AI-powered system that analyzes user queries using multiple agents to detect hallucinations and calculate a trust score for generated responses.

---

## 🚀 Features

- 🧠 AI Response Generation (Gemini/OpenAI)
- 🔍 Fact Checking Agent
- 🧩 Logic Checking Agent
- 📚 Evidence Verification Agent
- ⚠️ Hallucination Detection Agent
- 📊 Trust Score Engine
- 🌐 FastAPI Backend
- ⚛️ React + Vite Frontend

---

## 🏗️ Project Structure

backend/ ├── main.py ├── agents/ ├── score/ ├── groq_service.py └── requirements.txt
frontend/ ├── src/ ├── public/ ├── package.json └── vite.config.js
---

## ⚙️ Backend Setup (FastAPI)

### 📌 Install dependencies

bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
"https://multi-agent-hallucination-detective-and.onrender.com
uvicorn main:app --reload
Install dependencies
cd frontend
npm install
📌 Run frontend
npm run dev
Frontend runs at:
https://multi-agent-hallucination-detective-and-yyub.onrender.com
