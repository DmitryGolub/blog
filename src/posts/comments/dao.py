from uuid import UUID
from sqlalchemy import select, desc

from src.dao.base import BaseDAO
from src.posts.comments.models import Comments
from src.users.models import Users
from src.database import async_session_maker
from src.posts.comments.schemas import SComments


class CommentsDAO(BaseDAO):
    model = Comments


    @classmethod
    async def get_all_by_post_id(cls, post_id: UUID):
        async with async_session_maker() as session:
            query = select(Comments, Users).outerjoin(Users).where(Comments.post_id==post_id).order_by(desc(Comments.datetime_create))
            comments = await session.execute(query)
            data = comments.all()
            
            return [SComments(id=comment.id, text=comment.text, datetime_create=comment.datetime_create, post_id=comment.post_id, user_id=user.id, username=user.username) for comment, user in data]
    
