# import google.generativeai as genai

# from dotenv import load_dotenv
# import os

# # Load .env file
# load_dotenv()

# # Get API key
# api_key = os.getenv("GEMINI_API_KEY")

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Load Gemini model
# model = genai.GenerativeModel("gemini-3.5-flash")

# # Ask user for a prompt
# prompt = input("Enter your question: ")

# # Generate response
# response = model.generate_content(prompt)

# # Print response
# print("\nGemini Response:\n")
# print(response.text)
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model= "gemini-flash-latest",
    contents="Who is the President of India?"
)

print(response.text)