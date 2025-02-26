from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from server.settings import Base, ENGINE


class Follow(Base):
    """
    フォローモデル
    """

    __tablename__ = 'follows'
    __table_args__ = {
        'comment': 'フォロー情報のマスターテーブル'
    }

    from_user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    to_user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)