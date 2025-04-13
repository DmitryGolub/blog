import pytest
from datetime import datetime
from uuid import UUID
from src.posts.dao import PostsDAO


@pytest.mark.parametrize("id, title, text, image_id, user_id", [
    (UUID('21111111-1111-1111-1111-111111111113'), 'Post3', 'Text Post3', 1, UUID('11111111-1111-1111-1111-111111111112'))
])
async def test_add_and_get_posts(id, title, text, image_id, user_id):
    id_new_post = await PostsDAO.add(
        id=id,
        title=title, 
        text=text, 
        image_id=image_id, 
        user_id=user_id, 
        datetime_create=datetime.utcnow()
        )

    assert id_new_post == id

    new_post = await PostsDAO.find_one_or_none(
        id=id_new_post
    )

    assert new_post is not None
    
    
