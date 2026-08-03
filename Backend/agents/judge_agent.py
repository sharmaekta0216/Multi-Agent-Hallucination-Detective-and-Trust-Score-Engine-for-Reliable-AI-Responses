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
# from services.gemini_service import get_gemini_response
# from utils.json_parser import parse_json


# class JudgeAgent:

#     def __init__(self):
#         print("Judge Agent Initialized")

#     def evaluate(self, question, ai_response, analysis, adversarial):

#         prompt = f"""
# You are the Final AI Judge.

# Question:
# {question}

# AI Response:
# {ai_response}

# Analysis Report:

# Fact Score:
# {analysis["fact_score"]}
# Reason:
# {analysis["fact_message"]}

# Logic Score:
# {analysis["logic_score"]}
# Reason:
# {analysis["logic_message"]}

# Evidence Score:
# {analysis["evidence_score"]}
# Reason:
# {analysis["evidence_message"]}

# Hallucination Score:
# {analysis["hallucination_score"]}
# Reason:
# {analysis["hallucination_message"]}

# Adversarial Score:
# {adversarial["adversarial_score"]}

# Issues:
# {adversarial["issues"]}

# Summary:
# {adversarial["summary"]}

# Your job:

# 1. Review every agent.
# 2. Decide whether the answer is Reliable.
# 3. Give a short explanation.
# 4. Give one recommendation.

# Return ONLY JSON.

# {{
# "judge_decision":"Reliable",

# "explanation":"The answer is factually correct and logically consistent. Minor improvements are possible.",

# "recommendation":"Provide one supporting source to improve reliability."
# }}

# Do not write markdown.
# Only JSON.
# """

#         try:

#             result = get_gemini_response(prompt)

#             data = parse_json(result)

#             return {

#                 "judge_decision": data.get(
#                     "judge_decision",
#                     "Unknown"
#                 ),

#                 "explanation": data.get(
#                     "explanation",
#                     ""
#                 ),

#                 "recommendation": data.get(
#                     "recommendation",
#                     ""
#                 )

#             }

#         except Exception as e:

#             print(e)

#             return {

#                 "judge_decision": "Unknown",

#                 "explanation": str(e),

#                 "recommendation": "Judge Agent Failed"

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

Analysis Report

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


=========================
Evaluation Instructions
=========================

You are a FAIR and BALANCED AI Judge.

Your responsibility is to determine whether the AI response is reliable based on factual correctness, logical reasoning, evidence quality, hallucination detection, and the adversarial review.

Follow these rules strictly:

1. Prioritize factual accuracy over completeness.

2. DO NOT criticize an answer simply because it omits optional, historical, edge-case, or unrelated information.

3. Missing information should only be considered an issue if it is necessary to correctly answer the user's question.

4. Ignore additional trivia, historical background, tourist information, or extra governance details unless the user specifically asked for them.

5. If the response correctly answers the user's question and contains no factual errors or hallucinations, mark it as "Reliable".

6. Do NOT invent criticisms just to make the review more adversarial.

7. If the Adversarial Review only points out optional omissions or irrelevant improvements, ignore them when making the final decision.

8. Only consider these as major issues:
   - Factually incorrect statements
   - Fabricated information
   - Contradictions
   - Misleading claims
   - Unsupported critical claims

9. Recommendations should only be given if there is a genuine weakness.
If no meaningful improvement is required, return:
"None"

10. Keep the explanation concise (1–3 sentences).

11. If Fact, Logic, and Evidence scores are high and Hallucination score indicates no hallucination, the decision should normally be "Reliable".


Return ONLY valid JSON.

Example:

{{
    "judge_decision": "Reliable",
    "explanation": "The response accurately answers the user's question without factual errors or hallucinations. Optional omitted details do not reduce reliability.",
    "recommendation": "None"
}}

Do not return Markdown.
Do not return code fences.
Return ONLY JSON.
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
                    "None"
                )

            }

        except Exception as e:

            print(e)

            return {

                "judge_decision": "Unknown",

                "explanation": str(e),

                "recommendation": "Judge Agent Failed"

            }