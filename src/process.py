# Makes the API call to the LLM and extracts key points
from google import genai
import os

def process_input(input_text):

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-3-flash-preview")

    with open("prompts/extract_notes.md", "r") as f:
        prompt = f.read()

    response = model.generate_content(f"{prompt}\n\n{input_text}")

    return response.text
