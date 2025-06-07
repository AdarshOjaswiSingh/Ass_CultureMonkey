import streamlit as st
import requests

st.title("Skill Trend Detector")

description = st.text_area("Paste job_description_text")

if st.button("Analyze"):
    if description:
        # Update this with your deployed API endpoint if needed
        api_url = "https://your-api-url/skill-trend"
        try:
            response = requests.post(api_url, json={"job_description_text": description})
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error("API Error: " + str(response.status_code))
        except Exception as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a description")
