from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, ForeignKey, UUID, String, DateTime, func
from sqlalchemy.orm import relationship
from src.database import Base



class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(256), nullable=False)
    text = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    datetime_create = Column(DateTime, nullable=False, default=func.now())
