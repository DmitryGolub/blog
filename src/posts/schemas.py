from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SPosts(BaseModel):
    id: UUID
    title: str
    text: str
    user_id: UUID
    datetime_create: datetime
