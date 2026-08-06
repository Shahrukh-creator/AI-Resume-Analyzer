from fastapi import APIRouter

from app.models.compare_request import CompareRequest
from app.core.dependencies import compare_service


router = APIRouter(
    prefix="/api",
    tags=["Resume Comparison"]
)


@router.post("/compare")
async def compare_resume(request: CompareRequest):

    result = compare_service.compare(
        request.job_description
    )

    return {
        "comparison": result
    }