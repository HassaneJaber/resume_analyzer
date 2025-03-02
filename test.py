import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def test_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "List 5 trending tech skills"}]
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print("OpenAI API Error:", str(e))

test_openai()
