# class FactAgent:

#     def check_fact(self, response: str):

#         print("Fact Agent Running...")

#         # Demo fact score
#         fact_score = 85

#         return {
#             "fact_score": fact_score,
#             "message": "Facts Verified"
#         }
# import json
# from services.gemini_service import get_gemini_response

# class FactAgent:

#     def check_fact(self, response: str):

#         prompt = f"""
# You are a fact-checking AI.

# Evaluate the factual accuracy of the following response.

# Response:
# {response}

# Return ONLY valid JSON in this format:

# {{
#     "fact_score": 0-100,
#     "message": "Short explanation"
# }}
# """

#         result = get_gemini_response(prompt)

#         try:
#             return json.loads(result)
#         except Exception:
#             return {
#                 "fact_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
# import json
# from services.gemini_service import get_gemini_response


# class FactAgent:

#     def check_fact(self, response: str):

#         prompt = f"""
# You are a fact-checking AI.

# Evaluate the factual accuracy of the following response.

# Response:
# {response}

# Return ONLY valid JSON in this format:

# {{
#     "fact_score": 0-100,
#     "message": "Short explanation"
# }}

# Do not include markdown, code fences, or any extra text.
# """

#         result = get_gemini_response(prompt)

#         print("\n========== FACT AGENT ==========")
#         print("Raw Gemini Response:")
#         print(result)

#         try:
#             # Remove markdown code blocks if Gemini adds them
#             clean_result = result.replace("```json", "")
#             clean_result = clean_result.replace("```", "")
#             clean_result = clean_result.strip()

#             print("\nCleaned Response:")
#             print(clean_result)

#             data = json.loads(clean_result)

#             print("\nParsed JSON:")
#             print(data)

#             return data

#         except Exception as e:
#             print("\nFactAgent JSON Parsing Error:")
#             print(e)

#             return {
#                 "fact_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
import json
from services.gemini_service import get_gemini_response


class FactAgent:

    def check_fact(self, response: str):

        prompt = f"""
You are an expert Fact Verification Agent.

Your job is to evaluate the factual accuracy of an AI-generated response.

Evaluate based on:
1. Accuracy of facts.
2. Correct names, dates, numbers and places.
3. Presence of false or misleading statements.
4. Overall factual reliability.

Scoring Guide:
- 90-100: Completely factually correct.
- 70-89: Mostly correct with minor issues.
- 50-69: Some factual mistakes.
- 30-49: Many incorrect facts.
- 0-29: Mostly false or fabricated.

AI Response:
{response}

Return ONLY valid JSON in this exact format:

{{
    "fact_score": 95,
    "message": "Short explanation of why this score was given."
}}

Do NOT include markdown.
Do NOT include ```json.
Do NOT include any extra text.
"""

        result = get_gemini_response(prompt)

        print("\n========== FACT AGENT ==========")
        print("Raw Gemini Response:")
        print(result)

        try:
            clean_result = result.replace("```json", "")
            clean_result = clean_result.replace("```", "")
            clean_result = clean_result.strip()

            print("\nCleaned Response:")
            print(clean_result)

            data = json.loads(clean_result)

            print("\nParsed JSON:")
            print(data)

            return data

        except Exception as e:
            print("\nFactAgent JSON Parsing Error:")
            print(e)
            print("Gemini Output:", result)

            return {
                "fact_score": 50,
                "message": "Unable to parse Gemini response."
            }