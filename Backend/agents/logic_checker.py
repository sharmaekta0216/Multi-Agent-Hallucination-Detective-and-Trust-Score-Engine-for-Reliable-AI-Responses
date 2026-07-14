# class LogicAgent:

#     def check_logic(self, response: str):

#         print("Logic Agent Running...")

#         # Demo logic score
#         logic_score = 88

#         return {
#             "logic_score": logic_score,
#             "message": "Logical Consistency Verified"
#         }
import json
from services.gemini_service import get_gemini_response


class LogicAgent:

    def check_logic(self, response: str):

        print("Logic Agent Running...")

        prompt = f"""
You are an AI Logic Checking Agent.

Analyze the logical consistency of the following AI response.

AI Response:
{response}

Check for:
1. Logical consistency
2. Contradictions
3. Reasoning quality
4. Coherence

Return ONLY valid JSON.

Example:

{{
    "logic_score": 88,
    "message": "The response is logically consistent with no major contradictions."
}}
"""

        try:

            result = get_gemini_response(prompt)

            # Remove markdown if Gemini returns ```json
            result = result.replace("```json", "").replace("```", "").strip()

            data = json.loads(result)

            return {
                "logic_score": data.get("logic_score", 50),
                "message": data.get("message", "No explanation")
            }

        except Exception as e:

            print(e)

            return {
                "logic_score": 50,
                "message": "Logic checking failed."
            }