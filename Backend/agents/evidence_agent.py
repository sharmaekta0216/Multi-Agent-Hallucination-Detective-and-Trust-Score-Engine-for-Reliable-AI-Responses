# class EvidenceAgent:

#     def check_evidence(self, response: str):

#         print("Evidence Agent Running...")

#         evidence_score = 90

#         return {
#             "evidence_score": evidence_score,
#             "message": "Evidence Found"
#         }
import json
from backend.services.gemini_service import get_gemini_response


class EvidenceAgent:

    def check_evidence(self, response: str):

        print("Evidence Agent Running...")

        prompt = f"""
You are an AI Evidence Evaluation Agent.

Analyze the following AI response and determine whether the claims are supported by evidence.

AI Response:
{response}

Evaluate:
1. Are factual claims supported?
2. Is sufficient evidence provided?
3. Are important claims missing evidence?
4. Overall evidence quality.

Return ONLY valid JSON.

Example:

{{
    "evidence_score": 85,
    "message": "Most claims are supported, but some important statements lack evidence."
}}
"""

        try:

            result = get_gemini_response(prompt)

            # Remove markdown if Gemini returns ```json
            result = result.replace("```json", "").replace("```", "").strip()

            data = json.loads(result)

            return {
                "evidence_score": data.get("evidence_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print(e)
            return{
                "evidence_score": 50,
                "message": "Unable to parse Gemini response."
            }