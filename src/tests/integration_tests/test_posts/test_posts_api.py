import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("title, text, image_id, status_code", [
    ("Post1", "Text of post1", 1, 200),
    ("Post1", "Text of post1", 1, 200),
    ("Post2", "Text of post2", None, 200),
    ("", "Text of post1", 2, 422),
    ("Post1", "", 3, 422),
])
async def test_add_and_get_posts(title, text, status_code, image_id, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/posts/", json={
        "title": title,
        "text": text,
        "image_id": image_id,
    })

    assert response.status_code == status_code
