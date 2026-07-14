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
# from gemini_service import get_gemini_response
# from agents.response_agent import ResponseAgent
# from agents.fact_checker import FactAgent
# from agents.logic_checker import LogicAgent
# from agents.evidence_agent import EvidenceAgent
# from agents.hallucination_agent import HallucinationAgent
# from score.trust_score import TrustAgent


# def run_workflow(query):

#     response_agent = ResponseAgent()
#     fact_checker = FactAgent()
#     logic_checker = LogicAgent()
#     evidence_agent = EvidenceAgent()
#     hallucination_agent = HallucinationAgent()
#     trust_agent = TrustAgent()

#     response = response_agent.generate_response(query)

#     fact = fact_checker.check_fact(response["response"])
#     logic = logic_checker.check_logic(response["response"])
#     evidence = evidence_agent.check_evidence(response["response"])
#     hallucination = hallucination_agent.detect_hallucination(response["response"])

#     trust = trust_agent.calculate_score(
#         fact["fact_score"],
#         logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )

#     return {
        
#     "success": True,
#     "question": query,
#     "ai_response": response["response"],

#     "fact_score": fact["fact_score"],
#     "logic_score": logic["logic_score"],
#     "evidence_score": evidence["evidence_score"],
#     "hallucination_score": hallucination["hallucination_score"],

#     "trust_score": trust["trust_score"],
#     "trust_level": trust["trust_level"]
# }
# from agents.response_agent import ResponseAgent
# from agents.fact_checker import FactAgent
# from agents.logic_checker import LogicAgent
# from agents.evidence_agent import EvidenceAgent
# from agents.hallucination_agent import HallucinationAgent
# from score.trust_score import TrustAgent


# def run_workflow(query):

#     # Initialize all agents
#     response_agent = ResponseAgent()
#     fact_checker = FactAgent()
#     logic_checker = LogicAgent()
#     evidence_agent = EvidenceAgent()
#     hallucination_agent = HallucinationAgent()
#     trust_agent = TrustAgent()

#     # Step 1: Generate AI Response
#     response = response_agent.generate_response(query)

#     ai_response = response["response"]

#     # Step 2: Run all evaluation agents
#     fact = fact_checker.check_fact(ai_response)
#     logic = logic_checker.check_logic(ai_response)
#     evidence = evidence_agent.check_evidence(ai_response)
#     hallucination = hallucination_agent.detect_hallucination(ai_response)

#     # Step 3: Calculate Trust Score
#     trust = trust_agent.calculate_score(
#         fact["fact_score"],
#         logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )

#     # Step 4: Return complete response
#     return {

#         "success": True,

#         "question": query,

#         "ai_response": ai_response,

#         "fact_score": fact["fact_score"],
#         "fact_message": fact["message"],

#         "logic_score": logic["logic_score"],
#         "logic_message": logic["message"],

#         "evidence_score": evidence["evidence_score"],
#         "evidence_message": evidence["message"],

#         "hallucination_score": hallucination["hallucination_score"],
#         "hallucination_message": hallucination["message"],

#         "trust_score": trust["trust_score"],
#         "trust_level": trust["trust_level"]
#     }
#  from agents.response_agent import ResponseAgent
#  from agents.fact_checker import FactAgent
#  from agents.logic_checker import LogicAgent
#  from agents.evidence_agent import EvidenceAgent
#  from agents.hallucination_agent import HallucinationAgent
#  from score.trust_score import TrustAgent
#  def run_workflow(query):
#     print("1. Workflow started")

#     response_agent = ResponseAgent()
#     fact_checker = FactAgent()
#     logic_checker = LogicAgent()
#     evidence_agent = EvidenceAgent()
#     hallucination_agent = HallucinationAgent()
#     trust_agent = TrustAgent()

#     print("2. Calling Gemini...")
#     response = response_agent.generate_response(query)
#     print("3. Gemini completed")

#     ai_response = response["response"]

#     print("4. Fact checking...")
#     fact = fact_checker.check_fact(ai_response)
#     print("5. Fact done")

#     print("6. Logic checking...")
#     logic = logic_checker.check_logic(ai_response)
#     print("7. Logic done")

