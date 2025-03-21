import uuid
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from src.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
