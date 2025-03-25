from fastapi import Depends, APIRouter
from uuid import uuid4, UUID
from datetime import datetime

from src.posts.comments.dao import CommentsDAO
from src.posts.comments.schemas import SCommentsAdd, SComments
from src.users.models import Users
from src.users.dependecies import get_current_user


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/{post_id}/comments")
async def get_comments(
    post_id: UUID
) -> list[SComments]:
    comments = await CommentsDAO.get_all_by_post_id(post_id=post_id)
    return comments


@router.post("/{post_id}/comments")
async def add_comment(
    post_id: UUID,
    data: SCommentsAdd,
    user: Users = Depends(get_current_user)
):
    await CommentsDAO.add(id=uuid4(), text=data.text, datetime_create=datetime.utcnow(), user_id=user.id, post_id=post_id)
    return {"ok": True, "msg": "Success add comment"}
