# class FactAgent:

#     def check_fact(self, response: str):

#         print("Fact Agent Running...")

#         # Demo fact score
#         fact_score = 85

#         return {
#             "fact_score": fact_score,
#             "message": "Facts Verified"
#         }
import json
from backend.services.gemini_service import get_gemini_response

class FactAgent:

    def check_fact(self, response: str):

        prompt = f"""
You are a fact-checking AI.

Evaluate the factual accuracy of the following response.

Response:
{response}

Return ONLY valid JSON in this format:

{{
    "fact_score": 0-100,
    "message": "Short explanation"
}}
"""

        result = get_gemini_response(prompt)

        try:
            return json.loads(result)
        except Exception:
            return {
                "fact_score": 50,
                "message": "Unable to parse Gemini response."
            }