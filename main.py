from agent.fact_checker import fact_check
from agent.logic_checker import logic_check
from agent.source_verifier import source_verify
from agent.context_analyzer import context_check

from engine.trust_score import calculate_trust_score

question = input("Enter Question: ")

fact = fact_check(question)
logic = logic_check(question)
source = source_verify(question)
context = context_check(question)

trust_score = calculate_trust_score(
    fact, logic, source, context
)

print("Fact Score:", fact)
print("Logic Score:", logic)
print("Source Score:", source)
print("Context Score:", context)
print("Trust Score:", trust_score)