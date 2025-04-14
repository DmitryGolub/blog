from sqlalchemy import select, desc
from sqlalchemy.exc import SQLAlchemyError

from src.dao.base import BaseDAO
from src.posts.models import Posts
from src.database import async_session_maker

from src.logger import logger


class PostsDAO(BaseDAO):
    model = Posts

    @classmethod
    async def get_all(cls):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).order_by(desc(Posts.datetime_create))
                posts = await session.execute(query)
                return posts.scalars().all()
            
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot get posts"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot get posts"
            
            logger.error(msg, exc_info=True)

        
