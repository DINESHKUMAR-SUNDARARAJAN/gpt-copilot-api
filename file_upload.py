import os
import uuid
from fastapi import UploadFile, File, APIRouter
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import pickle

router = APIRouter()

UPLOAD_DIR = "uploads"
DB_DIR = "db"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

@router.post("/upload/{user_id}")
async def upload_pdf(user_id: str, file: UploadFile = File(...)):
    user_dir = os.path.join(UPLOAD_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)
    file_path = os.path.join(user_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Load & chunk
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)

    # Save to disk
    persist_path = os.path.join(DB_DIR, user_id)
    os.makedirs(persist_path, exist_ok=True)
    vectordb.save_local(persist_path)

    print(f"✅ Saved {len(chunks)} chunks to {persist_path}")
    return {"status": "uploaded and indexed", "chunks": len(chunks)}
