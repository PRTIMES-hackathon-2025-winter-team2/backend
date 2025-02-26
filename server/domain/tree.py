from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from server.settings import Base, ENGINE


class Tree(Base):
    """
    ツリーモデル
    """

    __tablename__ = 'trees'
    __table_args__ = {
        'comment': 'ツリー情報のマスターテーブル'
    }

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at = Column('created_at', DateTime)
    ended_at = Column('ended_at', DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)