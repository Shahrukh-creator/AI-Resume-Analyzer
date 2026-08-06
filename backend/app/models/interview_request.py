from pydantic import BaseModel


class InterviewRequest(BaseModel):

    job_description: str | None = None