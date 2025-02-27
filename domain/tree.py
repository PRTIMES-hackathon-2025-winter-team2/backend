from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID
from domain.dream import Dream
import uuid
from typing import Optional

from settings import Base


class Tree(Base):
    """
    ツリーモデル
    """

    __tablename__ = "trees"
    __table_args__ = {"comment": "ツリー情報のマスターテーブル"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id")
    )
    created_at: Mapped[datetime] = mapped_column(DateTime)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    dreams: Mapped[list[Dream]] = relationship("Dream", backref="tree")
