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
# import os
# import time
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
# print("Loaded API Key:", api_key[:10] + "...")
# if not api_key:
#     raise Exception("GEMINI_API_KEY not found")

# client = genai.Client(api_key=api_key)

# MODEL_NAME = "gemini-3.6-flash"   # or another valid model

# def get_gemini_response(prompt, retries=3):
#     for attempt in range(retries):
#         try:
#             response = client.models.generate_content(
#                 model=MODEL_NAME,
#                 contents=prompt
#             )

#             if response and response.text:
#                 return response.text.strip()

#             raise Exception("Empty response")

#         except Exception as e:
#             error = str(e)

#             if ("429" in error or "503" in error) and attempt < retries - 1:
#                 time.sleep(5)
#                 continue

#             raise
# import time
# from google import genai
# from config import GEMINI_API_KEY


# client = genai.Client(api_key=GEMINI_API_KEY)

# MODEL_NAME = "gemini-3.5-flash"


# def get_gemini_response(prompt):

#     retries = 3

#     for attempt in range(retries):

#         try:
#             print(f"Gemini Attempt {attempt + 1}")

#             response = client.models.generate_content(
#                 model=MODEL_NAME,
#                 contents=prompt
#             )

#             return response.text


#         except Exception as e:
#             print("Gemini Error:", e)

#             if attempt < retries - 1:
#                 time.sleep(5)

#             else:
#                 return "Unable to generate AI response due to API connection issue."
import os
import time

# from dotenv import load_dotenv
# from groq import (
#     APIConnectionError,
#     APIStatusError,
#     OpenAI,
#     RateLimitError,
# )
# from dotenv import load_dotenv
# from groq import (
#     Groq,
#     APIConnectionError,
#     APIStatusError,
#     RateLimitError,
# )
# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# if not api_key:
#     raise Exception("GROQ_API_KEY not found")

# client = Groq(api_key=api_key)

# MODEL_NAME = model="llama-3.3-70b-versatile"


# def get_groq_response(prompt, retries=3):
#     for attempt in range(retries):
#         try:
#             print(f"Groq API attempt {attempt + 1}/{retries}")

#             response = client.responses.create(
#                 model=MODEL_NAME,
#                 input=prompt,
#             )

#             if response.output_text:
#                 return response.output_text.strip()

#             raise Exception("Empty response received from Groq")

#         except (RateLimitError, APIConnectionError, APIStatusError) as error:
#             print("Groq error:", error)

#             if attempt < retries - 1:
#                 wait_time = 5 * (attempt + 1)
#                 print(f"Temporary Groq error. Retrying after {wait_time} seconds...")
#                 time.sleep(wait_time)
#                 continue

#             return "Unable to generate an AI response due to a Groq API issue."

#         except Exception as error:
#             print("Groq error:", error)
#             return "Unable to generate an AI response currently."

#     return "Unable to generate an AI response."
import os
import time
from dotenv import load_dotenv
from groq import (
    Groq,
    APIConnectionError,
    APIStatusError,
    RateLimitError,
)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ_API_KEY not found")

client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.3-70b-versatile"


def get_groq_response(prompt, retries=3):
    for attempt in range(retries):
        try:
            print(f"Groq API attempt {attempt + 1}/{retries}")

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.2,
            )

            return response.choices[0].message.content.strip()

        except (RateLimitError, APIConnectionError, APIStatusError) as error:
            print("Groq error:", error)

            if attempt < retries - 1:
                wait_time = 5 * (attempt + 1)
                print(f"Retrying after {wait_time} seconds...")
                time.sleep(wait_time)
                continue

            return "Unable to generate an AI response due to a Groq API issue."

        except Exception as error:
            print("Groq error:", error)
            return "Unable to generate an AI response currently."

    return "Unable to generate an AI response."