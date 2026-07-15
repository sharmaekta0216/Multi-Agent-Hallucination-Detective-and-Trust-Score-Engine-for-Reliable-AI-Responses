
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):
#         try:
#             ai_response = get_gemini_response(query)

#             return {
#                 "query": query,
#                 "response": ai_response
#             }

#         except Exception as e:
#             print("Error in generating response:", e)
#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }
from services.gemini_service import get_gemini_response


class ResponseAgent:

    def __init__(self):
        print("Response Agent Initialized")

    def generate_response(self, query):

        prompt = f"""
You are an expert AI assistant.

Your task is to answer the user's question accurately, clearly, and professionally.

Rules:
1. Give only factually correct information.
2. If you are unsure, clearly say that you are not certain.
3. Do not invent names, dates, statistics, or references.
4. Explain the answer in simple language.
5. Use bullet points whenever appropriate.
6. Keep the answer well-structured and easy to read.
7. If the question has multiple parts, answer each part separately.

User Question:
{query}

Provide only the answer to the question.
"""

        try:
            ai_response = get_gemini_response(prompt)

            return {
                "query": query,
                "response": ai_response
            }

        except Exception as e:
            print("Error in generating response:", e)

            return {
                "query": query,
                "response": "Unable to generate response.",
                "error": str(e)
            }