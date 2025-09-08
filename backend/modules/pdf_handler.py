import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    Handles multiple pages and returns combined text.
    """
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
    return text
