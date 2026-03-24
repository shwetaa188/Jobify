import streamlit as st
import plotly.graph_objects as go
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

    #Match score
    st.subheader("Match Score")
    st.metric(label = "Your Resume Match", value = f"{round(score,2)}%")
    st.progress(int(score))

    #skills- two colums
    col1, col2 = st.columns(2)

    #helper func to render colored badges
    def render_badges(skills, color):
        badges = " ".join([
            f"<span style = 'backgrounf-color:{color};color:white; padding:4px 10px; border-radius:12px; margin:3px; display:inline-block; font-weight:500'>{skill}</span>"
            for skill in skills
        ])
        st.markdown(badges, unsafe_allow_html = True)

    with col1:
        st.subheader("Matched skills")
        if matched:
            render_badges(matched, "#90EE90")    

    with col2:
        st.subheader("Missing skills")
        if missing:
            render_badges(missing, "#A81212")    
        else:
            st.write("You have all required skills")      

    #Resume skills summary at the bottom 
    st.divider()
    st.subheader("All skills found in your Resume")
    render_badges(resume_skills, "#ADD8E6")  

    st.subheader("📊 Skills Breakdown")

    fig = go.Figure(data=[go.Pie(
         labels=["Matched", "Missing"],
        values=[len(matched), len(missing)],
        hole=0.4,  # makes it a donut chart
        marker=dict(colors=["#90EE90", "#A81212"])  # green, red
    )])

    fig.update_layout(
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",  # transparent background
        font=dict(color="white")
    )

    st.plotly_chart(fig) 
    
     
          



