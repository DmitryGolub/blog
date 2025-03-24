from uuid import uuid4
from sqlalchemy import Column, ForeignKey, UUID, String
from sqlalchemy.orm import relationship
from src.database import Base


class Comments(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    text = Column(String(256), nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
