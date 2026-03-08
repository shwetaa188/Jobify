import fitz

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    doc.close() 
    return text

def clean_text(text):
    text = text.replace("\n", " ")   # remove new lines
    text = text.replace("\t", " ")   # remove tabs
    text = " ".join(text.split())    # remove extra spaces
    return text

skills_list = [
    "python",
    "c++",
    "java",
    "machine learning",
    "data analysis",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask",
    "pandas",
    "numpy"
]



resume_text = extract_text_from_pdf("MY_resume.pdf")
cleaned_resume = clean_text(resume_text)
cleaned_resume = cleaned_resume.lower()

print(cleaned_resume)

def extract_skills(resume_text, skills_list):
    found_skills = []
    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills

matched_skills = extract_skills(cleaned_resume, skills_list)
print("Skills found in resume: ")
print(matched_skills)

job_description = """
We are looking for a Python developer with knowledge of SQL, Machine Learning, 
Pandas, NumPy, html, css, javascript and Flask. Experience in Data Analysis is a plus.
"""
job_description = job_description.lower()
job_skills = extract_skills(job_description, skills_list)

def calculate_match(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    return score, matched
    missing_skills = set(job_skills) - set(resume_skills) 

score, matched_skills = calculate_match(matched_skills, job_skills)

print("Job Skills Required:", job_skills)
print("Matching Skills:", matched_skills)
print(f"Match Score: {round(score, 2)}%")


 
