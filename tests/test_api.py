from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Meeting Intelligence API is running"}


def test_analyze_endpoint() -> None:
    payload = {
        "transcript": (
            "John: We should send the updated proposal by Friday.\n"
            "Sarah: I will take ownership of that.\n"
            "Mike: We decided to schedule a client review next Tuesday.\n"
            "John: The team agreed to delay the product demo until Thursday."
        ),
        "query": "What was decided about the demo?",
    }

    response = client.post("/analyze", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "action_items" in data
    assert "decisions" in data
    assert "topics" in data
    assert "search_results" in data

    assert len(data["decisions"]) > 0
    assert len(data["search_results"]) > 0