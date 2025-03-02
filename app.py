from flask import Flask, request, jsonify, render_template
import os
from models.resume_parser import extract_text_from_pdf, extract_skills
from models.job_matcher import match_job_description

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["resume"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    resume_text = extract_text_from_pdf(file_path)
    skills = extract_skills(resume_text)

    return jsonify({"resume_text": resume_text, "skills": skills})

@app.route("/match", methods=["POST"])
def match_job():
    try:
        data = request.json
        resume_text = data.get("resume_text")
        job_description = data.get("job_description")

        print("DEBUG - Extracted Resume Skills:", resume_text)
        print("DEBUG - Job Description:", job_description)

        if not resume_text or not job_description:
            return jsonify({"error": "Missing data"}), 400

        missing_skills = match_job_description(resume_text, job_description)

        print("DEBUG - AI Missing Skills Response:", missing_skills)
        return jsonify({"missing_skills": missing_skills})

    except Exception as e:
        print("Error in /match:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
