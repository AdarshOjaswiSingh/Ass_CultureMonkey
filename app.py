import streamlit as st
import spacy
import subprocess

# Try loading model, or download if not present
try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="Skill Trend Detector")
st.title("🧠 Skill Trend Detector")

description = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if description.strip():
        doc = nlp(description)
        keywords = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "PERSON"]]
        if keywords:
            st.success("Detected Skills/Keywords:")
            st.write(keywords)
        else:
            st.info("No keywords found.")
    else:
        st.warning("Please enter a description first.")
