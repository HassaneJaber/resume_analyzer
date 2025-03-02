import re
import pdfminer.high_level
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF resume."""
    text = pdfminer.high_level.extract_text(pdf_path)

    if not text.strip():  # If extraction fails
        return "ERROR: Resume extraction failed or file is empty."

    print("DEBUG - Extracted Resume Text:", text[:500])  # Print first 500 chars
    return text

def extract_skills(text):
    """Basic keyword matching for extracting skills from resume text."""
    skills = {"Python", "Java", "SQL", "Machine Learning", "AI", "Flask", "Django", "React", "Angular", "TensorFlow"}
    words = re.findall(r'\b\w+\b', text)
    extracted_skills = {word for word in words if word in skills and word.lower() not in stop_words}
    return list(extracted_skills)
