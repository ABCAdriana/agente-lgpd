
import os
from pathlib import Path


# ==========================================================
# CONFIGURAÇÕES DO AGENTE LGPD
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

VECTORSTORE_DIR = BASE_DIR / "vectorstore"

CHROMA_DIR = BASE_DIR / "chroma_db"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_MODEL = "gemini-2.0-flash"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

COLLECTION_NAME = "lgpd_conhecimento"

DOCUMENT_NAME = "Lei13709_Lgpd(1).pdf"
