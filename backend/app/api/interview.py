from fastapi import APIRouter

from app.models.interview_request import InterviewRequest
from app.core.dependencies import interview_service


router = APIRouter(
    prefix="/api",
    tags=["Interview"]
)


@router.post("/interview")
async def generate_interview_questions(request: InterviewRequest):

    result = interview_service.generate_questions(
        request.job_description
    )

    return {
        "questions": result
    }