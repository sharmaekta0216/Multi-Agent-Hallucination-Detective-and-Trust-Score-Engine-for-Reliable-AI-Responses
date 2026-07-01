# Imports
print("Starting the Trust Score Engine...")
from database import get_connection
print("Database connection established.")
from validation import validate_query

from agent.fact_checker import fact_check
from agent.logic_checker import logic_check
from agent.source_verifier import source_verify
from agent.context_analyzer import context_check

from engine.trust_score import calculate_trust_score

# Connect to MySQL
conn = get_connection()
print("Database connection established.")
cursor = conn.cursor()
print("Cursor initialized.")

# Take input
question = input("Enter Question: ")
print("Question received:", question)

# Validate
valid, message = validate_query(question)

if not valid:
    print(message)
    conn.close()
    exit()

# Run agents
fact = fact_check(question)
logic = logic_check(question)
source = source_verify(question)
context = context_check(question)

# Calculate trust score
trust_score = calculate_trust_score(fact, logic, source, context)

# Print results
print("Fact Score:", fact)
print("Logic Score:", logic)
print("Source Score:", source)
print("Context Score:", context)
print("Trust Score:", trust_score)

# Close database connection
conn.close()