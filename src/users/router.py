from fastapi import APIRouter, HTTPException, Response, Depends

from src.users.dao import UsersDAO
from src.users.schemas import SUserAuth
from src.users.auth import get_password_hash, authenticate_user, create_access_token
from src.users.dependecies import get_current_user
from src.users.models import Users


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
        raise HTTPException(status_code=409) # ошибка, пользователь с такин username уже существует
    
    hashed_password = get_password_hash(data.password) # хэшируем пароль
    
    await UsersDAO.add(username=data.username, hashed_password=hashed_password) # добавляем пользователя в бд


@router.post("/login")
async def login(
    response: Response,
    data: SUserAuth
):
    user = await authenticate_user(username=data.username, password=data.password)

    if not user:
        raise HTTPException(status_code=409)
    
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)

    return {"access_token": access_token}


@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
