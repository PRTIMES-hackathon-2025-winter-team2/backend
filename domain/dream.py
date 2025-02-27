from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
import uuid
from typing import Optional

from settings import Base


class Dream(Base):
    """
    ドリームモデル
    """

    __tablename__ = 'dreams'
    __table_args__ = {
        'comment': 'ドリーム情報のマスターテーブル'
    }

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(200))
    tree_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trees.id'))
    position: Mapped[int] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
