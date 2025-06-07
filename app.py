import streamlit as st
import spacy
import subprocess

# Load or download spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="Skill Trend Detector", layout="centered")
st.title("🧠 Skill Trend Detector")

description = st.text_area("📄 Paste Job Description Here")

if st.button("🔍 Analyze"):
    if not description.strip():
        st.warning("⚠️ Please enter a job description first.")
    else:
        # Extract potential skills from text
        doc = nlp(description)
        keywords = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "PERSON"]]

        if keywords:
            st.success("✅ Skills / Keywords Detected:")
            st.write(keywords)
        else:
            st.info("No relevant skills detected — try another description.")
