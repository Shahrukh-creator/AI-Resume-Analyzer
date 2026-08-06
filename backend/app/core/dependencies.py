from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.services.summary_service import SummaryService
from app.services.ats_service import ATSService
from app.services.compare_service import CompareService
from app.services.interview_service import InterviewService


embedding_service = EmbeddingService()

vector_service = VectorStoreService(
    embedding_service.get_embedding_model()
)

summary_service = SummaryService(vector_service)

ats_service = ATSService(vector_service)

compare_service = CompareService(vector_service)

interview_service = InterviewService(vector_service)