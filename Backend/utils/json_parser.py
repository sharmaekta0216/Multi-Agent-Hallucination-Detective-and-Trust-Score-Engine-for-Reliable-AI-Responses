
import json
import re


def parse_json(result):

    cleaned = result.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    match = re.search(
        r"\{.*\}",
        cleaned,
        re.DOTALL
    )

    if match:
        cleaned = match.group()

    data = json.loads(cleaned)

    return data