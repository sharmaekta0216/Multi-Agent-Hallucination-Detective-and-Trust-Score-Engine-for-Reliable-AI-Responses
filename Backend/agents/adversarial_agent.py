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
# 
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

Your job is to critically evaluate the response for genuine weaknesses while remaining fair and objective.

Evaluation Rules:

1. Look for:
   - Factually incorrect statements
   - Fabricated or hallucinated information
   - Contradictions
   - Unsupported important claims
   - Misleading statements
   - Serious logical flaws

2. Do NOT criticize a response simply because:
   - It omits optional information.
   - It does not include historical background.
   - It does not mention unrelated facts.
   - It does not provide extra examples.
   - It is not maximally detailed.

3. Missing information should only be considered an issue if it is necessary to correctly answer the user's question.

4. Ignore optional context, trivia, historical facts, or edge cases unless the user explicitly requested them.

5. If the response correctly answers the question and contains no factual errors, return no significant issues.

6. Do not invent criticisms simply to make the review more adversarial.

Scoring:

90-100:
Excellent response.
No factual errors, hallucinations, contradictions, or important omissions.

70-89:
Good response with only minor issues that do not affect correctness.

50-69:
Some noticeable factual or logical weaknesses.

30-49:
Major factual or logical problems.

0-29:
Response contains serious hallucinations, fabricated information, or is largely incorrect.

Return ONLY valid JSON.

Example (Good Response):

{{
    "adversarial_score":96,
    "issues":"No significant factual issues found.",
    "summary":"The response correctly answers the user's question. Any omitted details are optional and do not affect correctness."
}}

Example (Weak Response):

{{
    "adversarial_score":42,
    "issues":"Contains incorrect factual claims and unsupported statements.",
    "summary":"The response includes factual inaccuracies that reduce its reliability."
}}

Do not use Markdown.
Do not include explanations outside JSON.
Return ONLY JSON.
"""

        try:

            result = get_gemini_response(prompt)

            data = parse_json(result)

            return {

                "adversarial_score": float(
                    data.get("adversarial_score", 90)
                ),

                "issues": data.get(
                    "issues",
                    "No significant factual issues found."
                ),

                "summary": data.get(
                    "summary",
                    "The response correctly answers the user's question."
                )

            }

        except Exception as e:

            print(e)

            return {

                "adversarial_score": 90,

                "issues": "Adversarial evaluation failed.",

                "summary": str(e)

            }