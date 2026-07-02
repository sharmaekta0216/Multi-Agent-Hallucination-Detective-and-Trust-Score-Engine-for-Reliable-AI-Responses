class FactAgent:

    def check_fact(self, response: str):

        print("Fact Agent Running...")

        # Demo fact score
        fact_score = 85

        return {
            "fact_score": fact_score,
            "message": "Facts Verified"
        }