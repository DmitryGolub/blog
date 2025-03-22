from src.dao.base import BaseDAO
from src.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

