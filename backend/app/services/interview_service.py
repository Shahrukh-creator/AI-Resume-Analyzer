from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService


class InterviewService:

    def __init__(self, vector_store: VectorStoreService):

        self.vector_store = vector_store

        self.llm = LLMService().get_llm()

    def generate_questions(self, job_description: str | None = None):

        # Retrieve relevant resume chunks
        query = job_description if job_description else "Resume"

        documents = self.vector_store.similarity_search(
            query,
            k=5
        )

        resume = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = f"""
You are an experienced technical interviewer.

Below is a candidate's resume.

Resume:
{resume}
"""

        if job_description:

            prompt += f"""

Target Job Description:
{job_description}
"""

        prompt += """

Generate professional interview questions.

Organize the response into the following sections:

1. Technical Questions
2. Project-Based Questions
3. Behavioral Questions
4. Scenario-Based Questions

For each section generate 5 questions.

Do not provide answers.

Only generate the interview questions.
"""

        response = self.llm.invoke(prompt)

        return response.content