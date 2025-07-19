import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)

# Your prompt
prompt = """
You are a senior recruiter. Analyze this resume and job description and give:
1. A match score out of 100
2. 3 strengths
3. 3 missing skills

Please format the output using markdown with headings, bullet points, and bold text for clarity.

Resume: Jane has experience in Python, ML, Tableau, and NLP using spaCy. She built churn models and dashboards.

Job Description: We need a data scientist with LLM, TensorFlow, and LangChain knowledge, and deployment experience using Streamlit.
"""

# Call the Chat Completions API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Print the response
print(response.choices[0].message.content)
