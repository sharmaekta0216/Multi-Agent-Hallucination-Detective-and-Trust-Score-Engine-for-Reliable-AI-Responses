class EvidenceAgent:

    def check_evidence(self, response: str):

        print("Evidence Agent Running...")

        evidence_score = 90

        return {
            "evidence_score": evidence_score,
            "message": "Evidence Found"
        }