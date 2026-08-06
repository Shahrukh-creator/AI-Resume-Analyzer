from app.services.vector_store_service import VectorStoreService


class RetrievalService:

    def __init__(self, vector_store: VectorStoreService):

        self.vector_store = vector_store

    def get_resume_context(
        self,
        query: str,
        k: int = 5
    ):

        documents = self.vector_store.similarity_search(
            query,
            k=k
        )

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        return context