from langchain_chroma import Chroma


class VectorStoreService:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

        self.vector_store = None

    def create_vector_store(self, chunks):

        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model
        )

        return self.vector_store

    def similarity_search(self, question, k=3):

        if self.vector_store is None:
            raise Exception("Resume has not been uploaded.")

        return self.vector_store.similarity_search(
            question,
            k=k
        )