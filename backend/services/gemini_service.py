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
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(prompt):

    try:

        response = model.generate_content(prompt)

        # Check for empty response
        if response is None:
            raise Exception("Gemini returned None.")

        # Check text exists
        if hasattr(response, "text") and response.text:
            return response.text.strip()

        # Sometimes Gemini returns candidates instead of text
        if hasattr(response, "candidates") and response.candidates:

            try:
                parts = response.candidates[0].content.parts

                text = "".join(
                    part.text
                    for part in parts
                    if hasattr(part, "text")
                )

                if text.strip():
                    return text.strip()

            except Exception:
                pass

        raise Exception("Empty response from Gemini.")

    except Exception as e:

        print("\n========== GEMINI ERROR ==========")
        print(str(e))
        print("==================================")

        raise Exception(str(e))