#     print("8. Evidence checking...")
#     evidence = evidence_agent.check_evidence(ai_response)
#     print("9. Evidence done")

#     print("10. Hallucination checking...")
#     hallucination = hallucination_agent.detect_hallucination(ai_response)
#     print("11. Hallucination done")

#     print("12. Calculating trust...")
#     trust = trust_agent.calculate_score(
#         fact["fact_score"],
#         logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )

#     print("13. Workflow finished")

#     return {
#         "success": True,

#          "question": query,

#          "ai_response": ai_response,

#          "fact_score": fact["fact_score"],
#          "fact_message": fact["message"],

#          "logic_score": logic["logic_score"],
#          "logic_message": logic["message"],

#          "evidence_score": evidence["evidence_score"],
#          "evidence_message": evidence["message"],

#          "hallucination_score": hallucination["hallucination_score"],
#          "hallucination_message": hallucination["message"],

#          "trust_score": trust["trust_score"],
#          "trust_level": trust["trust_level"]
#      }
# from agents.response_agent import ResponseAgent
# from agents.fact_checker import FactAgent
# from agents.logic_checker import LogicAgent
# from agents.evidence_agent import EvidenceAgent
# from agents.hallucination_agent import HallucinationAgent
# from score.trust_score import TrustAgent
# from services.database_service import (
#     save_query,
#     save_response,
#     save_trust_score
# )


# def run_workflow(user_id, query):
#  def run_workflow(query):


#     print("1. Workflow Started")

#     response_agent = ResponseAgent()
#     print("2. ResponseAgent Created")

#     fact_checker = FactAgent()
#     print("3. FactAgent Created")

#     logic_checker = LogicAgent()
#     print("4. LogicAgent Created")

#     evidence_agent = EvidenceAgent()
#     print("5. EvidenceAgent Created")

#     hallucination_agent = HallucinationAgent()
#     print("6. HallucinationAgent Created")

#     trust_agent = TrustAgent()
#     print("7. TrustAgent Created")

#     print("8. Calling Gemini...")
#     response = response_agent.generate_response(query)
#     print("9. Gemini Finished")

#     ai_response = response["response"]
#     query_id = save_query(
#     user_id=user_id,
#     query_text=query
# )

#     print("10. Fact Checking")
#     fact = fact_checker.check_fact(ai_response)

#     print("11. Logic Checking")
#     logic = logic_checker.check_logic(ai_response)

#     print("12. Evidence Checking")
#     evidence = evidence_agent.check_evidence(ai_response)

#     print("13. Hallucination Checking")
#     hallucination = hallucination_agent.detect_hallucination(ai_response)

#     print("14. Calculating Trust Score")
#     trust = trust_agent.calculate_score(
#         fact["fact_score"],
#         logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )
#     response_id = save_response(
#     query_id=query_id,
#     response_text=ai_response,
#     model_name="Gemini 2.5 Flash",
#     response_time_ms=None
# )
#     save_trust_score(
#     response_id=response_id,
#     fact_score=fact["fact_score"],
#     logic_score=logic["logic_score"],
#     evidence_score=evidence["evidence_score"],
#     hallucination_score=hallucination["hallucination_score"],
#     final_trust_score=trust["trust_score"],
#     trust_level=trust["trust_level"]
# )

#     print("15. Workflow Complete")

#     return {
#         "success": True,
#         "question": query,
#         "ai_response": ai_response,
#         "fact_score": fact["fact_score"],
#         "fact_message": fact["message"],
#         "logic_score": logic["logic_score"],
#         "logic_message": logic["message"],
#         "evidence_score": evidence["evidence_score"],
#         "evidence_message": evidence["message"],
#         "hallucination_score": hallucination["hallucination_score"],
#         "hallucination_message": hallucination["message"],
#         "trust_score": trust["trust_score"],
#         "trust_level": trust["trust_level"]
#     }


# def run_workflow(query):
#     # Initialize agents
#     response_agent = ResponseAgent()
#     fact_checker = FactAgent()
#     logic_checker = LogicAgent()
#     evidence_agent = EvidenceAgent()
#     hallucination_agent = HallucinationAgent()
#     trust_agent = TrustAgent()

