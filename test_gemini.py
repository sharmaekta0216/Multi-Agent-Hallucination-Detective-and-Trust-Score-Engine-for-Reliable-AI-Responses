
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Ask user for a prompt
prompt = input("Enter your question: ")

# Generate response
response = model.generate_content(prompt)

# Print response
print("\nGemini Response:\n")
print(response.text)