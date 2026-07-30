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
# from agents.response_agent import ResponseAgent
# from agents.fact_checker import FactAgent
# from agents.logic_checker import LogicAgent
# from agents.evidence_agent import EvidenceAgent
# from agents.hallucination_agent import HallucinationAgent
# from score.trust_score import TrustAgent
# from agents.analysis_agent import AnalysisAgent
# from services.database_service import (
#     save_query,
#     save_response,
#     save_trust_score,
#     save_evidence,
#     save_hallucination_analysis
# )


# def run_workflow(user_id, query):

#     print("1. Workflow Started")

#     response_agent = ResponseAgent()
#     fact_checker = FactAgent()
#     logic_checker = LogicAgent()
#     evidence_agent = EvidenceAgent()
#     hallucination_agent = HallucinationAgent()
#     trust_agent = TrustAgent()

#     print("2. Calling Gemini...")
#     response = response_agent.generate_response(query)
#     print("3. Gemini Response:", response)

#     ai_response = response["response"]
#     print("After gemini")
#     print("before save query")
#     query_id = save_query(
#         user_id=user_id,
#         query_text=query
        
#     )
#     print("after save query")

#     fact = fact_checker.check_fact(ai_response)
#     print("after fact checker")
#     logic = logic_checker.check_logic(ai_response)
#     print("after logic checker")
#     evidence = evidence_agent.check_evidence(ai_response)
#     print("after evidence checker")
#     hallucination = hallucination_agent.detect_hallucination(ai_response)
#     print("after hallucination checker")

#     trust = trust_agent.calculate_score (
        
#         fact["fact_score"],
#           logic["logic_score"],
#         evidence["evidence_score"],
#         hallucination["hallucination_score"]
#     )
#     print("after trust score calculation")

#     response_id = save_response(
#         query_id=query_id,
#         response_text=ai_response,
#         model_name="Gemini 2.5 Flash",
#         response_time_ms=None
#     )
#     save_evidence(
#     response_id=response_id,
#     source_title="Evidence Source",
#     source_url="N/A",
#     evidence_text=evidence["message"]
#     )
#     save_hallucination_analysis(
#     response_id=response_id,
#     hallucination_score=hallucination["hallucination_score"],
#     unsupported_claims=0,
#     contradiction_count=0,
#     remarks=hallucination["message"]
#     )

#     save_trust_score(
#         response_id=response_id,
#         fact_score=fact["fact_score"],
#         logic_score=logic["logic_score"],
#         evidence_score=evidence["evidence_score"],
#         hallucination_score=hallucination["hallucination_score"],
#         final_trust_score=trust["trust_score"],
#         trust_level=trust["trust_level"]
#     )

#     print("4. Workflow Complete")

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
# from agents.response_agent import ResponseAgent
# from agents.analysis_agent import AnalysisAgent
# from score.trust_score import TrustAgent
# from agents.adversarial_agent import AdversarialAgent
# from agents.judge_agent import JudgeAgent

# from services.database_service import (
#     save_query,
#     save_response,
#     save_trust_score,
#     save_evidence,
#     save_hallucination_analysis
# )


# def run_workflow(user_id, query):

#     print("========== WORKFLOW STARTED ==========")

#     response_agent = ResponseAgent()
#     analysis_agent = AnalysisAgent()
#     trust_agent = TrustAgent()
#     adversarial_agent = AdversarialAgent()
#     judge_agent = JudgeAgent()

#     print("Generating AI Response...")

#     response = response_agent.generate_response(query)

#     ai_response = response["response"]
#     if "error" in response:
#      print("Response Agent Error:", response["error"]) 

#     print("AI Response Generated")

#     query_id = save_query(
#         user_id=user_id,
#         query_text=query
#     )

#     print("Query Saved")

#     analysis = analysis_agent.analyze(ai_response)

#     print("Analysis Completed")

#     trust = trust_agent.calculate_score(

#         analysis["fact_score"],
#         analysis["logic_score"],
#         analysis["evidence_score"],
#         analysis["hallucination_score"]

#     )

#     print("Trust Score Calculated")

#     response_id = save_response(

#         query_id=query_id,
#         response_text=ai_response,
#         model_name="Gemini 3.5 Flash",
#         response_time_ms=None

#     )

#     save_evidence(

#         response_id=response_id,
#         source_title="Evidence Analysis",
#         source_url="N/A",
#         evidence_text=analysis["evidence_message"]

#     )

#     save_hallucination_analysis(

#         response_id=response_id,
#         hallucination_score=analysis["hallucination_score"],
#         unsupported_claims=0,
#         contradiction_count=0,
#         remarks=analysis["hallucination_message"]

#     )

#     save_trust_score(

#         response_id=response_id,

#         fact_score=analysis["fact_score"],

#         logic_score=analysis["logic_score"],

#         evidence_score=analysis["evidence_score"],

#         hallucination_score=analysis["hallucination_score"],

#         final_trust_score=trust["trust_score"],

#         trust_level=trust["trust_level"]

