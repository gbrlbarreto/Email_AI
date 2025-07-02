import os
import PyPDF2

def extract_text_from_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.pdf':
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return ' '.join(page.extract_text() or '' for page in reader.pages)
    return ''