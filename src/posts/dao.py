from sqlalchemy import select, desc

from src.dao.base import BaseDAO
from src.posts.models import Posts
from src.database import async_session_maker


class PostsDAO(BaseDAO):
    model = Posts

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model).order_by(desc(Posts.datetime_create))
            posts = await session.execute(query)
            return posts.scalars().all()
