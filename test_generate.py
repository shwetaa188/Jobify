import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Say hello in one sentence.")
    print(response.text)

except Exception as e:
    print(type(e).__name__)
    print(e)