from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from server.settings import Base, ENGINE


class Dream(Base):
    """
    ドリームモデル
    """

    __tablename__ = 'dreams'
    __table_args__ = {
        'comment': 'ドリーム情報のマスターテーブル'
    }

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column('title', String(200))
    tree_id = Column(UUID(as_uuid=True), ForeignKey('trees.id'))
    created_at = Column('created_at', DateTime)
    ended_at = Column('ended_at', DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)