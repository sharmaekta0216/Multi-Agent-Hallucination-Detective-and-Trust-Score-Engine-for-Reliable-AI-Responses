
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):
#         try:
#             ai_response = get_gemini_response(query)

#             return {
#                 "query": query,
#                 "response": ai_response
#             }

#         except Exception as e:
#             print("Error in generating response:", e)
#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):

#         prompt = f"""
# You are an expert AI assistant.

# Your task is to answer the user's question accurately, clearly, and professionally.

# Rules:
# 1. Give only factually correct information.
# 2. If you are unsure, clearly say that you are not certain.
# 3. Do not invent names, dates, statistics, or references.
# 4. Explain the answer in simple language.
# 5. Use bullet points whenever appropriate.
# 6. Keep the answer well-structured and easy to read.
# 7. If the question has multiple parts, answer each part separately.

# User Question:
# {query}

# Provide only the answer to the question.
# """

#         try:
#             ai_response = get_gemini_response(prompt)

#             return {
#                 "query": query,
#                 "response": ai_response
#             }

#         except Exception as e:
#             print("Error in generating response:", e)

#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):

#         prompt = f"""
# You are an expert AI assistant responsible for generating reliable answers.

# Answer the user's question accurately and provide enough information for fact checking.

# User Question:
# {query}

# Follow this exact format:

# Answer:
# (Provide the direct answer)

# Explanation:
# (Explain the answer briefly and clearly)

# Key Facts:
# - Fact 1
# - Fact 2
# - Fact 3

# Evidence:
# (Mention reliable sources, references, or explain why the information is trustworthy)

# Uncertainty:
# (If any part is uncertain, mention it. Otherwise write "No known uncertainty.")

# Rules:
# 1. Do not create fake information.
# 2. Do not guess unknown facts.
# 3. If information may change over time, mention that.
# 4. Keep facts separate from opinions.
# 5. Use simple professional language.
# """

#         try:
#             ai_response = get_gemini_response(prompt)

#             return {
#                 "query": query,
#                 "response": ai_response
#             }

#         except Exception as e:
#             print("Error in generating response:", e)

#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }


from services.gemini_service import get_gemini_response


class ResponseAgent:

    def __init__(self):
        print("Response Agent Initialized")

    def generate_response(self, query):

        prompt = f"""
You are an expert AI assistant.

Your goal is to generate a factually accurate, well-structured, and evidence-based answer.

User Question:
{query}

Follow this EXACT structure.

Answer:
(Give a direct answer.)

Explanation:
(Explain the answer in 2–5 concise paragraphs.)

Key Facts:
- Fact 1
- Fact 2
- Fact 3
- Fact 4 (if applicable)

Evidence:
- Mention official organizations, government websites, academic papers, or other reliable sources.
- If exact sources are unavailable, state that the answer is based on well-established public knowledge.

Limitations / Uncertainty:
- Mention any uncertainty, assumptions, or information that may change over time.
- If there is no uncertainty, write:
  "No known uncertainty."

Rules:
1. Never fabricate facts.
2. Never invent names, dates, statistics, quotations, or references.
3. If you are unsure, clearly say so.
4. Separate facts from opinions.
5. Use simple professional English.
6. Keep the answer concise but complete.
7. Do NOT use markdown tables.
8. Do NOT include unnecessary introductions or conclusions.
"""

        try:

            print("\n========== RESPONSE AGENT ==========")

            ai_response = get_gemini_response(prompt)

            print("AI Response Generated Successfully.")

            return {
                "query": query,
                "response": ai_response
            }

        except Exception as e:

            print("\nResponse Agent Error:")
            print(e)

            return {
                "query": query,
                "response": "Unable to generate response.",
                "error": str(e)
            }