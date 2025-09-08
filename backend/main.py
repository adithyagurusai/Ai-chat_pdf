from fastapi import FastAPI
from modules.auth import router as auth_router
from modules.pdf_handler import extract_text_from_pdf
app = FastAPI()
app.include_router(auth_router, prefix="/auth")
if __name__ == "__main__":
    sample_text = extract_text_from_pdf("/Users/kothavamsi/Git/chat-pdf-ai/sample.pdf")
    print(sample_text)
