# Makes the API call to the LLM and extracts key points
import google.genai as genai
import os

def process_input(input_text):

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    

    with open("prompts/extract_notes.md", "r") as f:
        prompt = f.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"{prompt}\n\n{input_text}",
    )

    return response.text
