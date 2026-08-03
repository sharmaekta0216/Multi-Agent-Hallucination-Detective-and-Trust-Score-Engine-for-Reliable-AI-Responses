
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


# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):

#         prompt = f"""
# You are an expert AI assistant.

# Your goal is to generate a factually accurate, well-structured, and evidence-based answer.

# User Question:
# {query}

# Follow this EXACT structure.

# Answer:
# (Give a direct answer.)

# Explanation:
# (Explain the answer in 2–5 concise paragraphs.)

# Key Facts:
# - Fact 1
# - Fact 2
# - Fact 3
# - Fact 4 (if applicable)

# Evidence:
# - Mention official organizations, government websites, academic papers, or other reliable sources.
# - If exact sources are unavailable, state that the answer is based on well-established public knowledge.

# Limitations / Uncertainty:
# - Mention any uncertainty, assumptions, or information that may change over time.
# - If there is no uncertainty, write:
#   "No known uncertainty."

# Rules:
# 1. Never fabricate facts.
# 2. Never invent names, dates, statistics, quotations, or references.
# 3. If you are unsure, clearly say so.
# 4. Separate facts from opinions.
# 5. Use simple professional English.
# 6. Keep the answer concise but complete.
# 7. Do NOT use markdown tables.
# 8. Do NOT include unnecessary introductions or conclusions.
# """

#         try:

#             print("\n========== RESPONSE AGENT ==========")

#             ai_response = get_gemini_response(prompt)

#             print("AI Response Generated Successfully.")

#             return {
#                 "query": query,
#                 "response": ai_response
#             }

#         except Exception as e:

#             print("\nResponse Agent Error:")
#             print(e)

#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }
# from backend.api import query
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):

#         print("Response Agent Initialized")

#     def generate_response(self, query):

# #         prompt = f"""
# # You are ChatGPT-level professional AI.

# # Answer the user's question naturally.

# # Requirements:

# # • Write like ChatGPT.
# # • Never output JSON.
# # • Never output code unless requested.
# # • Use headings.
# # • Use bullet points where useful.
# # • Explain in simple English.
# # • Include important facts.
# # • Mention uncertainty only if required.

# # Question:
# prompt = f"""
# Answer the question below.

# Question:
# {query}

# Instructions:
# - Write in Markdown.
# - Use headings (## or ###).
# - Use bullet points where appropriate.
# - Keep the answer neat and easy to read.
# - Do not return JSON.
# - Keep the answer concise and professional.
# """

# {query}
# """

#         try:

#             print("\n========== RESPONSE AGENT ==========")

#             answer = get_gemini_response(prompt)

#             return {

#                 "query": query,

#                 "response": answer

#             }

#         except Exception as e:

#             return {

#                 "query": query,

#                 "response": "Unable to generate response.",

#                 "error": str(e)

#             }
# from backend.api import query
# from services.gemini_service import get_gemini_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):

# #         prompt = f"""
# # You are a professional AI assistant.

# # Answer the following question in a clean and well-formatted Markdown style.

# # Question:
# # {query}

# # Instructions:
# # - Give a direct answer first.
# # - Use Markdown headings (## and ###).
# # - Use bullet points where appropriate.
# # - Highlight important terms using **bold**.
# # - Keep the answer easy to understand.
# # - Keep paragraphs short.
# # - Do NOT return JSON.
# # - Do NOT mention these instructions.
# # - If the answer contains facts, explain them briefly.
# # """
# prompt = f"""
# You are a professional AI assistant.

# Answer the user's question in plain English.

# Rules:
# - Do NOT use Markdown.
# - Do NOT use ## or ### headings.
# - Do NOT use ** or * characters.
# - Do NOT use --- separators.
# - Write naturally like ChatGPT.
# - Use short paragraphs.
# - Use numbered lists only when necessary.
# - Keep the answer easy to read.
# - Be concise but complete.
# - Return only the answer.

# Question:
# {query}
# """

# try:

#             print("\n========== RESPONSE AGENT ==========")

#             answer = get_gemini_response(prompt)

#             return {
#                 "query": query,
#                 "response": answer
#             }

#         except Exception as e:

#             return {
#                 "query": query,
#                 "response": "Unable to generate response.",
#                 "error": str(e)
#             }
# from services.groq_service import get_groq_response


# class ResponseAgent:

#     def __init__(self):
#         print("Response Agent Initialized")

#     def generate_response(self, query):

#         prompt = f"""
# "You are an expert AI assistant specializing in factual accuracy, logical reasoning, and trustworthy responses.

# Answer the user's question naturally.

# Requirements:

# - Give the direct answer first.
# - If the question contains a false assumption or misleading statement, clearly identify and correct it before answering.
# - Write in plain English.
# - Do NOT use Markdown.
# - Do NOT use #, ##, ### headings.
# - Do NOT use **, *, or --- symbols.
# - Use short paragraphs.
# - Use numbered lists only if they improve readability.
# - Explain important facts briefly.
# - Provide 2 to 4 additional relevant facts whenever they help the user understand the topic better.
# - If the question is about a city, state, country, person, organization, or historical event, include relevant context such as:
#   • Administrative hierarchy
#   • Current office holders (when relevant)
#   • Geographic location
#   • Historical significance
#   • Important landmarks or achievements
# - Never fabricate facts, names, dates, or statistics.
# - If you are uncertain about any information, clearly state that instead of guessing.
# - Keep the answer professional, user-friendly, and easy to understand.
# - Do NOT return JSON.
# - Do NOT include code unless requested.
# - Return only the final answer.

# Question:
# {query}

#         try:

#             print("\n========== RESPONSE AGENT ==========")
#             print(prompt)

#             answer = get_groq_response(prompt)

#             return {
#                 "query": query,
#                 "response": answer
#             }

#         except Exception as e:

#             print("\n========== RESPONSE AGENT ERROR ==========")
#             print(str(e))

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
You are an expert AI assistant specializing in factual accuracy, logical reasoning, and trustworthy responses.

Answer the user's question naturally.

Requirements:

- Give the direct answer first.
- If the question contains a false assumption or misleading statement, clearly identify and correct it before answering.
- Write in plain English.
- Do NOT use Markdown.
- Do NOT use #, ##, ### headings.
- Do NOT use **, *, or --- symbols.
- Use short paragraphs.
- Use numbered lists only if they improve readability.
- Explain important facts briefly.
- Provide 2 to 4 additional relevant facts whenever they help the user understand the topic better.
- If the question is about a city, state, country, person, organization, or historical event, include relevant context such as:
  - Administrative hierarchy
  - Current office holders (when relevant)
  - Geographic location
  - Historical significance
  - Important landmarks or achievements
- If the question contains incorrect information, politely correct it before answering.
- Include relevant current facts whenever appropriate.
- Never fabricate facts, names, dates, statistics, or references.
- If you are uncertain about any information, clearly state that instead of guessing.
- Keep the answer professional, user-friendly, and easy to understand.
- Do NOT return JSON.
- Do NOT include code unless requested.
- Return only the final answer.

Question:
{query}
"""

        try:

            print("\n========== RESPONSE AGENT ==========")
            print(prompt)

            answer = get_gemini_response(prompt)

            return {
                "query": query,
                "response": answer
            }

        except Exception as e:

            print("\n========== RESPONSE AGENT ERROR ==========")
            print(str(e))

            return {
                "query": query,
                "response": "Unable to generate response.",
                "error": str(e)
            }