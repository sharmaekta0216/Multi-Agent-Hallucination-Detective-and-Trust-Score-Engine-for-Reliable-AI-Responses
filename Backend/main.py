# #from agents.workflow import run_workflow
# from score.trust_score import TrustAgent
# #query = input("Enter your query: ")

# #result = run_workflow(query)

# print("\n========== RESULT ==========\n")

# print("Query:")
# print(result["response"]["query"])

# print("\nAI Response:")
# print(result["response"]["response"])

# print("\nFact Score:")
# print(result["fact"]["fact_score"])

# print("\nLogic Score:")
# print(result["logic"]["logic_score"])

# print("\nEvidence Score:")
# print(result["evidence"]["evidence_score"])

# print("\nHallucination Score:")
# print(result["hallucination"]["hallucination_score"])

# print("\nTrust Score:")
# print(result["trust"]["trust_score"])

# print("\nTrust Level:")
# print(result["trust"]["trust_level"])

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.workflow import run_workflow

app = FastAPI(
    title="Multi-Agent Hallucination Detection API",
    version="1.0.0"
)

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite React
        "http://127.0.0.1:5173"   # Create React App
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }


@app.post("/analyze")
def analyze(request: QueryRequest):
    try:
        result = run_workflow(request.question)
        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }