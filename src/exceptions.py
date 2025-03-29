from fastapi import HTTPException, status


class PostsException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenAbsentException(PostsException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"


class TokenExpiredException(PostsException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен истек"


class IncorrectFormatTokenException(PostsException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"


class UserIsNotPresentException(PostsException):
    status_code=status.HTTP_401_UNAUTHORIZED


class UserAlreadyExistsException(PostsException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"


class IncorrectEmailOrPasswordException(PostsException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"
