
# **AI PDF Chatbot – Project Guide**

## **1️⃣ Project Overview**

This project is a web-based AI assistant that allows users to:

* Upload PDF documents.
* Extract text and store embeddings for semantic search.
* Ask natural language questions about the uploaded PDFs.
* Receive AI-generated answers using Ollama LLM.
* Maintain user sessions and chat history.

---

## **2️⃣ Prerequisites**

* **Python:** >= 3.11
* **Node.js:** >= 20
* **Docker:** optional, for containerized deployment
* **Git:** for version control

---

## **3️⃣ Project Structure**

```
chat-pdf-ai/
├── backend/               # FastAPI backend
├── frontend/              # React + Vite frontend
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── venv/                  # Python virtual environment (optional)
```

---

## **4️⃣ Setup Instructions**

### 4.1 Clone the Repository

```bash
git clone <repo-url> chat-pdf-ai
cd chat-pdf-ai
```

### 4.2 Backend Setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 4.3 Frontend Setup

```bash
cd ../frontend
npm install
npm run dev  # Start frontend in dev mode
```

### 4.4 Run Backend Locally

```bash
cd ../backend
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### 4.5 Optional – Run via Docker

```bash
docker-compose build
docker-compose up
```

* Backend → [http://localhost:8080](http://localhost:8080)
* Frontend → [http://localhost:5173](http://localhost:5173)

---

## **5️⃣ Usage Instructions**

### 5.1 Authentication

* Register a new user via frontend form.
* Login to access PDF uploads and chat.

### 5.2 PDF Upload

* Go to Dashboard → Upload PDF.
* Supported format: `.pdf`.
* PDF is parsed and text embeddings are stored.

### 5.3 Chat Interface

* Navigate to ChatPage.
* Ask questions related to uploaded PDFs.
* Responses are generated from PDF content + Ollama LLM.

### 5.4 Chat History

* Previous sessions are stored per user.
* Access via Dashboard → Session History.

---

## **6️⃣ Environment Variables (`.env`)**

```env
SECRET_KEY=your_jwt_secret
OLLAMA_API_KEY=your_ollama_key
DATABASE_URL=sqlite:///./database/app.db
```

---

## **7️⃣ Testing**

```bash
# Backend tests
cd backend
pytest

# Frontend tests (if added)
npm run test
```

---

## **8️⃣ Code Quality Recommendations**

### Backend Modules

| Module             | Recommendations                                                 |
| ------------------ | --------------------------------------------------------------- |
| `auth.py`          | JWT with expiration, secure hashing, validate inputs.           |
| `pdf_handler.py`   | Handle large PDFs in chunks, catch parsing errors.              |
| `vector_store.py`  | Modular embeddings, efficient FAISS index, separate functions.  |
| `chat_engine.py`   | Decouple embedding queries and LLM calls, handle empty results. |
| `ollama_client.py` | Centralize API calls, handle rate limits, validate responses.   |
| `memory.py`        | Per-user context, limit history, optional caching.              |
| `utils.py`         | Reusable helpers only, small single-purpose functions.          |
| `database/`        | SQLAlchemy ORM, migrations, context-managed sessions.           |

### Frontend Modules

| Module             | Recommendations                                                |
| ------------------ | -------------------------------------------------------------- |
| `AuthContext.jsx`  | Store JWT securely, modular login/logout logic.                |
| `ChatContext.jsx`  | Reactive chat state, avoid unnecessary re-renders.             |
| `FileUploader.jsx` | Validate file type/size, show upload progress.                 |
| `ChatWindow.jsx`   | Separate message rendering from logic, unique keys.            |
| `PDFViewer.jsx`    | Render uploaded PDFs only, handle errors gracefully.           |
| API Services       | Centralize requests, handle network errors, config via `.env`. |

### General Practices

* Follow **PEP8** for Python, consistent naming for frontend.
* Unit tests for all modules, including edge cases.
* Structured logging with `loguru`.
* Sanitize all user inputs.
* Modular and reusable code.
* Use async where possible for LLM and vector queries.

---
## **9 Troubleshooting**

| Issue                | Solution                                                |
| -------------------- | ------------------------------------------------------- |
| Backend not starting | Activate `.venv`, check Python version                  |
| Frontend not loading | Run `npm install`, check Vite port conflicts            |
| PDF parsing errors   | Ensure PDFs are not scanned/password-protected          |
| Docker issues        | Check `docker-compose.yml` ports, remove old containers |

---

## **10 Future Enhancements**

* OCR for scanned PDFs.
* Multi-format document support (Word, TXT).
* Real-time collaborative chat.
* Admin dashboard for user/document management.

---

✅ **End of PROJECT\_GUIDE.md**
