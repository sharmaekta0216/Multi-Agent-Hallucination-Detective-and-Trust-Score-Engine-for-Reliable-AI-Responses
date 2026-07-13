# class HallucinationAgent:

#     def detect_hallucination(self, response: str):

#         print("Hallucination Agent Running...")

#         hallucination_score = 10

#         return {
#             "hallucination_score": hallucination_score,
#             "message": "No Hallucination Detected"
#         }
import json
from backend.services.gemini_service import get_gemini_response


class HallucinationAgent:

    def detect_hallucination(self, response: str):

        print("Hallucination Agent Running...")

        prompt = f"""
You are an AI Hallucination Detection Agent.

Analyze the following AI response and estimate its hallucination risk.

AI Response:
{response}

Check:
1. Unsupported claims
2. Fabricated facts
3. False information
4. Confidence of the response

Return ONLY valid JSON.

Example:

{{
    "hallucination_score": 15,
    "message": "Low hallucination risk. Most claims appear reliable."
}}
"""

        try:

            result = get_gemini_response(prompt)

            # Remove markdown if Gemini returns ```json
            result = result.replace("```json", "").replace("```", "").strip()

            data = json.loads(result)

            return {
                "hallucination_score": data.get("hallucination_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print(e)

            return {
                "hallucination_score": 50,
                "message": "Hallucination detection failed."
            }