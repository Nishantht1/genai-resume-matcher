# 🤖 GenAI Resume Matcher

This is a simple Generative AI-powered web app that compares a **resume** with a **job description** using GPT (gpt-3.5-turbo). It returns:

- ✅ A match score out of 100
- 💪 3 strengths from the resume
- 🔍 3 missing skills or gaps

---

## 🧠 How It Works

The app uses:
- [Streamlit](https://streamlit.io) \\\for the web interface
- [OpenAI GPT-3.5](https://platform.openai.com/docs) for natural language analysis
- `python-dotenv` for secure API key management

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/genai-resume-matcher.git
cd genai-resume-matcher
2. Create virtual environment & install packages
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Add your .env file
OPENAI_API_KEY=your-api-key-here
4. Run the app
streamlit run app.py
☁️ Deployed Version
👉 Live App on Streamlit Cloud

📄 Example Prompt
Analyze this resume and job description. Return:

Match score out of 100
3 strengths
3 missing skills


📌 Screenshot
(Add a screenshot of your working app here if you’d like)
