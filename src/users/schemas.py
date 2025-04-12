from pydantic import BaseModel
from pydantic import Field


class SUserAuth(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
