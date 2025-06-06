from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class SPosts(BaseModel):
    id: UUID
    title: str
    text: str
    user_id: UUID
    datetime_create: datetime


class SPostsAdd(BaseModel):
    title: str = Field(max_length=256, min_length=1)
    text: str = Field(min_length=1)
    image_id: int | None = Field(ge=1, le=2147483647)
