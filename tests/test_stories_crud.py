import pytest
from httpx import Response

@pytest.mark.asyncio
async def test_create_story(client, db_session):
    response: Response = await client.post("/stories/", json={"title": "Test Story", "description": "A test story", "category": "Test"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Story"
    assert "id" in data

@pytest.mark.asyncio
async def test_read_stories(client, db_session):
    response: Response = await client.get("/stories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
