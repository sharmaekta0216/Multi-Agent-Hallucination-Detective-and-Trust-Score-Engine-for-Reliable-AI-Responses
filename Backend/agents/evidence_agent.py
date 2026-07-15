# class EvidenceAgent:

#     def check_evidence(self, response: str):

#         print("Evidence Agent Running...")

#         evidence_score = 90

#         return {
#             "evidence_score": evidence_score,
#             "message": "Evidence Found"
#         }
# import json
# from services.gemini_service import get_gemini_response


# class EvidenceAgent:

#     def check_evidence(self, response: str):

#         print("Evidence Agent Running...")

#         prompt = f"""
# You are an AI Evidence Evaluation Agent.

# Analyze the following AI response and determine whether the claims are supported by evidence.

# AI Response:
# {response}

# Evaluate:
# 1. Are factual claims supported?
# 2. Is sufficient evidence provided?
# 3. Are important claims missing evidence?
# 4. Overall evidence quality.

# Return ONLY valid JSON.

# Example:

# {{
#     "evidence_score": 85,
#     "message": "Most claims are supported, but some important statements lack evidence."
# }}
# """

#         try:

#             result = get_gemini_response(prompt)

#             # Remove markdown if Gemini returns ```json
#             result = result.replace("```json", "").replace("```", "").strip()

#             data = json.loads(result)

#             return {
#                 "evidence_score": data.get("evidence_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print(e)
#             return{
#                 "evidence_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
import json
from services.gemini_service import get_gemini_response


class EvidenceAgent:

    def check_evidence(self, response: str):

        print("\n========== EVIDENCE AGENT ==========")

        prompt = f"""
You are an expert Evidence Evaluation Agent.

Your task is to evaluate how well the AI response is supported by evidence.

Evaluate the following:

1. Are factual claims supported?
2. Are examples provided where appropriate?
3. Is the explanation complete?
4. Are important claims missing supporting evidence?
5. Is the information reliable and well-supported?

Scoring Guide:
- 90-100 = Excellent evidence and supporting facts.
- 70-89 = Good evidence with minor gaps.
- 50-69 = Limited supporting evidence.
- 30-49 = Weak evidence.
- 0-29 = No evidence or unsupported claims.

AI Response:
{response}

Return ONLY valid JSON in this exact format:

{{
    "evidence_score": 90,
    "message": "Short explanation."
}}

Do NOT include markdown.
Do NOT include ```json.
Do NOT include any extra text.
"""

        try:

            result = get_gemini_response(prompt)

            print("Raw Gemini Response:")
            print(result)

            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

            print("\nCleaned Response:")
            print(result)

            data = json.loads(result)

            print("\nParsed JSON:")
            print(data)

            return {
                "evidence_score": data.get("evidence_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print("\nEvidenceAgent JSON Parsing Error:")
            print(e)

            return {
                "evidence_score": 50,
                "message": "Unable to parse Gemini response."
            }