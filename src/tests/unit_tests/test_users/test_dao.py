import pytest
from uuid import UUID

from src.users.dao import UsersDAO


@pytest.mark.parametrize("id, exists, username", [
    (UUID('11111111-1111-1111-1111-111111111111'), True, 'User1'),
    (UUID('11111111-1111-1111-1111-111111111112'), True, 'User2'),
    (UUID('11111111-1111-1111-1111-111111111113'), False, '')
])
async def test_find_one_user_or_none(id, exists, username):
    user = await UsersDAO.find_one_or_none(id=id)

    if exists:
        assert user
        assert user.id == id
        assert user.username == username
    else:
        assert not user
