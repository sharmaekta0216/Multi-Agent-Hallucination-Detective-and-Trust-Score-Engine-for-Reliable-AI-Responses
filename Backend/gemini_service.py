# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")


# def get_gemini_response(prompt):
#     response = model.generate_content(prompt)
#     return response.text
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(prompt):

    try:

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text.strip()

        return """
        {
            "error":"Empty response from Gemini"
        }
        """

    except Exception as e:

        return f'''
        {{
            "error":"{str(e)}"
        }}
        '''