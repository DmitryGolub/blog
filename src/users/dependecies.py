from fastapi import Depends, Request, HTTPException
from jose import ExpiredSignatureError, JWTError, jwt
from uuid import UUID

from src.config import settings
from src.users.dao import UsersDAO
from src.exceptions import TokenAbsentException, TokenExpiredException, IncorrectFormatTokenException, UserIsNotPresentException


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise IncorrectFormatTokenException
    
    user_id: UUID = payload.get("sub")

    if not user_id:
        raise IncorrectFormatTokenException
    
    user = await UsersDAO.find_one_or_none(id=user_id)

    if not user:
        raise UserIsNotPresentException
    
    return user


