from app.services.vector_store_service import VectorStoreService
from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService
from app.prompts.ats_prompt import get_ats_prompt


class ATSService:

    def __init__(self, vector_store: VectorStoreService):
        self.retrieval = RetrievalService(vector_store)

        self.vector_store = vector_store
        self.llm = LLMService()

    def analyze_resume(self):

        context = self.retrieval.get_resume_context(
       "Analyze this resume")

        prompt = get_ats_prompt(context)

        return self.llm.ask(prompt)