from uuid import uuid4
from sqlalchemy import Column, ForeignKey, UUID, String
from sqlalchemy.orm import relationship
from src.database import Base
from src.users.models import Users


class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(256), nullable=False)
    text = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("posts.id"))