#     # Step 1: Generate AI response
#     response = response_agent.generate_response(query)
#     ai_response = response["response"]

#     # Step 2: Evaluate response
#     fact = fact_checker.check_fact(ai_response)
#     logic = logic_checker.check_logic(ai_response)
#     evidence = evidence_agent.check_evidence(ai_response)
#     hallucination = hallucination_agent.detect_hallucination(ai_response)

#     # Step 3: Calculate trust score
#     trust = trust_agent.calculate_score(
#         fact["fact_score"],
#         logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )

#     # Step 4: Return final result
#     return {
#         "success": True,
#         "question": query,
#         "ai_response": ai_response,

#         "fact_score": fact["fact_score"],
#         "fact_message": fact["message"],

#         "logic_score": logic["logic_score"],
#         "logic_message": logic["message"],

#         "evidence_score": evidence["evidence_score"],
#         "evidence_message": evidence["message"],

#         "hallucination_score": hallucination["hallucination_score"],
#         "hallucination_message": hallucination["message"],

#         "trust_score": trust["trust_score"],
#         "trust_level": trust["trust_level"]
#     }
from agents.response_agent import ResponseAgent
from agents.fact_checker import FactAgent
from agents.logic_checker import LogicAgent
from agents.evidence_agent import EvidenceAgent
from agents.hallucination_agent import HallucinationAgent
from score.trust_score import TrustAgent

from services.database_service import (
    save_query,
    save_response,
    save_trust_score,
    save_evidence,
    save_hallucination_analysis
)


def run_workflow(user_id, query):

    print("1. Workflow Started")

    response_agent = ResponseAgent()
    fact_checker = FactAgent()
    logic_checker = LogicAgent()
    evidence_agent = EvidenceAgent()
    hallucination_agent = HallucinationAgent()
    trust_agent = TrustAgent()

    print("2. Calling Gemini...")
    response = response_agent.generate_response(query)
    print("3. Gemini Response:", response)

    ai_response = response["response"]
    print("After gemini")
    print("before save query")
    query_id = save_query(
        user_id=user_id,
        query_text=query
        
    )
    print("after save query")

    fact = fact_checker.check_fact(ai_response)
    print("after fact checker")
    logic = logic_checker.check_logic(ai_response)
    print("after logic checker")
    evidence = evidence_agent.check_evidence(ai_response)
    print("after evidence checker")
    hallucination = hallucination_agent.detect_hallucination(ai_response)
    print("after hallucination checker")

    trust = trust_agent.calculate_score (
        
        fact["fact_score"],
          logic["logic_score"],
        evidence["evidence_score"],
        hallucination["hallucination_score"]
    )
    print("after trust score calculation")

    response_id = save_response(
        query_id=query_id,
        response_text=ai_response,
        model_name="Gemini 2.5 Flash",
        response_time_ms=None
    )
    save_evidence(
    response_id=response_id,
    source_title="Evidence Source",
    source_url="N/A",
    evidence_text=evidence["message"]
    )
    save_hallucination_analysis(
    response_id=response_id,
    hallucination_score=hallucination["hallucination_score"],
    unsupported_claims=0,
    contradiction_count=0,
    remarks=hallucination["message"]
    )

    save_trust_score(
        response_id=response_id,
        fact_score=fact["fact_score"],
        logic_score=logic["logic_score"],
        evidence_score=evidence["evidence_score"],
        hallucination_score=hallucination["hallucination_score"],
        final_trust_score=trust["trust_score"],
        trust_level=trust["trust_level"]
    )

    print("4. Workflow Complete")

    return {
        "success": True,
        "question": query,
        "ai_response": ai_response,
        "fact_score": fact["fact_score"],
        "fact_message": fact["message"],
        "logic_score": logic["logic_score"],
        "logic_message": logic["message"],
        "evidence_score": evidence["evidence_score"],
        "evidence_message": evidence["message"],
        "hallucination_score": hallucination["hallucination_score"],
        "hallucination_message": hallucination["message"],
        "trust_score": trust["trust_score"],
        "trust_level": trust["trust_level"]
    }