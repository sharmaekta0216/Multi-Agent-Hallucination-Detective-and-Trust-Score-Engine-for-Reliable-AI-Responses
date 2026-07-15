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
import json
from services.gemini_service import get_gemini_response


class LogicAgent:

    def check_logic(self, response: str):

        print("\n========== LOGIC AGENT ==========")

        prompt = f"""
You are an expert Logical Reasoning Agent.

Your job is to evaluate the logical quality of the AI response.

Evaluate the following:

1. Is the reasoning logical?
2. Are there any contradictions?
3. Does the conclusion follow from the explanation?
4. Is the answer coherent and well-organized?
5. Is every statement consistent with the rest of the response?

Scoring Guide:
- 90-100 = Excellent logical reasoning.
- 70-89 = Mostly logical with minor issues.
- 50-69 = Some logical inconsistencies.
- 30-49 = Weak reasoning.
- 0-29 = Illogical or contradictory.

AI Response:
{response}

Return ONLY valid JSON in this exact format:

{{
    "logic_score": 90,
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
                "logic_score": data.get("logic_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print("\nLogicAgent JSON Parsing Error:")
            print(e)

            return {
                "logic_score": 50,
                "message": "Unable to parse Gemini response."
            }