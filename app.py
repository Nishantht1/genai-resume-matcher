import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

# Set Streamlit page config
st.set_page_config(page_title="GenAI Resume Matcher", layout="wide")
st.title("🤖 GenAI Resume vs Job Description Matcher")
st.markdown("Compare a resume and job description using GPT and get a match score, strengths, and missing skills.")

st.markdown("---")

# Layout: two side-by-side columns
col1, col2 = st.columns(2)

with col1:
    resume = st.text_area("📄 Paste Resume", height=250, placeholder="Paste resume text here...")

with col2:
    jd = st.text_area("📝 Paste Job Description", height=250, placeholder="Paste job description here...")

# Submit button
if st.button("🔍 Analyze Match"):
    if resume and jd:
        with st.spinner("Analyzing with GPT..."):
            prompt = f"""
You are a senior recruiter. Analyze this resume and job description and give:
1. A match score out of 100
2. 3 strengths based on the resume
3. 3 missing skills or gaps

Resume:
{resume}

Job Description:
{jd}

Format the output using markdown with bold text and bullet points.
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
                st.markdown("### ✅ Match Analysis Result")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
    else:
        st.warning("⚠️ Please paste both Resume and Job Description.")
