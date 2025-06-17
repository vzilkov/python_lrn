import ollama
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def ask_ollama(prompt, model="llama3", context=None):
    """Query Ollama with a prompt"""
    response = ollama.chat(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'context': context if context else None
            }
        ]
    )
    return response['message']['content']

def process_pdf_with_ollama(pdf_path, questions):
    # Step 1: Extract text from PDF
    print(f"Extracting text from {pdf_path}...")
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Process with Ollama
    print("Processing with Ollama...")
    results = {}
    
    for question in questions:
        # Combine question with PDF text as context
        prompt = f"Ты отвечаешь на русском языке. {question}\n\nКонтекст из PDF:\n{pdf_text[:3000]}"  # Limiting context size
        
        # Get response from Ollama
        response = ask_ollama(prompt)
        results[question] = response
    
    return results

if __name__ == "__main__":
    # Example usage
    pdf_file = "Nissan_Ariya.pdf"  # Replace with your PDF file path
    questions = [
        "Какой тип двигателя используется?",
        "Как называется машина?",
        "На сколько километров хватает заряда?"
    ]
    
    results = process_pdf_with_ollama(pdf_file, questions)
    
    print("\nResults:")
    for question, answer in results.items():
        print(f"\nQ: {question}")
        print(f"A: {answer}\n")