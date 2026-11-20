from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, StringConstraints


class ClassifyRequest(BaseModel):
    message: Annotated[
        str,
        StringConstraints(strict=True, strip_whitespace=True, min_length=1),
    ]


class ClassifyResponse(BaseModel):
    category: str
    priority: str
    reason: str

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/classify")
def classify(ticket: ClassifyRequest) -> ClassifyResponse:
    return ClassifyResponse(
        category="infrastructure",
        priority="high",
        reason="Resposta simulada para validar o contrato.",
    )
