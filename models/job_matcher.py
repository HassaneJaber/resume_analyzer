import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def match_job_description(resume_text, job_description):
    """Uses OpenAI GPT-4 to compare resume with job description and identify missing skills."""
    prompt = f"""
    I have extracted the following skills from a resume:
    {resume_text}

    The job description requires the following skills:
    {job_description}

    Compare the resume skills with the job description and provide a **structured list** of missing skills.
    Respond **only in this format**:
    - **Missing Skills:**
      1. Skill 1
      2. Skill 2
      3. Skill 3

    If all required skills are present, respond with:
    - **No missing skills.**
    """

    try:
        print("Sending request to OpenAI API...")

        client = openai.OpenAI()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that identifies missing skills in resumes."},
                {"role": "user", "content": prompt}
            ]
        )

        missing_skills = response.choices[0].message.content
        print("OpenAI Response:", missing_skills)
        return missing_skills

    except openai.OpenAIError as e:
        print("OpenAI API Error:", str(e))
        return f"OpenAI API Error: {str(e)}"
