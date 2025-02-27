import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from settings import Base


class Follow(Base):
    """
    フォローモデル
    """

    __tablename__ = "follows"
    __table_args__ = {"comment": "フォロー情報のマスターテーブル"}

    from_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    to_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
