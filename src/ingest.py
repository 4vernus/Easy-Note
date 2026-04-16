from bs4 import BeautifulSoup
from docx import Document
from pathlib import Path
import pdfplumber

# Validate user input
def accept_txt(input_txt_path):
    with open(input_txt_path, "r", encoding="utf-8") as f:
        return f.read()
      


def accept_docx(input_docx_path):
    with open(input_docx_path, "rb", encoding="utf-8") as f:
        document = Document(f)
        text = "\n".join([paragraph.text for paragraph in document.paragraphs])
        return text


def accept_pdf(input_pdf_path):
    with pdfplumber.open(input_pdf_path, encoding="utf-8") as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text


def accept_html(input_html_path):
    with open(input_html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        text = soup.get_text()
        return text


def read_file(input_file):
    input_file_path = Path(input_file)
    
    if not input_file_path.is_file():
        raise FileNotFoundError(f"File not found: {input_file}")
    
    readers = {".txt": accept_txt,
              ".md": accept_txt,
              ".docx": accept_docx,
              ".pdf": accept_pdf,
              ".html": accept_html,
              ".htm": accept_html}

    extension = input_file_path.suffix.lower()
    reader = readers.get(extension)

    if reader is None:
        raise ValueError(f"Invalid file type: {extension}")
    
    return reader(input_file_path)