# 🤖 GenAI Resume Matcher
![Powered by OpenAI](https://img.shields.io/badge/Powered%20By-OpenAI-10a37f?logo=openai&logoColor=white)

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
<img width="2532" height="1083" alt="image" src="https://github.com/user-attachments/assets/9d4660f8-ce20-491c-a6a4-8ef193173b70" />
<img width="2380" height="1046" alt="image" src="https://github.com/user-attachments/assets/2cfefa1d-68ff-412a-bb21-5525d74b167b" />

