from domain.user import User  # noqa
from domain.tree import Tree  # noqa
from domain.follow import Follow  # noqa
from domain.dream import Dream  # noqa
from settings import Base, get_db_engine


def create_tables():
    """
    テーブルを作成する
    """
    Base.metadata.drop_all(bind=get_db_engine())
    Base.metadata.create_all(bind=get_db_engine())
