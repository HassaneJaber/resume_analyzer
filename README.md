# 🚀 AI Resume Analyzer

## 📌 About the Project
The **AI Resume Analyzer** helps job seekers evaluate their resumes against job descriptions. It extracts key skills from a resume and compares them with the required skills in a job posting, identifying **missing competencies**.

## 🎯 Key Features
✅ **Upload Resumes** (PDF format)  
✅ **Extracts Skills** from resume text  
✅ **Compares Resume with Job Description**  
✅ **Identifies Missing Skills** for the job  
✅ **Real-time AI Analysis** using OpenAI GPT-4  

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI Processing:** OpenAI API (GPT-4)
- **Data Handling:** PDF Parsing with `pdfminer`
- **Storage:** MySQL (optional for future enhancements)



## 🚀 Installation Guide
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/HassaneJaber/resume_analyzer.git
cd resume_analyzer

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file in the root directory:


touch .env
Inside .env, add your OpenAI API key:


OPENAI_API_KEY=your-api-key-here
5️⃣ Run the Application

python app.py
Visit http://127.0.0.1:5000 in your browser.

🏗️ File Structure

resume_analyzer/
│── models/
│   ├── job_matcher.py
│   ├── resume_parser.py
│── static/
│── templates/
│── uploads/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
🌟 Future Enhancements
✅ Improve UI with TailwindCSS/Bootstrap
✅ Add Authentication for user-based resume storage
✅ Support More File Types (DOCX, TXT)
📜 License
This project is open-source and available under the MIT License.
