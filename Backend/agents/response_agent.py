
from gemini_service import get_gemini_response


class ResponseAgent:

    def __init__(self):
        print("Response Agent Initialized")

    def generate_response(self, query):
        try:
            ai_response = get_gemini_response(query)

            return {
                "query": query,
                "response": ai_response
            }

        except Exception as e:
            return {
                "query": query,
                "response": "Unable to generate response.",
                "error": str(e)
            }