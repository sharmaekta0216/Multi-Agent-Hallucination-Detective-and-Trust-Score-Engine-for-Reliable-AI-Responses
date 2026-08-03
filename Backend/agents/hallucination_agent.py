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
# import json
# from services.gemini_service import get_gemini_response


# class HallucinationAgent:

#     def detect_hallucination(self, response: str):

#         print("\n========== HALLUCINATION AGENT ==========")

#         prompt = f"""
# You are an expert AI Hallucination Detection Agent.

# Your task is to detect whether the AI response contains fabricated,
# unsupported, misleading, or imaginary information.

# Evaluate the following:

# 1. Does the response contain invented facts?
# 2. Are there unsupported claims?
# 3. Are names, dates, places, or statistics fabricated?
# 4. Does the response sound overly confident despite lacking evidence?
# 5. Overall hallucination risk.

# Scoring Guide:
# - 0-10 = No hallucination detected.
# - 11-30 = Very low hallucination risk.
# - 31-50 = Moderate hallucination risk.
# - 51-70 = High hallucination risk.
# - 71-100 = Severe hallucination.

# AI Response:
# {response}

# Return ONLY valid JSON in this exact format:

# {{
#     "hallucination_score": 15,
#     "message": "Short explanation."
# }}

# Do NOT include markdown.
# Do NOT include ```json.
# Do NOT include any extra text.
# """

#         try:

#             result = get_gemini_response(prompt)

#             print("Raw Gemini Response:")
#             print(result)

#             result = result.replace("```json", "")
#             result = result.replace("```", "")
#             result = result.strip()

#             print("\nCleaned Response:")
#             print(result)

#             data = json.loads(result)

#             print("\nParsed JSON:")
#             print(data)

#             return {
#                 "hallucination_score": data.get("hallucination_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print("\nHallucinationAgent JSON Parsing Error:")
#             print(e)

#             return {
#                 "hallucination_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
# import json
# import re
# from services.gemini_service import get_gemini_response


# class HallucinationAgent:

#     def detect_hallucination(self, response: str):

#         print("\n========== HALLUCINATION AGENT ==========")

#         prompt = f"""
# You are an expert AI Hallucination Detection Agent.

# Analyze the AI response and detect fabricated, unsupported,
# misleading, or incorrect information.

# AI Response:
# {response}

# Evaluate:
# 1. Are any facts invented?
# 2. Are claims unsupported?
# 3. Are names, dates, numbers, or events suspicious?
# 4. Is the response overly confident without evidence?
# 5. Overall hallucination risk.

# Scoring:
# 0-10   : No hallucination
# 11-30  : Very low risk
# 31-50  : Moderate risk
# 51-70  : High risk
# 71-100 : Severe hallucination

# Return ONLY JSON:

# {{
#     "hallucination_score": number,
#     "message": "short explanation"
# }}

# Do not add markdown.
# Do not add extra text.
# """

#         try:

#             result = get_gemini_response(prompt)

#             print("Raw Gemini Response:")
#             print(result)


#             # Remove markdown if present
#             cleaned = result.replace("```json", "")
#             cleaned = cleaned.replace("```", "")
#             cleaned = cleaned.strip()


#             # Extract JSON from extra text
#             match = re.search(r"\{.*\}", cleaned, re.DOTALL)

#             if match:
#                 cleaned = match.group()


#             print("Cleaned JSON:")
#             print(cleaned)


#             data = json.loads(cleaned)


#             score = data.get("hallucination_score", 50)


#             # Validate score
#             if not isinstance(score, (int, float)):
#                 score = 50


#             score = max(0, min(100, score))


#             return {
#                 "hallucination_score": score,
#                 "message": data.get(
#                     "message",
#                     "Hallucination analysis completed."
#                 )
#             }


#         except Exception as e:

#             print("HallucinationAgent Error:")
#             print(e)

#             return {
#                 "hallucination_score": 50,
#                 "message": "Hallucination analysis failed."
#             }
import json
import re
from services.gemini_service import get_gemini_response


class HallucinationAgent:

    def __init__(self):
        print("Hallucination Agent Initialized")

    def detect_hallucination(self, response: str):

        print("\n========== HALLUCINATION AGENT ==========")

        prompt = f"""
You are an expert AI Hallucination Detection Agent.

Your task is to detect fabricated, unsupported, misleading,
or incorrect information in the AI response.

AI Response:
{response}

Evaluate:

1. Are any facts invented?
2. Are any claims unsupported?
3. Are names, dates, numbers or events fabricated?
4. Does the response sound overconfident without evidence?
5. What is the overall hallucination risk?

Scoring Guide:

0-10   = No hallucination
11-30  = Very Low hallucination risk
31-50  = Moderate hallucination risk
51-70  = High hallucination risk
71-100 = Severe hallucination

Return ONLY valid JSON.

Example:

{{
    "hallucination_score": 12,
    "message": "The response contains no fabricated or unsupported claims."
}}

Rules:
- Return only JSON.
- Do not use markdown.
- Do not write anything outside the JSON object.
"""

        try:

            result = get_gemini_response(prompt)

            print("\nRaw Gemini Response:")
            print(result)

            if not result:
                raise ValueError("Empty response from Gemini.")

            # Remove markdown
            cleaned = result.replace("```json", "")
            cleaned = cleaned.replace("```", "")
            cleaned = cleaned.strip()

            # Extract JSON
            match = re.search(r"\{[\s\S]*\}", cleaned)

            if not match:
                raise ValueError("No JSON object found.")

            cleaned = match.group(0)

            print("\nExtracted JSON:")
            print(cleaned)

            data = json.loads(cleaned)

            score = data.get("hallucination_score", 50)

            # Convert score safely
            try:
                score = float(score)
            except:
                score = 50

            score = max(0, min(100, score))

            return {
                "hallucination_score": score,
                "message": data.get(
                    "message",
                    "Hallucination analysis completed."
                )
            }

        except json.JSONDecodeError as e:

            print("\nJSON Decode Error:")
            print(e)

            return {
                "hallucination_score": 50,
                "message": "Invalid JSON returned by Gemini."
            }

        except Exception as e:

            print("\nHallucination Agent Error:")
            print(e)

            return {
                "hallucination_score": 50,
                "message": str(e)
            }