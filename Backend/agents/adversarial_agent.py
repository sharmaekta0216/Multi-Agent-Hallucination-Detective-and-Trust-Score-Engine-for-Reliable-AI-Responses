# import json
# from services.gemini_service import get_gemini_response


# class AdversarialAgent:

#     def analyze(self, question, answer):
#         prompt = f"""
# You are an expert AI adversarial evaluator.

# Question:
# {question}

# AI Answer:
# {answer}

# Your task is to challenge the answer.

# Check for:
# 1. Incorrect facts
# 2. Weak reasoning
# 3. Missing important information
# 4. Contradictions
# 5. Overconfidence
# 6. Unsupported claims

# Return ONLY valid JSON.

# Example:

# {{
#     "adversarial_score": 85,
#     "issues": [
#         "Minor missing information"
#     ],
#     "summary": "Answer is mostly reliable but could include more details."
# }}
# """

#         try:
#             response = get_gemini_response(prompt)

#             # Extract JSON if Gemini adds markdown
#             response = response.replace("```json", "").replace("```", "").strip()

#             return json.loads(response)

#         except Exception as e:

#             return {
#                 "adversarial_score": 50,
#                 "issues": ["Evaluation failed"],
#                 "summary": str(e)
#             }
import json
from services.gemini_service import get_gemini_response
from utils.json_parser import parse_json


class AdversarialAgent:

    def __init__(self):
        print("Adversarial Agent Initialized")

    def analyze(self, question, ai_response):

        prompt = f"""
You are an AI Adversarial Evaluation Agent.

Question:
{question}

AI Response:
{ai_response}

Your task is to challenge the AI response instead of supporting it.

Find:

1. Incorrect facts
2. Missing important information
3. Weak reasoning
4. Unsupported claims
5. Contradictions
6. Overconfidence
7. Ambiguous statements

Give an overall score.

Scoring:

90-100 = Excellent response with almost no weaknesses

70-89 = Good response with minor weaknesses

50-69 = Average response

30-49 = Weak response

0-29 = Poor response

Return ONLY JSON.
Example:

{{
    "adversarial_score":85,
    "issues":"Minor missing information.",
    "summary":"The answer is mostly reliable but lacks complete details."
}}

Do not use markdown.
Do not explain outside JSON.
"""

        try:

            result = get_gemini_response(prompt)

            data = parse_json(result)

            return {

                "adversarial_score": float(
                    data.get("adversarial_score", 50)
                ),

                "issues": data.get(
                    "issues",
                    ""
                ),

                "summary": data.get(
                    "summary",
                    ""
                )

            }

        except Exception as e:

            print(e)

            return {

                "adversarial_score": 50,

                "issues": str(e),

                "summary": "Adversarial analysis failed."

            }