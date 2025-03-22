from src.dao.base import BaseDAO
from src.posts.models import Posts


class PostsDAO(BaseDAO):
    model = Posts
