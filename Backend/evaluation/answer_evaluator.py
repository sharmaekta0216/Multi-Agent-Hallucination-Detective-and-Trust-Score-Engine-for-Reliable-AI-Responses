from services.gemini_service import get_gemini_response


def check_answer(correct_answer, ai_response):

    prompt = f"""
You are an answer evaluator.

Correct Answer:
{correct_answer}

AI Answer:
{ai_response}

Determine whether the AI answer is correct in meaning.

Return ONLY one word:
CORRECT
or
INCORRECT

An answer should be CORRECT if it gives the same factual meaning,
even if the wording is different.
"""

    result = get_gemini_response(prompt)

    result = result.strip().upper()

    if "CORRECT" in result:
        return "Correct"

    return "Incorrect"