# Resume Analyzer

An AI-powered Resume Analyzer built using FastAPI, LangChain, embeddings, ChromaDB, OpenAI, and Angular.

The application allows users to upload a resume and perform AI-powered analysis.

# Features

Resume PDF upload
PDF text extraction
Resume document chunking
Embedding generation
Vector storage
Resume summary generation
ATS analysis
Job description comparison
Interview question generation
Architecture

                  Resume PDF
                      │
                      ▼
                Upload API
                      │
                      ▼
                PDF Service
                      │
                      ▼
              Document Chunks
                      │
                      ▼
              Embedding Service
                      │
                      ▼
                  ChromaDB
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
       Summary       ATS       Comparison
          │           │            │
          └───────────┼────────────┘
                      │
                      ▼
                     LLM
                      │
                      ▼
                AI Response

# Backend Structure

backend/
│
├── app/
│   ├── api/
│   │   ├── upload.py
│   │   ├── summary.py
│   │   ├── ats.py
│   │   ├── compare.py
│   │   └── interview.py
│   │
│   ├── core/
│   │   └── dependencies.py
│   │
│   ├── models/
│   │   ├── compare_request.py
│   │   └── interview_request.py
│   │
│   ├── prompts/
│   │   ├── ats_prompt.py
│   │   └── summary_prompt.py
│   │
│   └── services/
│       ├── pdf_service.py
│       ├── embedding_service.py
│       ├── vector_store_service.py
│       ├── retrieval_service.py
│       ├── llm_service.py
│       ├── summary_service.py
│       ├── ats_service.py
│       ├── compare_service.py
│       └── interview_service.py
│
├── uploads/
├── .env
└── requirements.txt


# API Endpoints

# Upload Resume
POST /api/upload

Uploads a resume PDF and creates its vector representation.

# Resume Summary
GET /api/summary

Generates an AI-powered summary of the uploaded resume.

# ATS Analysis
GET /api/ats

Analyzes the resume from an ATS/recruiter perspective.

# Job Description Comparison
POST /api/compare

Compares the uploaded resume against a supplied job description.

Example request:

{
  "job_description": "Looking for a Python developer with FastAPI, REST API and SQL experience."
}


# Interview Questions
POST /api/interview

Generates interview questions based on the resume and job description.
