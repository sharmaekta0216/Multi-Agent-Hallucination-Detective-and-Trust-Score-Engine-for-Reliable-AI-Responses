from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

question = input("Enter your question: ")

response = model.generate_content(question)

print("\nGemini Response:")
print(response.text)