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
# import json
# from services.gemini_service import get_gemini_response


# class FactAgent:

#     def check_fact(self, response: str):

#         prompt = f"""
# You are an expert Fact Verification Agent.

# Your job is to evaluate the factual accuracy of an AI-generated response.

# Evaluate based on:
# 1. Accuracy of facts.
# 2. Correct names, dates, numbers and places.
# 3. Presence of false or misleading statements.
# 4. Overall factual reliability.

# Scoring Guide:
# - 90-100: Completely factually correct.
# - 70-89: Mostly correct with minor issues.
# - 50-69: Some factual mistakes.
# - 30-49: Many incorrect facts.
# - 0-29: Mostly false or fabricated.

# AI Response:
# {response}

# Return ONLY valid JSON in this exact format:

# {{
#     "fact_score": 95,
#     "message": "Short explanation of why this score was given."
# }}

# Do NOT include markdown.
# Do NOT include ```json.
# Do NOT include any extra text.
# """

#         result = get_gemini_response(prompt)

#         print("\n========== FACT AGENT ==========")
#         print("Raw Gemini Response:")
#         print(result)

#         try:
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
#             print("Gemini Output:", result)

#             return {
#                 "fact_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
# import json
# import re
# from services.gemini_service import get_gemini_response


# class FactAgent:

#     def __init__(self):
#         print("Fact Agent Initialized")


#     def check_fact(self, response: str):

#         print("\n========== FACT AGENT ==========")


#         prompt = f"""
# You are an expert Fact Verification Agent.

# Analyze the factual accuracy of the AI response.

# AI Response:
# {response}

# Evaluate:

# 1. Are the facts correct?
# 2. Are names, dates, places, and numbers accurate?
# 3. Are there false or misleading claims?
# 4. Is the overall information reliable?


# Scoring:

# 90-100 : Completely factually correct
# 70-89  : Mostly correct with minor issues
# 50-69  : Some factual errors
# 30-49  : Many incorrect facts
# 0-29   : False or fabricated information


# Return ONLY JSON:

# {{
#     "fact_score": number,
#     "message": "short explanation"
# }}


# Rules:
# - Return only JSON.
# - Do not add markdown.
# - Do not add extra text.
# """


#         try:

#             result = get_gemini_response(prompt)

#             print("Raw Gemini Response:")
#             print(result)


#             # Remove markdown formatting
#             cleaned = result.replace("```json", "")
#             cleaned = cleaned.replace("```", "")
#             cleaned = cleaned.strip()


#             # Extract JSON if Gemini adds extra text
#             match = re.search(
#                 r"\{.*\}",
#                 cleaned,
#                 re.DOTALL
#             )

#             if match:
#                 cleaned = match.group()


#             print("Cleaned JSON:")
#             print(cleaned)


#             data = json.loads(cleaned)


#             fact_score = data.get(
#                 "fact_score",
#                 50
#             )


#             # Validate score
#             try:
#                 fact_score = float(fact_score)
#             except:
#                 fact_score = 50


#             fact_score = max(
#                 0,
#                 min(100, fact_score)
#             )


#             return {
#                 "fact_score": fact_score,
#                 "message": data.get(
#                     "message",
#                     "Fact evaluation completed."
#                 )
#             }


#         except Exception as e:

#             print("Fact Agent Error:")
#             print(e)

#             return {
#                 "fact_score": 50,
#                 "message": "Unable to evaluate factual accuracy."
#             }
import json
import re
from services.gemini_service import get_gemini_response


class FactAgent:

    def __init__(self):
        print("Fact Agent Initialized")

    def check_fact(self, response: str):

        print("\n========== FACT AGENT ==========")

        prompt = f"""
You are an expert Fact Verification Agent.

Your task is to evaluate the factual accuracy of the AI response.

AI Response:
{response}

Evaluate:

1. Are all factual statements correct?
2. Are names, dates, places, numbers and events accurate?
3. Are there misleading or false claims?
4. Is the information consistent with known facts?
5. Is the response reliable?

Scoring Guide:

90-100 = Completely factually correct
70-89  = Mostly correct with minor inaccuracies
50-69  = Some factual mistakes
30-49  = Many factual errors
0-29   = Mostly false or fabricated

Return ONLY valid JSON.

Example:

{{
    "fact_score": 95,
    "message": "The response is factually correct with accurate information."
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

            score = data.get("fact_score", 50)

            # Convert score safely
            try:
                score = float(score)
            except:
                score = 50

            score = max(0, min(100, score))

            return {
                "fact_score": score,
                "message": data.get(
                    "message",
                    "Fact evaluation completed."
                )
            }

        except json.JSONDecodeError as e:

            print("\nJSON Decode Error:")
            print(e)

            return {
                "fact_score": 50,
                "message": "Invalid JSON returned by Gemini."
            }

        except Exception as e:

            print("\nFact Agent Error:")
            print(e)

            return {
                "fact_score": 50,
                "message": str(e)
            }