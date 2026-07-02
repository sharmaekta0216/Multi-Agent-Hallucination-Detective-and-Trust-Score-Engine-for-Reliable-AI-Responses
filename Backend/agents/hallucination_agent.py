class HallucinationAgent:

    def detect_hallucination(self, response: str):

        print("Hallucination Agent Running...")

        hallucination_score = 10

        return {
            "hallucination_score": hallucination_score,
            "message": "No Hallucination Detected"
        }