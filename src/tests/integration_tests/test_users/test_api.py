import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("username, password, status_code", [
    ('user1', 'qwerty1234', 200),
    ('user1', 'qwerty', 409),
    ('user2', 'qwerty1234', 200),
    ('', 'qwerty1234', 422),
    ('user3', '', 422),
    (123, 'querty1234', 422),
    ('user3', 123, 422)
])
async def test_register_user(username, password, status_code, ac: AsyncClient):
    response = await ac.post("/users/register", json={
        "username": username,
        "password": password
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("username, password, status_code", [
    ('User12345', 'qwerty1234', 401),
    ('User1', 'string21334', 401),
    ('User1', 'string', 200),
    ('User2', 'string', 200),
])
async def test_login_user(username, password, status_code, ac: AsyncClient):
    response = await ac.post("/users/login", json={
        "username": username,
        "password": password
    })

    assert response.status_code == status_code
