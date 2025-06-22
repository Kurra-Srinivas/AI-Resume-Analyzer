import PyPDF2

def extract_resume_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from docx import Document
from PyPDF2 import PdfReader
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def evaluate_resume(file, tone="General", language="English"):
    if file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        resume_text = extract_text_from_docx(file)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX."

    prompt = f"""
You are an expert resume evaluator.

Please assess the following resume for quality, relevance, clarity, and professionalism.

Tone to consider: {tone}
Language of output: {language}

Resume Content:
\"\"\"
{resume_text}
\"\"\"

Instructions:
- Provide a detailed evaluation in 5-7 sentences
- Highlight strengths and weaknesses
- Suggest improvements (e.g., formatting, keywords, structure)
- Conclude with a rating out of 10
    """

    response = llm.invoke(prompt)
    return response.content.strip()
