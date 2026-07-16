# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")


# def get_gemini_response(prompt):
#     response = model.generate_content(prompt)
#     return response.text
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# # Configure Gemini API

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Load Gemini Model
# model = genai.GenerativeModel("gemini-2.5-flash")


# def get_gemini_response(prompt):

#     try:

#         response = model.generate_content(prompt)

#         if response and response.text:
#             return response.text.strip()

#         return """
#         {
#             "error":"Empty response from Gemini"
#         }
#         """

#     except Exception as e:

#         return f'''
#         {{
#             "error":"{str(e)}"
#         }}
#         '''
# import os
# import google as genai
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file.")

# genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-2.5-flash")


# def get_gemini_response(prompt):

#     try:

#         response = model.generate_content(prompt)

#         # Check for empty response
#         if response is None:
#             raise Exception("Gemini returned None.")

#         # Check text exists
#         if hasattr(response, "text") and response.text:
#             return response.text.strip()

#         # Sometimes Gemini returns candidates instead of text
#         if hasattr(response, "candidates") and response.candidates:

#             try:
#                 parts = response.candidates[0].content.parts

#                 text = "".join(
#                     part.text
#                     for part in parts
#                     if hasattr(part, "text")
#                 )

#                 if text.strip():
#                     return text.strip()

#             except Exception:
#                 pass

#         raise Exception("Empty response from Gemini.")

#     except Exception as e:

#         print("\n========== GEMINI ERROR ==========")
#         print(str(e))
#         print("==================================")

#         raise Exception(str(e))
# from google import genai

# print(genai.__file__)
# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found.")

# client = genai.Client(api_key=api_key)


# def get_gemini_response(prompt):
  
#     try:
#         print("Using latest google-genai SDK")
#         print("Model: gemini-2.5-flash")
#         response = client.models.generate_content(
#             model="gemini-3.5-flash",
#             contents=prompt
#         )

#         if response.text:
#             return response.text.strip()

#         raise Exception("Empty response from Gemini.")

#     except Exception as e:
#         print("Gemini Error:", e)
#         raise Exception(str(e))
# import os
# import time
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise Exception("GEMINI_API_KEY not found in .env")

# client = genai.Client(api_key=api_key)

# MODEL_NAME = "gemini-3.5-flash"


# def get_gemini_response(prompt, retries=3):

#     for attempt in range(retries):

#         try:

#             response = client.models.generate_content(
#                 model=MODEL_NAME,
#                 contents=prompt
#             )

#             if (
#                 response
#                 and hasattr(response, "text")
#                 and response.text
#             ):
#                 return response.text.strip()

#             raise Exception("Empty response from Gemini.")

#         except Exception as e:

#             error = str(e)

#             print("\n========== GEMINI ERROR ==========")
#             print(error)

#             if "429" in error and attempt < retries - 1:

#                 print("Retrying after quota wait...")

#                 time.sleep(5)

#                 continue

#             raise Exception(error)
# import time

# def get_gemini_response(prompt, retries=3):

#     for attempt in range(retries):

#         try:
#             response = client.models.generate_content(
#                 model=MODEL_NAME,
#                 contents=prompt
#             )

#             if response and hasattr(response, "text") and response.text:
#                 return response.text.strip()

#             raise Exception("Empty response from Gemini.")

#         except Exception as e:

#             error = str(e)

#             print("\n========== GEMINI ERROR ==========")
#             print(error)

#             # Retry for temporary server errors and rate limits
#             if ("429" in error or "503" in error) and attempt < retries - 1:

#                 wait_time = 5 * (attempt + 1)

#                 print(f"Retrying in {wait_time} seconds...")

#                 time.sleep(wait_time)

#                 continue

#             raise Exception(error)
import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", api_key[:10] + "...")
if not api_key:
    raise Exception("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-flash-latest"   # or another valid model

def get_gemini_response(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            if response and response.text:
                return response.text.strip()

            raise Exception("Empty response")

        except Exception as e:
            error = str(e)

            if ("429" in error or "503" in error) and attempt < retries - 1:
                time.sleep(5)
                continue

            raise