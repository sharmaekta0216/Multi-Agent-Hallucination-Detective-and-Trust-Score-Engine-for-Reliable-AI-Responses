from agents.workflow import run_workflow
from score.trust_score import TrustAgent
query = input("Enter your query: ")

result = run_workflow(query)

print("\n========== RESULT ==========\n")

print("Query:")
print(result["response"]["query"])

print("\nAI Response:")
print(result["response"]["response"])

print("\nFact Score:")
print(result["fact"]["fact_score"])

print("\nLogic Score:")
print(result["logic"]["logic_score"])

print("\nEvidence Score:")
print(result["evidence"]["evidence_score"])

print("\nHallucination Score:")
print(result["hallucination"]["hallucination_score"])

print("\nTrust Score:")
print(result["trust"]["trust_score"])

print("\nTrust Level:")
print(result["trust"]["trust_level"])