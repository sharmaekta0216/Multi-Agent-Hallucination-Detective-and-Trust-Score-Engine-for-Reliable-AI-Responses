class TrustAgent:

    def calculate_score(
        self,
        fact_score,
        evidence_score,
        hallucination_score
    ):

        final_score = (
            fact_score * 0.4 +
            evidence_score * 0.4 +
            (100 - hallucination_score) * 0.2
        )

        if final_score >= 80:
            level = "HIGH"
        elif final_score >= 60:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "trust_score": round(final_score, 2),
            "trust_level": level
        }