from fastapi import FastAPI
from pydantic import BaseModel


from chatbot import ask_question

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    video_url: str
    question: str


@app.post("/ask")
async def ask(data: Query):

    answer = ask_question(
        data.video_url,
        data.question
    )

    return {
        "answer": answer
    }