from fastapi import FastAPI
from pydantic import BaseModel
from rag import *


app = FastAPI()

@app.on_event("startup")
def startup():
    init_engine()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat_api(query: Query):

    db, llm = get_engine()

    answer, references = ask_question(
        db,
        query.question
    )

    return {
        "answer": answer,
        "references": references
    }