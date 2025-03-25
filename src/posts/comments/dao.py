from uuid import UUID
from sqlalchemy import select, desc

from src.dao.base import BaseDAO
from src.posts.comments.models import Comments
from src.database import async_session_maker


class CommentsDAO(BaseDAO):
    model = Comments


    @classmethod
    async def get_all_by_post_id(cls, post_id: UUID):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(post_id=post_id).order_by(desc(Comments.datetime_create))
            comments = await session.execute(query)
            return comments.scalars().all()
    
