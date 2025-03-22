from pydantic import BaseModel


class SUserAuth(BaseModel):
    username: str
    password: str
