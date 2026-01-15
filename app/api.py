import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.store import DocumentStore
from app.services.workflow import RagWorkflow
from app.services.embedding import OpenRouterEmbeddingService
from app.services.llm import OpenRouterLLMService

router = APIRouter()

embedding = OpenRouterEmbeddingService()
store = DocumentStore(embedding)

llm = OpenRouterLLMService()
workflow = RagWorkflow(store, llm)
    
class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(req: QuestionRequest):
    start = time.time()
    try:
        result = workflow.run(req.question)
        return {
            "question": req.question,
            "answer": result.answer,
            "context_used": result.context,
            "latency_sec": round(time.time() - start, 3)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class DocumentRequest(BaseModel):
    text: str
    
@router.post("/add")
def add_document(req: DocumentRequest):
    try:
        doc_id = store.add(req.text)
        return {"id": doc_id, "status": "added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
def status():
    return store.status()