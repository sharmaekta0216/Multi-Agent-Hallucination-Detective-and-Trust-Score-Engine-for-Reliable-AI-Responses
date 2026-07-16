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
# import json
# from services.gemini_service import get_gemini_response


# class EvidenceAgent:

#     def check_evidence(self, response: str):

#         print("\n========== EVIDENCE AGENT ==========")

#         prompt = f"""
# You are an expert Evidence Evaluation Agent.

# Your task is to evaluate how well the AI response is supported by evidence.

# Evaluate the following:

# 1. Are factual claims supported?
# 2. Are examples provided where appropriate?
# 3. Is the explanation complete?
# 4. Are important claims missing supporting evidence?
# 5. Is the information reliable and well-supported?

# Scoring Guide:
# - 90-100 = Excellent evidence and supporting facts.
# - 70-89 = Good evidence with minor gaps.
# - 50-69 = Limited supporting evidence.
# - 30-49 = Weak evidence.
# - 0-29 = No evidence or unsupported claims.

# AI Response:
# {response}

# Return ONLY valid JSON in this exact format:

# {{
#     "evidence_score": 90,
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
#                 "evidence_score": data.get("evidence_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print("\nEvidenceAgent JSON Parsing Error:")
#             print(e)

#             return {
#                 "evidence_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
import json
# import re
# from services.gemini_service import get_gemini_response


# class EvidenceAgent:

#     def check_evidence(self, response: str):

#         print("\n========== EVIDENCE AGENT ==========")

#         prompt = f"""
# You are an Evidence Evaluation Agent.

# Analyze the AI response and evaluate evidence quality.

# AI Response:
# {response}

# Evaluate:
# 1. Are factual claims supported?
# 2. Are explanations provided?
# 3. Are important claims backed by evidence?
# 4. Is the response reliable?

# Scoring:
# 90-100: Strong evidence
# 70-89: Good evidence
# 50-69: Limited evidence
# 30-49: Weak evidence
# 0-29: No evidence

# Return ONLY JSON.

# Required format:
# {{
#     "evidence_score": number,
#     "message": "short explanation"
# }}
# """

#         try:
#             result = get_gemini_response(prompt)

#             print("Raw Gemini Response:")
#             print(result)

#             # Remove markdown formatting if Gemini adds it
#             cleaned = result.replace("```json", "")
#             cleaned = cleaned.replace("```", "")
#             cleaned = cleaned.strip()

#             # Extract JSON object if extra text exists
#             match = re.search(r"\{.*\}", cleaned, re.DOTALL)

#             if match:
#                 cleaned = match.group()

#             print("Cleaned JSON:")
#             print(cleaned)

#             data = json.loads(cleaned)

#             score = data.get("evidence_score", 50)

#             # Validate score range
#             if not isinstance(score, (int, float)):
#                 score = 50

#             score = max(0, min(100, score))

#             return {
#                 "evidence_score": score,
#                 "message": data.get(
#                     "message",
#                     "Evidence evaluation completed."
#                 )
#             }

#         except Exception as e:

#             print("EvidenceAgent Error:")
#             print(e)

#             return {
#                 "evidence_score": 50,
#                 "message": "Evidence evaluation failed."
#             }
import json
import re
from services.gemini_service import get_gemini_response


class EvidenceAgent:

    def __init__(self):
        print("Evidence Agent Initialized")

    def check_evidence(self, response: str):

        print("\n========== EVIDENCE AGENT ==========")

        prompt = f"""
You are an expert Evidence Evaluation Agent.

Your task is to evaluate how well the AI response is supported by evidence.

AI Response:
{response}

Evaluate:

1. Are factual claims supported?
2. Are reliable sources or references mentioned?
3. Is the explanation complete?
4. Are important claims backed by evidence?
5. Is the information trustworthy?

Scoring Guide:

90-100 = Excellent evidence
70-89  = Good evidence
50-69  = Moderate evidence
30-49  = Weak evidence
0-29   = No supporting evidence

Return ONLY valid JSON.

Example:

{{
    "evidence_score": 88,
    "message": "The response is supported by reliable evidence and explanations."
}}

Rules:
- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT include ```json.
- Do NOT write anything outside the JSON.
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

            score = data.get("evidence_score", 50)

            # Convert string score if needed
            try:
                score = float(score)
            except:
                score = 50

            score = max(0, min(100, score))

            return {
                "evidence_score": score,
                "message": data.get(
                    "message",
                    "Evidence evaluation completed."
                )
            }

        except json.JSONDecodeError as e:

            print("\nJSON Decode Error:")
            print(e)

            return {
                "evidence_score": 50,
                "message": "Invalid JSON returned by Gemini."
            }

        except Exception as e:

            print("\nEvidence Agent Error:")
            print(e)

            return {
                "evidence_score": 50,
                "message": str(e)
            }