from fastapi import Depends, Request, HTTPException
from jose import ExpiredSignatureError, JWTError, jwt
from uuid import UUID

from src.config import settings
from src.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=409)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=409)
    except JWTError:
        raise HTTPException(status_code=409)
    
    user_id: UUID = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=409)
    
    user = await UsersDAO.find_one_or_none(id=user_id)

    if not user:
        raise HTTPException(status_code=409)
    
    return user


