import pytest
import json
import asyncio
from sqlalchemy import insert
from datetime import datetime
from fastapi.testclient import TestClient
from httpx import AsyncClient
from httpx import ASGITransport


from src.database import Base, async_session_maker, engine
from src.config import settings

from src.posts.models import Posts
from src.posts.comments.models import Comments
from src.users.models import Users

from src.main import app as fastapi_app

@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    def open_mock_json(model: str):
        with open(f"src/tests/mock_{model}.json", "r") as file:
            return json.load(file)

    users = open_mock_json("users")
    posts = open_mock_json("posts")
    comments = open_mock_json("comments")

    for comment in comments:
        comment["datetime_create"] = datetime.strptime(comment["datetime_create"], "%Y-%m-%d %H:%M:%S.%f")

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)
        add_posts = insert(Posts).values(posts)
        add_comments = insert(Comments).values(comments)

        await session.execute(add_users)
        await session.execute(add_posts)
        await session.execute(add_comments)

        await session.commit()
    

@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_ac():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        await ac.post("/users/login", json={
            "username": "User1",
            "password": "string",
        })
        assert ac.cookies["access_token"]
        yield ac

