from uuid import uuid4
from sqlalchemy import Column, String
from src.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)

    post = relationship("Posts", back_populates="user")
    comment = relationship("Comments", back_populates="user")
