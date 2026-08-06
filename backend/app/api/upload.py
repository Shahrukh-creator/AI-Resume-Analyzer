from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.pdf_service import PDFService
from app.core.dependencies import (
    embedding_service,
    vector_service
)

router = APIRouter(
    prefix="/api",
    tags=["Resume"]
)

pdf_service = PDFService()



@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = pdf_service.load_pdf(file_path)

    chunks = embedding_service.split_documents(documents)

    vector_service.create_vector_store(chunks)

    return {
        "message": "Resume uploaded successfully."
    }