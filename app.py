
import streamlit as st

st.set_page_config(
    page_title="ScamShield",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamShield")
st.subheader("AI-Based Job Scam Detection")

st.write(
    "Analyze job and internship advertisements "
    "for potential warning signs."
)

job_text = st.text_area(
    "Paste the job advertisement here:",
    height=200,
    placeholder="Paste the complete job advertisement..."
)

if st.button("Analyze Advertisement"):
    if job_text.strip():
        st.info(
            "Your advertisement has been received. "
            "The machine learning model will be "
            "integrated in the next development stage."
        )
    else:
        st.warning("Please enter a job advertisement.")
