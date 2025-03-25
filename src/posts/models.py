from uuid import uuid4
from sqlalchemy import Column, ForeignKey, UUID, String, DateTime, func, Integer
from sqlalchemy.orm import relationship
from src.database import Base
from src.posts.comments.models import Comments


class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(256), nullable=False)
    text = Column(String, nullable=False)
    image_id = Column(Integer, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    datetime_create = Column(DateTime, nullable=False, default=func.now())

    comments = relationship("Comments", cascade="all, delete", passive_deletes=True)
