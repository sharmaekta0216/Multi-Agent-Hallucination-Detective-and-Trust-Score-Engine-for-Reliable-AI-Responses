# class HallucinationAgent:

#     def detect_hallucination(self, response: str):

#         print("Hallucination Agent Running...")

#         hallucination_score = 10

#         return {
#             "hallucination_score": hallucination_score,
#             "message": "No Hallucination Detected"
#         }
# import json
# from services.gemini_service import get_gemini_response


# class HallucinationAgent:

#     def detect_hallucination(self, response: str):

#         print("Hallucination Agent Running...")

#         prompt = f"""
# You are an AI Hallucination Detection Agent.

# Analyze the following AI response and estimate its hallucination risk.

# AI Response:
# {response}

# Check:
# 1. Unsupported claims
# 2. Fabricated facts
# 3. False information
# 4. Confidence of the response

# Return ONLY valid JSON.

# Example:

# {{
#     "hallucination_score": 15,
#     "message": "Low hallucination risk. Most claims appear reliable."
# }}
# """

#         try:

#             result = get_gemini_response(prompt)

#             # Remove markdown if Gemini returns ```json
#             result = result.replace("```json", "").replace("```", "").strip()

#             data = json.loads(result)

#             return {
#                 "hallucination_score": data.get("hallucination_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print(e)

#             return {
#                 "hallucination_score": 50,
#                 "message": "Hallucination detection failed."
#             }
import json
from services.gemini_service import get_gemini_response


class HallucinationAgent:

    def detect_hallucination(self, response: str):

        print("\n========== HALLUCINATION AGENT ==========")

        prompt = f"""
You are an expert AI Hallucination Detection Agent.

Your task is to detect whether the AI response contains fabricated,
unsupported, misleading, or imaginary information.

Evaluate the following:

1. Does the response contain invented facts?
2. Are there unsupported claims?
3. Are names, dates, places, or statistics fabricated?
4. Does the response sound overly confident despite lacking evidence?
5. Overall hallucination risk.

Scoring Guide:
- 0-10 = No hallucination detected.
- 11-30 = Very low hallucination risk.
- 31-50 = Moderate hallucination risk.
- 51-70 = High hallucination risk.
- 71-100 = Severe hallucination.

AI Response:
{response}

Return ONLY valid JSON in this exact format:

{{
    "hallucination_score": 15,
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
                "hallucination_score": data.get("hallucination_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print("\nHallucinationAgent JSON Parsing Error:")
            print(e)

            return {
                "hallucination_score": 50,
                "message": "Unable to parse Gemini response."
            }