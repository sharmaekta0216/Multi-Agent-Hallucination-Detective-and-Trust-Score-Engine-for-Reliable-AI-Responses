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

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from agents.workflow import run_workflow
# from api.auth import router as auth_router
# from services.database_service import (
#     save_query,
#     save_response,
#     save_trust_score
# )

# app = FastAPI(
#     title="Multi-Agent Hallucination Detection API",
#     version="1.0.0"
# )
# app.include_router(auth_router)

# # Allow React frontend to connect
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173", 
#         "http://localhost:5174",  # Vite React
#         "http://localhost:5175",  # Vite React
#         "http://localhost:5176",  # Vite React
#         "http://localhost:5177",  # Vite React
#         "http://localhost:5178",  # Vite React
#           # Vite React
#         "http://127.0.0.1:5173"   # Create React App
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# class QueryRequest(BaseModel):
#     user_id: int
#     question: str


# @app.get("/")
# def home():
#     return {
#         "message": "Backend is running successfully!"
#     }


# @app.post("/analyze")
# def analyze(request: QueryRequest):
#     try:
#         # Run AI workflow
#         result = run_workflow(
#     request.user_id,
#     request.question
# )

#         # Temporary user (until login integration)
#         user_id = 1

#         # Save query
#         query_id = save_query(
#             user_id,
#             request.question
#         )

#         # Save AI response
#         response_id = save_response(
#             query_id,
#             result["ai_response"]
#         )

#         # Save trust score
#         save_trust_score(
#             response_id,
#             result["fact_score"],
#             result["logic_score"],
#             result["evidence_score"],
#             result["hallucination_score"],
#             result["trust_score"],
#             result["trust_level"]
#         )

#         return result

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from agents.workflow import run_workflow
# from api.auth import router as auth_router
# from services.database_service import get_user_history

# app = FastAPI(
#     title="Multi-Agent Hallucination Detection API",
#     version="1.0.0"
# )

# app.include_router(auth_router)

# # Allow React frontend to connect
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://localhost:5174",
#         "http://localhost:5175",
#         "http://localhost:5176",
#         "http://localhost:5177",
#         "http://localhost:5178",
#         "http://127.0.0.1:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# class QueryRequest(BaseModel):
#     user_id: int
#     question: str


# @app.get("/")
# def home():
#     return {
#         "message": "Backend is running successfully!"
#     }


# @app.post("/analyze")
# def analyze(request: QueryRequest):
#     try:
#         # Run AI workflow
#         result = run_workflow(request.question)

#         # Temporary user (until login integration)
#         user_id = 1

#         # Save query
#         query_id = save_query(
#             user_id,
#             request.question
#         )

#         # Save AI response
#         response_id = save_response(
#             query_id,
#             result["ai_response"]
#         )

#         # Save trust score
#         save_trust_score(
#             response_id,
#             result["fact_score"],
#             result["logic_score"],
#             result["evidence_score"],
#             result["hallucination_score"],
#             result["trust_score"],
#             result["trust_level"]
#         )

#         return result

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }
# @app.post("/analyze")
# def analyze(request: QueryRequest):
#     try:

#         result = run_workflow(
#             request.user_id,
#             request.question
#         )

#         return result

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }
    
# @app.get("/history/{user_id}")
# def get_history(user_id: int):
#     try:
#         history = get_user_history(user_id)

#         return {
#             "success": True,
#             "history": history
#         }

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }
    
# #         print("Request received:", request.question)

# #         print("Calling workflow...")
# #         result = run_workflow(request.question)
# #         print("Workflow completed")

# #         user_id = 1

# #         print("Saving query...")
# #         query_id = save_query(user_id, request.question)

# #         print("Saving response...")
# #         response_id = save_response(query_id, result["ai_response"])

# #         print("Saving trust score...")
# #         save_trust_score(
# #             response_id,
# #             result["fact_score"],
# #             result["logic_score"],
# #             result["evidence_score"],
# #             result["hallucination_score"],
# #             result["trust_score"],
# #             result["trust_level"]
# #         )

# #         print("Returning result...")
# #         return result

# #     except Exception as e:
# #         print("ERROR:", e)
# #         return {"success": False, "error": str(e)}
# # >>>>>>> Stashed changes
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from agents.workflow import run_workflow
# from api.auth import router as auth_router
# from services.database_service import get_user_history

# app = FastAPI(
#     title="Multi-Agent Hallucination Detection API",
#     version="1.0.0"
# )

