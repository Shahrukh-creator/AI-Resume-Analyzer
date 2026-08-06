from fastapi import APIRouter

from app.core.dependencies import summary_service


router = APIRouter(
    prefix="/api",
    tags=["Resume Summary"]
)


@router.get("/summary")
async def get_summary():

    result = summary_service.generate_summary()

    return {
        "summary": result
    }