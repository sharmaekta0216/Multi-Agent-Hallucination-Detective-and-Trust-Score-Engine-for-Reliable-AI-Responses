# agents/workflow.py

# from agents.response_agent import ResponseAgent
# from agents.evidence_agent import EvidenceAgent
# from agents.hallucination_agent import HallucinationAgent
# from agents.trust_agent import TrustAgent


# class MultiAgentWorkflow:

#     def __init__(self, llm):

#         self.response_agent = ResponseAgent(llm)
#         self.evidence_agent = EvidenceAgent()
#         self.hallucination_agent = HallucinationAgent()
#         self.trust_agent = TrustAgent()

#     def execute(self, query):

#         # Step 1
#         response = self.response_agent.generate_response(query)

#         # Step 2
#         evidence = self.evidence_agent.collect_evidence(
#             query,
#             response["response"]
#         )

#         # Step 3
#         hallucination = self.hallucination_agent.analyze(
#             response["response"],
#             evidence
#         )

#         # Step 4
#         trust = self.trust_agent.calculate_score(
#             fact_score=90,
#             evidence_score=90,
#             hallucination_score=hallucination["hallucination_score"]
#         )

#         return {
#             "query": query,
#             "response": response["response"],
#             "evidence": evidence,
#             "hallucination": hallucination,
#             "trust": trust
#         }
from gemini_service import get_gemini_response
from agents.response_agent import ResponseAgent
from agents.fact_checker import FactAgent
from agents.logic_checker import LogicAgent
from agents.evidence_agent import EvidenceAgent
from agents.hallucination_agent import HallucinationAgent
from score.trust_score import TrustAgent


def run_workflow(query):

    response_agent = ResponseAgent()
    fact_checker = FactAgent()
    logic_checker = LogicAgent()
    evidence_agent = EvidenceAgent()
    hallucination_agent = HallucinationAgent()
    trust_agent = TrustAgent()

    response = response_agent.generate_response(query)

    fact = fact_checker.check_fact(response["response"])
    logic = logic_checker.check_logic(response["response"])
    evidence = evidence_agent.check_evidence(response["response"])
    hallucination = hallucination_agent.detect_hallucination(response["response"])

    trust = trust_agent.calculate_score(
        fact["fact_score"],
        logic["logic_score"],
        evidence["evidence_score"],
        hallucination["hallucination_score"]
    )

    return {
        "response": response,
        "fact": fact,
        "logic": logic,
        "evidence": evidence,
        "hallucination": hallucination,
        "trust": trust
    }