# # Authentication routes
# app.include_router(auth_router)

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://localhost:5174",
#         "http://localhost:5175",
#         "http://localhost:5176",
#         "http://localhost:5177",
#         "http://localhost:5178",
#         "http://127.0.0.1:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # -----------------------------
# # Request Model
# # -----------------------------
# class QueryRequest(BaseModel):
#     user_id: int
#     question: str


# # -----------------------------
# # Home API
# # -----------------------------
# @app.get("/")
# def home():
#     return {
#         "success": True,
#         "message": "Backend is running successfully!"
#     }


# # -----------------------------
# # Analyze API
# # -----------------------------
# @app.post("/analyze")
# def analyze(request: QueryRequest):
#     try:
#         result = run_workflow(
#             request.user_id,
#             request.question
#         )

#         return {
#             "success": True,
#             "result": result
#         }
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from agents.workflow import run_workflow
# from api.auth import router as auth_router
# from services.database_service import get_user_history

# app = FastAPI(
#     title="Multi-Agent Hallucination Detection API",
#     version="1.0.0"
# )

# # Authentication routes
# app.include_router(auth_router)

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://localhost:5174",
#         "http://localhost:5175",
#         "http://localhost:5176",
#         "http://localhost:5177",
#         "http://localhost:5178",
#         "http://127.0.0.1:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # -----------------------------
# # Request Model
# # -----------------------------
# class QueryRequest(BaseModel):
#     user_id: int
#     question: str


# # -----------------------------
# # Home API
# # -----------------------------
# @app.get("/")
# def home():
#     return {
#         "success": True,
#         "message": "Backend is running successfully!"
#     }


# # -----------------------------
# # Analyze API
# # -----------------------------
# @app.post("/analyze")
# def analyze(request: QueryRequest):
#     print("Request received:", request.question)
#     try:
#         print("Request received:")
#         result = run_workflow(
#             request.user_id,
#             request.question
#         )
#         print("Workflow completed",result)
#         return result
    
#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e)
#         }
# #-----------------------------
# # User History API
# # -----------------------------
# @app.get("/history/{user_id}")
# def get_history(user_id: int):
#     try:
#         history = get_user_history(user_id)

#         return {
#             "success": True,
#             "history": history
#         }

#     # except Exception as e:
#     #     return {
#     #         "success": False,
#     #         "error": str(e)
#     #     }
#  except Exception as e:

#      print("API ERROR:", e)

#      return {
#         "success": False,
#         "error": str(e),
#         "fact_score":0,
#         "logic_score":0,
#         "evidence_score":0,
#         "hallucination_score":100,
#         "adversarial_score":0,
#         "trust_score":0,
#         "trust_level":"Failed",
#         "judge_decision":"Unable to evaluate",
#         "explanation":str(e),
#         "recommendation":"Check backend logs"
#     }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.workflow import run_workflow
from api.auth import router as auth_router
from services.database_service import get_user_history


app = FastAPI(
    title="Multi-Agent Hallucination Detection API",
    version="1.0.0"
)


# =============================
# Authentication Routes
# =============================

app.include_router(auth_router)



# =============================
# CORS Configuration
# =============================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
        "http://localhost:5177",
        "http://localhost:5178",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://127.0.0.1:5176",
        "http://127.0.0.1:5177",
        "http://127.0.0.1:5178"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# =============================
# Request Model
# =============================

class QueryRequest(BaseModel):

    user_id: int

    question: str





# =============================
# Home API
# =============================

@app.get("/")
def home():

    return {

        "success": True,

        "message": "Backend is running successfully!"

    }




# =============================
# Analyze API
# =============================

@app.post("/analyze")
def analyze(request: QueryRequest):

    print("\n========== NEW REQUEST ==========")

    print("Question:", request.question)


    try:

        result = run_workflow(

            request.user_id,

            request.question

        )


        print("Workflow Completed Successfully")

        return result



    except Exception as e:


        print("WORKFLOW ERROR:", e)


        return {

            "success": False,

            "error": str(e),


            # Default values for frontend safety

            "question": request.question,

            "ai_response": "Unable to generate response",


            "fact_score": 0,

            "logic_score": 0,

            "evidence_score": 0,

            "hallucination_score": 100,

            "adversarial_score": 0,


            "trust_score": 0,

            "trust_level": "Failed",


            "judge_decision": "Evaluation Failed",

            "explanation": str(e),

            "recommendation": "Check backend logs"

        }





# =============================
# User History API
# =============================

@app.get("/history/{user_id}")
def get_history(user_id: int):

    try:

        history = get_user_history(user_id)


        return {

            "success": True,

            "history": history

        }



    except Exception as e:


        print("History Error:", e)


        return {

            "success": False,

            "error": str(e)

        }