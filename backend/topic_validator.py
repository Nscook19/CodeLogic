import openai
import os
from dotenv import load_dotenv

# Set up OpenAI client
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def is_valid_topic(user_input):
    validation_prompt = f"""
You are an AI that classifies whether a user's question is related to coding/programming or math topics.
Examples of coding and math topics include:
- Python, C, C++, Java, JavaScript, etc.
- Variables, loops, functions, arrays
- Any question asking for code help or syntax help
- Any math problem or calculation

Question: "{user_input}"

Respond only with "yes" if this is related to coding or math (even if the code is broken or malformed). 
Respond "no" if this is about writing essays, general knowledge, relationships, or anything unrelated to coding or math.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": validation_prompt}]
        )
        result = response.choices[0].message.content.strip().lower()

        # Accept only strict yes
        return result == "yes"
    except Exception as e:
        # In case of API failure, assume invalid to be safe
        return False
