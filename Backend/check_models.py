# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for model in client.models.list():
#     print(model.name)
from services.gemini_service import GeminiService
from dotenv import load_dotenv
import os

load_dotenv()

client = GeminiService(api_key=os.getenv("GEMINI_API_KEY"))

response = client.chat.completions.create(
    model="qwen/qwen3.6-27b",  # or another available model
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)