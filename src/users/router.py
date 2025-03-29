from fastapi import APIRouter, HTTPException, Response, Depends
from pydantic import UUID4

from src.users.dao import UsersDAO
from src.users.schemas import SUserAuth
from src.users.auth import get_password_hash, authenticate_user, create_access_token
from src.users.dependecies import get_current_user
from src.users.models import Users
from src.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
async def get_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.post("/register")
async def register(
    data: SUserAuth
):
    exists_user = await UsersDAO.find_one_or_none(username=data.username) # проверяем есть ли такой пользователь
    
    if exists_user:
        raise UserAlreadyExistsException # ошибка, пользователь с такин username уже существует
    
    hashed_password = get_password_hash(data.password) # хэшируем пароль
    
    await UsersDAO.add(username=data.username, hashed_password=hashed_password) # добавляем пользователя в бд

    return {"ok": True, "msg": "User has been succesfully registed"}


@router.post("/login")
async def login(
    response: Response,
    data: SUserAuth
):
    user = await authenticate_user(username=data.username, password=data.password)

    if not user:
        raise IncorrectEmailOrPasswordException
    
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)

    return {"access_token": access_token}


@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"ok": True, "msg": "User logged out of the account"}


@router.get("/{user_id}")
async def get_user(user_id: UUID4):
    user = await UsersDAO.find_one_or_none(id=user_id)
    return user
