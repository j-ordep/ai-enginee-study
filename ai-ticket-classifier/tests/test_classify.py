import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_classify_returns_simulated_response():
    response = client.post("/classify", json={"message": "  Banco indisponível  "})

    assert response.status_code == 200
    assert response.json() == {
        "category": "infrastructure",
        "priority": "high",
        "reason": "Resposta simulada para validar o contrato.",
    }


@pytest.mark.parametrize(
    ("body", "error_type"),
    [
        ({}, "missing"),
        ({"message": 123}, "string_type"),
        ({"message": None}, "string_type"),
        ({"message": ""}, "string_too_short"),
        ({"message": "  \t  "}, "string_too_short"),
    ],
)
def test_classify_rejects_invalid_message(body, error_type):
    response = client.post("/classify", json=body)

    assert response.status_code == 422
    [error] = response.json()["detail"]
    assert error["loc"] == ["body", "message"]
    assert error["type"] == error_type


def test_classify_documents_input_and_output_models():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    operation = response.json()["paths"]["/classify"]["post"]
    request_schema = operation["requestBody"]["content"]["application/json"]["schema"]
    response_schema = operation["responses"]["200"]["content"]["application/json"]["schema"]
    assert request_schema["$ref"] == "#/components/schemas/ClassifyRequest"
    assert response_schema["$ref"] == "#/components/schemas/ClassifyResponse"
