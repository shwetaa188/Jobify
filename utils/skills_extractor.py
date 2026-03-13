def extract_skills(resume_text, skills_list):
    found_skills = []
    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills

