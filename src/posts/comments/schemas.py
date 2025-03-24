from pydantic import BaseModel


class SCommentsAdd(BaseModel):
    text: str
    