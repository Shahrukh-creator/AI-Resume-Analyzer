from fastapi import APIRouter

from app.core.dependencies import ats_service


router = APIRouter(
    prefix="/api",
    tags=["ATS"]
)


@router.get("/ats")
async def ats_analysis():

    result = ats_service.analyze_resume()

    return {
        "analysis": result
    }