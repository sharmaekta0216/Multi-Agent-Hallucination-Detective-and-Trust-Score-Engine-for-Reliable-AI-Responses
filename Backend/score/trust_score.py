# class TrustAgent:

#     def calculate_score(self, fact_score, logic_score, evidence_score, hallucination_score):

#         trust_score = (
#             fact_score * 0.30 +
#             logic_score * 0.20 +
#             evidence_score * 0.30 +
#             (100 - hallucination_score) * 0.20
#         )

#         if trust_score >= 80:
#             trust_level = "High"
#         elif trust_score >= 60:
#             trust_level = "Medium"
#         else:
#             trust_level = "Low"

#         return {
#             "trust_score": round(trust_score, 2),
#             "trust_level": trust_level
#         }
# class TrustAgent:

#     def calculate_score(
#         self,
#         fact_score,
#         logic_score,
#         evidence_score,
#         hallucination_score
#     ):

#         # Convert all values to float
#         fact_score = float(fact_score)
#         logic_score = float(logic_score)
#         evidence_score = float(evidence_score)
#         hallucination_score = float(hallucination_score)

#         # Calculate Trust Score
#         trust_score = (
#             (fact_score * 0.30) +
#             (logic_score * 0.20) +
#             (evidence_score * 0.30) +
#             ((100 - hallucination_score) * 0.20)
#         )

#         # Determine Trust Level
#         if trust_score >= 90:
#             trust_level = "Very High"

#         elif trust_score >= 80:
#             trust_level = "High"

#         elif trust_score >= 60:
#             trust_level = "Medium"

#         elif trust_score >= 40:
#             trust_level = "Low"

#         else:
#             trust_level = "Very Low"

#         return {

#             "trust_score": round(trust_score, 2),

#             "trust_level": trust_level,

#             "details": {
#                 "fact_score": fact_score,
#                 "logic_score": logic_score,
#                 "evidence_score": evidence_score,
#                 "hallucination_score": hallucination_score
#             }
#         }
# class TrustAgent:

#     def calculate_score(
#         self,
#         fact_score,
#         logic_score,
#         evidence_score,
#         hallucination_score
#     ):

#         # Convert to float
#         fact_score = float(fact_score)
#         logic_score = float(logic_score)
#         evidence_score = float(evidence_score)
#         hallucination_score = float(hallucination_score)

#         # Keep values between 0 and 100
#         fact_score = max(0, min(100, fact_score))
#         logic_score = max(0, min(100, logic_score))
#         evidence_score = max(0, min(100, evidence_score))
#         hallucination_score = max(0, min(100, hallucination_score))

#         # Weighted Trust Score
#         trust_score = (
#             (fact_score * 0.30) +
#             (logic_score * 0.20) +
#             (evidence_score * 0.30) +
#             ((100 - hallucination_score) * 0.20)
#         )

#         trust_score = round(trust_score, 2)

#         # Trust Level
#         if trust_score >= 90:
#             trust_level = "Very High"
#         elif trust_score >= 80:
#             trust_level = "High"
#         elif trust_score >= 60:
#             trust_level = "Medium"
#         elif trust_score >= 40:
#             trust_level = "Low"
#         else:
#             trust_level = "Very Low"

#         print("\n========== TRUST AGENT ==========")
#         print(f"Fact Score          : {fact_score}")
#         print(f"Logic Score         : {logic_score}")
#         print(f"Evidence Score      : {evidence_score}")
#         print(f"Hallucination Score : {hallucination_score}")
#         print(f"Trust Score         : {trust_score}")
#         print(f"Trust Level         : {trust_level}")

#         return {
#             "trust_score": trust_score,
#             "trust_level": trust_level,
#             "details": {
#                 "fact_score": fact_score,
#                 "logic_score": logic_score,
#                 "evidence_score": evidence_score,
#                 "hallucination_score": hallucination_score
#             }
#         }
# class TrustAgent:

#     def __init__(self):
#         print("Trust Agent Initialized")


#     def calculate_score(
#         self,
#         fact_score,
#         logic_score,
#         evidence_score,
#         hallucination_score
#     ):

#         print("\n========== TRUST AGENT ==========")


#         # Safe score conversion
#         def normalize_score(value):
#             try:
#                 value = float(value)
#             except:
#                 value = 50

#             return max(0, min(100, value))


#         fact_score = normalize_score(fact_score)
#         logic_score = normalize_score(logic_score)
#         evidence_score = normalize_score(evidence_score)
#         hallucination_score = normalize_score(hallucination_score)


#         # Trust calculation
#         trust_score = (
#             (fact_score * 0.30) +
#             (logic_score * 0.20) +
#             (evidence_score * 0.30) +
#             ((100 - hallucination_score) * 0.20)
#         )


#         trust_score = round(trust_score, 2)


#         # Trust classification
#         if trust_score >= 90:
#             trust_level = "Very High"

#         elif trust_score >= 80:
#             trust_level = "High"

#         elif trust_score >= 60:
#             trust_level = "Medium"

#         elif trust_score >= 40:
#             trust_level = "Low"

#         else:
#             trust_level = "Very Low"



#         print(f"Fact Score          : {fact_score}")
#         print(f"Logic Score         : {logic_score}")
#         print(f"Evidence Score      : {evidence_score}")
#         print(f"Hallucination Score : {hallucination_score}")
#         print(f"Final Trust Score   : {trust_score}")
#         print(f"Trust Level         : {trust_level}")


#         return {

#             "trust_score": trust_score,

#             "trust_level": trust_level,

#             "details": {

#                 "fact_score": fact_score,

#                 "logic_score": logic_score,

#                 "evidence_score": evidence_score,

#                 "hallucination_score": hallucination_score

#             }
#         }
class TrustAgent:

    def __init__(self):
        print("Trust Agent Initialized")


    def calculate_score(
        self,
        fact_score,
        logic_score,
        evidence_score,
        hallucination_score,
        adversarial_score
    ):

        print("\n========== TRUST AGENT ==========")


        def normalize_score(value):
            try:
                value = float(value)
            except:
                value = 50

            return max(0, min(100, value))


        fact_score = normalize_score(fact_score)
        logic_score = normalize_score(logic_score)
        evidence_score = normalize_score(evidence_score)
        hallucination_score = normalize_score(hallucination_score)
        adversarial_score = normalize_score(adversarial_score)


        # Improved Trust Formula
        trust_score = (
            (fact_score * 0.25) +
            (logic_score * 0.20) +
            (evidence_score * 0.20) +
            ((100 - hallucination_score) * 0.20) +
            (adversarial_score * 0.15)
        )


        trust_score = round(trust_score, 2)


        if trust_score >= 90:
            trust_level = "Very High"

        elif trust_score >= 80:
            trust_level = "High"

        elif trust_score >= 60:
            trust_level = "Medium"

        elif trust_score >= 40:
            trust_level = "Low"

        else:
            trust_level = "Very Low"


        print(f"Fact Score          : {fact_score}")
        print(f"Logic Score         : {logic_score}")
        print(f"Evidence Score      : {evidence_score}")
        print(f"Hallucination Score : {hallucination_score}")
        print(f"Adversarial Score   : {adversarial_score}")
        print(f"Final Trust Score   : {trust_score}")
        print(f"Trust Level         : {trust_level}")


        return {

            "trust_score": trust_score,

            "trust_level": trust_level,

            "details": {

                "fact_score": fact_score,

                "logic_score": logic_score,

                "evidence_score": evidence_score,

                "hallucination_score": hallucination_score,

                "adversarial_score": adversarial_score

            }

        }