#     )

#     print("========== WORKFLOW COMPLETE ==========")

#     return {

#         "success": True,

#         "question": query,

#         "ai_response": ai_response,

#         "fact_score": analysis["fact_score"],
#         "fact_message": analysis["fact_message"],

#         "logic_score": analysis["logic_score"],
#         "logic_message": analysis["logic_message"],

#         "evidence_score": analysis["evidence_score"],
#         "evidence_message": analysis["evidence_message"],

#         "hallucination_score": analysis["hallucination_score"],
#         "hallucination_message": analysis["hallucination_message"],

#         "trust_score": trust["trust_score"],

#         "trust_level": trust["trust_level"]

#     }
from agents.response_agent import ResponseAgent
from agents.analysis_agent import AnalysisAgent
from agents.adversarial_agent import AdversarialAgent
from agents.judge_agent import JudgeAgent

from score.trust_score import TrustAgent

from services.database_service import (
    save_query,
    save_response,
    save_trust_score,
    save_evidence,
    save_hallucination_analysis
)


def run_workflow(user_id, query):

    print("========== WORKFLOW STARTED ==========")


    # Initialize Agents

    response_agent = ResponseAgent()
    analysis_agent = AnalysisAgent()
    adversarial_agent = AdversarialAgent()
    judge_agent = JudgeAgent()
    trust_agent = TrustAgent()


    # -------------------------------
    # 1. Generate AI Response
    # -------------------------------

    print("Generating AI Response...")

    response = response_agent.generate_response(query)

    ai_response = response["response"]

    if "error" in response:
        print("Response Agent Error:", response["error"])


    print("AI Response Generated")


    # -------------------------------
    # 2. Save Query
    # -------------------------------

    query_id = save_query(
        user_id=user_id,
        query_text=query
    )

    print("Query Saved")


    # -------------------------------
    # 3. Analysis Agent
    # Fact + Logic + Evidence + Hallucination
    # -------------------------------

    analysis = analysis_agent.analyze(ai_response)


    print("Analysis Completed")


    # -------------------------------
    # 4. Adversarial Agent
    # -------------------------------

    adversarial = adversarial_agent.analyze(
        query,
        ai_response
    )


    print("Adversarial Analysis Completed")


    # -------------------------------
    # 5. Judge Agent
    # -------------------------------

    judge = judge_agent.evaluate(
        query,
        ai_response,
        analysis,
        adversarial
    )


    print("Judge Decision Completed")


    # -------------------------------
    # 6. Trust Score
    # -------------------------------

    trust = trust_agent.calculate_score(

        analysis["fact_score"],

        analysis["logic_score"],

        analysis["evidence_score"],

        analysis["hallucination_score"],

        adversarial["adversarial_score"]

    )


    print("Trust Score Calculated")



    # -------------------------------
    # 7. Save Response
    # -------------------------------

    response_id = save_response(

        query_id=query_id,

        response_text=ai_response,

        model_name="gpt-5.5",

        response_time_ms=None

    )


    # -------------------------------
    # 8. Save Evidence
    # -------------------------------

    save_evidence(

        response_id=response_id,

        source_title="Evidence Analysis",

        source_url="N/A",

        evidence_text=analysis["evidence_message"]

    )



    # -------------------------------
    # 9. Save Hallucination Result
    # -------------------------------

    save_hallucination_analysis(

        response_id=response_id,

        hallucination_score=
        analysis["hallucination_score"],

        unsupported_claims=0,

        contradiction_count=0,

        remarks=
        analysis["hallucination_message"]

    )



    # -------------------------------
    # 10. Save Trust Score
    # -------------------------------

    save_trust_score(

        response_id=response_id,

        fact_score=
        analysis["fact_score"],

        logic_score=
        analysis["logic_score"],

        evidence_score=
        analysis["evidence_score"],

        hallucination_score=
        analysis["hallucination_score"],

        final_trust_score=
        trust["trust_score"],

        trust_level=
        trust["trust_level"]

    )


    print("========== WORKFLOW COMPLETE ==========")



    # Final API Response

    return {

        "success": True,

        "question": query,


        "ai_response": ai_response,


        # Analysis Scores

        "fact_score":
        analysis["fact_score"],

        "fact_message":
        analysis["fact_message"],



        "logic_score":
        analysis["logic_score"],

        "logic_message":
        analysis["logic_message"],



        "evidence_score":
        analysis["evidence_score"],

        "evidence_message":
        analysis["evidence_message"],



        "hallucination_score":
        analysis["hallucination_score"],

        "hallucination_message":
        analysis["hallucination_message"],



        # New Features ⭐

        "adversarial_score":
        adversarial["adversarial_score"],

        "adversarial_issues":
        adversarial["issues"],



        "judge_decision":
        judge["judge_decision"],

        "explanation":
        judge["explanation"],

        "recommendation":
        judge["recommendation"],



        # Final Trust

        "trust_score":
        trust["trust_score"],

        "trust_level":
        trust["trust_level"]

    }