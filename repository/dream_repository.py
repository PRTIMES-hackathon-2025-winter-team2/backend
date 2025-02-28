from datetime import datetime

from sqlalchemy.orm import scoped_session

from domain.dream import Dream
from domain.tree import Tree
from domain.user import User
from uuid import UUID


class DreamRepository:
    def __init__(self, session: scoped_session):
        self.session = session

    def creates(self, dreams: list[Dream]) -> list[Dream]:
        for dream in dreams:
            dream.created_at = datetime.now()
            self.session.add(dream)
        self.session.commit()
        return dreams

    def create(self, dream: Dream) -> Dream:
        dream.created_at = datetime.now()
        self.session.add(dream)
        self.session.commit()
        return dream

    def update_ended_at(self, dream_id: str):
        dream = self.session.query(Dream).filter(Dream.id == dream_id).first()
        if not dream:
            raise Exception(f"指定されたIDのDreamが存在しません: {dream_id}")
        dream.ended_at = datetime.now()
        self.session.commit()

    def get_dream_owner(self, dream_id: str) -> UUID:
        # userに紐付いたtreeに紐付いたdreamのIDからuserを取得する
        result = (
            self.session.query(User.id)  # User.idのみを選択
            .join(Tree, User.id == Tree.user_id)
            .join(Dream, Tree.id == Dream.tree_id)
            .filter(Dream.id == dream_id)
            .scalar()  # 単一の値を返す
        )

        if result is None:
            raise Exception(f"指定されたIDのDreamが存在しません: {dream_id}")
        return result
