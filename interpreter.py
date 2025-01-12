import os
from openai import OpenAI
from dotenv import load_dotenv
from main import getFileContent

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
example_code = getFileContent("example_code.txt")
lang_rules = getFileContent("lang_rules.txt")

def interpret(code):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
                "content":
                    f"You are the interpreter of language VintLang. EXAMPLE_CODE: {example_code},LANGAUGE_RULES: {lang_rules}"},
            {
                "role": "user",
                "content": f"ONLY RETURN THE OUTPUT NOTHING ELSE ALSO USE THE GENERALY PROVIDED EXAMPLE CODEAS A REFERENCE AND YOU GENERALLY PROGRAMMIN KNOWLEGE TO INTERPRET THIS. CODE: {code}"
            }
        ]
    )
    return completion.choices[0].message

