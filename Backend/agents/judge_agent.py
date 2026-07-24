# import json
# from services.gemini_service import get_gemini_response


# class JudgeAgent:

#     def evaluate(
#         self,
#         question,
#         answer,
#         fact_result,
#         logic_result,
#         evidence_result,
#         hallucination_result,
#         adversarial_result
#     ):

#         prompt = f"""
# You are the Final AI Judge.

# Question:
# {question}

# Answer:
# {answer}

# Fact Agent:
# {fact_result}

# Logic Agent:
# {logic_result}

# Evidence Agent:
# {evidence_result}

# Hallucination Agent:
# {hallucination_result}

# Adversarial Agent:
# {adversarial_result}

# Analyze all reports.

# Return ONLY JSON.

# Example:

# {{
#     "trust_level":"High",
#     "judge_decision":"Reliable Answer",
#     "explanation":"The answer passed all verification agents."
# }}
# """

#         try:

#             response = get_gemini_response(prompt)

#             response = response.replace("```json", "").replace("```", "").strip()

#             return json.loads(response)

#         except Exception as e:

#             return {
#                 "trust_level": "Unknown",
#                 "judge_decision": "Evaluation Failed",
#                 "explanation": str(e)
#             }
from services.gemini_service import get_gemini_response
from utils.json_parser import parse_json


class JudgeAgent:

    def __init__(self):
        print("Judge Agent Initialized")

    def evaluate(self, question, ai_response, analysis, adversarial):

        prompt = f"""
You are the Final AI Judge.

Question:
{question}

AI Response:
{ai_response}

Analysis Report:

Fact Score:
{analysis["fact_score"]}
Reason:
{analysis["fact_message"]}

Logic Score:
{analysis["logic_score"]}
Reason:
{analysis["logic_message"]}

Evidence Score:
{analysis["evidence_score"]}
Reason:
{analysis["evidence_message"]}

Hallucination Score:
{analysis["hallucination_score"]}
Reason:
{analysis["hallucination_message"]}

Adversarial Score:
{adversarial["adversarial_score"]}

Issues:
{adversarial["issues"]}

Summary:
{adversarial["summary"]}

Your job:

1. Review every agent.
2. Decide whether the answer is Reliable.
3. Give a short explanation.
4. Give one recommendation.

Return ONLY JSON.

{{
"judge_decision":"Reliable",

"explanation":"The answer is factually correct and logically consistent. Minor improvements are possible.",

"recommendation":"Provide one supporting source to improve reliability."
}}

Do not write markdown.
Only JSON.
"""

        try:

            result = get_gemini_response(prompt)

            data = parse_json(result)

            return {

                "judge_decision": data.get(
                    "judge_decision",
                    "Unknown"
                ),

                "explanation": data.get(
                    "explanation",
                    ""
                ),

                "recommendation": data.get(
                    "recommendation",
                    ""
                )

            }

        except Exception as e:

            print(e)

            return {

                "judge_decision": "Unknown",

                "explanation": str(e),

                "recommendation": "Judge Agent Failed"

            }
        