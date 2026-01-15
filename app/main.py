from fastapi import FastAPI
from app.api import router

app = FastAPI(title="ChatBot RAG Demo")
app.include_router(router)