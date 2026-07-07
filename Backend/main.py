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
from api.auth import router as auth_router
from services.database_service import (
    save_query,
    save_response,
    save_trust_score
)

app = FastAPI(
    title="Multi-Agent Hallucination Detection API",
    version="1.0.0"
)
app.include_router(auth_router)

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://localhost:5174",  # Vite React
        "http://localhost:5175",  # Vite React
        "http://localhost:5176",  # Vite React
        "http://localhost:5177",  # Vite React
        "http://localhost:5178",  # Vite React
          # Vite React
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
        # Run AI workflow
        result = run_workflow(request.question)

        # Temporary user (until login integration)
        user_id = 1

        # Save query
        query_id = save_query(
            user_id,
            request.question
        )

        # Save AI response
        response_id = save_response(
            query_id,
            result["ai_response"]
        )

        # Save trust score
        save_trust_score(
            response_id,
            result["fact_score"],
            result["logic_score"],
            result["evidence_score"],
            result["hallucination_score"],
            result["trust_score"],
            result["trust_level"]
        )

        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }