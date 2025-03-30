from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID, uuid4
from datetime import datetime
from fastapi_cache.decorator import cache

from src.posts.schemas import SPosts, SPostsAdd
from src.posts.dao import PostsDAO
from src.users.models import Users
from src.users.dependecies import get_current_user
from src.exceptions import PostNotFoundException, UserIsNotAuthorPostException


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/")
@cache(expire=60)
async def get_posts() -> list[SPosts]:
    return await PostsDAO.get_all()


@router.get("/{post_id}")
@cache(expire=60)
async def get_post(
    post_id: UUID,
) -> SPosts | None:
    return await PostsDAO.find_one_or_none(id=post_id)


@router.post("/")
async def add_post(
    data: SPostsAdd,
    user: Users = Depends(get_current_user)
):
    post_id = await PostsDAO.add(id=uuid4(), title=data.title, text=data.text, image_id=data.image_id, user_id=user.id, datetime_create=datetime.utcnow())
    post = await PostsDAO.find_one_or_none(id=post_id)
    return post


@router.delete("/{post_id}")
async def delete_post(
    post_id: UUID,
    user: Users = Depends(get_current_user)
):
    post = await PostsDAO.find_one_or_none(id=post_id)

    if not post:
        return PostNotFoundException
    elif user.id != post.user_id:
        return UserIsNotAuthorPostException
    
    await PostsDAO.delete(id=post_id)

    return {"ok": True, "msg": "Success delete post"}
