from app.services.vector_store_service import VectorStoreService
from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService
from app.prompts.summary_prompt import get_summary_prompt


class SummaryService:

    def __init__(self, vector_store: VectorStoreService):

        self.retrieval = RetrievalService(vector_store)

        self.vector_store = vector_store
        self.llm = LLMService()

    def generate_summary(self):


        # Build context
        context = self.retrieval.get_resume_context(
    "Summarize this resume")

        # Prompt
        prompt = get_summary_prompt(context)

        return self.llm.ask(prompt)