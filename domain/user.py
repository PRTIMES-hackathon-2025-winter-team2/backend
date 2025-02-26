from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from settings import Base

class User(Base):
    """
    ユーザーモデル
    """

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column('name', String(200))
    email = Column('email', String(100))
    password = Column('password', String(100))
    created_at = Column('created_at', DateTime)
    updated_at = Column('updated_at', DateTime)
