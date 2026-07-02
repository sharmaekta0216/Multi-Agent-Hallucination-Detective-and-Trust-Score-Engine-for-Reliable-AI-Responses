class TrustAgent:

    def calculate_score(self, fact_score, logic_score, evidence_score, hallucination_score):

        trust_score = (
            fact_score * 0.30 +
            logic_score * 0.20 +
            evidence_score * 0.30 +
            (100 - hallucination_score) * 0.20
        )

        if trust_score >= 80:
            trust_level = "High"
        elif trust_score >= 60:
            trust_level = "Medium"
        else:
            trust_level = "Low"

        return {
            "trust_score": round(trust_score, 2),
            "trust_level": trust_level
        }