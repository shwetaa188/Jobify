import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def get_ai_advice(matched_skills, missing_skills, job_skills):
    prompt = f"""
    A candidate has applied for a job. Here is their skill analysis:

    Matched Skills: {list(matched_skills)}
    Missing Skills: {list(missing_skills)}
    Job Required Skills: {list(job_skills)}

    Please give:
    1. A brief overall assessment (2-3 lines)
    2. For each missing skill, one specific action they can take to learn it
    3. An encouraging closing line

    Keep it concise and practical.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        # check what type of error it is
        error_message = str(e)

        if "429" in error_message or "quota" in error_message.lower():
            return "Sorry!:( AI advice unavailable right now due to API quota limits. Your analysis above is still accurate!"
        elif "404" in error_message:
            return ":( AI model not found. Please check the model name in ai_advisor.py"
        else:
            return f":( AI advice temporarily unavailable. Error: {error_message[:100]}"