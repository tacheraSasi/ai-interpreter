import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def interpret(code: str, example_code: str, lang_rules: str) -> str:
    """
    Interprets a given code using the specified example and language rules
    and returns only the output of the code.

    Args:
        code (str): The code to be interpreted.
        example_code (str): An example code to guide the interpretation.
        lang_rules (str): Language-specific rules to assist with interpretation.

    Returns:
        str: The output of the code interpretation.
    """
    # Prepare the prompt for the AI
    prompt = f"""
    You are the interpreter for the VintLang programming language.
    You have been given an example code: {example_code}
    You also have the following language rules: {lang_rules}

    Your task is to execute the following code:
    CODE: {code}

    Only return the output of the code execution. Do not provide any extra text or explanation.
    """

    # Make the API call to OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Use the appropriate GPT model
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": "Execute the code and return only the output."
            }
        ]
    )

    # Extract and return the output message
    output_message = completion.choices[0].message['content'].strip()
    return output_message
