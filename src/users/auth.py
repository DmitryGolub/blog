from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from passlib.context import CryptContext

from src.users.dao import UsersDAO
from src.config import settings
from src.exceptions import IncorrectEmailOrPasswordException


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    
    return encoded_jwt


async def authenticate_user(username: str, password: str):
    user = await UsersDAO.find_one_or_none(username=username)

    if not user or not verify_password(password, user.hashed_password): 
        raise IncorrectEmailOrPasswordException
    
    return user


