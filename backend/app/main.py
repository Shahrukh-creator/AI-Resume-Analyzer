from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.compare import router as compare_router

from app.api.upload import router as upload_router
from app.api.summary import router as summary_router
from app.api.ats import router as ats_router
from app.api.interview import router as interview_router

app = FastAPI(
    title="Resume Analyzer API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5400"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(ats_router)
app.include_router(compare_router)
app.include_router(interview_router)