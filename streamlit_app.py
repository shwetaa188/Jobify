import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills, calculate_match, missing_skills
from data.skills import skills_list


st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here")



if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    cleaned_resume = clean_text(resume_text).lower()
    job_text = job_description.lower()

    resume_skills = extract_skills(cleaned_resume, skills_list)
    job_skills = extract_skills(job_text, skills_list)

    score, matched = calculate_match(resume_skills, job_skills)
    missing = missing_skills(job_skills, resume_skills)

    # --UI DISPLAY--

    st.subheader("Match Score")
    st.write(f"{round(score, 2)} %")

    st.subheader("Matching Skills")
    st.write(list(matched))

    st.subheader("Skills in Resume")
    st.write(resume_skills)

    st.subheader("Missing skills (Improve These!)")
    st.write(list(missing))