from fastapi import APIRouter
from src.posts.dao import PostsDAO
from uuid import UUID

from src.posts.schemas import SPosts

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/")
async def get_posts() -> list[SPosts]:
    return await PostsDAO.get_all()


@router.get("/{id}")
async def get_post(
    id: UUID,
) -> SPosts | None:
    return await PostsDAO.find_one_or_none(id=id)
