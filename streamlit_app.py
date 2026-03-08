import streamlit as st
import fitz

# ------------------ Functions ------------------

def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = " ".join(text.split())
    return text


def extract_skills(resume_text, skills_list):
    found_skills = []

    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    return score, matched
    missing_skills = set(job_skills) - set(resume_skills) 


# ------------------ UI ------------------

st.title("AI Resume Analyzer 💼")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here")

skills_list = [
    "python", "c++", "java", "machine learning",
    "data analysis", "sql", "html", "css",
    "javascript", "react", "django",
    "flask", "pandas", "numpy"
]

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    cleaned_resume = clean_text(resume_text).lower()
    job_description = job_description.lower()

    resume_skills = extract_skills(cleaned_resume, skills_list)
    job_skills = extract_skills(job_description, skills_list)

    score, matched = calculate_match(resume_skills, job_skills)

    st.subheader("Match Score")
    st.write(f"{round(score, 2)} %")

    st.subheader("Matching Skills")
    st.write(list(matched))

    st.subheader("Skills in Resume")
    st.write(resume_skills)

    st.subheader("Missing skills (Improve These!)")
    st.write(list(missing_skills))