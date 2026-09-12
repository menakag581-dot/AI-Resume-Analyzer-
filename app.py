import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("AI Resume Analyzer")
st.write("Upload your resume to analyze your skills and resume score.")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("📄 Resume Text")
    st.write(text)

    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    detected_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            detected_skills.append(skill)

    st.subheader("🧠 Skills Detected")

    if detected_skills:
        for skill in detected_skills:
            st.write("✅", skill)
    else:
        st.write("No skills detected.")

    score = len(detected_skills) * 5

    if score > 100:
        score = 100

    st.subheader("📊 Resume Score")

    st.progress(score / 100)

    st.write(f"Your resume score is {score}/100")

    st.subheader("💼 Suggested Job Role")

    if "Python" in detected_skills and "SQL" in detected_skills:
        st.success("Python / Data Analyst")

    elif "Java" in detected_skills and "SQL" in detected_skills:
        st.success("Java Developer")

    elif "Machine Learning" in detected_skills:
        st.success("Machine Learning Intern")

    else:
        st.info("Add more technical skills for better recommendations.")

    st.subheader("💡 Improvement Suggestions")

    important_skills = [
        "Python",
        "SQL",
        "Git",
        "Machine Learning"
    ]

    missing_skills = []

    for skill in important_skills:
        if skill.lower() not in text.lower():
            missing_skills.append(skill)

    if missing_skills:

        st.write("Consider adding:")

        for skill in missing_skills:
            st.write("🔹", skill)

    else:
        st.success("Your resume contains the important skills!")
