# class LogicAgent:

#     def check_logic(self, response: str):

#         print("Logic Agent Running...")

#         # Demo logic score
#         logic_score = 88

#         return {
#             "logic_score": logic_score,
#             "message": "Logical Consistency Verified"
#         }
# import json
# from services.gemini_service import get_gemini_response


# class LogicAgent:

#     def check_logic(self, response: str):

#         print("Logic Agent Running...")

#         prompt = f"""
# You are an AI Logic Checking Agent.

# Analyze the logical consistency of the following AI response.

# AI Response:
# {response}

# Check for:
# 1. Logical consistency
# 2. Contradictions
# 3. Reasoning quality
# 4. Coherence

# Return ONLY valid JSON.

# Example:

# {{
#     "logic_score": 88,
#     "message": "The response is logically consistent with no major contradictions."
# }}
# """

#         try:

#             result = get_gemini_response(prompt)

#             # Remove markdown if Gemini returns ```json
#             result = result.replace("```json", "").replace("```", "").strip()

#             data = json.loads(result)

#             return {
#                 "logic_score": data.get("logic_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print(e)

#             return {
#                 "logic_score": 50,
#                 "message": "Logic checking failed."
#             }
# import json
# from services.gemini_service import get_gemini_response


# class LogicAgent:

#     def check_logic(self, response: str):

#         print("\n========== LOGIC AGENT ==========")

#         prompt = f"""
# You are an expert Logical Reasoning Agent.

# Your job is to evaluate the logical quality of the AI response.

# Evaluate the following:

# 1. Is the reasoning logical?
# 2. Are there any contradictions?
# 3. Does the conclusion follow from the explanation?
# 4. Is the answer coherent and well-organized?
# 5. Is every statement consistent with the rest of the response?

# Scoring Guide:
# - 90-100 = Excellent logical reasoning.
# - 70-89 = Mostly logical with minor issues.
# - 50-69 = Some logical inconsistencies.
# - 30-49 = Weak reasoning.
# - 0-29 = Illogical or contradictory.

# AI Response:
# {response}

# Return ONLY valid JSON in this exact format:

# {{
#     "logic_score": 90,
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
#                 "logic_score": data.get("logic_score", 50),
#                 "message": data.get("message", "No explanation")
#             }

#         except Exception as e:

#             print("\nLogicAgent JSON Parsing Error:")
#             print(e)

#             return {
#                 "logic_score": 50,
#                 "message": "Unable to parse Gemini response."
#             }
# import json
# import re
# from services.gemini_service import get_gemini_response


# class LogicAgent:

#     def __init__(self):
#         print("Logic Agent Initialized")


#     def check_logic(self, response: str):

#         print("\n========== LOGIC AGENT ==========")

#         prompt = f"""
# You are an expert Logical Reasoning Agent.

# Your task is to evaluate the logical quality of an AI-generated response.

# AI Response:
# {response}

# Evaluate these points:

# 1. Is the reasoning clear and logical?
# 2. Are there contradictions or inconsistent statements?
# 3. Does the conclusion follow from the explanation?
# 4. Is the response coherent and well structured?
# 5. Are claims connected logically?

# Scoring:

# 90-100 = Excellent logical reasoning
# 70-89  = Good reasoning with minor issues
# 50-69  = Average reasoning with some gaps
# 30-49  = Weak reasoning
# 0-29   = Illogical or contradictory


# Return ONLY valid JSON in this format:

# {{
#     "logic_score": 85,
#     "message": "Short explanation about logical quality."
# }}

# Rules:
# - Return only JSON.
# - Do not use markdown.
# - Do not add extra text.
# """

#         try:

#             result = get_gemini_response(prompt)

#             print("Raw Gemini Response:")
#             print(result)


#             # Remove markdown if Gemini adds it
#             cleaned = result.replace("```json", "")
#             cleaned = cleaned.replace("```", "")
#             cleaned = cleaned.strip()


#             # Extract JSON from response
#             json_match = re.search(
#                 r"\{.*\}",
#                 cleaned,
#                 re.DOTALL
#             )

#             if json_match:
#                 cleaned = json_match.group()


#             print("Cleaned JSON:")
#             print(cleaned)


#             data = json.loads(cleaned)


#             logic_score = data.get(
#                 "logic_score",
#                 50
#             )


#             # Score validation
#             try:
#                 logic_score = float(logic_score)
#             except:
#                 logic_score = 50


#             logic_score = max(
#                 0,
#                 min(100, logic_score)
#             )


#             return {
#                 "logic_score": logic_score,
#                 "message": data.get(
#                     "message",
#                     "Logic evaluation completed."
#                 )
#             }


#         except Exception as e:

#             print("Logic Agent Error:")
#             print(e)

#             return {
#                 "logic_score": 50,
#                 "message": "Unable to evaluate logical reasoning."
#             }
import json
import re
from services.groq_service import get_groq_response


class LogicAgent:

    def __init__(self):
        print("Logic Agent Initialized")

    def check_logic(self, response: str):

        print("\n========== LOGIC AGENT ==========")

        prompt = f"""
You are an expert Logical Reasoning Evaluation Agent.

Your task is to evaluate the logical quality of the AI response.

AI Response:
{response}

Evaluate:

1. Is the response logically consistent?
2. Are there any contradictions?
3. Does the conclusion follow from the explanation?
4. Is the answer coherent and well-structured?
5. Does the response avoid unsupported reasoning?

Scoring Guide:

90-100 = Excellent logical reasoning
70-89  = Good logical reasoning
50-69  = Average reasoning with some issues
30-49  = Weak reasoning
0-29   = Illogical or contradictory

Return ONLY valid JSON.

Example:

{{
    "logic_score": 92,
    "message": "The response is logically consistent and well structured."
}}

Rules:
- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT include ```json.
- Do NOT add any extra explanation outside JSON.
"""

        try:

            result = get_groq_response(prompt)

            print("\nRaw GROQ Response:")
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

            score = data.get("logic_score", 50)

            try:
                score = float(score)
            except:
                score = 50

            score = max(0, min(100, score))

            return {
                "logic_score": score,
                "message": data.get(
                    "message",
                    "Logic evaluation completed."
                )
            }

        except json.JSONDecodeError as e:

            print("\nJSON Decode Error:")
            print(e)

            return {
                "logic_score": 50,
                "message": "Invalid JSON returned by Gemini."
            }

        except Exception as e:

            print("\nLogic Agent Error:")
            print(e)

            return {
                "logic_score": 50,
                "message": str(e)
            }