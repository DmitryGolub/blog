from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SComments(BaseModel):
    id: UUID
    text: str
    datetime_create: datetime
    post_id: UUID
    user_id: UUID
    username: str


class SCommentsAdd(BaseModel):
    text: str
