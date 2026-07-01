<<<<<<< HEAD
'''from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello! Can you tell me who am I?")

print(response.text)'''

'''>>>>>>> 3c7123526f09f11f6d3de6ecac2e4c4b206f5716'''
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