from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService


class CompareService:

    def __init__(self, vector_store: VectorStoreService):

        self.vector_store = vector_store
        self.llm = LLMService()

    def compare(self, job_description: str):

        documents = self.vector_store.similarity_search(
            job_description,
            k=5
        )

        resume = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = f"""
You are an expert technical recruiter.

Compare the following resume with the job description.

Resume:
{resume}

Job Description:
{job_description}

Generate the response in the following format:

1. ATS Match Percentage
2. Matching Skills
3. Missing Skills
4. Strengths
5. Weaknesses
6. Suggestions to improve the resume

Be professional and concise.
"""

        return self.llm.ask(prompt)