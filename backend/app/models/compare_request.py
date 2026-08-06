from pydantic import BaseModel


class CompareRequest(BaseModel):

    job_description: str