import json
from services.gemini_service import get_gemini_response
from utils.json_parser import parse_json


class AnalysisAgent:

    def __init__(self):
        print("Analysis Agent Initialized")

    def analyze(self, ai_response):

        prompt = f"""
You are an AI Response Evaluation Agent.

Evaluate the following AI response.

AI Response:
{ai_response}

Evaluate these four aspects:

1. Factual Accuracy
2. Logical Consistency
3. Evidence Quality
4. Hallucination Risk

Scoring Rules:

Fact Score
90-100 = Completely correct
70-89 = Mostly correct
50-69 = Some mistakes
30-49 = Many mistakes
0-29 = Mostly incorrect

Logic Score
90-100 = Excellent reasoning
70-89 = Good reasoning
50-69 = Average reasoning
30-49 = Weak reasoning
0-29 = Illogical

Evidence Score
90-100 = Strong supporting evidence
70-89 = Good evidence
50-69 = Limited evidence
30-49 = Weak evidence
0-29 = No evidence

Hallucination Score
0-10 = None
11-30 = Very Low
31-50 = Moderate
51-70 = High
71-100 = Severe

Return ONLY JSON.

{{
"fact_score":95,
"fact_message":"...",

"logic_score":92,
"logic_message":"...",

"evidence_score":88,
"evidence_message":"...",

"hallucination_score":8,
"hallucination_message":"..."
}}

Do not write markdown.
Do not write explanations outside JSON.
"""

        try:

            result = get_gemini_response(prompt)

            data = parse_json(result)

            return {

                "fact_score": float(data.get("fact_score",50)),
                "fact_message": data.get("fact_message",""),

                "logic_score": float(data.get("logic_score",50)),
                "logic_message": data.get("logic_message",""),

                "evidence_score": float(data.get("evidence_score",50)),
                "evidence_message": data.get("evidence_message",""),

                "hallucination_score": float(data.get("hallucination_score",50)),
                "hallucination_message": data.get("hallucination_message","")

            }

        except Exception as e:

            print(e)

            return {

                "fact_score":50,
                "fact_message":str(e),

                "logic_score":50,
                "logic_message":str(e),

                "evidence_score":50,
                "evidence_message":str(e),

                "hallucination_score":50,
                "hallucination_message":str(e)

            }